#!/usr/bin/env python3
"""
decrypt_tfl.py — Decrypt Galaxy Legends .tfl files.

Usage:
    python3 decrypt_tfl.py <file.tfl> [file2.tfl ...] [--outdir DIR]
    python3 decrypt_tfl.py --all            (decrypt every TFL under data/)

Cipher (reverse-engineered from libgalaxylegend.so, arm64):
    PRNG:  LCG  state = state*0x19660d + 0x3c6ef35f;  getRand(max) = (state>>16) % max
    Seed:  0x0003857A  (passed at the game's open-file call site)
    Per 4-byte block:  dir=getRand(2), rot=getRand(0x20)
        rotated = rol(cipher, rot) if dir==0 else ror(cipher, rot)   # rotate FIRST
        plain   = rotated ^ mask                                       # then XOR
        mask    = (getRand(0x100)<<24) | (getRand(0x100)<<16) |
                  (getRand(0x100)<<8)  |  getRand(0x100)
    Tail (1-3 bytes): same scheme with width-sized rotates (24/16/8).
    The 16-byte file prefix is ciphertext, not a header — decrypt the whole file.

Output: <name>.tfl.luac next to the input (or in --outdir).
Plaintext is modified Lua 5.1 bytecode ('\\x1bLuaQ'); see extract_tfl_data.py to parse it.
"""
import os, sys, glob

SEED = 0x0003857A

class LCG:
    def __init__(self, seed):
        self.state = seed & 0xFFFFFFFF
    def getRand(self, max_val):
        self.state = (self.state * 0x19660d + 0x3c6ef35f) & 0xFFFFFFFF
        result = self.state >> 16
        return result % max_val if max_val else result

def _ror(val, n, bits):
    n &= bits - 1
    return ((val >> n) | (val << (bits - n))) & ((1 << bits) - 1)

def _rol(val, n, bits):
    return _ror(val, bits - (n & (bits - 1)), bits)

def decrypt_tfl(data, seed=SEED):
    """Decrypt an entire TFL buffer; returns Lua bytecode."""
    lcg = LCG(seed)
    out = bytearray()
    size = len(data)
    if size < 4:
        return bytes(data)
    nblocks = ((size - 4) >> 2) + 1
    i = 0
    for _ in range(nblocks):
        cipher = data[i] | (data[i+1] << 8) | (data[i+2] << 16) | (data[i+3] << 24)
        direction = lcg.getRand(2)
        rot = lcg.getRand(0x20)
        rotated = _rol(cipher, rot, 32) if direction == 0 else _ror(cipher, rot, 32)
        mask = ((lcg.getRand(0x100) << 24) | (lcg.getRand(0x100) << 16) |
                (lcg.getRand(0x100) << 8) | lcg.getRand(0x100))
        out += (rotated ^ mask).to_bytes(4, 'little')
        i += 4
    remaining = size - i
    if remaining in (1, 2, 3):
        direction = lcg.getRand(2)
        if remaining == 3:
            rot = lcg.getRand(0x18)
            cipher = data[i] | (data[i+1] << 8) | (data[i+2] << 16)
            rotated = _rol(cipher, rot, 24) if direction == 0 else _ror(cipher, rot, 24)
            mask = (lcg.getRand(0x100) << 16) | (lcg.getRand(0x100) << 8) | lcg.getRand(0x100)
            plain = rotated ^ mask
            out += bytes([plain & 0xFF, (plain >> 8) & 0xFF, (plain >> 16) & 0xFF])
        elif remaining == 2:
            rot = lcg.getRand(0x10)
            cipher = data[i] | (data[i+1] << 8)
            rotated = _rol(cipher, rot, 16) if direction == 0 else _ror(cipher, rot, 16)
            mask = (lcg.getRand(0x100) << 8) | lcg.getRand(0x100)
            plain = rotated ^ mask
            out += bytes([plain & 0xFF, (plain >> 8) & 0xFF])
        else:
            rot = lcg.getRand(8)
            cipher = data[i]
            rotated = _rol(cipher, rot, 8) if direction == 0 else _ror(cipher, rot, 8)
            plain = rotated ^ lcg.getRand(0x100)
            out.append(plain & 0xFF)
    return bytes(out)

def decrypt_file(path, outdir=None):
    data = open(path, 'rb').read()
    plain = decrypt_tfl(data)
    ok = plain[:4] == b'\x1bLua'
    base = os.path.basename(path)
    outdir = outdir or os.path.dirname(path) or '.'
    os.makedirs(outdir, exist_ok=True)
    out_path = os.path.join(outdir, base + '.luac')
    with open(out_path, 'wb') as f:
        f.write(plain)
    status = 'OK' if ok else f'UNEXPECTED MAGIC {plain[:5]!r}'
    print(f'{base:28s} {len(data):>9} B -> {out_path}  [{status}]')
    return ok

def main():
    args = sys.argv[1:]
    outdir = None
    if '--outdir' in args:
        i = args.index('--outdir')
        outdir = args[i + 1]
        del args[i:i + 2]
    if not args:
        print(__doc__)
        sys.exit(1)
    paths = []
    for a in args:
        if a == '--all':
            root = os.path.join(os.path.dirname(__file__) or '.', '..', 'data')
            paths += glob.glob(os.path.join(root, '**', '*.tfl'), recursive=True)
        else:
            paths.append(a)
    ok = all(decrypt_file(p, outdir) for p in paths)
    sys.exit(0 if ok else 1)

if __name__ == '__main__':
    main()
