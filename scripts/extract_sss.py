#!/usr/bin/env python3
"""
extract_sss.py — Stage 1: extract hero tables from data1.pak.

Scans data1.pak for zlib-compressed Lua scripts and parses the hero tables:
    GameData.heros.Ability   → heros_ability.json    (identity, stats, per-level rows)
    GameData.heros.basic     → heros_basic.json
    GameData.heros.growing   → heros_growing.json
    GameData.heros.enhance   → heros_enhance.json    (augment costs; conditions contain nested braces)
    GameData.heros_skill.skill → heros_skill_skill.json  (per-augment skill panels)

Lua table entries look like:
    table.insert(Table, {
        ["ID"] = 608,
        ["condition"] = "[{item,{1203,5}},{money,100000}]",   ← nested braces!
        ...
    })
Parsing uses brace matching (a naive regex breaks on nested braces in values).

Output: extracted/raw_tables/heros_*.json
"""
import json, re, zlib, os

PAK_PATH = os.path.join(os.path.dirname(__file__), '..',
                        'data', 'game_files', 'documents', 'Documents', 'data1.pak')
OUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'extracted', 'raw_tables')

TABLES = {
    'heros_ability':      'GameData.heros.Ability',
    'heros_basic':        'GameData.heros.basic',
    'heros_growing':      'GameData.heros.growing',
    'heros_enhance':      'GameData.heros.enhance',
    'heros_skill_skill':  'GameData.heros_skill.skill',
}

def parse_entries(lua_text):
    """Parse table.insert(T, { ... }) blocks with brace matching."""
    entries = []
    for m in re.finditer(r'table\.insert\(\w+,\s*\{', lua_text):
        start = m.end() - 1
        depth = 0
        i = start
        while i < len(lua_text):
            if lua_text[i] == '{': depth += 1
            elif lua_text[i] == '}':
                depth -= 1
                if depth == 0: break
            i += 1
        block = lua_text[start:i+1]
        fields = {}
        pat = re.compile(r'\["(\w+)"\]\s*=\s*')
        matches = list(pat.finditer(block))
        for j, fm in enumerate(matches):
            key = fm.group(1)
            p = fm.end()
            end = matches[j+1].start() if j+1 < len(matches) else len(block)
            val = block[p:end].strip().rstrip('}').strip().rstrip(',').strip()
            if val.startswith('"') and val.endswith('"'):
                val = val[1:-1]
            fields[key] = val
        if fields:
            entries.append(fields)
    return entries

def coerce(entries):
    """Convert numeric-looking string fields to int/float."""
    out = []
    for e in entries:
        row = {}
        for k, v in e.items():
            if isinstance(v, str) and re.fullmatch(r'-?\d+', v):
                row[k] = int(v)
            elif isinstance(v, str) and re.fullmatch(r'-?\d+\.\d+', v):
                row[k] = float(v)
            else:
                row[k] = v
        out.append(row)
    return out

def main():
    pak = open(PAK_PATH, 'rb').read()
    # identify table→lua-text once per table marker
    found = {name: None for name in TABLES}
    pos = 0
    while pos < len(pak) - 2:
        if pak[pos] == 0x78 and pak[pos+1] in (0x01, 0x5e, 0x9c, 0xda):
            try:
                text = zlib.decompress(pak[pos:]).decode('utf-8', errors='ignore')
            except zlib.error:
                pos += 1
                continue
            head = text[:400]
            for name, marker in TABLES.items():
                # require the declaration at file head — other lua files merely
                # reference GameData paths without being the table
                if found[name] is None and marker in head and 'table.insert' in text:
                    found[name] = text
        pos += 1
    os.makedirs(OUT_DIR, exist_ok=True)
    for name, text in found.items():
        if text is None:
            print(f'{name}: NOT FOUND in pak'); continue
        rows = coerce(parse_entries(text))
        out = os.path.join(OUT_DIR, f'{name}.json')
        with open(out, 'w', encoding='utf-8') as f:
            json.dump(rows, f, ensure_ascii=False, indent=1)
        print(f'{name}: {len(rows)} rows -> {out}')

if __name__ == '__main__':
    main()
