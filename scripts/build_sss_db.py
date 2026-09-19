#!/usr/bin/env python3
"""
build_sss_db.py — Stage 5: join the extracted tables into the SSS hero database.

Readable-schema rebuild (2026-09-18). Behaviour changed from the first version:

  * Skill panels are grouped by SLOT, not by guessing tier offsets across the whole
    hero. The old code matched `sid - 110000 in seen`, which collided whenever one
    hero's tier id happened to equal another panel's id — e.g. Qin Yue (628), whose
    4th slot steps by +10000 instead of +110000, was split into 6 panels with two
    tiers mis-numbered. Slots are what the game actually shows, so group by slot.
  * Tier numbers come from the id encoding when it decodes (110000/120000/130000/
    140000 -> II/III/IV/V, or the rarer +10000-per-tier scheme), and fall back to
    slot position. This keeps genuine gaps visible (Valdi's missing tier III).
  * `30000` is an "unreleased" placeholder, always in slot 4, and is NOT
    flagship-specific — 30 heroes across all six roles have it. Dropped.
  * `assess` is dropped: it is 30 for every SSS hero at every level (verified across
    all 9,960 heros_ability rows), so it carried zero information. Only `rate` varies.
  * Augment costs are parsed out of the raw Erlang-ish condition strings into
    {money, items:[{id, name, qty}]}, with item names resolved from both loc sources.

Inputs (in extracted/):
  raw_tables/heros_ability.json        - per-hero identity/stats (data1.pak)
  raw_tables/heros_skill_skill.json    - per-augment-level skill panels (latest gen)
  raw_tables/heros_enhance.json        - augment costs per level
  loc/all_loc_en.json                  - tap4fun.zip tables (old item names, TYPE_*)
  loc/extra_text_en.json / _cn.json    - EXTRA_TEXT TFL pairs (LC_NPC_*, LC_ITEM_*)
  raw_tables/v1_extrafleet_spells.json - old-gen spell table (awaken-tier CN names)

Outputs (in extracted/):
  sss_database.json       - all 194 SSS heroes
  by_class/<role>s.json   - per-role subsets
"""
import json, os, re

EX = os.path.join(os.path.dirname(__file__), '..', 'extracted')
ROLES = {1: 'Ranger', 2: 'Striker', 3: 'Protector', 4: 'Destroyer', 5: 'Rover', 6: 'Flagship'}
EXCLUDE_IDS = {998, 999}            # internal test heroes
VARIANT_IDS = {530: 529, 536: 535}  # transform forms -> base hero
UNRELEASED = 30000                  # "not yet released" placeholder skill id
SLOTS = ('skill_one', 'skill_two', 'skill_three', 'skill_four')
# Beyond Second Awaken the game has no known display name, so stay descriptive
# rather than inventing "Third Awaken" / "Fourth Awaken" as if they were real tiers.
AWAKEN_LABELS = ['Awaken', 'Second Awaken', 'Awaken +3', 'Awaken +4', 'Awaken +5']


def parse_awaken_sets(raw):
    """Parse heros_skill_skill's flagship_awaken_skill.

    Looks like  {{{1,131560},{2,121561},{3,131562}},{{1,131560},{2,131561},{3,131562}}}
    i.e. one group per awaken state (Awaken, then Second Awaken), each a list of
    {slot, skill_id}. 13 heroes carry it; the slot table's last row stops one or two
    tiers short of these, so without it their awaken skills are simply missing.
    """
    pairs = [(int(a), int(b)) for a, b in re.findall(r'\{(\d+),(\d+)\}', raw or '')]
    groups, cur = [], []
    for slot, sid in pairs:
        if slot == 1 and cur:
            groups.append(cur)
            cur = []
        cur.append((slot, sid))
    if cur:
        groups.append(cur)
    return groups
TIER_ROMAN = {1: 'Ⅰ', 2: 'Ⅱ', 3: 'Ⅲ', 4: 'Ⅳ', 5: 'Ⅴ'}
# Standard tier encoding: base+110000 = II, +120000 = III, +130000 = IV, +140000 = V.
OFFSET_TIER = {110000: 2, 120000: 3, 130000: 4, 140000: 5}


def load(name):
    with open(os.path.join(EX, name), encoding='utf-8') as f:
        return json.load(f)


def main():
    ability = load('raw_tables/heros_ability.json')
    skill = load('raw_tables/heros_skill_skill.json')
    enhance = load('raw_tables/heros_enhance.json')
    loc = load('loc/all_loc_en.json')
    fleet = loc['fleet']
    item_loc = loc.get('item', {})
    extra = load('loc/extra_text_en.json')
    extra_cn = load('loc/extra_text_cn.json')
    v1spells = load('raw_tables/v1_extrafleet_spells.json')

    lvl0 = {x['ID']: x for x in ability if x['LEVEL'] == 0}
    # SPELL_ID per augment LEVEL: this is where the old-gen skill progression lives.
    spell_by_level = {}
    for x in ability:
        spell_by_level.setdefault(x['ID'], {})[x['LEVEL']] = x['SPELL_ID']
    # Who actually owns a spell id. Needed to reject offset-probe collisions.
    spell_owners = {}
    for x in ability:
        spell_owners.setdefault(x['SPELL_ID'], set()).add(x['ID'])
    vessel_cn = {x['ID']: x['VESSELS_NAME'] for x in ability if x['LEVEL'] == 0}

    def level_seq(hid):
        """Ordered (augment_level, spell_id) change-points for a hero."""
        lv = spell_by_level.get(hid, {})
        out = []
        for level in sorted(lv):
            if not out or out[-1][1] != lv[level]:
                out.append((level, lv[level]))
        return out

    panels = {}
    for x in skill:
        panels.setdefault(x['ID'], {})[x['LEVEL']] = x
    costs = {}
    for e in enhance:
        costs.setdefault(e['ID'], {})[e['LEVEL']] = e['condition']

    # ---------- helpers ----------

    def item_name(iid):
        """Item names live in two places: newer ids only in EXTRA_TEXT, older
        (chips, Pandora cores) only in the tap4fun.zip item table."""
        return (extra.get(f'LC_ITEM_ITEM_NAME_{iid}')
                or item_loc.get(f'ITEM_NAME_{iid}')
                or '')

    def parse_cost(raw):
        """'[{item,{1203,5}},{money,100000}]' -> {'money':100000,'items':[...]}"""
        items, money = [], 0
        for m in re.finditer(r'\{item,\{(\d+),(\d+)\}\}', raw):
            iid, qty = m.group(1), int(m.group(2))
            entry = {'id': int(iid), 'qty': qty}
            nm = item_name(iid)
            if nm:
                entry['name'] = nm
            items.append(entry)
        for m in re.finditer(r'\{money,(\d+)\}', raw):
            money += int(m.group(1))
        out = {}
        if money:
            out['money'] = money
        if items:
            out['items'] = items
        return out

    def augment_label(level):
        """Fallback: internal augment LEVEL -> the label the game shows.

        Ladder (verified three ways: the fan wiki's augmentation tables, Horus's
        authored Chinese spell names checked in-game by the user, and the fact
        that no hero gets a new spell at L21 - it is a padding row):

            L0..L15 -> +0 .. +15
            L16     -> +T      (bare T, a state of its own - NOT the same as +T1)
            L17..L20-> +T1..+T4
            L21     -> Awaken

        An earlier version mapped 16->+T1 ... 20->Awaken, i.e. off by one from
        L16 up. That is what made Horus read "+T1/+T4/Awaken" when the game says
        "+T/+T3/+T4".
        """
        if level <= 15:
            return f'+{level}'
        if level == 16:
            return '+T'
        if level <= 20:
            return f'+T{level - 16}'
        return 'Awaken'

    def augment_marker(name_cn):
        """The unlock augment the game itself authored, read off the Chinese spell
        name: '荷鲁斯+T3，死亡沉寂Ⅲ' -> '+T3'.

        This is per-hero, not a function of the augment LEVEL row. Horus unlocks
        Dead Silence Ⅲ at +T3 and Ⅳ at +T4 and then has nothing further at Awaken;
        deriving the label from LEVEL instead (19 -> +T4, 20 -> Awaken) is what
        used to put a phantom 'Awaken' tier on heroes that cap at +T4. The client
        shows these authored strings, so prefer them whenever they exist.

        Some heroes write a bare '+T' where others write '+T1' - that variance is
        real and comes from the data, so it is preserved rather than normalised.
        """
        m = re.search(r'\+(T\d*)', name_cn or '')
        return '+' + m.group(1) if m else ''

    def level_marker(name_cn):
        """Augment written as a number or as an awaken count: '洛希+6' -> '+6',
        '双生之魂，觉醒+2，坚毅' -> 'Second Awaken'."""
        m = re.search(r'觉醒\s*\+?(\d*)', name_cn or '')
        if m:
            n = int(m.group(1) or 1)
            return AWAKEN_LABELS[n - 1] if n <= len(AWAKEN_LABELS) else f'Awaken +{n}'
        m = re.search(r'\+(\d{1,2})(?!\s*%)', name_cn or '')
        if m:
            n = int(m.group(1))
            if n <= 21:
                return augment_label(n)
        return ''

    def pick_augment(name_cn, fallback, last_rank=-1):
        """Authored marker wins, but only when it moves the chain forward.

        Several heroes reuse one marker across tiers — Wukong (470) writes '+13' on
        both tier Ⅱ and tier Ⅳ — so a marker that repeats or goes backwards is
        dropped in favour of the fallback rather than trusted.
        """
        for lbl in (augment_marker(name_cn), level_marker(name_cn)):
            if lbl and augment_rank(lbl) > last_rank:
                return lbl
        return fallback

    def belongs_to(sid, hid):
        """Guard for the offset probe, which can land on an unrelated hero's spell:
        Welly (620) probing +110000 reaches 131949 = '洛希+6', which heros_ability
        assigns to Roche (621), not Welly.

        Sharing is legitimate too — Wukong's clone (471) uses 470's ids — so an id
        is kept when its name mentions the hero, and only rejected when it both
        belongs to someone else and names a different ship.
        """
        owners = spell_owners.get(sid)
        if not owners or hid in owners:
            return True
        me = re.sub(r'[^\u4e00-\u9fff]', '', vessel_cn.get(hid, '') or '')
        return bool(me) and me in re.sub(
            r'[^\u4e00-\u9fff]', '', v1spells.get(str(sid), {}).get('spell_name', '') or '')

    def augment_rank(label):
        """Sortable rank for an augment label; -1 when it does not parse."""
        label = (label or '').strip()
        if label.startswith('+T'):
            # '+T' is its own state, one step below '+T1' - not a synonym for it.
            return 100 if label == '+T' else 100 + int(label[2:])
        if label in AWAKEN_LABELS:
            return 200 + 100 * AWAKEN_LABELS.index(label)
        m = re.fullmatch(r'\+(\d+)', label)
        return int(m.group(1)) if m else -1

    def tier_of(sid, base):
        """Decode a tier number from a skill id, or None if it does not decode."""
        t = OFFSET_TIER.get(sid - base)
        if t:
            return t
        d = sid - base
        # rarer scheme: +10000 per tier (Qin Yue's 4th slot)
        if 0 < d < 100000 and d % 10000 == 0:
            return d // 10000 + 1
        return None

    def strip_tier_suffix(name):
        """'Astral BastionⅠ' -> 'Astral Bastion'. The game mixes unicode numerals
        (Ⅰ-Ⅲ) with ASCII 'IV', so strip both."""
        return re.sub(r'(?:[ⅠⅡⅢⅣⅤ]+|IV|V)$', '', name).strip()

    def tier_from_name(name, fallback):
        """The skill's own name carries its tier numeral ('Dead Silence Ⅱ',
        'Final Glory II'). Prefer that over anything we compute."""
        m = re.search(r'(Ⅰ|Ⅱ|Ⅲ|Ⅳ|Ⅴ|Ⅵ|VII|VIII|VI|IV|V|III|II|I)\s*$', name or '')
        if m:
            return m.group(1)
        return TIER_ROMAN.get(fallback, str(fallback))

    def skill_named(sid):
        """True if the game shipped a name for this skill id."""
        s = str(sid)
        return bool((fleet.get(f'SKILL_NAME_{s}') or extra.get(f'LC_FLEET_SKILL_NAME_{s}')
                     or v1spells.get(s, {}).get('spell_name') or '').strip())

    def skill_info(sid):
        """Localized name/description for a skill id."""
        s = str(sid)
        n = (fleet.get(f'SKILL_NAME_{s}') or extra.get(f'LC_FLEET_SKILL_NAME_{s}') or '').strip()
        d = (fleet.get(f'SKILL_DES_{s}') or extra.get(f'LC_FLEET_SKILL_DES_{s}') or '').strip()
        name_cn = v1spells.get(s, {}).get('spell_name', '')
        out = {'id': sid}
        if n:
            out['name_en'] = n
        if name_cn:
            out['name_cn'] = name_cn
        if d:
            out['description_en'] = d
        return out

    def build_old_gen(h, level_spells):
        """Old-gen: one signature skill that upgrades as you augment.

        The authoritative progression is `heros_ability`'s SPELL_ID per augment LEVEL —
        reading only LEVEL 0 (as the first version did) throws away the whole chain.
        Horus (460) is the canonical case: 994 at +0, 10994 at +T, 11994 at +T3,
        12994 at +T4. Note the gaps — he has no Ⅱ-at-+T2 and nothing at Awaken,
        which is why the label must come from the authored name, not the LEVEL.

        A second, disjoint mechanism also exists: some heroes ship further tiers only as
        id offsets (+110000/+120000/+130000/+140000 = tiers Ⅱ/Ⅲ/Ⅳ/Ⅴ) with no level row,
        e.g. Janus (529). Append those when the game gave them a name.
        """
        out, seen, last_rank = [], set(), -1
        for i, (level, sid) in enumerate(level_spells, start=1):
            if sid in seen:
                continue
            seen.add(sid)
            info = skill_info(sid)
            info['tier_label'] = tier_from_name(info.get('name_en', ''), i)
            # Here we HAVE a real level row, so the level wins; only an explicit
            # T-marker overrides it. (A bare '+N' in the name is not trusted here —
            # Liora 607's slot 1 names say +2/+6/+9 where the level rows say +6/+10/+15.)
            lbl = augment_marker(info.get('name_cn', '')) or augment_label(level)
            info['from_augment'] = lbl
            last_rank = augment_rank(lbl)
            out.append(info)
        base = h['SPELL_ID']
        # Tiers beyond Ⅰ use one of two alternative id encodings, never both:
        #   small steps  +10000/+11000/+12000/+13000/+14000  = tiers Ⅱ…Ⅵ
        #   large steps  +110000/+120000/+130000/+140000     = tiers Ⅱ…Ⅴ
        # A few heroes (Valerian 451, Sorcerer Supreme 440, Medusa 476) carry only
        # small-step variants with no level rows at all, so probe both families.
        cand = []
        for off, fb in ((10000, 2), (11000, 3), (12000, 4), (13000, 5), (14000, 6),
                        (110000, 2), (120000, 3), (130000, 4), (140000, 5)):
            sid = base + off
            if sid in seen or not skill_named(sid):
                continue
            if not belongs_to(sid, h['ID']):
                continue          # id collision: another hero's spell, not a variant
            cand.append((fb, off, sid))
        for i, (fb, _off, sid) in enumerate(sorted(cand)):
            info = skill_info(sid)
            info['tier_label'] = tier_from_name(info.get('name_en', ''), fb)
            # Authored marker wins here too, but heroes found only via id offset
            # (Valerian 451) carry no marker, so they keep the Awaken ladder.
            fallback = (AWAKEN_LABELS[i] if i < len(AWAKEN_LABELS)
                        else f'Awaken +{i + 1}')
            lbl = pick_augment(info.get('name_cn', ''), fallback, last_rank)
            info['from_augment'] = lbl
            last_rank = augment_rank(lbl)
            out.append(info)
        return out

    def build_latest_gen(hid):
        """533-646 (96 heroes): one panel per slot, each with its own tier chain."""
        lv = panels[hid]
        # slot -> ordered list of (augment_level, skill_id), ignoring 0 / 30000
        seqs = {i: [] for i in range(4)}
        for level in sorted(lv):
            row = lv[level]
            for i, key in enumerate(SLOTS):
                v = row[key]
                if not v or v == UNRELEASED:
                    continue
                if not seqs[i] or seqs[i][-1][1] != v:
                    seqs[i].append((level, v))

        out = []
        for i in range(4):
            seq = seqs[i]
            if not seq:
                continue
            base = seq[0][1]
            tiers, used = [], set()
            for pos, (level, sid) in enumerate(seq, start=1):
                tier = tier_of(sid, base) or pos
                if tier in used:            # defensive: never emit a duplicate tier
                    continue
                used.add(tier)
                info = skill_info(sid)
                info['tier'] = tier
                info['tier_label'] = TIER_ROMAN.get(tier, str(tier))
                info['from_augment'] = augment_label(level)
                tiers.append(info)
            tiers.sort(key=lambda t: t['tier'])
            first_name = tiers[0].get('name_en', '')
            panel = {
                'slot': i + 1,
                'name_en': strip_tier_suffix(first_name) or first_name,
                'unlocks_at': tiers[0]['from_augment'],
                'tiers': tiers,
            }
            out.append(panel)

        # 13 heroes ship an extra Awaken / Second Awaken set: per-slot skill ids the
        # slot table never reaches (its L21 row stops a tier or two short). The field
        # is only populated on the LEVEL 21 row, so scan for it rather than read L0.
        bases = {i + 1: seqs[i][0][1] for i in range(4) if seqs[i]}
        awaken_raw = next((lv[l].get('flagship_awaken_skill') for l in sorted(lv)
                           if (lv[l].get('flagship_awaken_skill') or '[]') != '[]'), '')
        for gi, grp in enumerate(parse_awaken_sets(awaken_raw)):
            label = AWAKEN_LABELS[gi] if gi < len(AWAKEN_LABELS) else f'Awaken +{gi + 1}'
            for slot, sid in grp:
                panel = next((p for p in out if p['slot'] == slot), None)
                if not panel or sid in [t['id'] for t in panel['tiers']]:
                    continue
                tier = tier_of(sid, bases.get(slot, sid))
                if tier is None or tier in [t['tier'] for t in panel['tiers']]:
                    tier = max(t['tier'] for t in panel['tiers']) + 1
                info = skill_info(sid)
                info['tier'] = tier
                info['tier_label'] = TIER_ROMAN.get(tier, str(tier))
                info['from_augment'] = label
                panel['tiers'].append(info)
            for p in out:
                p['tiers'].sort(key=lambda t: t['tier'])
        return out

    # ---------- build ----------

    db = []
    for hid, h in sorted(lvl0.items()):
        if h['Rank'] not in (100, 200):
            continue
        if hid in EXCLUDE_IDS or hid in VARIANT_IDS:
            continue
        if not (extra.get(f'LC_NPC_NPC_{hid}', '') or '').strip() \
           and str(h['VESSELS_NAME']).strip() in ('', 'nan'):
            continue

        entry = {
            'id': hid,
            'name_en': (extra.get(f'LC_NPC_NPC_{hid}') or '').strip(),
            'name_cn': (extra_cn.get(f'LC_NPC_NPC_{hid}') or str(h['VESSELS_NAME'])).strip(),
            'role': ROLES.get(h['vessels'], str(h['vessels'])),
            'attack_type': 'physical' if h['ATK_TYPE'] == 1 else 'energy',
            # assess is 30 for every SSS hero at every level — only rate carries signal
            'ratings': {
                'damage': h['Damage_Rate'],
                'defence': h['Defence_Rate'],
                'assist': h['Assist_Rate'],
            },
            'assets': {'ship': h['SHIP'], 'avatar': h['AVATAR'], 'pic': h['PIC']},
            'generation': 'latest' if hid in panels else 'old',
            'main_spell_id': h['SPELL_ID'],
            'skills': build_latest_gen(hid) if hid in panels else build_old_gen(h, level_seq(hid)),
        }
        if hid in costs:
            entry['augment'] = [
                dict(to=augment_label(l), **parse_cost(costs[hid][l]))
                for l in sorted(costs[hid])
            ]
        db.append(entry)

    # merge transform variants into their base heroes
    for var, base in VARIANT_IDS.items():
        b = next((x for x in db if x['id'] == base), None)
        v = lvl0.get(var)
        if b and v:
            b['transform'] = {
                'id': var,
                'name_cn': str(v['VESSELS_NAME']),
                'main_spell_id': v['SPELL_ID'],
                'assets': {'ship': v['SHIP'], 'avatar': v['AVATAR']},
                'skills': build_old_gen(v, level_seq(var)),
            }

    with open(os.path.join(EX, 'sss_database.json'), 'w', encoding='utf-8') as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

    by_class = {}
    for h in db:
        by_class.setdefault(h['role'].lower(), []).append(h)
    bc_dir = os.path.join(EX, 'by_class')
    os.makedirs(bc_dir, exist_ok=True)
    for role, heroes in by_class.items():
        with open(os.path.join(bc_dir, f'{role}s.json'), 'w', encoding='utf-8') as f:
            json.dump(heroes, f, ensure_ascii=False, indent=2)

    gen = {'latest': sum(1 for h in db if h['generation'] == 'latest'),
           'old': sum(1 for h in db if h['generation'] == 'old')}
    print(f'built {len(db)} heroes; generations: {gen}; classes: '
          f'{ {r: len(v) for r, v in sorted(by_class.items())} }')


if __name__ == '__main__':
    main()
