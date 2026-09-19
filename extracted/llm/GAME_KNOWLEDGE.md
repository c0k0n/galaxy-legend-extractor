# Galaxy Legend — Complete Game Knowledge Base

**Purpose.** This file exists so a language model can reason about Galaxy Legend without
guessing. It covers what the game is, how it is played, every major system, the combat
model, the progression economy, the event cadence, and the vocabulary the game uses
(including the gap between internal names and displayed names).

**How to read the confidence markers.** Galaxy Legend has very little official English
documentation, so claims here come from three tiers of source:

| Marker | Source | Trust |
|---|---|---|
| `[DATA]` | Read directly out of the shipped game files (v2.6.2) in this repository — localisation strings, data tables | Highest. This is the game describing itself |
| `[WIKI]` | The active fan wiki (galaxylegend.wiki), current to ~mid-2026 | Good, but community-authored and sometimes stale |
| `[INFERRED]` | Reasoning from the two above | Treat as a hypothesis |

Where a `[DATA]` and a `[WIKI]` claim conflict, the `[DATA]` claim is printed as fact and the
conflict is noted.

**Companion files in this folder.** `rangers.md`, `strikers.md`, `protectors.md`,
`destroyers.md`, `rovers.md`, `flagships.md` contain every SSS commander's full skill data.
This file gives you the frame to read those in. Load this one first.

---

## 1. What the game is

**Galaxy Legend** (Chinese: 银河传说, "Galaxy Legend"; also marketed as 银河传说：时空舰队,
"Galaxy Legend: Spacetime Fleet") is a free-to-play mobile strategy/RPG by **tap4fun**
(Chengdu Chuangrenzuoai / Chengdu Trident Technology), set in an original sci-fi space-war
setting. `[WIKI][DATA]`

- **Genre:** the developer's own pitch is "SLG + RPG" — a base-building strategy layer
  wrapped around a hero/commander-collecting RPG layer, with auto-battler combat
- **Platforms:** Android and iOS. Android released 2017-07-25; iOS app id `599877646`
- **Current version in this dataset:** 2.6.2 (Android), ~818 MB install
- **Persistence:** online-only, account-bound to a tap4fun account `[WIKI]`
- **Age rating / monetisation:** 16+, heavy in-app purchase. Premium currency is Credits;
  there is a deep VIP ladder (at least VIP 0–11) `[DATA]`
- **Longevity:** the game has run continuously since 2013 in some form; the 12th anniversary
  event ran in August 2026. It is a live-service game with a ~3-commanders-per-month release
  cadence and a permanently rotating event calendar `[WIKI]`

The official English tagline frames it as: build a galactic empire, assemble a fleet of
commanders, fight other players across nine star systems, uncover a rebel conspiracy.

### 1.1 The two-layer structure

Almost everything in Galaxy Legend belongs to one of two layers, and understanding which
layer a system lives in explains most of the game's design:

**Layer 1 — the planet (SLG).** You own a planet with buildings: a Citadel (hub), Research
Center, Engineering Hub, Construction Yard, Galactonite Center, Diplomacy Center,
Conservatory, Celestial Portal, Dexter's Lab, Control Hub. These produce resources, run
technologies, and gate account-wide power. `[DATA]`

**Layer 2 — the fleet (RPG).** You collect **commanders** — individual named characters who
each pilot a ship. You field up to five of them in a formation. Commanders have classes,
augment levels, skills, starships, medals, exteriors, and more. This is where essentially
all of the modern power and all of the monetisation live. `[WIKI][DATA]`

A useful mental model: the planet layer is the *engine room* that feeds the fleet layer, and
the fleet layer is what actually fights.

---

## 2. Setting and story

Narrative framing, from the game's own story strings and the official description. `[DATA]`

- **Year 2841 AD:** Earth is dying; humanity expands into the galaxy. This begins the
  **Galaxy Era (GE)** calendar.
- **GE 1131–1137:** war between the **Galaxy Empire** and the **Rebels** intensifies. The
  Empire's strongest commander, **General Hopkins**, vanishes after the Battle of the
  Triffid Nebula. Massive numbers of unexplained wormholes begin appearing near the galaxy.
- The player is cast as Hopkins's subordinate: put down the rebellion, restore the Empire's
  honour, become the new legend of the galaxy.
- Recurring proper nouns in the story strings: **Lawsry** (a border star district / planetary
  fortress, and the player's starting home), **Triffid Nebula**, **Zone NGC-6514**, the
  **Apostles**, the **Emma Empire** (an ally), the rebel leader **Raphael**, and a large
  cast of named imperial officers (Lyon, Sylver, O'Neal, Sophitia, Cassandra, Du'doria,
  Matthias, Batis, Bartholomew, Carter …).

Story content is delivered as **story battles** (campaign stages grouped into
constellations/chapters) with a 3-star rating per battle, plus **elite battles**. Full
constellation 3-star clears pay Credits. `[DATA]`

---

## 3. Commanders — the core concept

**A "commander" is one unit: a named character and their ship, treated as a single entity.**
The community and the game's own help text use *commander*, *ship*, *hero*, and
*fleet commander* interchangeably depending on the screen. Internally the data uses
`vessels`. `[DATA]`

Every commander has four fixed attributes: **[WIKI]**

1. **Type** — combat role (6 values)
2. **Class** — quality tier (A / S / SS-red / SS-dark / SSS / SP)
3. **Sex** — Female / Male / Gender-neutral / Non-biological
4. **Generation / release era** — not an official stat, but it strongly determines how the
   commander's skills are structured (see §7)

### 3.1 Type (role) — 6 types

The game's own type descriptors, straight from the localisation table: `[DATA]`

| # | Type | Official description | Attack |
|---|---|---|---|
| 1 | **Ranger** | "Equal physical attack(ATK) and defense(DEF)" | Physical (ATK) |
| 2 | **Striker** | "Strong physical attack(ATK) but weak physical defense(DEF)" | Physical (ATK) |
| 3 | **Protector** | "Strong physical defense(DEF) but weak physical attack(ATK)" | Physical (ATK) |
| 4 | **Destroyer** | "Strong energy attack(E-ATK) but weak physical attack(ATK) and defense(DEF)" | **Energy (E-ATK)** |
| 5 | **Rover** | "Support battle ship containing diversified control and assistive abilities" | Physical (ATK) |
| 6 | **Flagship** | *(`TYPE_6` exists; no `TYPE_6_DESC` string ships)* | Physical (ATK) |

An older in-game help entry gives a slightly different flavour for each, and is worth quoting
because it names the archetypes the way players talk about them: `[DATA]`

> Hero: Physical attack (ATK). Strong in all aspects.
> Rover: Physical attack (ATK). Good at debuff and buff skills but weak in defense.
> Ranger: Physical attack (ATK). Equal in attack and defense and skilled at dodging.
> Protector: Physical attack (ATK). Strong in defense and skilled at blocking but weak in attack.
> Striker: Physical attack (ATK). Strong in physical attack and also has a chance to deal critical damage but weak in defense.
> Destroyer: Energy attack (E-ATK). Ignores physical defense (DEF) and has a chance to deal critical damage, but very weak in defense.

Note the help text calls type 6 **"Hero"**, not Flagship — the older name for the role. Both
names appear in the wild.

**The Destroyer exception is the single most important rule in combat.** Destroyers use
**E-ATK** for their normal attacks, which is countered by **E-DEF**, not DEF. E-DEF is
"very limited and barely boosted, unlike DEF". Their special attack is countered by neither
DEF nor S-DEF. That asymmetry is why Destroyers dominate PvP. `[WIKI]`

**Flagship rule:** a fleet must contain exactly one Flagship — no more, no less. It is the
only mandatory slot. `[WIKI][DATA]`

### 3.2 Class (quality)

Low to high: `[WIKI]`

| Class | Colour | Notes |
|---|---|---|
| **A** | green | starter-tier |
| **S** | blue | |
| **SS red** | red | |
| **SS dark** | dark | explicitly designed as *weaker analogues* of red SS and SSS |
| **SSS** | gold | the only class that matters at endgame |
| **SP** | — | above SSS. Introduced July 2026; the first and only SP commander is Flagship **Jayce Lot - Silver Wolf** |

No new commanders have been released below SSS for a long time. At endgame you deploy
nothing but SSS. `[WIKI]`

### 3.3 Hull names are NOT roles

A common trap. The game has a separate set of 15 **hull model** names — Pegasus, Unicorn,
Sphinx, Stamen, Gorgon, Ares, Typho, Hera, Eos, Crius, Pride, Glutton, Envy, Greed, Wrath.
These are ship *chassis* (and the last five are a themed "seven deadly sins"-style set), **not**
combat roles. A ship's role comes from its type, never from its hull name. `[DATA]`

### 3.4 Population size

From the shipped data in this repository (v2.6.2): `[DATA]`

- **194 SSS commanders** total: Ranger 42, Striker 36, Protector 26, Destroyer 30,
  Rover 36, Flagship 24

From the fan wiki, for the whole game including all classes: `[WIKI]`

- **449 commanders** in game; 37 Flagships (22 SSS, 1 SP), 96 Rangers (40 SSS), 85 Strikers
  (36 SSS), 71 Protectors (26 SSS), 72 Destroyers (30 SSS), 93 Rovers (37 SSS), plus 68
  lieutenants (a category that intersects the others, 17 of them SSS)

New commanders arrive at roughly **3 per month**, historically one via Stellar Voyage, one
via a Carnival-type event, and one by other means. `[WIKI]`

### 3.5 Lieutenants (internally: Adjutants)

A lieutenant is a commander deployed *attached to* another commander rather than in a fleet
slot. Every fleet commander may have exactly one lieutenant. `[WIKI][DATA]`

- A lieutenant boosts its host's attributes and contributes its **own** lieutenant skills on
  top of the host's skills.
- Lieutenant skills are mostly **type-scoped passives**: "increases all friendly Protectors'
  HP +8%", "increases all friendly Destroyers' E-ATK +6000", "increases all friendly ships'
  Speed by 100". `[DATA]`
- Lieutenants **should be augmented while assigned** — that is the only improvement that
  affects them in the role.
- Lieutenants make poor fleet commanders: their skills in that role are very weak.
- Old (A/S class) lieutenants have **type compatibility restrictions** with their host;
  SS and SSS lieutenants work with any host. `[WIKI]`
- The interface is deliberately hidden: *Main interface → Fleet*, then on the Equip or Medal
  page, tap the **hexagonal window** near the ship image.

There are 16 SSS lieutenants: Adele, Yvonne, Kelly, Bonnie, Bebo, Hassan, Silvia, Sasha,
Kristen (Adele's Chest), Vera, Amber, Roselle (Challenge Trade Station), Welly,
EntropyZero, Jiang Changxing, Vid, Darius. `[WIKI]`

---

## 4. Fleet and formation

- A fleet holds **at most 5 commanders**, and **exactly one must be a Flagship**. With 6
  types and 5 slots you can never field all types at once. `[WIKI][DATA]`
- **Prestige** (a player rank resource, see §10) unlocks additional formation slots. Max is
  5. `[DATA]`
- Formation is a grid: **front row and back row**, with slots left to right.

**Attack order** (the game's own help text): `[DATA]`

> Ships in the front row attack first. Ships in the same row attack from left to right.
> Target order: attack the ship of the same line in the front first. If there are no ships in
> the same line, then attack ships of the adjoining line.
> Player attack order depends on players' total speed. If both sides have the same speed,
> then the attacker will attack first.

**How to raise Speed** (from the same help entry): level up ships; upgrade the four Engine
technologies in the Research Center (Basic / Enhanced / Advanced / Extra Dimensional Engine);
put high-speed ships in formation; equip Speed Galactonite; complete collections in League of
Heroes; specific lieutenant effects (e.g. Violette[+4] as lieutenant gives +100 speed per
Rover in formation; John gives each ship +10 speed).

**Attack direction / AoE patterns** a skill can have: `[DATA]`

`Single Attack` · `Vertical Attack` · `Horizontal Attack` · `Cross Attack` · `All Attack`

*(The internal keys are confusingly crossed: `DIRECTION_HORIZONTAL` renders as "Vertical
Attack" and `DIRECTION_VERTICAL` renders as "Horizontal Attack". Trust the rendered strings,
not the keys.)*

---

## 5. Combat model

Combat is **auto-resolved and turn-based** — you set the formation and the battle plays out
in rounds. Your inputs are all made before the fight.

### 5.1 The Accumulator and S-attacks

This is the core combat loop. `[DATA]`

- Every ship has an **Accumulator** that charges during battle.
- A ship gains **25 Accumulator** after attacking, countering, or being attacked (some ships
  are exceptions — check the skill text).
- At **100 Accumulator** the ship fires its **S-attack** (its skill) automatically on its next
  attack.
- Accumulator can exceed 100 (this is not displayed), and **a skill fired above 100 is
  proportionally more powerful**.
- Accumulator resets to **0** after an S-attack fires.
- Accumulator can be raised via Galactonite with the accumulator attribute; some augments and
  skills grant "new Accumulator effects".

Practical consequence: being attacked charges your skill. Fast, wide-AoE attackers feed the
enemy's skills. This is why Protectors and control effects matter.

### 5.2 Full stat glossary

From the game's own "Ship Attributes Guide" and parameter tables: `[DATA]`

| Stat | Meaning |
|---|---|
| **HP** | Life points. A ship is destroyed at 0 HP |
| **Shield** | Unique to Protectors. Absorbs damage *before* HP |
| **ATK** | Determines normal-attack damage (all types **except** Destroyers). Also affects S-attack damage (except Destroyers) |
| **DEF** | Reduces damage taken from physical attacks |
| **S-ATK** | Determines **skill** (S-attack) damage, for **all** ship types |
| **S-DEF** | Reduces damage taken from S-attacks |
| **E-ATK** | Determines normal-attack damage **for Destroyers only**; also their S-attack damage |
| **E-DEF** | Reduces damage taken from energy attacks. Rarely available and barely scalable |
| **Critical** | Chance to deal bonus damage. Affects normal and S-attacks |
| **Crit ATK** | % bonus to damage when a critical hit lands |
| **Anti Crit** | Reduces the chance of receiving a critical hit |
| **Hit Rate** | Chance to hit with normal or S-attacks |
| **Dodge** | Chance to evade an attack, including S-attacks |
| **Block** | Chance to block. Blocking a normal attack cuts damage 50% **and triggers a counter-attack**; blocking an S-attack cuts damage 50% only |
| **Penetration** | Lowers the chance your attacks get blocked |
| **Speed** | Decides which fleet attacks first |
| **Accum / Accumulator** | Charges the S-attack (see above) |
| **Damage Inc / Dec** | Global outgoing / incoming damage modifier |
| **S-Damage Inc / Dec** | Same, but for S-attacks specifically |
| **CR DMG RES** | Critical damage resistance |
| **Force** | The single-number power score the game shows for a fleet. Useful as a rough proxy only |

The three-way attack/defence axis (physical: ATK↔DEF · skill: S-ATK↔S-DEF · energy:
E-ATK↔E-DEF) is the thing to internalise. Most "why did I lose" questions resolve to an
axis mismatch.

### 5.3 Durability

Ships lose **1% durability per battle** (per primary battle; on Galaxy servers also per elite
battle). **Below 50% durability a ship's attributes are reduced.** Ships are repaired in the
Construction Yard. `[DATA]`

### 5.4 Supply

Battles consume **Supply**. Supply regenerates 1 per 30 minutes up to a cap of 20; login
packs give 5; levelling up restores to 20 if below 20; more can be bought. `[DATA]`

---

## 6. Augmentation — the central progression system

Augmentation ("改造" / "refit" in Chinese, sometimes "modification" in older English text) is
the oldest and still one of the most important commander power systems. It raises many
attributes and, for modern commanders, **improves their skills**. `[WIKI]`

### 6.1 The ladder

**This is the single most error-prone piece of vocabulary in the game.** The ladder is:

```
+0 → +1 → … → +15 → +T → +T1 → +T2 → +T3 → +T4 → Awaken → Second Awaken
```

Two things people get wrong:

1. **`+T` is its own state, one step below `+T1`** — it is *not* a shorthand for `+T1`. Both
   spellings appear in the game; some commanders display `+T`, others `+T1`, and they are
   consecutive rungs, not synonyms. `[DATA][WIKI]`
2. **Awaken and Second Awaken only exist for Flagships** (with rare exceptions noted below).
   Non-flagship SSS commanders cap at `+T4`. `[WIKI]`

Internally this is a `LEVEL` integer 0–21 in `heros_ability`. Mapping:

| LEVEL | 0–15 | 16 | 17 | 18 | 19 | 20 | 21 |
|---|---|---|---|---|---|---|---|
| Label | `+0`–`+15` | `+T` | `+T1` | `+T2` | `+T3` | `+T4` | `Awaken` |

*Verified three independent ways:* the fan wiki's augmentation cost tables list
`+15 → +T → +T1 → +T2 → +T3 → +T4` as five separate steps; Horus's authored Chinese skill
names put his tiers at `+T` / `+T3` / `+T4` for LEVELs 16 / 19 / 20 (confirmed in-game by the
user); and **no commander in the shipped data gets a new spell at LEVEL 21** — it is a
padding row. `[DATA][WIKI]`

### 6.2 Flagship augmentation works differently

Flagships get three special rules: `[WIKI]`

- **Success rate is always 100%.**
- **Augmentation is shared.** When you augment *any* flagship up to `+T4`, *all* other
  flagships gain the same level. Awaken and Second Awaken remain individual.
- **Awaken / Second Awaken require commander ship parts.** Other levels do not.
- Steps past `+15` require the rare **Galaxy Heart** material; other types do not.

Non-flagship rules, by contrast: `[WIKI]`

- **Success rate is not always 100%.** On failure, **80% of consumed materials are returned**.
  (Carnival-type events routinely grant 100% success rate for the featured new commander —
  this is a major, recurring reason to augment during events.) `[DATA][WIKI]`
- Each commander is augmented individually.
- **Augmentation to `+T` and above requires commander ship parts.**
- SS class commanders have **no `+T4`**.
- S and A class commanders have **no `+T` or higher** at all.

### 6.3 Materials

Non-flagship SSS, `+0 → +15`: **Class Chips** (type-specific: Flagship / Destroyer / Rover /
Ranger / Protector / Striker Chips) plus **Cubits**, then **Pandora Power Cores** at `+5→+7`,
then **Pandora Power Crystals** from `+7` onward. `[WIKI][DATA]`

Non-flagship SSS, `+15 → +T4`: **ship parts** + **Inert Alloy** + **Heated Alloy**, then
**Alien Essence** + **Transcendence Core** for the final `+T3 → +T4` step. `[WIKI]`

Flagship, `+15 → +T4`: **Galaxy Heart** + Inert Alloy + Heated Alloy, then Alien Essence +
Transcendence Core for `+T3 → +T4`.

Flagship Awaken: 60 ship parts, 100 Alien Essence, 100 Transcendence Core, 500 Galaxy Heart.
Second Awaken: 120 ship parts, 150 Alien Essence, 150 Transcendence Core, 800 Galaxy Heart. `[WIKI]`

The in-game help gives a slightly older, simpler breakdown that matches the shape: `[DATA]`

> Augmentation Materials: Ship augmentations from +1 to +5 require corresponding class chips.
> High level augmentations (+6,+7) require extra special materials: Pandora Power Cores.
> Augmentations from +8 to +15 require Pandora Power Crystals.

### 6.4 Revert

Augmentation can be **reverted**. Class Chips are refunded **100%**; Pandora Power Cores and
Crystals only **partially**; Cubits are **not** refunded. After a Breakthrough, the first
revert drops you to `+15`, and only a second revert takes you to `+0` — and after a
Breakthrough, all materials are returned. `[WIKI][DATA]`

### 6.5 Breakthrough

> Breakthrough: Heroes can use the "Breakthrough" function at Augmentation +15.
> Breakthrough Effects: New Accumulator effects, new Augmentation levels, and Legendary
> Equipment of higher star levels can be equipped to the Cabin. `[DATA]`

So `+15` is a soft wall: Breakthrough is what opens the `+T` ladder.

### 6.6 Known special cases `[WIKI]`

- **Theel** (red SS Destroyer) requires ship parts for *every* augmentation step — very
  unusual. Max is `+T3` like other SS. Worth doing, but for its out-of-battle economy
  effect, not for combat (see §13).
- **Snowchub** (SSS Striker) reportedly still has no `+T4`.
- **Natasha** and **Elijah** (SSS Flagships, possibly Erlang Shen too) reportedly have no
  Awaken levels.

---

## 7. Skills and skill tiers

### 7.1 Two commander generations

Commanders fall into two structural generations, and this is *not* the same as their release
date or id range. `[DATA]`

**`latest` generation (96 of the 194 SSS).** Four skill panels (slots 1–4). Each panel is its
own skill line that unlocks at its own augment level and then tiers up: Ⅰ → Ⅱ → Ⅲ → Ⅳ (and
rarely Ⅴ). Think of it as four independent mini-skills.

**`old` generation (98 of the 194 SSS).** One **signature skill** with a richer tier chain:
a base version plus Awaken / Second Awaken variants. Fewer, deeper lines.

> Important: generation is determined by **presence in the `heros_skill_skill` table**, not by
> id. Several `old`-generation commanders have ids above 532 (e.g. 476, 604, 620), so any
> "old = ids 327–532" rule-of-thumb is wrong.

### 7.2 Tier roman numerals

Tiers are shown as Ⅰ, Ⅱ, Ⅲ, Ⅳ, Ⅴ. `[DATA]`

### 7.3 How a tier's unlock level is determined

**The unlock augment is authored per version and written into the Chinese spell name.** It is
*not* a fixed function of the augment level. `[DATA]`

Canonical example — **Horus (460)**, Ranger, `old` generation:

```
LEVEL  0  spell   994   死亡沉寂 Ⅰ            →  +0
LEVEL 16  spell 10994   荷鲁斯+T，死亡沉寂Ⅱ   →  +T
LEVEL 19  spell 11994   荷鲁斯+T3，死亡沉寂Ⅲ  →  +T3
LEVEL 20  spell 12994   荷鲁斯+T4，死亡沉寂IV →  +T4
```

Note: **Horus has no `+T2` step and nothing at Awaken.** His skill chain simply stops at
`+T4` — he can still be augmented further, but his skill does not change. Confirmed in-game.

This is why an earlier version of this project printed Horus as `+T1 / +T4 / Awaken`: it
derived the label from the LEVEL with a fixed ladder instead of reading the authored marker,
and the fixed ladder was itself off by one from `+T` onward.

**Consequences to internalise:**

- Unlock levels are **per hero and may skip rungs**.
- Both `+T` and `+T1` spellings occur in real data. Do not normalise them.
- Where no authored marker exists, the ladder in §6.1 is used as a fallback — and that
  fallback is a guess, flagged as such.

### 7.4 Flagship Awaken skills

Flagships carry a **second skill table** (`flagship_awaken_skill`) holding the skill versions
granted at Awaken and Second Awaken. Critically, in the shipped data **this field is only
populated on the LEVEL 21 row** — reading LEVEL 0 returns an empty value silently. 13 heroes
have awaken skills this way. `[DATA]`

---

## 8. Other commander improvement systems

The fan wiki lists these as the permanent improvement paths: `[WIKI]`

| System | What it does |
|---|---|
| **Avatar frames** | cosmetic + small stats |
| **Equip** | five slots of ship equipment |
| **Augmentation** | §6 |
| **Officer Room / Lieutenant** | §3.5 |
| **Galactonite** | socketable gems |
| **Medal** (+ Empire HQ Medal Archive, Medal Skill) | five medal types, per-commander |
| **Cabin and Sets** (Manoinver's Cabin) | components + legendary equipment |
| **Starship** | per-commander ship, star level 1–20 |
| **Exterior** | cosmetic hull skin with real stats |
| **Potential and Potential Chip** | per-commander, includes Exclusive Chips |
| **Hall of Honor** | ranking / collection bonus |
| **League of Heroes** | collection bonus (also grants Speed) |
| **Control Hub Modules** | tactical modules with bonuses |
| **Masters** | goal-based bonuses (e.g. "Module Master") |
| **Research Center** | 4 tiers × 8 fleet technologies |
| **Armor Reshape** | per-part ship armor progression |
| **Hull Enhance** | hull enhancement, costs Tech Points |

Temporary: **Galaxy League** season bonus (long), **Coatings / Paintcoat** (24 h). `[DATA][WIKI]`

### 8.1 Equipment `[DATA]`

Five slots: **Main Artillery, Armor, Shield, Engine, Accelerator**. Equipment is typed
(Universal / Physical attack fleet / Energy attack fleet) and level-gated. Equipment is
**enhanced** in the Engineering Hub, and **upgraded** using **Plans** — each upgrade costs
5 enhancement levels. Plans come from Elite Challenges in the Conservatory and from the Shop.

### 8.2 Medals `[DATA][WIKI]`

- Five qualities: green < silver < purple < golden < **red**. Endgame uses red only.
- Five types: **Bravery** (ATK, E-ATK; red also CR DMG RES), **Cross** (DEF; red also Damage
  Inc), **Revolution** (S-ATK; red also S-Damage Dec), **Five-Star** (HP; red also S-Damage
  Inc), **Freedom** (S-DEF; red also Damage Dec). Every deployed commander can wear one of
  each type — 25 medals for a full fleet.
- Red medals enhance to **level 110** and upgrade to **rank 21**; rank upgrades require a
  minimum level. Rank 7+ on a red medal adds Speed.
- **Attribute modification** (red medals only) can push each attribute to **+150%** of base.
  It is stochastic. "Full 25 medal maximization is a process that will not end for most
  players' lifetime."
- **Medal Archive / Honor Combinations:** consume unequipped medals of rank ≤4 to activate
  combinations that give **fleet-wide** bonuses. Consumed medals yield Honor Points (blue 1,
  purple 8, golden 50, red 90) which unlock Achievement bonuses. Resettable.

### 8.3 Starship `[WIKI]`

A per-commander ship with a single stat: **star level 1→20** (SS/SSS start at 3★). Higher
stars are composed from lower ones plus **Starship Core**. Requirements escalate from "same
commander's starship" to "same type" to "any starship of a level". Starship mostly boosts
**defensive** attributes. **Starswap** lets you move star level between starships.
Advice from the wiki: don't push above 10★ until endgame, and never feed a commander's own
starship if you can feed an obsolete one.

### 8.4 Exterior `[WIKI]`

A cosmetic skin for SSS commanders (avatar + ship model) with real stats. Costs **120
Exterior Shards** to compose; not every SSS has one; a few have two. Three attribute tiers:
standard (+1200 Speed, +8% HP/DEF/S-DEF/Damage Inc/Damage Dec), high (Aiola: +2000 Speed,
+12%), low (+1000 Speed, +5% — only Immortal Vanguard: Hellfire and Horus: God of the Sky).
Upgradeable once (20 shards + 50k Exterior Tokens).

### 8.5 Galactonite `[DATA]`

Socketable gems, composed in the Galactonite Center (Laboratory / Advanced Laboratory).

- Levels are named **R-1 … R-9** (R-8 was long the cap; R-9 now appears in Galactonite
  Frenzy). Dual-Attribute Galactonite exists and counts as two types.
- **Composing** raises an energy level; higher energy = higher cost but better odds of high
  results. **Composition can fail** — at low energy some Cubits are refunded, at high energy
  none. The Advanced Laboratory **never fails**, caps at R-7, and costs Credits not Cubits.
- **Galactonite Energy** (used to level Galactonite) comes from decomposing unwanted
  Galactonite, diplomat Sokolov, and mining.
- A ship cannot hold two of the same type. Higher Galactonite Center level = more sockets.
- Only players **Lv. 50+** see all Laboratory types; the Advanced Laboratory has no
  restriction.

### 8.6 Control Hub / Modules `[DATA]`

Internally "Tactical Center". Equip **tactical modules** for stat bonuses; modules can be
enhanced, adjusted (free adjusts accumulate, up to 5), and decomposed.

### 8.7 Armor Reshape `[DATA]`

Per-part armor progression in the Construction Yard, with named parts: Command Room Shield,
Fleet Ship Keel, Pri-Engine Compartment, Pri-Reactor Armor, Fleet Armor. Each page must be
maxed to unlock the next. A flagship promotion gates higher caps. Allies can help speed it up.

### 8.8 Research Center `[DATA]`

**4 tiers × 8 technologies**, all fed by Tech Points:

| | Hull | Primary Gun | Armor | Firepower | Protection | Energy Output | Shield | Engine |
|---|---|---|---|---|---|---|---|---|
| Basic | Basic Hull | Basic Primary Gun | Basic Armor | Basic Firepower | Basic Protection | Basic Energy Output | Basic Shield | Basic Engine |
| Enhanced | Enhanced Hull | Enhanced Prim. Gun | Enhanced Armor | Enhanced Firepower | Enhanced Protection | Enhanced E-Output | Enhanced Shield | Enhanced Engine |
| Advanced | Advanced Hull | Adv Primary Gun | Advanced Armor | Advanced Firepower | Advanced Protection | Adv Energy Output | Advanced Shield | Advanced Engine |
| H-Dimension | H-Dimension Hull | H-Dimension Cannon | H-Dimension Armor | H-Dimension AP | H-Dimension SPE | H-Dimension Output | H-Dimension Shield | H-Dimension Engine |

### 8.9 Manoinver's Cabin `[DATA]`

Upgrade **Components** with **Dark Aerosiderites**. Legendary equipment amplifies Components
and adds unique special effects. Matching equipment colour to the slot unlocks active
effects; a mismatch gives only passive effects. Resettable (partial refund), or "Perfect
Reset" with Credits for a full refund.

---

## 9. Player progression: Force and level

**Force** is the single-number power score. The game's own list of permanent ways to raise it:
`[DATA]`

1. Increase Fleet level
2. Get new Ships from the Celestial Portal or events
3. Enhance and upgrade Ship equipment in the Engineering Hub
4. Upgrade Technology in the Research Center
5. Equip high-rank Galactonite, and upgrade Galactonite level
6. Reshape Armor in the Construction Yard
7. Use Class Chips, Pandora Power Cores and Crystals to augment ships
8. Adjust Ship Modules and save a better attribute bonus
9. Use Z-Bosons to interfere with equipment
10. Use Legendary Equipment in Manoinver's Cabin and upgrade Components

Temporary boosts: **Paintcoat** (24 h, applies in story/elite/Arena/Pandora/Conquer the
Cosmos), **Galaxy League** season bonus (monthly cycle), **daily Primus bonus** (14:58 UTC,
Primus only), **Primus Invasion** bonus (Fridays).

**Q-Interfere / Z-Boson** is a gamble layer: it can change equipment characteristics, has
different effects on different equipment types, a new interference **overrides** the previous
one, and is explicitly flagged in-game as an "emerging technology" with reliability
questions. `[DATA]`

**EXP sources:** rush story battles (donate to the Alliance first for a bonus), story battles,
elite battles, colony, battle training, main and daily tasks. `[DATA]`

---

## 10. Economy and currencies

| Currency | Role | Main sources |
|---|---|---|
| **Cubits** | Basic currency: buildings, equipment, Galactonite composing, ship repair, Armor Reshape | main/daily tasks, Citadel collection, diplomat Greenspan, story + elite battles, Arena, Infinite Cosmos, daily packs, Galaxy Slot, **Primus** (big), **Primus Invasion** (Fridays), **Mining** |
| **Credits** | Premium currency | login rewards, Month Card, Arena ranking, tasks/achievements, 3-starring a full constellation, rush battles, purchase, Galaxy League, Pandora Executive, Top-32 Cross-Cosmos |
| **Tech Points** | Research, Hull Enhance, temporary Force in Primus | diplomat Sonia, daily tasks, Chaos Quasar, daily packs, Galaxy Slot, **Arena** (large), **Pandora Cluster** (huge) |
| **Prestige** | Raises player Rank (better daily empire rewards), **unlocks Form Cells and Flagship skills** | diplomat Roosevelt, Infinite Cosmos, first storyline boss kills, mining, Arena daily rank, Primus rank, Cosmic Expedition |
| **Galactonite Energy** | Levels up Galactonite | diplomat Sokolov, decomposing Galactonite, mining |
| **Dark Aerosiderite** | Upgrades Cabin Components | Forest of Stellar Territory, selling Legendary Equipment |
| **Dexter Coins** | Free pulls on the Galaxy Slot | 5/day login, level-up gifts, main tasks |
| **Class Chips** (6 types) | Augmentation to +15 | 10 daily Arena battles → Class Chip Pack, weekly Wormhole, Pandora Ruling Star, Galaxy League, Galaxy Slot |
| **Pandora Power Core / Crystal** | Higher augmentation | Galaxy League exchange, Shop/Black Market/Event Center, Primus Invasion, Conquer the Cosmos, Corridor of Time and Space first-pass |
| **Exterior Token / Shard** | Exteriors | Exterior Shop, events |
| **Starship Core** | Starship star level | Starship Carnival, events, Pandora |
| **Challenge Coin** | Galaxy Challenge Season shop | Season tasks |
| **Galaxy Heart, Inert Alloy, Heated Alloy, Alien Essence, Transcendence Core** | Post-+15 augmentation | various events |

The wiki notes that at endgame **only two things consume more Cubits than you earn**: the
Mothership event (cabin upgrades) and unlocking Galactonite Center slots. `[WIKI]`

**Free Credits are genuinely farmable** — the wiki lists ~20 regular free sources
(Primus 100+/day, Free Month Card 80/day, Daily Mission packs 200/day, Free Pack 50/day,
Sign-in, Arena rank + battle rewards, SERVER GROUP BUY, Carnival Apex Leaderboard 5,000/day,
alliance gifting, compensation for downtime at ~500 Credits per planned maintenance). `[WIKI]`

---

## 11. Planet buildings `[DATA]`

| Building | Function |
|---|---|
| **Citadel** (internal: Planetary Fortress) | Central hub. Its level gates all economic and political development. Collect Cubits here |
| **Research Center** (Tech Lab) | Fleet technology R&D (§8.8) |
| **Engineering Hub** (Engineering Bay) | Enhance and upgrade ship weapons and defences |
| **Construction Yard** (Factory) | Repair fleet durability; Armor Reshape |
| **Galactonite Center** (Krypton Center) | Galactonite Lab + Equip center |
| **Diplomacy Center** (Affairs Hall) | Send **diplomats** out for resources. Named diplomats: Greenspan (Cubits), Sokolov (Galactonite Energy), Sonia (Tech Points), Roosevelt (Prestige) |
| **Conservatory** (Commander Academy) | Elite Challenges → equipment upgrade **Plans** |
| **Celestial Portal** (Star Portal) | Recruit ships and commanders |
| **Dexter's Lab** (Dicos Lab) | Combat hub: Primus, Primus Invasion, Mine, Battle Training, Galaxy Slot |
| **Control Hub** (Tactical Center) | Modules |
| **Arena** | PvP ladder |
| **Expedition Portal** (Spacewar) | Entry to Pandora Cluster |
| **Colony** | The colonization system |
| **Stellar Territory** | Territory mode (Forest of Stellar Territory) |
| **Conquer the Cosmos** | Monthly alliance PvP |

---

## 12. PvE content

- **Story battles / campaign** (`story`): chapters grouped into constellations, 3-star ratings.
  "Rush" mode speeds through them for EXP. VIP 5+ can skip battles. `[DATA]`
- **Elite battles** (`Elite Challenge`, in the Conservatory): harder versions; drop **Plans**.
  Refreshes are VIP-gated (VIP 3 → 3/day, VIP 6 → 5/day).
- **Chaos Quasar**: daily PvE with escalating waves. Has a "Restore" option to repair HP and
  shields mid-run and **Time Flip** to restart a Battle of Fate. You can even be matched
  against yourself. `[DATA]`
- **Infinite Cosmos → Worm Hole: Dimension Space**: a weekly (Mon–Sat) mode that drops Class
  Chip Fragments. Also a Prestige source. `[DATA]`
- **Corridor of Time and Space**: first-pass rewards include Pandora Core/Crystal fragments.
- **Conservatory**: 10 battles/day task; also Theel-gated extra rewards.
- **Mine** (in Dexter's Lab): **Mine Veins** of 9 ranks (Normal, Gas, Energy, Essence, Rare,
  Pilgrim, Plymouth, Historical Remains, Battle Ruins). Actions: Scan Veins, Advanced Scan,
  Scan Pure Veins (VIP 3+), Overclock, **Plunder** other players' mines. Major source of
  Cubits, Galactonite Energy, Tech Points, Prestige. `[DATA]`
- **Stellar Territory / Forest of Stellar Territory**: occupation, invasion, mining, plunder.
  Source of Dark Aerosiderites. `[DATA]`
- **Galaxy Trial**: a PvE ladder of 11 enemies ending in an endless-HP boss, central to
  Carnival events.
- **Void Rift**: a recurring 9-day PvE mode (a damage-ranking leaderboard).
- **Primus**: daily world boss, 15:00 UTC, 45 s hit cooldown (§14).
- **Mothership**: a large separate game mode (§16).

---

## 13. Commanders with out-of-battle effects

A small set of commanders change the *game* rather than the *battle*: `[WIKI]`

- **Theel** (red SS Destroyer, 80 ship parts to acquire, from Challenge Trade Station): owning
  and augmenting Theel makes **Mine Veins, Conservatory and Battle** produce additional
  rewards, scaling with his augment level. Every one of his augmentation steps costs ship
  parts. Purely an economy commander.
- **Hermes** (Ranger): owning Hermes unlocks the **Hermes token shop**; augmenting him widens
  its stock.
- **Kolossos** (Protector): owning and augmenting to +3+ affects **Stellar Territory** and
  **Galaxy Trial**.

---

## 14. PvP content

### Arena `[DATA]`
Challenge other players' fleets. Produces **Tech Points** (large), **Class Chips** (10 battles
daily → Class Chip Pack), **Prestige** (daily rank), **Credits** (rank rewards + 30/day for 5
battles). Players you beat land in your **Loser** list (see Colonization).

### Colonization `[DATA]`
A social dominance loop with its own full vocabulary:

- You can colonize players on your **Loser** list (people you beat in Arena) or your
  **Enemy** list (people who took a colony from you).
- Statuses: **Single Planet** (free), **Colony** (colonized), **Ruler** (holds colonies).
- Ruler actions: **Reap** accumulated EXP, **Command** (10 flavoured actions: Outage, Tax
  Check, War Game, Torture, Extort, Jeer, Almsgiving, Encourage, Praise, Canonize).
- Colonized player actions: **Overthrow**, **Protest** (10 flavoured: Paparazzi, Accident,
  Bomb, Outage, Trick, Prank, Curse, Gratitude, Visit, Tribute), **SOS** to allies → ally
  **Liberates** you.
- Colonized players **lose nothing** except the ability to colonize others.
- Rules: daily EXP caps per status; **level gap between players cannot exceed 15**; cooldowns
  on Command/Protest.

### Pandora Cluster `[WIKI][DATA]`
Weekly **3-day** (Sat–Mon) server-vs-server "king of the hill". Three randomly chosen servers;
same-server players are allies.

- Map: 25 vertices, 36 routes, with 3 homebases, a central **Ruling Star**, 3 White Holes,
  3 Headquarters (fire missiles), 3 Docks (resupply 1 Supply/12 s), and groups of Speedup /
  Hub / Anticlockwise / Uniting vertices, each with production and/or combat buffs.
- Fleets have **100 Supply**; losing all Supply kills the fleet → 15 min respawn at homebase
  (5 min during "Know the Nodes"). Winning costs the winner at least 10 Supply; every 20
  Supply lost removes one ship (the last in the acting chain).
- **Influence Points** rank both players and servers; tiered influence rewards (5/10/20/40/60/
  80/100/200/300/500/1000/1500/2000/3000) plus rank-group rewards.
- **Pandora Executive**: the highest-influence player on the side holding the Ruling Star.
  Gets periodic rewards, is visible on the map, and their location is announced.
- Two "Know the Nodes" sub-events run twice daily (Space Dock 30 min at 09:00/15:00 UTC;
  Ruling Star 1 h at 06:00/12:00 UTC).
- **Huge Tech Point source.** Also gives Class Chips at each Ruling Star reward.
- **Liora** (Destroyer) ship parts come *only* from Pandora rank 1–100.

### Galaxy League `[WIKI]`
A ~4-week season (e.g. 2026-08-14 – 2026-09-11). The main exchange source for **Class Chips,
Pandora Power Cores and Crystals**. Also grants a **temporary Force bonus** for the following
month.

### Fleet League `[WIKI]`
A ~monthly season (2026-09-01 – 2026-09-29). A common daily/weekly task source. Goes offline
for a few days each month.

### Empire Colosseum `[DATA]`
A **3v3 draft mode**, Lv. 90+. You pick ships *and lieutenants* from a randomly provided pool
and submit **three formations**. Normalisation: **all ships are Lv.100, Augmentation +15, max
Tech, max Armor Reshape**, and Module/Galactonite/Cabin bonuses are equalised within a class.
You are then matched for 20 battles. Scoring: 5 points for a "perfect" win (6+ surviving
ships), 3 for a win, 1 for a loss. Ranking is by score → success rate → fewest victories.

### Conquer the Cosmos `[DATA]`
Monthly **alliance** PvP. Source of Pandora Power Cores/Crystals at top ranks.

### Primus / Primus Invasion `[DATA][WIKI]`
- **Primus**: daily server-wide world boss, starts **15:00 UTC**, up to an hour or until
  slain, 45 s hit cooldown. Rewards Cubits (up to ~60m), Prestige (up to 10k), and Credits
  only if slain (1,200 / 800 / 600 for top 3). Bonus Cubits at 75/50/25% HP thresholds and for
  the last blow. Currently a "harmless punching bag" for endgame players — its real use is
  tuning a fleet.
- **Primus Invasion**: Fridays, 1:00 and 13:00 UTC. Big Cubits.

---

## 15. Alliance `[DATA]`

- Private chat with like-minded players.
- **Donating** once daily increases **Rush** story-battle EXP gain.
- **Cosmic Expedition**: get 6 allies together for a Prestige reward.
- **Conquer the Cosmos**: monthly alliance PvP.
- Alliance EXP accrues 1:1 with members' Prestige; each level adds +1 member cap.

---

## 16. Events — the calendar you actually live in

Events are the game. The wiki's timeline (current to Sept 2026) shows a dense, overlapping
schedule with **major** and **minor** tiers. `[WIKI]`

### Galaxy Challenge Season
The **permanent** event — 28 days (occasionally 29) with only a few days' gap between
seasons. Started 2020.

- Tasks: 4 **season** tasks (require the paid Season Pass), 14 **weekly** tasks added per week
  (56 total, need ≥10/14 for the week bonus), 3 **daily** tasks (84 total, randomly generated
  from a closed set; you may swap one per day).
- Completed tasks give **Tier Points** (100 season / 10–40 weekly / 3 daily). **80 Tiers × 10
  points** each. Tier 81+ gives 1 Eternal Friendship each.
- **Season Pass** tiers: $9.99 / $19.99 (+15 tiers) / $49.99 (+30) / $99.99 (+50). Extra tiers
  purchasable.
- Season tasks (stable across events): *Persistence* (log in 25 days — buy the Pass by day 4),
  *Social Butterfly* (send 50 gifts), *Galactic Ace* (3000 Influence in Pandora), *Big Shot*
  (purchase 15,000 Credits — costs ≥$99.99).
- **Challenge Trade Station** (shop, Challenge Coins only) sells SSS ship parts (e.g. Elowyn
  at 25 Coins/part, capped 120/season) and Starship Choice Packs (200 Coins).
- Widely considered **the best value purchase in the game**.

### Stellar Voyage (monthly, 10 days)
PvE/PvP hybrid, introduces a new **non-flagship** commander each month; those commanders are
usually very strong and comparatively hard to get.

- Travel **100,000 AU**; every 100 AU is an encounter; every 5,000 AU is a **cooperative
  boss** (10 h window, resurrects on death, blocks all player progress while alive, vanishes
  after 10 h regardless); final boss at 99,900 AU fights until 14:00 UTC on the last day.
- **Voyage Energy**: 10 energy per 100 AU, start with 500, regen 1 per 90 s (caps at 500),
  plunderable from other players.
- **Boss attack costs** escalate: 20, 20, 23, 27, 32, 40, 48, 59, 71, 84, 100, 116, 135, 155,
  176, 200, then 200 flat. A Conquest Permit gives one attack instead.
- **Assault Heroes**: each chapter 6 previously-released SSS commanders get **+500% damage to
  bosses** (3 for odd-numbered bosses, 3 for even).
- PvP: **energy plunder** (max 100/attack) via Voyage Radar, and **Voyage Arena** (5
  opponents, Courage points, no loss on attack, daily rank rewards at 23:55 UTC).
- Shops: Stellar Merchant Honor Token, Stellar Merchant Commemorative Coin.

### Carnival (monthly, 10 days)
Mostly PvE, introduces one new non-flagship commander, easier to obtain than Stellar Voyage
ones but usually slightly weaker. **100% augmentation success rate during the event.**
Composition system: 4 event items combine at ratios `1/2/5/10` → 1 ship part guaranteed;
weaker recipes give probabilistic results. Activities include Custom Wheel, Legendary Wheel,
Godlike Wheel, Galaxy Formation, Galaxy Trial, Slots Frenzy, Arcade, Stacking Rewards,
Treasure Hunt, Wish Recruit, Mystery Exchange, and an **Apex Leaderboard** paying 5,000
Credits/day to the top 200.

### Mothership (45 days, since late 2024)
Effectively **a game inside a game**, reached via *Vision of the Starfield*. Three stages:
3-day PvE prep, 39-day main (PvE+PvP), 3-day settlement.

- You assemble up to **5 Fleets**, each deploying up to **3 Motherships**.
- Motherships have **cabins** — Command (best: Flagship), Weapon (Striker), Energy
  (Destroyer), Armor (…). A hero's class, quality and augment level all affect cabin bonus,
  and each cabin has a best-fitting class.
- Cabins are upgraded; cabin level caps at the **Mothership level**. Motherships also have a
  **star level** (Gold Star → Orange Star) which determines how much **Energy** you can
  allocate across cabins.
- PvE: challenge Sector Stages for 15 Fuel per Mothership per challenge; wins grant Mothership
  EXP.
- **Commander Bonds**: all SSS commanders are divided into **20 bonds** (Empire Nobility,
  Empire Rebels, Roamer, Criminal, Mercenary, Machinery, Interstellar Warrior, Adventurer,
  Stellar Rogue, Bounty Hunter, Astroengeneer, Scientist, Star Spirit, Divine Apostile, Shadow
  Apostile, Evil Spirit, Galactic Deity, Augmented Person, Feral, Jedi). Assigning 2
  commanders at `+T` or 4 at `+T4` from the same bond to the same mothership's cabins grants
  bonuses — e.g. Astroengeneer: "+5% trigger chance of the assigned mothership's active
  weapon". `[WIKI][DATA]`

### Four-week catch-up cycle `[WIKI]`
Weeks start Tuesday: **Starship Carnival** → **Medal of Honor** → **Heroes' Rally** →
**Galactonite Frenzy**. Each week is themed around one improvement system.

- *Starship Carnival*: Space Exploration pools (Space / Class / Red SS / Purple SS / Gold SSS),
  Space Gems; score thresholds at 6k/12k/18k/24k/30k/40k.
- *Medal of Honor*: Medal Wheel, Medal Week Exchange Shop, Medal Ticket Special.
- *Heroes' Rally*: old-commander catch-up via **Celestial Portal** recruitment stations
  (Ranger&Striker / Protector&Destroyer&Rover / S class). 1 free draw per station per day,
  then 1,888 Credits per draw (20% off for 10×). **Guaranteed commander at the 10th draw.**
  The list has not been updated in years — not for endgame players.
- *Galactonite Frenzy*: Advanced Galactonite Laboratory, R-6 to R-9, including Dual-Attribute.

### Void Rift
A recurring 9-day PvE damage-ranking mode (`#8` ran 2026-08-01 – 08-09).

### Primus Invasion, Pandora
See §14.

### Irregular / seasonal
April Fool's Day (a Credits-spending catch-up with a tiered commander wheel), Anniversary
(September — 2026 was the 12th), Halloween, Christmas/New Year, Spring Festival, plus
recurring **SERVER GROUP BUY** (global progress unlocks shared stage rewards),
**Limited-Time Exchange**, **Hero Return**, **Stellar Treasure Hunt**, **Surprise Conveyor
Belt**, **Medal of Honor**, **Wheel of Fortune**, and **Space Station** (spend Credits → get
Cosmos Passes and Cubits).

---

## 17. Meta: which types and commanders are good

This is the most volatile part of the game and the most honest place to admit uncertainty.
`[WIKI]`

**Type-level meta (mid-2026):**

| Type | State |
|---|---|
| **Destroyer** | Strongest. You "definitely will use a destroyer in PvP, maybe even 2". E-ATK bypasses the well-scaled DEF stat |
| **Protector** | Strong. Rescued from a long crisis by Andrea and Selika (2023); Ironwall Prototype: Serratine (2025) raised the bar again. One or two is "a must" |
| **Rover** | Strong. Power players "always have a rover, sometimes even two". Modern rovers lean into debuffs (compare old-school Vaccine, late 2020, vs new-school Night Phantom, mid-2024) |
| **Flagship** | Mandatory by rule; modern ones are buffers and PvE damage dealers |
| **Striker** | In crisis. Lose to Destroyers on PvP damage and sometimes to modern Flagships on PvE. Some (Angelo, Tracy) are still good at PvE |
| **Ranger** | In the deepest crisis. Too average — worse than Strikers/Destroyers at damage, worse than Protectors at defence, worse than Flagships/Rovers at support. Power players often field none |

**Documented power-creep and counter chains** (a good illustration of how the meta moves):

- **Catherine** (Destroyer, early 2024, Stellar Voyage) — absolutely dominant; her **Dark
  Conceal** state (2 rounds at battle start and on revive/rebirth) opens at **`+T1`**.
- Countered (unsuccessfully) by **Viperian** (late 2024).
- Countered successfully by **Grusen** (mid-2025).
- Also countered by **Liora** (2025, Pandora).
- Catherine's decline is dated to roughly mid-2025.

**A recurring design pattern:** new commanders are released overtuned, dominate, and are then
explicitly countered by a later release. "Which augment level unlocks the broken effect" is
usually the single most important line in a commander's data — Catherine's whole dominance
hinged on `+T1`.

---

## 18. Vocabulary and naming traps

Things that will trip up a model reading this data:

| Trap | Reality |
|---|---|
| Hull names (Pegasus, Sphinx, Ares…) | Ship chassis, **not** combat roles. Roles come from type |
| "Hero" vs "Flagship" | Older name vs current name for type 6 |
| "Commander" / "ship" / "hero" | All the same unit |
| "Adjutant" | Internal name for **Lieutenant** |
| "改造" / "refit" / "modification" | **Augmentation** |
| `+T` vs `+T1` | Consecutive rungs, **not** synonyms |
| "Awaken +2" | An older string for **Second Awaken** (seen in 2023 event text for Janus and Chronos) |
| Generation ≠ id range | Determined by table presence; old-gen commanders exist with ids > 532 |
| `DIRECTION_HORIZONTAL` | Renders as "Vertical Attack" — the keys are crossed; trust the strings |
| "Force" | A composite power score, not a raw stat |

---

## 19. Known gaps and honest caveats

1. **Numeric `+N` markers in Chinese skill names are unreliable.** For `old`-generation
   heroes they often match the real unlock level; for `latest`-generation heroes they
   frequently **disagree with the level rows**. Example: Liora (607) slot 1 is named
   `莉奥拉+0 / +2 / +6 / +9` but the level rows give `+0 / +6 / +10 / +15`, while her slot 2
   matches exactly. This pipeline therefore trusts only the explicit `+T…` and `觉醒+N` forms
   and otherwise falls back to the level ladder. **Latest-generation slot-1 unlock levels may
   still be wrong for some heroes** and need an in-game check.
2. **Second Awaken is not represented in `heros_ability`.** The level table stops at 21
   (`Awaken`), and no commander gains a new spell at 21. Second Awaken skill data comes from
   `flagship_awaken_skill` and id-offset probing instead.
3. **15 `old`-generation heroes reach Second Awaken but have only one recorded skill
   version** (Elijah, Natasha, Erlang Shen, Kristen, Sasha, Silvia, Hassan, Bebo, Bonnie,
   Kelly, Yvonne, Amber, Vid, Jiang Changxing, Darius). Possibly correct (they are
   lieutenants, whose skills barely change), possibly a gap.
4. **`Spell.Spell`** (a 247 KB table declared in `data1.pak`) is not currently extractable;
   some skill text may live only there.
5. **Some names are missing from every shipped localisation file:** hero 643 (柯罗诺斯SP)
   English name, SP-hero skills 2032–2047, and Valdi's tier-Ⅴ name.
6. **The fan wiki has known blind spots** — its "Combat system", "Beginner Guide", and
   "Progression Tips" pages are linked but unwritten, and it notes that in August 2026 the
   major-event schedule broke (Stellar Voyage skipped, Mothership #14 delayed).
7. **Monetisation is deep.** VIP goes to at least 11, with per-level perks (Galactonite bag
   slots, daily supply purchase limits, Force collect limits, Elite Challenge refreshes, Pure
   Veins at VIP 3). Any "how strong can a player get" reasoning must account for spend.

---

## 20. Source notes

- **Shipped game data (v2.6.2)** — the highest-trust source. Localisation tables
  (`all_loc_en.json`: 10,011 menu strings, 4,264 fleet strings, 852 achievement strings,
  1376 story strings, 120 help entries, 90 tech entries), plus `heros_ability`,
  `heros_basic`, `heros_growing`, `heros_enhance`, `heros_skill_skill`,
  `v1_extrafleet_spells`.
- **galaxylegend.wiki** — active fan wiki, 46 pages, current to ~mid-2026. The authoritative
  community source for augmentation cost tables, event structures, the commander roster, and
  the type meta. Unofficial, and its commander counts differ slightly from the shipped data.
- **galaxylegend.fandom.com** — an older (2013-era) wiki. **Its pages are all empty stubs**;
  only the page *titles* survive, which is still useful as a list of systems the game has had
  since launch (Buildings, Currencies, Galactonites, Vip Levels, Prestige Rank, Dexters Lab,
  Conservatory, Diplomacy Center, …).
- **Official** — TapTap listing (Chinese description, release data), tap4fun.com.
- **This repository** — `docs/DATABASE_SCHEMA.md` for the exact output contract,
  `docs/PIPELINE.md` for how the data was produced and which regression guards exist.
