#!/usr/bin/env python3
"""
export_llm.py — Render sss_database.json as one Markdown file per role, for LLM use.

Markdown beats JSON here: it is ~40% smaller for the same content, headings give a
model a stable outline to navigate, and tables/lists survive chunking. One file per
role so you can hand a model just the Protectors instead of all 194 heroes.

Usage:
    python3 scripts/export_llm.py [--out extracted/llm]

Outputs: <rangers|strikers|protectors|destroyers|rovers|flagships>.md
"""
import json, os, sys, collections

EX = os.path.join(os.path.dirname(__file__), '..', 'extracted')
ROLE_ORDER = ['Ranger', 'Striker', 'Protector', 'Destroyer', 'Rover', 'Flagship']
ROMAN = ['Ⅰ', 'Ⅱ', 'Ⅲ', 'Ⅳ', 'Ⅴ', 'Ⅵ']


def one_line(s):
    """Collapse whitespace so a description stays on one line."""
    return ' '.join((s or '').split())


def cell(s):
    return one_line(s).replace('|', '/')


def cost_line(step):
    parts = [f"{i['qty']}× {i.get('name') or ('item ' + str(i['id']))}" for i in step.get('items', [])]
    if step.get('money'):
        parts.append(f"{step['money']:,} money")
    return ' · '.join(parts) or '—'


def tier_block(t, indent=''):
    """One skill tier: tier numeral, unlock state, names, description."""
    names = t.get('name_en') or '—'
    if t.get('name_cn'):
        names += f" ({t['name_cn']})"
    out = f"{indent}- **{t.get('tier_label', '')}** at `{t.get('from_augment', '')}` — {one_line(names)}\n"
    if t.get('description_en'):
        out += f"{indent}  {one_line(t['description_en'])}\n"
    else:
        out += f"{indent}  _(no English description shipped)_\n"
    return out


def hero_md(h):
    o = []
    o.append(f"## {h['id']} · {one_line(h['name_en']) or '(no English name)'} {one_line(h['name_cn'])}")
    o.append(f"**Role** {h['role']} · **Attack** {h['attack_type']} · "
             f"**Generation** {h['generation']}")
    r = h['ratings']
    o.append(f"**Ratings** Damage {r['damage']}/10 · Defence {r['defence']}/10 · Assist {r['assist']}/10")
    o.append('')

    if h['generation'] == 'latest':
        o.append('### Skill panels')
        for s in h['skills']:
            o.append(f"**Slot {s['slot']} — {one_line(s['name_en']) or '—'}** (id {s['tiers'][0]['id']}, unlocks at `{s['unlocks_at']}`)")
            for t in s['tiers']:
                o.append(tier_block(t, '  ').rstrip())
            o.append('')
    else:
        o.append('### Signature skill')
        for s in h['skills']:
            o.append(tier_block(s).rstrip())
        o.append('')

    if h.get('transform'):
        t = h['transform']
        o.append(f"### Transform form ({t['id']} · {one_line(t.get('name_cn', ''))})")
        for s in t['skills']:
            o.append(tier_block(s).rstrip())
        o.append('')

    if h.get('augment'):
        o.append('### Augment cost (per step)')
        for s in h['augment']:
            o.append(f"- `{s['to']}` — {cost_line(s)}")
        o.append('')

    o.append('---')
    o.append('')
    return '\n'.join(o)


HEADER = """# Galaxy Legends — SSS {title} ({n} heroes)

Part of a complete SSS dataset: 194 heroes across 6 roles, extracted from game
version 2.6.2. Every hero below is SSS rank.

## How to read this

- **Ratings** are the game's own 1–10 bars for Damage / Defence / Assist. The game
  computes real HP/ATK/DEF from them at runtime — no numeric stat table is shipped.
- **Augment order**: `+0 < +1 < … < +15 < +T < +T1 < +T2 < +T3 < +T4 < Awaken < Second Awaken`.
  `+T` is its own rung, one step *below* `+T1` — the two are consecutive, not synonyms.
  The unlock state shown for each tier is the one the game itself ships; it is per hero, so a
  hero may skip a state (Horus goes `+0 → +T → +T3 → +T4`) and the first T step is written
  `+T` on some heroes and `+T1` on others.
- **Generation `latest`** (ids 533–646): up to 4 skill panels (slots 1–4). Each panel
  unlocks at its own augment state and upgrades Ⅰ → Ⅱ → Ⅲ → Ⅳ as you augment.
- **Generation `old`** (ids 327–637): one signature skill that upgrades as you augment.
  Tiers come from the hero's own augment table, so the unlock state is exact.
- **Augment cost** is per step — what it takes to move from the previous state to that one.
- Blank English name/description means the game never shipped that string in any file.

## Index

| # | Hero | CN | DMG | DEF | AST | Gen |
|---|---|---|---|---|---|---|
{index}

---

"""


def main():
    out_dir = 'extracted/llm'
    if '--out' in sys.argv:
        out_dir = sys.argv[sys.argv.index('--out') + 1]
    out_path = os.path.join(os.path.dirname(__file__), '..', out_dir)
    os.makedirs(out_path, exist_ok=True)

    with open(os.path.join(EX, 'sss_database.json'), encoding='utf-8') as f:
        db = json.load(f)

    by_role = collections.defaultdict(list)
    for h in db:
        by_role[h['role']].append(h)

    for role in ROLE_ORDER:
        heroes = sorted(by_role[role], key=lambda x: x['id'])
        idx = '\n'.join(
            f"| {h['id']} | {cell(h['name_en']) or '—'} | {cell(h['name_cn'])} | "
            f"{h['ratings']['damage']} | {h['ratings']['defence']} | {h['ratings']['assist']} | "
            f"{h['generation']} |"
            for h in heroes
        )
        body = HEADER.format(title=role + 's', n=len(heroes), index=idx)
        body += '\n'.join(hero_md(h) for h in heroes)
        p = os.path.join(out_path, f'{role.lower()}s.md')
        with open(p, 'w', encoding='utf-8') as f:
            f.write(body)
        print(f'{p}  {len(heroes):>3} heroes  {os.path.getsize(p)/1024:.0f} KB')


if __name__ == '__main__':
    main()
