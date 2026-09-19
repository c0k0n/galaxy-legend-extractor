#!/usr/bin/env python3
"""
Extract all English localization from tap4fun.zip data2/text tables
into extracted/loc/all_loc_en.json.

Format (correct - verified against raw bytes):
  <2-byte LE count> then per record: <2-byte LE length><string bytes>
  .idx holds keys, .en holds values, parallel arrays.
NOTE: an 8-bit length parse misjoins every string longer than 127 bytes and
desynchronises the whole table, so the 16-bit width above is load-bearing --
see docs/DATA_FORMATS.md.
"""
import zipfile, struct, json, os

ZIP = os.path.join(os.path.dirname(__file__), '..',
                   'data', 'tap4fun_assets', 'tap4fun.zip')
PREFIX = 'tap4fun/galaxylegend/AppOriginalData/data2/text/'

def read_tbl(data):
    (n,) = struct.unpack_from('<H', data, 0)
    p = 2
    out = []
    for _ in range(n):
        (l,) = struct.unpack_from('<H', data, p); p += 2
        out.append(data[p:p+l].decode('utf-8', 'replace')); p += l
    assert p == len(data), f'trailing {len(data)-p} bytes'
    return out

def main():
    z = zipfile.ZipFile(ZIP)
    maps = {}
    idxes = [n for n in z.namelist()
             if n.startswith(PREFIX) and n.endswith('.idx')]
    for n in idxes:
        base = os.path.basename(n)[:-4]
        en = PREFIX + base + '.en'
        if en not in z.namelist():
            continue
        keys = read_tbl(z.read(n))
        vals = read_tbl(z.read(en))
        assert len(keys) == len(vals), f'{base}: {len(keys)} keys vs {len(vals)} vals'
        maps[base] = dict(zip(keys, vals))
    out = os.path.join(os.path.dirname(__file__), '..', 'extracted', 'loc', 'all_loc_en.json')
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(maps, f, ensure_ascii=False, indent=1)
    print({k: len(v) for k, v in sorted(maps.items())})

if __name__ == '__main__':
    main()
