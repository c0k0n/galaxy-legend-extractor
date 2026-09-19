#!/usr/bin/env python3
"""
extract_tfl_data.py — Parse decrypted Galaxy Legends TFL bytecode and extract data tables.

The decrypted .tfl.luac files are modified Lua 5.1 bytecode:
  - 12-byte header: 1b 4c 75 61 51 00 01 04 04 04 08 00  (lua_Number = 8-byte double!)
  - nested protos have NO magic header
  - constants: 0=nil, 1/2=bool, 3=double(8B), 4=string(4B len + bytes incl. trailing \\x00)
  - shuffled opcodes; row-table pattern:
      op3  (LOADK-ext): R[A] := const[Bx(18-bit)]
      op7  (NEWTABLE): starts a row
      op10 (SETTABLE): R[A][K(B)] := K(C), 9-bit operands, RK(x) = K[x-256] if x>=256 else R[x]
      op11 (GETGLOBAL-ish): R[A] := const[C]
      op12 (CALL): table.insert

Two output modes:
  --loc EXTRA_TEXT.luac EXTRA_TEXT_V1.luac ...
      Extract localization pairs. Each chunk contains one table per language
      (closure-delimited segments; EN is segment 3). Emits loc JSON files.
  --rows ExtraFleetInfo.luac
      Extract row tables (spells, conditions, ability rows...) from the
      ExtraFleetInfo-style register-machine streams. Emits v1_extrafleet_spells.json.

Usage:
    python3 extract_tfl_data.py --loc <EXTRA_TEXT.tfl.luac> <EXTRA_TEXT_V1.tfl.luac>
    python3 extract_tfl_data.py --rows <v1_ExtraFleetInfo.tfl.luac>
"""
import struct, sys, os, json

# ---------------- bytecode parser ----------------

def parse_chunk(d, off=0, top=True):
    """Parse a modified Lua 5.1 chunk. Returns (info dict, end offset)."""
    if top:
        assert d[off:off+4] == b'\x1bLua', f'bad magic at {off}'
        p = off + 12
    else:
        p = off
    (srlen,) = struct.unpack_from('<I', d, p); p += 4
    src = d[p:p+srlen].decode('utf-8', 'replace') if srlen else ''
    p += srlen
    ld, lld = struct.unpack_from('<II', d, p); p += 8
    nups, nparams, vararg, maxstack = d[p], d[p+1], d[p+2], d[p+3]; p += 4
    (ncode,) = struct.unpack_from('<I', d, p); p += 4
    code = [struct.unpack_from('<I', d, p + 4*i)[0] for i in range(ncode)]
    p += 4 * ncode
    (nconst,) = struct.unpack_from('<I', d, p); p += 4
    consts = []
    for _ in range(nconst):
        t = d[p]; p += 1
        if t == 0: consts.append(None)
        elif t in (1, 2): consts.append(bool(t & 1)); p += 0
        elif t == 3: consts.append(struct.unpack_from('<d', d, p)[0]); p += 8
        elif t == 4:
            (l,) = struct.unpack_from('<I', d, p); p += 4
            consts.append(d[p:p+l].decode('utf-8', 'replace')); p += l
        else: raise ValueError(f'const type {t} at {p-1} in {src!r}')
    (nproto,) = struct.unpack_from('<I', d, p); p += 4
    protos = []
    for _ in range(nproto):
        sub, p = parse_chunk(d, p, top=False)
        protos.append(sub)
    # debug info
    (nline,) = struct.unpack_from('<I', d, p); p += 4 + 4*nline
    (nloc,) = struct.unpack_from('<I', d, p); p += 4
    for _ in range(nloc):
        (l,) = struct.unpack_from('<I', d, p); p += 4 + l + 8
    (nup,) = struct.unpack_from('<I', d, p); p += 4
    for _ in range(nup):
        (l,) = struct.unpack_from('<I', d, p); p += 4 + l
    return dict(src=src, ncode=ncode, code=code, consts=consts,
                protos=protos, nconst=nconst), p

# ---------------- loc-table extraction (EXTRA_TEXT chunks) ----------------

def extract_loc_pairs(path):
    """Extract all language tables from an EXTRA_TEXT chunk.

    Returns list of {lang_index: {key: value}} — index 3 is English,
    index 5 is Simplified Chinese (verified by content)."""
    d = open(path, 'rb').read()
    # locate the const region via the Extra_text marker
    marker = d.find(b'\x04\x0e\x00\x00\x00Extra_text')
    if marker < 0:
        marker = d.find(b'\x04\x0b\x00\x00\x00Extra_text')
    if marker < 0:
        raise ValueError(f'{path}: Extra_text marker not found')
    nconst = struct.unpack_from('<I', d, marker - 4)[0]
    ncode = (marker - 4 - 4 - 32) // 4
    consts = []
    p = marker
    for _ in range(nconst):
        t = d[p]; p += 1
        if t in (0, 1, 2):
            consts.append(bool(t & 1) if t else None)
        elif t == 3:
            consts.append(struct.unpack_from('<d', d, p)[0]); p += 8
        elif t == 4:
            ln = struct.unpack_from('<I', d, p)[0]; p += 4
            consts.append(d[p:p+ln-1].decode('utf-8', errors='replace')); p += ln
        else:
            raise ValueError(f'const type {t}')
    regs = {}
    pairs = []
    closures = []
    for i in range(ncode):
        ins = struct.unpack_from('<I', d, 32 + i*4)[0]
        op = ins & 0x3F
        if op == 3:
            regs[(ins >> 6) & 0xFF] = (ins >> 14) & 0x3FFFF
        elif op == 10:
            A = (ins >> 6) & 0xFF
            B = (ins >> 23) & 0x1FF
            C = (ins >> 14) & 0x1FF
            k = (B - 256) if B >= 256 else regs.get(B)
            v = (C - 256) if C >= 256 else regs.get(C)
            if k is not None and v is not None and k < len(consts) and v < len(consts):
                pairs.append((i, k, v))
        elif op == 7:
            closures.append(i)
    segs = []
    prev = closures[1]
    for ci in closures[2:]:
        segs.append((prev, ci)); prev = ci
    segs.append((prev, ncode))
    segs.insert(0, (2, closures[1]))
    tables = []
    for lo, hi in segs:
        t = {}
        for ii, k, v in pairs:
            if lo <= ii < hi:
                t.setdefault(consts[k], consts[v])
        tables.append(t)
    return tables

# ---------------- row-table extraction (ExtraFleetInfo chunks) ----------------

def extract_rows(path):
    """Extract row dicts from a register-machine chunk (ExtraFleetInfo style)."""
    d = open(path, 'rb').read()
    info, end = parse_chunk(d)
    code = info['code']
    consts = [c.rstrip('\x00') if isinstance(c, str) else c for c in info['consts']]
    regs = [None] * 64
    rows = []
    cur = None

    def RK(x):
        if x >= 256:
            i = x - 256
            return consts[i] if i < len(consts) else None
        v = regs[x]
        return consts[v] if isinstance(v, int) and v < len(consts) else v

    for ins in code:
        op = ins & 0x3F
        A = (ins >> 6) & 0xFF
        B = (ins >> 23) & 0x1FF
        C = (ins >> 14) & 0x1FF
        Bx = (ins >> 14) & 0x3FFFF
        if op == 3:
            regs[A] = Bx
        elif op == 7:
            if cur is not None and len(cur) > 1:
                rows.append(dict(cur))
            cur = {}
        elif op == 10 and cur is not None:
            k = RK(B); v = RK(C)
            if isinstance(k, str) and v is not None:
                cur[k] = v
        elif op == 11 and C >= 256:
            regs[A] = consts[C - 256] if C - 256 < len(consts) else None
    if cur is not None and len(cur) > 1:
        rows.append(dict(cur))
    return rows

# ---------------- main ----------------

def write_json(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
    print(f'{len(obj) if hasattr(obj, "__len__") else "?"} entries -> {path}')

def main():
    args = sys.argv[1:]
    ex = os.path.join(os.path.dirname(__file__), '..', 'extracted')
    if not args:
        print(__doc__); sys.exit(1)
    if args[0] == '--loc':
        en, cn = {}, {}
        for path in args[1:]:
            tables = extract_loc_pairs(path)
            if len(tables) < 6: continue
            for k, v in tables[3].items(): en.setdefault(k, v)   # EN
            for k, v in tables[5].items(): cn.setdefault(k, v)   # CN
        write_json(os.path.join(ex, 'loc', 'extra_text_en.json'), en)
        write_json(os.path.join(ex, 'loc', 'extra_text_cn.json'), cn)
    elif args[0] == '--rows':
        rows = extract_rows(args[1])
        spells = {}
        for r in rows:
            if 'spell_id' in r and 'spell_name' in r:
                sid = str(int(float(r['spell_id'])))
                spells[sid] = {k: v for k, v in r.items() if k != 'spell_id'}
        write_json(os.path.join(ex, 'raw_tables', 'v1_extrafleet_spells.json'), spells)
    else:
        print(__doc__); sys.exit(1)

if __name__ == '__main__':
    main()
