# Galaxy Legends Extractor — Agent Context

You are working on a pipeline that reads the shipped data files of **Galaxy Legends**
(Tap4Fun) and republishes them as structured, LLM-ready JSON.

**Read before changing anything:**

- [`docs/PIPELINE.md`](docs/PIPELINE.md) — the seven stages and the regression guards
- [`docs/DATA_FORMATS.md`](docs/DATA_FORMATS.md) — byte layouts for `pak`, `tfl`, loc tables
- [`docs/DATABASE_SCHEMA.md`](docs/DATABASE_SCHEMA.md) — the output contract and every field

This file does **not** restate those. It lists the traps: things that look reasonable, run
without error, and silently produce wrong data.

## Layout

```
AGENTS.md                  # this file
README.md                  # public landing page
LICENSE  NOTICE            # MIT for the code; NOTICE covers the game data
scripts/                   7 stages, standard library only
  extract_sss.py           #   1. data1.pak        → raw_tables/heros_*.json
  decrypt_tfl.py           #   2. *.tfl            → *.tfl.luac
  extract_tfl_data.py      #   3. *.tfl.luac       → loc/ + raw_tables/v1_extrafleet_spells.json
  extract_loc_tables.py    #   4. tap4fun.zip      → loc/all_loc_en.json
  build_sss_db.py          #   5. everything       → sss_database.json + by_class/
  render_handbook.py       #   6. database         → docs/heroes.html
  export_llm.py            #   7. database         → llm/<role>s.md
extracted/                 # committed output
  sss_database.json        #   primary deliverable
  by_class/ llm/           #   per-role JSON and Markdown
  loc/ raw_tables/         #   intermediates
docs/                      # PIPELINE, DATA_FORMATS, DATABASE_SCHEMA, heroes.html
data/                      # raw game files — gitignored, never commit
```

## Traps

**Formats**

- Loc table record lengths are **16-bit LE**. An 8-bit parse corrupts every string longer than
  127 bytes and desynchronises the whole table.
- The `.tfl` 16-byte prefix is ciphertext, not a header — decrypt the entire file. Plaintext
  starts `\x1bLuaQ`; `lua_Number` is an **8-byte double**; nested protos carry no magic header.
- `data1.pak` tables must be matched by the `GameData.<path>` declaration **at the head of the
  file** — several scripts merely reference the same paths.
- Lua table parsing needs brace matching; `condition` values contain nested braces.

**Skills**

- `heros_ability` holds a `SPELL_ID` **per LEVEL**. Reading only `LEVEL == 0` throws away the
  old-generation skill progression entirely (Horus 460: `994` → `10994` → `11994` → `12994`).
- **Group panels by slot, never by matching tier offsets.** `base + 110000` collides across
  panels; Qin Yue (628) steps by +10000 and came out as six panels with two tiers mis-numbered.
  Slots are what the game renders.
- **The augment label is authored, not derived.** It is written into the Chinese spell name
  (`荷鲁斯+T3，死亡沉寂Ⅲ`) and is per-hero: Horus skips +T2 and has nothing at Awaken. Use that
  marker first; fall back to the LEVEL ladder only when a name carries no marker. Never let a
  bare `+N` in a CN name override a real LEVEL row.
- **Offset probing collides across heroes.** `base + 110000` can land on a different hero's
  spell (Welly 620 → Roche 621's `洛希+6`). Reject a probed id when `heros_ability` gives it to
  someone else *and* its name does not name this hero. Sharing is legitimate for transform
  pairs (Wukong 470 / clone 471).
- `flagship_awaken_skill` is **populated only on the LEVEL 21 row** — reading LEVEL 0 returns
  `[]` silently.
- `30000` is a generic "unreleased" placeholder, always slot 4, on 30 heroes across all six
  roles. It is *not* flagship-specific. Drop it.
- Gaps are real. Valdi (550) ships Ⅰ, Ⅱ, Ⅳ, Ⅴ — no Ⅲ was ever shipped.

**Names**

- Prefer `loc/extra_text_cn.json` over data1.pak `VESSELS_NAME` for Chinese names — several
  heroes were renamed (587 is 冰怒 / Ice Fury, not 维拉).
- Item names need **both** loc sources for full coverage: `extra_text_en`
  `LC_ITEM_ITEM_NAME_<id>` for newer materials and `all_loc_en.item.ITEM_NAME_<id>` for older
  ones (chips 1201–1206, Pandora Power Core 1217, Pandora Power Crystal 20423).

**Dead data**

- `assess` is `30` for every hero at every level, across all 9,960 ability rows. It is not
  stored. Only `rate` (1–10) varies.
- Test heroes 998/999 are excluded; transform variants 530 and 536 are merged into 529 and 535
  as `transform`, not treated as separate heroes.

## After you change something

Changing stage 5 changes everything downstream — rerun 6 and 7 so `docs/heroes.html` and
`extracted/llm/*.md` do not drift from `sss_database.json`. Then check the guards in
`docs/PIPELINE.md`; each one exists because it broke once.

## Working preferences

- SSS heroes only; clean, LLM-ready JSON; per-role output files; tidy minimal file tree.
- The repo is public. `data/` is gitignored and must stay out of every commit, including
  history. No game asset is ever committed.
- When data is ambiguous, ask — the user will open the hero in-game and read the exact labels.
  Two rounds of "I assumed a fixed ladder" were wrong; one question settled it.
- Validate against an independent source, not your own assumptions.
