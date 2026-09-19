# Galaxy Legends — SSS Strikers (36 heroes)

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
| 327 | Illusion Spirit | 幻象之灵 | 10 | 5 | 5 | old |
| 371 | Rowen | 罗恩 | 8 | 8 | 6 | old |
| 381 | Logan | 罗根 | 10 | 6 | 1 | old |
| 383 | Enfar | 阿恩法 | 7 | 7 | 6 | old |
| 391 | Samedi | 萨麦迪 | 9 | 6 | 4 | old |
| 411 | Frances | 法兰希斯 | 9 | 5 | 6 | old |
| 442 | Beamon | 比蒙 | 9 | 8 | 10 | old |
| 449 | Immortal Vanguard | 不死先锋 | 10 | 7 | 8 | old |
| 476 | Medusa | 美杜莎 | 10 | 7 | 8 | old |
| 485 | Yone | 元 | 10 | 7 | 8 | old |
| 490 | Snowchub | 雪胖胖 | 10 | 7 | 8 | old |
| 496 | Tracy | 特蕾希 | 9 | 8 | 10 | old |
| 505 | Wulkas | 乌卡斯 | 10 | 7 | 8 | old |
| 515 | Negris | 奈格利斯 | 10 | 7 | 8 | old |
| 516 | Aidas | 艾达丝 | 9 | 8 | 10 | old |
| 537 | Silvia | 索菲亚 | 10 | 7 | 8 | old |
| 542 | Yvette | 伊薇特 | 10 | 7 | 8 | latest |
| 543 | Kane | 卡因 | 10 | 7 | 8 | latest |
| 554 | Angelo | 安杰罗 | 9 | 8 | 10 | latest |
| 556 | Bebo | 贝波 | 9 | 8 | 10 | old |
| 561 | Alana | 阿兰 | 9 | 5 | 6 | latest |
| 568 | Yvonne | 伊温 | 9 | 8 | 10 | old |
| 573 | Viollet Gray | 维奥莱·格雷斯 | 10 | 7 | 8 | latest |
| 574 | Woon Lionel | 乌恩·莱奥尼尔 | 10 | 7 | 8 | latest |
| 575 | Mond | 蒙德 | 10 | 7 | 8 | latest |
| 583 | Ignis | 伊格尼斯 | 9 | 8 | 10 | latest |
| 590 | Chun Hua | 春华 | 9 | 8 | 10 | latest |
| 597 | Eric Valk | 艾瑞克·瓦尔克 | 10 | 7 | 8 | latest |
| 603 | Karl Drakk | 卡尔·德拉克 | 9 | 8 | 10 | latest |
| 613 | Mu | 穆 | 10 | 6 | 9 | latest |
| 617 | Liser | 利瑟 | 10 | 7 | 9 | latest |
| 620 | Welly | 维利 | 10 | 7 | 8 | old |
| 623 | Zerina | 泽瑞娜 | 10 | 7 | 8 | latest |
| 627 | Lin Xingyao | 林星遥 | 10 | 7 | 10 | latest |
| 636 | Kaelum | 凯勒姆 | 9 | 7 | 9 | latest |
| 637 | Darius | 达里厄 | 7 | 7 | 9 | old |

---

## 327 · Illusion Spirit 幻象之灵
**Role** Striker · **Attack** physical · **Generation** old
**Ratings** Damage 10/10 · Defence 5/10 · Assist 5/10

### Signature skill
- **I** at `+0` — Photon Impulsion I (3月WD打击者)
  Vertical attack, plunders targets' S-DEF by 50% and deal 152% S-ATK damage, lasting for 1 round. And then deals 50% of the previous total damage to all enemies having more than 65% HP (ignores defense).
- **II** at `+T2` — Photon Impulsion II (幻想之灵+T2)
  Vertical attack, plunders targets' S-DEF by 70% and deal 250% S-ATK damage, lasting for 1 round. And then deals 100% of the previous total damage to all enemies having more than 65% HP (ignores defense).
- **Ⅲ** at `+T4` — Photon ImpulsionⅢ (幻想之灵+T4)
  Vertical attack, absorbs 80% S-DEF and DEF from the attacked target for one round, and deals 320% S-ATK damage. Then, it deals 180% of the first stage S-ATK total damage (True Damage) to each enemy ship with more than 50% HP (ignores defense).

### Augment cost (per step)
- `+1` — 5× Striker Chip · 100,000 money
- `+2` — 10× Striker Chip · 200,000 money
- `+3` — 21× Striker Chip · 300,000 money
- `+4` — 28× Striker Chip · 500,000 money
- `+5` — 35× Striker Chip · 800,000 money
- `+6` — 42× Striker Chip · 10× Pandora Power Core
- `+7` — 49× Striker Chip · 50× Pandora Power Core
- `+8` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Illusion Spirit’s Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Illusion Spirit’s Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Illusion Spirit’s Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Illusion Spirit’s Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Illusion Spirit’s Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Illusion Spirit’s Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 371 · Rowen 罗恩
**Role** Striker · **Attack** physical · **Generation** old
**Ratings** Damage 8/10 · Defence 8/10 · Assist 6/10

### Signature skill
- **Ⅰ** at `+0` — Earl's Rage (九月wd)
  Cross attack, plunders 35% Hit Rate from all enemies and then deals 250% S-ATK damage and 7M True Damage. It will also activate a BUFF which can reduce 50% receiving damage for self, lasting for two rounds.
- **Ⅱ** at `+T4` — Earl's RageⅡ (罗恩)
  Cross attack, plunders 45% Hit Rate from all enemies and then deals 280% S-ATK damage and 8M True Damage. It will also activate a BUFF which can reduce 80% receiving damage for self, lasting for two rounds.

### Augment cost (per step)
- `+1` — 5× Striker Chip · 100,000 money
- `+2` — 10× Striker Chip · 200,000 money
- `+3` — 21× Striker Chip · 300,000 money
- `+4` — 28× Striker Chip · 500,000 money
- `+5` — 35× Striker Chip · 800,000 money
- `+6` — 42× Striker Chip · 10× Pandora Power Core
- `+7` — 49× Striker Chip · 50× Pandora Power Core
- `+8` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Rowen Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Rowen Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Rowen Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Rowen Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Rowen Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Rowen Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 381 · Logan 罗根
**Role** Striker · **Attack** physical · **Generation** old
**Ratings** Damage 10/10 · Defence 6/10 · Assist 1/10

### Signature skill
- **Ⅰ** at `+0` — Alloy Strike (1月wd)
  Single attack, attack 5 times continuously and each attack will deal 250% S-ATK damage. After the attacks, the ship has a 80% chance to enter stasis state for 1 round. When in stasis state, the ship can withstand lethal damage one time. In addition, increases 100 Accumulator for the ship itself.
- **Ⅱ** at `+T2` — Alloy Strike Ⅱ (罗根+T2)
  Single attack, attack 5 times continuously and each attack will deal 260% S-ATK damage. After the attacks, the ship has a 100% chance to enter stasis state for 1 round. When in stasis state, the ship can withstand lethal damage one time. In addition, increases 100 Accumulator for the ship itself.
- **III** at `+T4` — Alloy Strike III (罗根，合金打击)
  Single attack, attack 5 times continuously and each attack will deal 320% S-ATK damage. After the attacks, the ship has a 100% chance to enter stasis state for 1 round. When in stasis state, the ship can withstand lethal damage one time. In addition, increases 100 Accumulator for the ship itself.

### Augment cost (per step)
- `+1` — 5× Striker Chip · 100,000 money
- `+2` — 10× Striker Chip · 200,000 money
- `+3` — 21× Striker Chip · 300,000 money
- `+4` — 28× Striker Chip · 500,000 money
- `+5` — 35× Striker Chip · 800,000 money
- `+6` — 42× Striker Chip · 10× Pandora Power Core
- `+7` — 49× Striker Chip · 50× Pandora Power Core
- `+8` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Logan’s Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Logan’s Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Logan’s Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Logan’s Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Logan’s Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Logan’s Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 383 · Enfar 阿恩法
**Role** Striker · **Attack** physical · **Generation** old
**Ratings** Damage 7/10 · Defence 7/10 · Assist 6/10

### Signature skill
- **I** at `+0` — Charge Force I (阿恩法，冲锋之力)
  Vertical attack, plunders 30% Accumulator from targets and deals 350% S-ATK damage. It can also increase 80% Hit for all members on the team for 1 round and reduce 50% ATK and S-ATK from targets which got hit for 1 round. Then, it can increase 60% DEF and S-DEF for the teammate (except self) with the lowest HP percentage for 2 rounds and Enfar will become immune to lock for 2 rounds. In addition, recovers 100 Accumulator for self.
- **II** at `+T` — Charge Force II (阿恩法，冲锋之力II)
  Vertical attack, plunders 50% Accumulator from targets and deals 380% S-ATK damage. It can also increase 85% Hit for all members on the team for 1 round and reduce 60% ATK and S-ATK from targets which got hit for 1 round. Then, it can increase 70% DEF and S-DEF for the teammate (except self) with the lowest HP percentage for 2 rounds and Enfar will become immune to lock for 2 rounds. In addition, recovers 100 Accumulator for self.
- **III** at `+T3` — Charge Force III (阿恩法，冲锋之力III)
  Cross attack, plunders 60% Accumulator from targets and deals 380% S-ATK damage. It can also increase 85% Hit for all members on the team for 1 round and reduce 60% ATK and S-ATK from targets which got hit for 1 round. Then, it can increase 70% DEF and S-DEF for the teammate (except self) with the lowest HP percentage for 2 rounds and Enfar will become immune to lock for 2 rounds. Increases the ATK, S-ATK, DEF and S-DEF of all allies by 80% for 2 rounds and grants all allies 60 Accumulator. In addition, recovers 100 Accumulator for self.
- **Ⅳ** at `+T4` — Charge Force Ⅳ (阿恩法T4，冲锋之力III)
  Cross attack, plunders 70% Accumulator from targets and deals 410% S-ATK damage. It can also increase 100% Hit for all members on the team for 1 round and reduce 75% ATK and S-ATK from targets which got hit for 1 round. Then, it can increase 100% DEF and S-DEF for the teammate (except self) with the lowest HP percentage for 2 rounds and Enfar will become immune to lock for 2 rounds. Increases the ATK, S-ATK, DEF and S-DEF of all allies by 100% for 2 rounds and grants all allies 80 Accumulator. Has a 50% chance to lock enemies hit for 1 round. In addition, recovers 100 Accumulator for self.

### Augment cost (per step)
- `+1` — 5× Striker Chip · 100,000 money
- `+2` — 10× Striker Chip · 200,000 money
- `+3` — 21× Striker Chip · 300,000 money
- `+4` — 28× Striker Chip · 500,000 money
- `+5` — 35× Striker Chip · 800,000 money
- `+6` — 42× Striker Chip · 10× Pandora Power Core
- `+7` — 49× Striker Chip · 50× Pandora Power Core
- `+8` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Enfar's Ship Parts · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Enfar's Ship Parts · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Enfar's Ship Parts · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Enfar's Ship Parts · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Enfar's Ship Parts · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Enfar's Ship Parts · 140× Alien Essence · 140× Transcendence Core

---

## 391 · Samedi 萨麦迪
**Role** Striker · **Attack** physical · **Generation** old
**Ratings** Damage 9/10 · Defence 6/10 · Assist 4/10

### Signature skill
- **I** at `+0` — Reaper's Scythe I (萨麦迪)
  Single attack. After hitting a main target, the attack will create a chain of lightning. The lightning will jump to enemy targets in proximity of the main target. The lightning will deal 400% S-ATK damage to each target it jumps to (at most 4 targets). In addition, it has a 70% chance to confuse each hitting target for 1 round and increases 100 Accumulator for self. The hero’s receiving S-ATK damage will always be reduced by 50% (passive).
- **II** at `+T2` — Reaper's Scythe II (萨麦迪+T2)
  Single attack. After hitting a main target, the attack will create a chain of lightning. The lightning will jump to enemy targets in proximity of the main target. The lightning will deal 450% S-ATK damage to each target it jumps to (at most 4 targets). In addition, it has a 80% chance to confuse each hitting target for 1 round and increases 100 Accumulator for self. The hero’s receiving S-ATK damage will always be reduced by 50% (passive).
- **Ⅲ** at `+T2` — Reaper's Scythe Ⅲ (萨麦迪+T2)
  Single attack. After hitting a main target, the attack will create a chain of lightning. The lightning will jump to enemy targets in proximity of the main target. The lightning will deal 480% S-ATK damage to each target it jumps to (at most 4 targets). In addition, it has a 100% chance to confuse each hitting target for 1 round and increases 100 Accumulator for self. The hero’s receiving S-ATK damage will always be reduced by 50%.

### Augment cost (per step)
- `+1` — 5× Striker Chip · 100,000 money
- `+2` — 10× Striker Chip · 200,000 money
- `+3` — 21× Striker Chip · 300,000 money
- `+4` — 28× Striker Chip · 500,000 money
- `+5` — 35× Striker Chip · 800,000 money
- `+6` — 42× Striker Chip · 10× Pandora Power Core
- `+7` — 49× Striker Chip · 50× Pandora Power Core
- `+8` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Samedi's Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Samedi's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Samedi's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Samedi's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Samedi's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Samedi's Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 411 · Frances 法兰希斯
**Role** Striker · **Attack** physical · **Generation** old
**Ratings** Damage 9/10 · Defence 5/10 · Assist 6/10

### Signature skill
- **I** at `+0` — Crazy Trick I (法兰西斯，疯狂诡计)
  Cross attack, deals 250% S-ATK damage and plunders 50% S-ATK from targets for 1 round; additionally deals 7M True Damage (ignores defense) to targets which get hit and curse them for 1 round. It also has a 90% chance to inflict the Death Code on hit targets for 2 rounds; when the curse is over, the hit targets will suffer 500% S-ATK damage. If a target ship is destroyed with the Death Code effect, the destroyed ship will induce a cross explosion which will deal 500% S-ATK to the enemy ships on the cross; the Hero's receiving damage will be reduced by 30% for 1 round. In addition, recover 100 Accumulator for self.
- **II** at `+T2` — Crazy Trick II (法兰西斯+T2)
  Cross attack, deals 320% S-ATK damage and plunders 50% S-ATK from targets for 1 round; additionally deals 8M True Damage (ignores defense) to targets which get hit and curse them for 1 round. It also has a 90% chance to inflict the Death Code on hit targets for 2 rounds; when the curse is over, the hit targets will suffer 500% S-ATK damage. If a target ship is destroyed with the Death Code effect, the destroyed ship will induce a cross explosion which will deal 500% S-ATK to the enemy ships on the cross; the Hero's receiving damage will be reduced by 50% for 1 round. In addition, recover 100 Accumulator for self.
- **Ⅲ** at `+T2` — Crazy Trick Ⅲ (法兰西斯+T2)
  Cross attack, deals 360% S-ATK damage and plunders 75% S-ATK from targets for 1 round; additionally deals 10M True Damage (ignores defense) to targets which get hit and curse them for 1 round. It also has a 100% chance to inflict the Death Code on hit targets for 2 rounds; when the curse is over, the hit targets will suffer 600% S-ATK damage. If a target ship is destroyed with the Death Code effect, the destroyed ship will induce a cross explosion which will deal 600% S-ATK to the enemy ships on the cross; the Hero's receiving damage will be reduced by 60% for 1 round. In addition, recover 100 Accumulator for self.

### Augment cost (per step)
- `+1` — 5× Striker Chip · 100,000 money
- `+2` — 10× Striker Chip · 200,000 money
- `+3` — 21× Striker Chip · 300,000 money
- `+4` — 28× Striker Chip · 500,000 money
- `+5` — 35× Striker Chip · 800,000 money
- `+6` — 42× Striker Chip · 10× Pandora Power Core
- `+7` — 49× Striker Chip · 50× Pandora Power Core
- `+8` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Frances's Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Frances's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Frances's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Frances's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Frances's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Frances's Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 442 · Beamon 比蒙
**Role** Striker · **Attack** physical · **Generation** old
**Ratings** Damage 9/10 · Defence 8/10 · Assist 10/10

### Signature skill
- **Ⅰ** at `+0` — Devastating BlowⅠ (比蒙，湮灭打击)
  Cross attack, plunder 50% S-DEF and 25% Accumulator from the target and deal 300% S-ATK damage. And lose 50% of the current HP to kill a random enemy, ignoring stasis status and damage block effects. After the attack, it becomes invisible for 1 round, and it has a 60% chance to expose invisible targets (the rate for each target will be settled independently). Increase 30% Block for all friendly ships (except for self) for 1 round. At last, recover 100 Accumulator for self.
- **Ⅱ** at `+T2` — Devastating BlowⅡ (比蒙，湮灭打击)
  Cross attack, plunder 50% S-DEF and 50% Accumulator from the target and deal 300% S-ATK damage. And lose 25% of the current HP to kill a random enemy, ignoring stasis status and damage block effects. After the attack, it becomes invisible for 1 round, and it has a 60% chance to expose invisible targets (the rate for each target will be settled independently). Increase 50% Block for all friendly ships (except for self) for 1 round. At last, recover 100 Accumulator for self.
- **III** at `+T4` — Devastating BlowIII (比蒙，湮灭打击)
  Cross attack, plunder 75% S-DEF and 75% Accumulator from the target and deal 350% S-ATK damage. And lose 20% of the current HP to kill 2 random enemies, ignoring stasis status and damage block effects. After the attack, it becomes invisible for 1 round, and it has a 100% chance to expose invisible targets (the rate for each target will be settled independently). Increase 80% Block for all friendly ships (except for self) for 1 round. At last, recover 100 Accumulator for self.

### Augment cost (per step)
- `+1` — 5× Striker Chip · 100,000 money
- `+2` — 10× Striker Chip · 200,000 money
- `+3` — 21× Striker Chip · 300,000 money
- `+4` — 28× Striker Chip · 500,000 money
- `+5` — 35× Striker Chip · 800,000 money
- `+6` — 42× Striker Chip · 10× Pandora Power Core
- `+7` — 49× Striker Chip · 50× Pandora Power Core
- `+8` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Beamon's Ship Parts · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Beamon's Ship Parts · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Beamon's Ship Parts · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Beamon's Ship Parts · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Beamon's Ship Parts · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Beamon's Ship Parts · 140× Alien Essence · 140× Transcendence Core

---

## 449 · Immortal Vanguard 不死先锋
**Role** Striker · **Attack** physical · **Generation** old
**Ratings** Damage 10/10 · Defence 7/10 · Assist 8/10

### Signature skill
- **Ⅰ** at `+0` — InfernoⅠ (不死先锋，深渊业火Ⅰ)
  Cross attack, deals 300% S-ATK damage and 3M True Damage to targets (Ignores DEF). Then clears all targets' Accumulators and stands a 50% chance to destroy 2 enemies instantly. Stands a 50% chance to lock 2 enemies for 1 round. Increases all friendly units' ATK and S-ATK by 25% for 2 rounds. Recovers 50 Accumulators for all friendly units and 100 Accumulators for self.
- **Ⅱ** at `+T` — InfernoⅡ (不死先锋，深渊业火Ⅱ)
  Cross attack, deals 350% S-ATK damage and 5M True Damage to targets (Ignores DEF). Then clears all targets' Accumulators and stands a 60% chance to destroy 2 enemies instantly. Stands a 60% chance to lock 2 enemies for 1 round. It makes self immune to Accumulator Reduce effects, for 1 rounds. Increases all friendly units' ATK and S-ATK by 35% for 2 rounds. Recovers 50 Accumulators for all friendly units and 100 Accumulators for self.
- **Ⅲ** at `+T3` — InfernoⅢ (不死先锋，深渊业火Ⅲ)
  Cross attack, deals 380% S-ATK damage and 6M True Damage to targets (Ignores DEF). Then clears all targets' Accumulators and stands a 65% chance to destroy 2 enemies instantly. Stands a 65% chance to lock 2 enemies for 1 round. It makes self immune to instant destruction and Accumulator Reduce effects, for 1 round. Increases all friendly units' ATK and S-ATK by 40% for 2 rounds. Recovers 50 Accumulators for all friendly units and 100 Accumulators for self.
- **IV** at `+T4` — InfernoIV (不死先锋，深渊业火IV)
  Cross attack, deals 450% S-ATK damage and 10M True Damage to targets (Ignores DEF). Then clears all targets' Accumulators and stands a 80% chance to destroy 2 enemies instantly. Stands a 100% chance to lock 2 enemies for 1 round. It makes self immune to instant destruction and Accumulator Reduce effects, for 1 round. Increases all friendly units' ATK and S-ATK by 50% for 2 rounds. Recovers 50 Accumulators for all friendly units and 100 Accumulators for self.

### Augment cost (per step)
- `+1` — 5× Striker Chip · 100,000 money
- `+2` — 10× Striker Chip · 200,000 money
- `+3` — 21× Striker Chip · 300,000 money
- `+4` — 28× Striker Chip · 500,000 money
- `+5` — 35× Striker Chip · 800,000 money
- `+6` — 42× Striker Chip · 10× Pandora Power Core
- `+7` — 49× Striker Chip · 50× Pandora Power Core
- `+8` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Immortal Vanguard Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Immortal Vanguard Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Immortal Vanguard Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Immortal Vanguard Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Immortal Vanguard Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Immortal Vanguard Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 476 · Medusa 美杜莎
**Role** Striker · **Attack** physical · **Generation** old
**Ratings** Damage 10/10 · Defence 7/10 · Assist 8/10

### Signature skill
- **I** at `+0` — Medusa's Gaze I (美杜莎，石化凝视Ⅰ)
  Cross attack; plunders 75% Accumulator from all female enemies, then deals 350% S-ATK damage. There's a 100% chance to confuse all gender-neutral enemies for 2 rounds. There's a 100% chance to [petrify] all male enemies, preventing them from moving for 1 round. There's a 50% chance to [estrange] all enemies(probability for each target is calculated independently), prevent enemy lieutenants from casting skills for 2 rounds. Finally, recovers 100 Accumulator for self.
- **II** at `Awaken` — Medusa's Gaze II (美杜莎，石化凝视Ⅱ)
  Cross attack; plunders 100% Accumulator from all female enemies, then deals 380% S-ATK damage. There's a 100% chance to confuse all gender-neutral enemies for 2 rounds. There's a 100% chance to [petrify] all male enemies, preventing them from moving for 1 round. There's a 50% chance to [estrange] all enemies(probability for each target is calculated independently), prevent enemy lieutenants from casting skills for 2 rounds. Finally, recovers 100 Accumulator for self.
- **III** at `Second Awaken` — Medusa's Gaze III (美杜莎，石化凝视Ⅲ)
  Cross attack; plunders 100% Accumulator from all female enemies, then deals 400% S-ATK damage. There's a 100% chance to confuse all gender-neutral enemies for 2 rounds. There's a 100% chance to [petrify] all male enemies, preventing them from moving for 1 round, and a 50% chance to lock non-biological enemies (probability for each target calculated separately), preventing them from moving for 1 round. There's also an 80% chance to [estrange] all enemies (probability for each target calculated separately), preventing enemy lieutenants from casting skills for 2 rounds. Finally, recovers 100 Accumulator for self.
- **IV** at `Awaken +3` — Medusa's Gaze IV (美杜莎，石化凝视IV)
  Cross attack,before attacking targets, activates Eye of True Sight until the end of battle; first, clears all buffs from targets, then plunders 100% Accumulator from all female enemies, then deals 450% S-ATK damage. There's a 100% chance to confuse all gender-neutral enemies for 2 rounds. There's a 100% chance to [petrify] all male enemies, during which they cannot be resurrected (can be reborn), while also preventing them from moving for 1 round, and a 100% chance to lock non-biological enemies (probability for each target calculated separately), preventing them from moving for 1 round. There's also a 100% chance to [estrange] all enemies (probability for each target calculated separately), preventing enemy lieutenants from casting skills for 2 rounds. Finally, recovers 100 Accumulator for self.

### Augment cost (per step)
- `+1` — 5× Striker Chip · 100,000 money
- `+2` — 10× Striker Chip · 200,000 money
- `+3` — 21× Striker Chip · 300,000 money
- `+4` — 28× Striker Chip · 500,000 money
- `+5` — 35× Striker Chip · 800,000 money
- `+6` — 42× Striker Chip · 10× Pandora Power Core
- `+7` — 49× Striker Chip · 50× Pandora Power Core
- `+8` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Medusa Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Medusa Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Medusa Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Medusa Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Medusa Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Medusa Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 485 · Yone 元
**Role** Striker · **Attack** physical · **Generation** old
**Ratings** Damage 10/10 · Defence 7/10 · Assist 8/10

### Signature skill
- **Ⅰ** at `+0` — Untold EnigmaⅠ (元，万道开天)
  As Yone, you build Domination once battle starts. You gain 5 points of Domination each time you or an ally launches a Normal Attack and gain 10 point of Domination from skill, and for every 20% of your Max HP lost gain 5 point of Domination. You gain 10 when an enemy uses a skill, and 20 when an allied ship is destroyed. You gain a stack of Domination for every 20 Domination built. You gain different skill effects depending on your number of stacks, and start off with 1 stack. Vertical Attacks deal 350% S-ATK damage, and gain different effects depending on your number of Domination stacks: 1 stack: Increases you and all friendly ships' S-ATK, Hit Rate and Block by 50% (absolute value) for 5 rounds. Has a 60% chance (probability for each target calculated separately) to grant you and all friendly ships Freeze, Lock and Confuse immunity for 5 rounds, while granting you invisibility for 1 round. If this triggers, all friendly ships gain 20 Accumulator and shields that block one attack, lasting for 1 round. 2 stacks: Increases you and all friendly ships' S-ATK and Hit Rate by 80%, and Block by 60% (absolute value) for 5 rounds. Also grants you and the ally with the lowest HP invisibility for 1 round, all allies 30 Accumulator, and has a 50% chance (probability for each target calculated separately) to Freeze all enemy ships for 1 round. 3 stacks: Increases you and all friendly ships' S-ATK and E-ATK by 100%, as well as all your Block and Crit by 80% (absolute value) for 5 rounds. Enemies hit lose HP equal to 50% of their Max HP, and it clears most debuffs from you and your allies (Lock, Confuse, Freeze, Poison, Curse and Forbidding Skill Use). Grants all friendly ships 40 Accumulator, and lastly, deals True Damage (equal to 50% of the total previous damage dealt) to each enemy ship with over 50% HP remaining. 4 stacks: First plunders 40% of all enemies' Accumulator, and 70% of the hit enemy's DEF and S-DEF. It then deals 350% S-ATK damage to the target hit, grants you Forbidding Skill immunity, Accumulator reduction immunity and reduces your damage taken by 70% all for 2 rounds. Has a 50% chance (probability for each target calculated separately) to Weaken all enemies, deducting 50% of targets' stats and granting you a shield that can withstand lethal damage one time for 1 round. Lastly, it deals True Damage (equal to 180% of the total previous damage dealt) to the enemy ship with the lowest HP remaining. 5 stacks: You gain the same effects as when you have 4 Domination stacks, but also have a 50% chance to destroy two random enemy ships instantly. Lastly, you recover 100 Accumulator.
- **Ⅱ** at `+T` — Untold EnigmaⅡ (元，万道开天)
  As Yone, you build Domination once battle starts. You gain 5 points of Domination each time you or an ally launches a Normal Attack and gain 10 point of Domination from skill, and for every 20% of your Max HP lost gain 10 point of Domination. You gain 20 when an enemy uses a skill, and 20 when an allied ship is destroyed. You gain a stack of Domination for every 20 Domination built. You gain different skill effects depending on your number of stacks, and start off with 1 stack. Vertical Attacks deal 350% S-ATK damage, and gain different effects depending on your number of Domination stacks: 1 stack: Increases you and all friendly ships' S-ATK, Hit Rate and Block by 80% (absolute value) for 5 rounds. Has a 60% chance (probability for each target calculated separately) to grant you and all friendly ships Freeze, Lock and Confuse immunity for 5 rounds, while granting you invisibility for 1 round. If this triggers, all friendly ships gain 20 Accumulator and shields that block one attack, lasting for 1 round. 2 stacks: Increases you and all friendly ships' S-ATK and Hit Rate by 100%, and Block by 80% (absolute value) for 5 rounds. Also grants you and the ally with the lowest HP invisibility for 1 round, all allies 30 Accumulator, and has a 50% chance (probability for each target calculated separately) to Freeze all enemy ships for 1 round. 3 stacks: Increases you and all friendly ships' S-ATK and E-ATK by 100%, as well as all your Block and Crit by 80% (absolute value) for 5 rounds. Enemies hit lose HP equal to 50% of their Max HP, and it clears most debuffs from you and your allies (Lock, Confuse, Freeze, Poison, Curse and Forbidding Skill Use). Grants all friendly ships 40 Accumulator, and lastly, deals True Damage (equal to 70% of the total previous damage dealt) to each enemy ship with over 50% HP remaining. 4 stacks: First plunders 40% of all enemies' Accumulator, and 70% of the hit enemy's DEF and S-DEF. It then deals 350% S-ATK damage to the target hit, grants you Forbidding Skill immunity, Accumulator reduction immunity and reduces your damage taken by 70% all for 2 rounds. Has a 50% chance (probability for each target calculated separately) to Weaken all enemies, deducting 50% of targets' stats and granting you a shield that can withstand lethal damage one time for 1 round. Lastly, it deals True Damage (equal to 180% of the total previous damage dealt) to the enemy ship with the lowest HP remaining. 5 stacks: You gain the same effects as when you have 4 Domination stacks, but also have a 50% chance to destroy two random enemy ships instantly. Lastly, you recover 100 Accumulator.
- **Ⅲ** at `+T3` — Untold EnigmaⅢ (元，万道开天)
  As Yone, you build Domination once battle starts. You gain 5 points of Domination each time you or an ally launches a Normal Attack and gain 10 point of Domination from skill, and for every 20% of your Max HP lost gain 10 point of Domination. You gain 20 when an enemy uses a skill, and 20 when an allied ship is destroyed. You gain a stack of Domination for every 20 Domination built. You gain different skill effects depending on your number of stacks, and start off with 1 stack. Vertical Attacks deal 350% S-ATK damage, and gain different effects depending on your number of Domination stacks: 1 stack: Increases you and all friendly ships' S-ATK, Hit Rate and Block by 80% (absolute value) for 5 rounds. Has a 60% chance (probability for each target calculated separately) to grant you and all friendly ships Freeze, Lock and Confuse immunity for 5 rounds, while granting you invisibility for 1 round. If this triggers, all friendly ships gain 20 Accumulator and shields that block one attack, lasting for 1 round. 2 stacks: Increases you and all friendly ships' S-ATK and Hit Rate by 100%, and Block by 80% (absolute value) for 5 rounds. Also grants you and the ally with the lowest HP invisibility for 1 round, all allies 30 Accumulator, and has a 50% chance (probability for each target calculated separately) to Freeze all enemy ships for 1 round. 3 stacks: Increases you and all friendly ships' S-ATK and E-ATK by 100%, as well as all your Block and Crit by 80% (absolute value) for 5 rounds. Enemies hit lose HP equal to 50% of their Max HP, and it clears most debuffs from you and your allies (Lock, Confuse, Freeze, Poison, Curse and Forbidding Skill Use). Grants all friendly ships 40 Accumulator, and lastly, deals True Damage (equal to 70% of the total previous damage dealt) to each enemy ship with over 50% HP remaining. 4 stacks: First plunders 40% of all enemies' Accumulator, and 70% of the hit enemy's DEF and S-DEF. It then deals 350% S-ATK damage to the target hit, grants you Forbidding Skill immunity, Accumulator reduction immunity and reduces your damage taken by 70% all for 2 rounds. Has a 50% chance (probability for each target calculated separately) to Weaken all enemies, deducting 50% of targets' stats and granting you a shield that can withstand lethal damage one time for 1 round. Lastly, it deals True Damage (equal to 180% of the total previous damage dealt) to the enemy ship with the lowest HP remaining. 5 stacks: You gain the same effects as when you have 4 Domination stacks, but also have a 50% chance to destroy two random enemy ships instantly. Domination stacks up to 7 times: upon reaching 7 stacks it grants the accumulated effects of all stacks. Lastly, you recover 100 Accumulator.（Yone's instant kills ignore Instant Destruction and Instant Kill immunity.）
- **Ⅳ** at `+T4` — Untold EnigmaⅣ (元，万道开天IV)
  As Yone, you build Domination once battle starts. You gain 5 points of Domination each time you or an ally launches a Normal Attack and gain 10 point of Domination from skill, and for every 20% of your Max HP lost gain 10 point of Domination. You gain 20 when an enemy uses a skill, and 20 when an allied ship is destroyed. You gain a stack of Domination for every 20 Domination built. You gain different skill effects depending on your number of stacks, and start off with 1 stack. Vertical Attacks deal 400% S-ATK damage, and gain different effects depending on your number of Domination stacks: 1 stack: Increases you and all friendly ships' S-ATK, Hit Rate and Block by 100% (absolute value) for 5 rounds. Has a 75% chance (probability for each target calculated separately) to grant you and all friendly ships Freeze, Lock, Confuse and Forbidding Skill Use immunity for 5 rounds, while granting you invisibility for 1 round. If this triggers, all friendly ships gain 30 Accumulator and shields that block one attack, lasting for 1 round. 2 stacks: Increases you and all friendly ships' S-ATK and Hit Rate by 120%, and Block by 100% (absolute value) for 5 rounds. Also grants you and the ally with the lowest HP invisibility for 1 round, all allies 40 Accumulator, and has a 75% chance (probability for each target calculated separately) to Freeze all enemy ships for 1 round. 3 stacks: Increases you and all friendly ships' S-ATK by 140% andE-ATK by 120%, as well as all your Block and Crit by 100% (absolute value) for 5 rounds. Enemies hit lose HP equal to 80% of their Max HP, and it clears most debuffs from you and your allies (Lock, Confuse, Freeze, Poison, Curse, Petrify, Entangle, Icebound and Forbidding Skill Use). Grants all friendly ships 50 Accumulator, and lastly, deals True Damage (equal to 80% of the total previous damage dealt) to each enemy ship with over 30% HP remaining. 4 stacks: First plunders 50% of all enemies' Accumulator, and 75% of the hit enemy's DEF and S-DEF. It then deals 400% S-ATK damage to the target hit, grants you Forbidding Skill immunity, Accumulator reduction immunity and reduces your damage taken by 75% all for 2 rounds. Has a 60% chance (probability for each target calculated separately) to Weaken all enemies, deducting 50% of targets' stats and granting you a shield that can withstand lethal damage one time for 1 round. Lastly, it deals True Damage (equal to 220% of the total previous damage dealt) to the enemy ship with the lowest HP remaining. 5 stacks: You gain the same effects as when you have 4 Domination stacks, but also have a 60% chance to destroy two random enemy ships instantly. Domination stacks up to 7 times: upon reaching 7 stacks it grants the accumulated effects of all stacks and increases the chance to instantly destroy enemies to 80%. Lastly, you recover 100 Accumulator. (Yone's Instant Destruction effects ignore immunity to lethal attacks and instant destruction. Enemies killed by Yone cannot be resurrected (nor Rebirth)).

### Augment cost (per step)
- `+1` — 5× Striker Chip · 100,000 money
- `+2` — 10× Striker Chip · 200,000 money
- `+3` — 21× Striker Chip · 300,000 money
- `+4` — 28× Striker Chip · 500,000 money
- `+5` — 35× Striker Chip · 800,000 money
- `+6` — 42× Striker Chip · 10× Pandora Power Core
- `+7` — 49× Striker Chip · 50× Pandora Power Core
- `+8` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Yone Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Yone Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Yone Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Yone Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Yone Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Yone Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 490 · Snowchub 雪胖胖
**Role** Striker · **Attack** physical · **Generation** old
**Ratings** Damage 10/10 · Defence 7/10 · Assist 8/10

### Signature skill
- **Ⅰ** at `+0` — Snowball FlurryⅠ (雪球连掷)
  Throw 5 snowballs in quick succession at a single enemy, each snowball dealing 180% S-ATK damage and 1M True Damage. When fighting against non-Player enemies, has a 50% chance to freeze the target and the enemy ship with the highest S-ATK. Those frozen will be unable to act for 1 round and will take an extra 20% damage from your allied units. The user becomes immune to Freeze, Lock, and Weaken for 2 rounds. The user and the ally with the least HP become invisible and enter Stasis for 1 round. The user gains 300K ATK and S-ATK each time they use this skill (this effect stacks and lasts until the end of battle or until the unit dies). Also recovers 100 Accumulator. (Deals 2x damage against non-Player units).
- **Ⅱ** at `+T` — Snowball FlurryⅡ (雪球连掷)
  Throw 5 snowballs in quick succession at a single enemy, each snowball dealing 200% S-ATK damage and 1.8M True Damage. When fighting against non-Player enemies, has a 75% chance to freeze the target and a 50% chance to freeze the enemy ship with the highest S-ATK. Those frozen will be unable to act for 1 round and will take an extra 30% damage from your allied units. The user becomes immune to Freeze, Lock, and Weaken for 2 rounds. The user and the ally with the least HP become invisible and enter Stasis for 1 round. The user gains 500K ATK and S-ATK each time they use this skill (this effect stacks and lasts until the end of battle or until the unit dies). Also recovers 100 Accumulator. (Deals 3x damage against non-Player units).
- **Ⅲ** at `+T3` — Snowball FlurryⅢ (雪球连掷)
  Throw 5 snowballs in quick succession at a single enemy, each snowball dealing 240% S-ATK damage and 3M True Damage. When fighting against non-Player enemies, has a 100% chance to freeze the target and a 75% chance to freeze the enemy ship with the highest S-ATK. Those frozen will be unable to act for 1 round and will take an extra 40% damage from your allied units. The user becomes immune to Freeze, Lock, and Weaken for 2 rounds. The user and the ally with the least HP become invisible and enter Stasis for 1 round. Renders the enemy's Eye of True Sight ineffective while granting the user Eye of True Sight for 2 rounds. The user gains 800K ATK and S-ATK each time they use this skill (this effect stacks and lasts until the end of battle or until the unit dies). Also recovers 100 Accumulator. (Deals 4x damage against non-Player units).

### Augment cost (per step)
- `+1` — 5× Striker Chip · 100,000 money
- `+2` — 10× Striker Chip · 200,000 money
- `+3` — 21× Striker Chip · 300,000 money
- `+4` — 28× Striker Chip · 500,000 money
- `+5` — 35× Striker Chip · 800,000 money
- `+6` — 42× Striker Chip · 10× Pandora Power Core
- `+7` — 49× Striker Chip · 50× Pandora Power Core
- `+8` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Snowchub Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Snowchub Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Snowchub Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Snowchub Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 60× Snowchub Ship Part · 130× Inert Alloy · 100× Heated Alloy

---

## 496 · Tracy 特蕾希
**Role** Striker · **Attack** physical · **Generation** old
**Ratings** Damage 9/10 · Defence 8/10 · Assist 10/10

### Signature skill
- **Ⅰ** at `+0` — Kinetic TrapⅠ (特蕾希，动能陷阱)
  Horizontal Attack, attacks the target hit 3 times, each attack dealing 120% S-ATK damage. The first enemy in a straight line enters a Kinetic Trap, becoming unable to move or be targeted (will not be targeted by attacks and skill effects; active skill effects still remain in effect). The Kinetic Trap gains energy during battle, recording the damage dealt by both sides (excluding instant death). It records damage up to 720% of the S-ATK self starts the battle with. Before launching a skill, Tracy will explode all active Kinetic Traps before her skill takes effect. Exploding Kinetic Traps deal 240% S-ATK damage to targets in them plus damage equal to the amount recorded (trap explosions deal True Damage and cannot be shared), while other units take 30% explosion damage. Traps will explode and deal an extra 100% explosion damage should Tracy die or if there is only 1 enemy remaining. Has a 100% chance for self to become immune to Lock and Confuse for 1 round. All allies gain 30 Accumulator. Has a 100% chance to expose invisible enemies. Finally, recovers 100 Accumulator.
- **Ⅱ** at `+T` — Kinetic TrapⅡ (特蕾希，动能陷阱)
  Horizontal Attack, attacks the target hit 3 times, each attack dealing 160% S-ATK damage. The first enemy in a straight line enters a Kinetic Trap, becoming unable to move or be targeted (will not be targeted by attacks and skill effects; active skill effects still remain in effect). The Kinetic Trap gains energy during battle, recording the damage dealt by both sides (excluding instant death). It records damage up to 1020% of the S-ATK self starts the battle with. Before launching a skill, Tracy will explode all active Kinetic Traps before her skill takes effect. Exploding Kinetic Traps deal 300% S-ATK damage to targets in them plus damage equal to the amount recorded (trap explosions deal True Damage and cannot be shared), while other units take 40% explosion damage. Traps will explode and deal an extra 120% explosion damage should Tracy die or if there is only 1 enemy remaining. Has a 100% chance for self to become immune to Lock and Confuse for 1 round. All allies gain 30 Accumulator. Has a 100% chance to expose invisible enemies. Finally, recovers 100 Accumulator.
- **Ⅲ** at `+T3` — Kinetic TrapⅢ (特蕾希，动能陷阱)
  Horizontal Attack, attacks the target hit 3 times, each attack dealing 160% S-ATK damage. The first enemy in a straight line enters a Kinetic Trap, becoming unable to move or be targeted (will not be targeted by attacks and skill effects; active skill effects still remain in effect). The Kinetic Trap gains energy during battle, recording the damage dealt by both sides (excluding instant death). It records damage up to 1020% of the S-ATK self starts the battle with. Before launching a skill, Tracy will explode all active Kinetic Traps before her skill takes effect. Exploding Kinetic Traps deal 300% S-ATK damage to targets in them plus damage equal to the amount recorded (trap explosions deal True Damage and cannot be shared), while other units take 40% explosion damage. Traps will explode and deal an extra 120% explosion damage should Tracy die or if there is only 1 enemy remaining. Has a 100% chance for self to become immune to Lock and Confuse for 1 round. All allies gain 30 Accumulator. Has a 100% chance to expose invisible enemies. Finally, recovers 100 Accumulator.Has a 100% chance to trap 1 random enemy in a Kinetic Trap at the start of battle.Has an extra 50% chance to trap 1 random enemy in a Kinetic Trap at the start of battle.
- **IV** at `+T4` — Kinetic TrapIV (特蕾希，动能陷阱)
  Horizontal Attack, attacks the target hit 4 times, each attack dealing 200% S-ATK damage. The first enemy in a straight line enters a Kinetic Trap, becoming unable to move or be targeted (will not be targeted by attacks and skill effects; active skill effects still remain in effect). The Kinetic Trap gains energy during battle, recording the damage dealt by both sides (excluding instant death). It records damage up to 1280% of the S-ATK self starts the battle with. Before launching a skill, Tracy will explode all active Kinetic Traps before her skill takes effect. Exploding Kinetic Traps deal 400% S-ATK damage to targets in them plus damage equal to the amount recorded (trap explosions deal True Damage and cannot be shared), while other units take 50% explosion damage. Traps will explode and deal an extra 150% explosion damage should Tracy die or if there is only 1 enemy remaining. Tracy's S-ATK and Kinetic Trap damage ignore immunity to lethal attacks or lethal damage-avoiding effects. Has a 100% chance for self to become immune to Lock and Confuse for 1 round. All allies gain 50 Accumulator. Has a 100% chance to expose invisible enemies. Finally, recovers 100 Accumulator. At the start of the battle, there is a 100% chance to trap a random enemy in a Kinetic Trap, with an additional 50% chance to trap another random enemy.

### Augment cost (per step)
- `+1` — 5× Striker Chip · 100,000 money
- `+2` — 10× Striker Chip · 200,000 money
- `+3` — 21× Striker Chip · 300,000 money
- `+4` — 28× Striker Chip · 500,000 money
- `+5` — 35× Striker Chip · 800,000 money
- `+6` — 42× Striker Chip · 10× Pandora Power Core
- `+7` — 49× Striker Chip · 50× Pandora Power Core
- `+8` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Tracy Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Tracy Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Tracy Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Tracy Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Tracy Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Tracy Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 505 · Wulkas 乌卡斯
**Role** Striker · **Attack** physical · **Generation** old
**Ratings** Damage 10/10 · Defence 7/10 · Assist 8/10

### Signature skill
- **Ⅰ** at `+0` — Anticipation Ⅰ (蓄势待发)
  Wulkas will not attack immediately upon issuing the command but will instead enter a state of [Anticipation]. During this state, Wulkas' S-ATK damage increases by 0.6% for every 1 Accumulator that any unit loses (by casting skills, removing or stealing Accumulator) for up to 1500%. Control effects (Freeze, Lock, Confuse, and Forbidding Skill Use) interrupt [Anticipation] , but the control effect is also cleared, after which Wulkas attacks the target that controlled it for the currently accumulated S-ATK damage. If the skill's damage accrues to 1500%, Wulkas attacks a single target, otherwise, Wulkas gains 300% S-ATK damage. If the skill kills an enemy, Wulkas deals True Damage equal to 50% of the damage dealt to all enemies. Cannot take more than 80% of max HP as damage from a single attack. Grants Eye of True Sight for self for 2 rounds. Finally, recovers 100 Accumulator. Enters Anticipation at the start of combat. Immune to Instant Destruction. Note: S-ATK damage must be charged up anew after attacking.
- **Ⅱ** at `+T` — Anticipation Ⅱ (蓄势待发)
  Wulkas will not attack immediately upon issuing the command but will instead enter a state of [Anticipation]. During this state, Wulkas' S-ATK damage increases by 0.8% for every 1 Accumulator that any unit loses (by casting skills, removing or stealing Accumulator) for up to 1800%. Control effects (Freeze, Lock, Confuse, Forbidding Skill Use, and Entangle) interrupt [Anticipation] , but the control effect is also cleared, after which Wulkas attacks the target that controlled it for the currently accumulated S-ATK damage. If the skill's damage accrues to 1800%, Wulkas attacks a single target, otherwise, Wulkas gains 400% S-ATK damage. If the skill kills an enemy, Wulkas deals True Damage equal to 80% of the damage dealt to all enemies. Cannot take more than 60% of max HP as damage from a single attack. Grants Eye of True Sight and Guaranteed Hit for self for 2 rounds. Wulkas is immune to Accumulator reduction effects for 2 rounds. Finally, recovers 100 Accumulator. Enters Anticipation at the start of combat. Immune to Instant Destruction. Note: S-ATK damage must be charged up anew after attacking.
- **Ⅲ** at `+T3` — Anticipation Ⅲ (蓄势待发)
  Wulkas will not attack immediately upon issuing the command but will instead enter a state of [Anticipation]. During this state, Wulkas' S-ATK damage increases by 1% for every 1 Accumulator that any unit loses (by casting skills, removing or stealing Accumulator) for up to 2400%. Control effects (Freeze, Lock, Confuse, Forbidding Skill Use, Entangle, and Icebound) interrupt [Anticipation] , but the control effect is also cleared, after which Wulkas attacks the target that controlled it for the currently accumulated S-ATK damage. If the skill's damage accrues to 2400%, Wulkas attacks a single target, otherwise, Wulkas gains 500% S-ATK damage. Ignores shields Stasis, as well as shields with Instant Destruction protection. If the skill kills an enemy, Wulkas deals True Damage equal to 100% of the damage dealt to all enemies. Cannot take more than 50% of max HP as damage from a single attack. Grants Eye of True Sight and Guaranteed Hit for self for 2 rounds. Wulkas is immune to Accumulator reduction effects for 2 rounds. Finally, recovers 100 Accumulator. Enters Anticipation at the start of combat. Immune to Instant Destruction. Note: S-ATK damage must be charged up anew after attacking.
- **IV** at `+T4` — Anticipation IV (蓄势待发)
  Wulkas will not attack immediately upon issuing the command but will instead enter a state of [Anticipation]. During this state, Wulkas' S-ATK damage increases by 1.2% for every 1 Accumulator that any unit loses (by casting skills, removing or stealing Accumulator) for up to 3000%. Control effects (Freeze, Lock, Confuse, Forbidding Skill Use, Entangle, Icebound, and Petrify) interrupt [Anticipation] , but the control effect is also cleared, after which Wulkas attacks the target that controlled it for the currently accumulated S-ATK damage. If the skill's damage accrues to 3000%, Wulkas attacks a single target, otherwise, Wulkas gains 600% S-ATK damage. When S-ATK damage reaches 3000%, Wulkas gains immunity to lethal attacks (including Instant Destruction) (cannot be removed) for 1 round. Ignores shields Stasis, as well as shields with Instant Destruction protection. If the skill kills an enemy, Wulkas deals True Damage equal to 100% of the damage dealt to all enemies. Cannot take more than 40% of max HP as damage from a single attack. Grants Eye of True Sight and Guaranteed Hit for self for 2 rounds. Wulkas is immune to Accumulator reduction effects for 2 rounds. Finally, recovers 100 Accumulator. Enters Anticipation at the start of combat. Immune to Instant Destruction. Note: S-ATK damage must be charged up anew after attacking.

### Augment cost (per step)
- `+1` — 5× Striker Chip · 100,000 money
- `+2` — 10× Striker Chip · 200,000 money
- `+3` — 21× Striker Chip · 300,000 money
- `+4` — 28× Striker Chip · 500,000 money
- `+5` — 35× Striker Chip · 800,000 money
- `+6` — 42× Striker Chip · 10× Pandora Power Core
- `+7` — 49× Striker Chip · 50× Pandora Power Core
- `+8` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Wulkas Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Wulkas Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Wulkas Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Wulkas Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Wulkas Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Wulkas Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 515 · Negris 奈格利斯
**Role** Striker · **Attack** physical · **Generation** old
**Ratings** Damage 10/10 · Defence 7/10 · Assist 8/10

### Signature skill
- **Ⅰ** at `+0` — Deadly AssaultⅠ (奈格利斯，死亡突袭I)
  Single Attack, deals 380% S-ATK damage to the enemy with the lowest HP%; also deals 1% more damage for every 1% max HP lost by the target. Whenever an enemy or allied unit dies, increases the allied Striker's Crit Rate by 30% (absolute value) and Crit ATK by 48% (absolute value), stacking up to 150% Crit Rate and 240% Crit ATK. Inflicts Death Code on 2 random enemy units, which will cause a cross explosion if they are destroyed with Death Code, dealing 400% S-ATK damage to the enemy ships on the cross. Gains 1 round of Invisibility. Finally, recovers 100 Accumulator for self. Note: Negris comes with a 50% extra Crit ATK.
- **Ⅱ** at `+T` — Deadly AssaultⅡ (奈格利斯，死亡突袭II)
  Single Attack, deals 400% S-ATK damage to the enemy with the lowest HP%; also deals 1.5% more damage for every 1% max HP lost by the target. Whenever an enemy or allied unit dies, increases the allied Striker's Crit Rate by 36% (absolute value) and Crit ATK by 56% (absolute value), stacking up to 180% Crit Rate and 280% Crit ATK. Inflicts Death Code on 2 random enemy units, which will cause a cross explosion if they are destroyed with Death Code, dealing 500% S-ATK damage to the enemy ships on the cross. Gains 1 round of Invisibility. Finally, recovers 100 Accumulator for self. Note: Negris comes with a 50% extra Crit ATK.
- **Ⅲ** at `+T3` — Deadly AssaultⅢ (奈格利斯，死亡突袭III)
  Single Attack, deals 430% S-ATK damage to the enemy with the lowest HP%; also deals 2% more damage for every 1% max HP lost by the target. S-ATK has a 60% chance to not be Blocked. If the target is killed, deals True Damage equal to 80% of the excess damage to all enemies. Whenever an enemy or allied unit dies, increases the allied Striker's Crit Rate by 60% (absolute value) and Crit ATK by 80% (absolute value), stacking up to 240% Crit Rate and 320% Crit ATK. Inflicts Death Code on 2 random enemy units, which will cause a cross explosion if they are destroyed with Death Code, dealing 600% S-ATK damage to the enemy ships on the cross. Gains 1 round of Invisibility. Finally, recovers 100 Accumulator for self. Note: Negris comes with a 50% extra Crit ATK.
- **IV** at `+T4` — Deadly AssaultIV (奈格利斯，死亡突袭IV)
  Single Attack, deals 480% S-ATK damage to the enemy with the lowest HP%; also deals 3% more damage for every 1% max HP lost by the target. S-ATK has a 100% chance to not be Blocked and ignores 80% of the target's DEF and S-DEF. If the target is killed, deals True Damage equal to 100% of the excess damage to all enemies. Whenever an enemy or allied unit dies, increases the allied Striker's Crit Rate by 100% (absolute value) and Crit ATK by 120% (absolute value), stacking up to 300% Crit Rate and 360% Crit ATK. Inflicts Death Code on 2 random enemy units, which will cause a cross explosion if they are destroyed with Death Code, dealing 800% S-ATK damage to the enemy ships on the cross. Gains 1 round of Invisibility. Finally, recovers 100 Accumulator for self. Note: Negris comes with a 50% extra Crit ATK.

### Augment cost (per step)
- `+1` — 5× Striker Chip · 100,000 money
- `+2` — 10× Striker Chip · 200,000 money
- `+3` — 21× Striker Chip · 300,000 money
- `+4` — 28× Striker Chip · 500,000 money
- `+5` — 35× Striker Chip · 800,000 money
- `+6` — 42× Striker Chip · 10× Pandora Power Core
- `+7` — 49× Striker Chip · 50× Pandora Power Core
- `+8` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Negris Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Negris Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Negris Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Negris Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Negris Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Negris Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 516 · Aidas 艾达丝
**Role** Striker · **Attack** physical · **Generation** old
**Ratings** Damage 9/10 · Defence 8/10 · Assist 10/10

### Signature skill
- **Ⅰ** at `+0` — Super SniperⅠ (艾达丝，超级狙击)
  Aidas is expert in ranged weapons such as guns and artillery. She does not gain Accumulator during battle and can't use Accumulator to cast skills, but can use Normal Attack 3 times on a single enemy in her round. Aidas' Normal Attack damage coefficient is 150%. After each Normal Attack, Damage and Crit Rate will be increased by 15% (absolute value), up to 200% Damage and 150% Crit Rate (absolute value) (reset when Aidas is killed). In enemy round, each time an ally is attacked, Aidas uses Normal Attack on the attacking enemy. She uses a custom sniper cannon, having 40% chance to lock the target for 1 round (every Normal Attack in her round has the chance to lock the target; counter attacks and cooperative attacks may also lock enemies). At the start of battle, Aidas gains Eye of True Sight until the end.
- **Ⅱ** at `+T` — Super SniperⅡ (艾达丝，超级狙击)
  Aidas is expert in ranged weapons such as guns and artillery. She does not gain Accumulator during battle and can't use Accumulator to cast skills, but can use Normal Attack 4 times on a single enemy in her round. Aidas' Normal Attack damage coefficient is 150%. After each Normal Attack, Damage and Crit Rate will be increased by 20% (absolute value), up to 240% Damage and 200% Crit Rate (absolute value) (reset when Aidas is killed). In enemy round, each time an ally is attacked, Aidas uses Normal Attack on the attacking enemy. She uses a custom sniper cannon, having 40% chance to lock the target for 1 round (every Normal Attack in her round has the chance to lock the target; counter attacks and cooperative attacks may also lock enemies). At the start of battle, Aidas gains Eye of True Sight until the end.
- **Ⅲ** at `+T3` — Super Sniper (艾达丝，超级狙击)
  Aidas is expert in ranged weapons such as guns and artillery. She does not gain Accumulator during battle and can't use Accumulator to cast skills, but can use Normal Attack 5 times on a single enemy in her round. Aidas' Normal Attack damage coefficient is 180% and ignores 80% enemy defense. After each Normal Attack, Damage will be increased by 25% and Crit Rate by 30% (absolute value), both up to 300% (absolute value) (reset when Aidas is killed). In enemy round, each time an ally is attacked, Aidas uses Normal Attack on the attacking enemy. In ally round, she cooperates with allies, using a Normal Attack on the enemy her ally is attacking. She uses a custom sniper cannon, having 40% chance to lock the target for 1 round (every Normal Attack in her round has the chance to lock the target; counter attacks and cooperative attacks may also lock enemies), and her attacks will not be blocked. At the start of battle, Aidas gains Eye of True Sight until the end. At the start of battle, she gains immunity to Lock, Freeze, Confuse, Petrify, Icebound, and Entangle for 3 rounds.
- **IV** at `+T4` — Super Sniper IV (艾达丝，超级狙击T4)
  Aidas is expert in ranged weapons such as guns and artillery. She does not gain Accumulator during battle and can't use Accumulator to cast skills, but can use Normal Attack 5 times on a single enemy in her round. Aidas' Normal Attack damage coefficient is 180% and ignores 80% enemy defense. Each Normal Attack deals damage equal to 10% of current Accumulator to the target and extra 3M True Damage. After each Normal Attack, Damage will be increased by 35% and Crit Rate by 40% (absolute value), the former can be increased up to 350% and the latter can be increased up to 400% (absolute value) (reset when Aidas is killed). In enemy round, each time an ally is attacked, Aidas uses Normal Attack on the attacking enemy. In ally round, she cooperates with allies, using a Normal Attack on the enemy her ally is attacking. She uses a custom sniper cannon, having 50% chance to lock the target for 1 round (every Normal Attack in her round has the chance to lock the target; counter attacks and cooperative attacks may also lock enemies), and her attacks will not be blocked. Aidas's each attack will heal equal to 50% of the damage dealt, and the part exceeding max HP will be converted into shield (up to 150% of Aidas's max HP). At the start of battle, Aidas gains Eye of True Sight until the end. At the start of battle, she gains immunity to Lock, Freeze, Confuse, Petrify, Icebound, Entangle, and Weaken for 5 rounds.

### Augment cost (per step)
- `+1` — 5× Striker Chip · 100,000 money
- `+2` — 10× Striker Chip · 200,000 money
- `+3` — 21× Striker Chip · 300,000 money
- `+4` — 28× Striker Chip · 500,000 money
- `+5` — 35× Striker Chip · 800,000 money
- `+6` — 42× Striker Chip · 10× Pandora Power Core
- `+7` — 49× Striker Chip · 50× Pandora Power Core
- `+8` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Aidas Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Aidas Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Aidas Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Aidas Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Aidas Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Aidas Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 537 · Silvia 索菲亚
**Role** Striker · **Attack** physical · **Generation** old
**Ratings** Damage 10/10 · Defence 7/10 · Assist 8/10

### Signature skill
- **Ⅰ** at `+0` — Metal Storm (金属风暴)
  Single Attack, attacks 3 times in succession, each hit dealing 200% S-ATK damage. Lastly, you recover 100 Accumulator.

### Augment cost (per step)
- `+1` — 5× Striker Chip · 100,000 money
- `+2` — 10× Striker Chip · 200,000 money
- `+3` — 21× Striker Chip · 300,000 money
- `+4` — 28× Striker Chip · 500,000 money
- `+5` — 35× Striker Chip · 800,000 money
- `+6` — 42× Striker Chip · 10× Pandora Power Core
- `+7` — 49× Striker Chip · 50× Pandora Power Core
- `+8` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Silvia Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Silvia Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Silvia Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Silvia Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Silvia Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Silvia Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 542 · Yvette 伊薇特
**Role** Striker · **Attack** physical · **Generation** latest
**Ratings** Damage 10/10 · Defence 7/10 · Assist 8/10

### Skill panels
**Slot 1 — Chains of Ruin** (id 1579, unlocks at `+0`)
  - **Ⅰ** at `+0` — Chains of RuinⅠ (伊薇特技能描述)
    Cross Attack, deals 350% S-ATK damage to targets. Has a 50% chance to apply Ruin Code with 1 stack of Virus to 2 random enemies. Units with Ruin Code gain 1 stack of Virus each time they're hit by an S-ATK. Ruin Code lasts 99 rounds. Also increases your ATK and S-ATK by 40% for 2 rounds. Has a 45% chance to Lock enemies hit for 2 rounds. Lastly, you recover 100 Accumulator. Ruin Code: When a ship with Ruin Code is destroyed, it creates an explosion that deals 350% S-ATK damage plus extra S-ATK damage based on Virus stacks (deals extra S-ATK damage equal to 10% of the exploding ship's Max HP per stack up to 4 stacks) to ships in a cross-shaped area.(The effective priority is higher than the Death Code, and the Death Code will be overwritten)
  - **Ⅱ** at `+7` — Chains of RuinⅡ (伊薇特技能描述)
    Cross Attack, plunders 50% Penetration (absolute value) from targets and deals 360% S-ATK. Applies Ruin Code with 1 stack of Virus to 2 random enemies. Units with Ruin Code gain 1 stack of Virus each time they're hit by an S-ATK. Ruin Code lasts 99 rounds. You gain Eye of True Sight for 2 rounds. Increases your ATK and S-ATK by 50% for 2 rounds. Has a 50% chance to Lock enemies hit for 2 rounds. Lastly, you recover 100 Accumulator. Ruin Code: When a ship with Ruin Code is destroyed, it creates an explosion that deals 360% S-ATK damage plus extra S-ATK damage based on Virus stacks (deals extra S-ATK damage equal to 15% of the exploding ship's Max HP per stack up to 4 stacks) to ships in a cross-shaped area.(The effective priority is higher than the Death Code, and the Death Code will be overwritten)
  - **Ⅲ** at `+13` — Chains of RuinⅢ (伊薇特技能描述)
    Cross Attack, plunders 70% Penetration (absolute value) from targets and deals 380% S-ATK. Applies Ruin Code with 1 stack of Virus to 2 random enemies. Units with Ruin Code gain 1 stack of Virus each time they're hit by an S-ATK and on each new application of Ruin Code. Ruin Code lasts 99 rounds. You gain Eye of True Sight for 2 rounds. Increases your ATK and S-ATK by 60% for 2 rounds. Has a 55% chance to Lock enemies hit for 2 rounds. Lastly, you recover 100 Accumulator. Ruin Code: When a ship with Ruin Code is destroyed, it creates an explosion that deals 380% S-ATK damage based on Virus stacks (deals extra S-ATK damage equal to 20% of the exploding ship's Max HP per stack up to 4 stacks) to ships in a cross-shaped area.(The effective priority is higher than the Death Code, and the Death Code will be overwritten)
  - **Ⅳ** at `+15` — Chains of RuinIV (伊薇特技能描述)
    Cross Attack, plunders 100% Penetration (absolute value) from targets and deals 400% S-ATK. Applies 1 stack of Virus to enemies with Ruin Code, and then applies Ruin Code with 1 stack of Virus to 2 random enemies. Units with Ruin Code gain 1 stack of Virus each time they're hit by an S-ATK and on each new application of Ruin Code. Ruin Code lasts 99 rounds. You gain Eye of True Sight for 2 rounds. Increases your ATK and S-ATK by 80% for 2 rounds. Has a 65% chance to Lock enemies hit for 2 rounds. Lastly, you recover 100 Accumulator. Ruin Code: When a ship with Ruin Code is destroyed, it creates an explosion that deals 400% S-ATK damage plus extra S-ATK damage based on Virus stacks (deals extra S-ATK damage equal to 30% of the exploding ship's Max HP per stack up to 4 stacks) to ships in a cross-shaped area.(The effective priority is higher than the Death Code, and the Death Code will be overwritten)

**Slot 2 — Virus** (id 1580, unlocks at `+3`)
  - **Ⅰ** at `+3` — VirusⅠ (伊薇特技能描述)
    (Takes effect at the start of battle) Applies Ruin Code and 1 stack of Virus to 2 random enemies, lasting 99 rounds.
  - **Ⅱ** at `+9` — VirusⅡ (伊薇特技能描述)
    (Takes effect at the start of battle) Applies Ruin Code and 1 stack of Virus to 2 random enemies, lasting 99 rounds. Ruin Code explosions now apply Ruin Code to ships in a cross-shaped area around the explosion, or 1 stack of Virus if they already have Ruin Code.
  - **Ⅲ** at `+T1` — VirusⅢ (伊薇特技能描述)
    (Takes effect at the start of battle) Applies Ruin Code and 1 stack of Virus to 2 random enemies, lasting 99 rounds. Ruin Code explosions now apply Ruin Code to ships in a cross-shaped area around the explosion, or 1 stack of Virus if they already have Ruin Code. Yvette deals 400% extra S-ATK damage against enemies with 3 or more stacks of Virus.
  - **Ⅳ** at `+T4` — VirusIV (伊薇特技能描述)
    (Takes effect at the start of battle) Applies Ruin Code and 1 stack of Virus to 2 random enemies, lasting 99 rounds. Ruin Code explosions now apply Ruin Code to ships in a cross-shaped area around the explosion, or 1 stack of Virus if they already have Ruin Code. Yvette deals 400% extra S-ATK damage against enemies with 3 or more stacks of Virus. Should Yvette die, all active Ruin Codes explode and are removed, dealing 400% S-ATK damage plus extra S-ATK damage based on Virus stacks to enemies with Ruin Code and those within a cross-shaped area near them.

**Slot 3 — Code Blessing** (id 1581, unlocks at `+5`)
  - **Ⅰ** at `+5` — Code BlessingⅠ (伊薇特技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +30% S-ATK: +30% DMG Bonus (Absolute Value): +15%
  - **Ⅱ** at `+11` — Code BlessingⅡ (伊薇特技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +60% S-ATK: +60% DMG Bonus (Absolute Value): +20%
  - **Ⅲ** at `+T2` — Code BlessingⅢ (伊薇特技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +90% S-ATK: +90% DMG Bonus (Absolute Value): +25%
  - **Ⅳ** at `+T3` — Code BlessingIV (伊薇特技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +120% S-ATK: +120% DMG Bonus (Absolute Value): +30%

### Augment cost (per step)
- `+1` — 5× Striker Chip · 100,000 money
- `+2` — 10× Striker Chip · 200,000 money
- `+3` — 21× Striker Chip · 300,000 money
- `+4` — 28× Striker Chip · 500,000 money
- `+5` — 35× Striker Chip · 800,000 money
- `+6` — 42× Striker Chip · 10× Pandora Power Core
- `+7` — 49× Striker Chip · 50× Pandora Power Core
- `+8` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Yvette Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Yvette Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Yvette Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Yvette Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Yvette Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Yvette Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 543 · Kane 卡因
**Role** Striker · **Attack** physical · **Generation** latest
**Ratings** Damage 10/10 · Defence 7/10 · Assist 8/10

### Skill panels
**Slot 1 — Shadow Ambush** (id 1589, unlocks at `+0`)
  - **Ⅰ** at `+0` — Shadow AmbushⅠ (卡因+20，被索敌目标死亡时自身附加buff)
    Target the enemy unit with the least HP (percentage) with a Horizontal Attack dealing 350% S-ATK damage. You lose 15% of Max HP (only triggers while at or above 70% HP), increasing the damage dealt by 1% and damage reduction by 1% for every 1% of HP below maximum. Can only be healed by your own skills. Gains Eye of True Sight for 2 rounds. Lastly, you recover 100 Accumulator.
  - **Ⅱ** at `+5` — Shadow AmbushⅡ (卡因技能描述，无实际意义)
    Target the enemy unit with the least HP (percentage) with a Horizontal Attack dealing 380% S-ATK damage. You lose 15% of Max HP (only triggers while at or above 70% HP), increasing the damage dealt by 1.5% and damage reduction by 1.5% for every 1% of HP below maximum. Can only be healed by your own skills. Kane's skills always critical hit. Gains Eye of True Sight for 2 rounds. Lastly, you recover 100 Accumulator.
  - **Ⅲ** at `+9` — Shadow AmbushⅢ (卡因技能描述，无实际意义)
    Target the enemy unit with the least HP (percentage) with a Horizontal Attack dealing 420% S-ATK damage. You lose 15% of Max HP (only triggers while at or above 70% HP), increasing the damage dealt by 2% and damage reduction by 2% for every 1% of HP below maximum. Can only be healed by your own skills. Kane's skills always critical hit and ignores 30% DEF and S-DEF. Gains Eye of True Sight for 2 rounds. Lastly, you recover 100 Accumulator.
  - **Ⅳ** at `+15` — Shadow AmbushIV (卡因技能描述，无实际意义)
    Target the enemy unit with the least HP (percentage) with a Horizontal Attack, plundering 70% of their Accumulator (not affected by immunity) and dealing 450% S-ATK damage. You lose 15% of Max HP (only triggers while at or above 70% HP), increasing the damage dealt by 3% and damage reduction by 3% for every 1% of HP below maximum. Can only be healed by your own skills. Kane's skills always critical hit and ignores 45% DEF and S-DEF. Gains Eye of True Sight for 2 rounds. Lastly, you recover 100 Accumulator.

**Slot 2 — Shadow Onslaught** (id 1590, unlocks at `+2`)
  - **Ⅰ** at `+2` — Shadow OnslaughtⅠ (卡因+20，行动前净化自身)
    (Takes effect at the start of battle) Killing an enemy with an S-ATK increases damage by 30% (absolute value; stacks and lasts until destroyed) and restores 100% of Max HP and Accumulator.
  - **Ⅱ** at `+7` — Shadow OnslaughtⅡ (卡因技能描述，无实际意义)
    (Takes effect at the start of battle) Killing an enemy with an S-ATK increases damage by 30% (absolute value; stacks and lasts until destroyed) and restores 100% of Max HP and Accumulator. Damage increases by 3% for every 1% of Max HP the enemy is missing.
  - **Ⅲ** at `+11` — Shadow OnslaughtⅢ (卡因技能描述，无实际意义)
    (Takes effect at the start of battle) Killing an enemy with an S-ATK increases damage by 30% (absolute value; stacks and lasts until destroyed) and restores 100% of Max HP and Accumulator. Damage increases by 3% for every 1% of Max HP the enemy is missing. When hit by lethal damage (including instant destruction; doesn't block instant destruction that ignores immunity), survives with at least 1 HP, gain Dark Conceal (cannot be targeted) for 1 rounds, and are cleansed of all crowd-control effects (Freeze, Lock, Confuse, Petrify, Icebound, Entangle, Forbidding Skill Use) and Weaken, gains 100 Accumulator, and then launches a single attack against the damage's origin. This attack deals 450% S-ATK damage, has all of Kane's skill effects apart from follow-up attacks, and comes with Hunter Focus. (Usable 1 time per battle, but being revived or rebirthed resets charges up to 3 times; triggers before Starcore Essence).
  - **Ⅳ** at `+T3` — Shadow OnslaughtIV (卡因技能描述，无实际意义)
    (Takes effect at the start of battle) Killing an enemy with an S-ATK increases damage by 30% (absolute value; stacks and lasts until destroyed) and restores 100% of Max HP and Accumulator. Damage increases by 3% for every 1% of Max HP the enemy is missing. When hit by lethal damage (including instant destruction; doesn't block instant destruction that ignores immunity), survives with at least 1 HP, gain Dark Conceal (cannot be targeted) for 1 rounds, and are cleansed of all crowd-control effects (Freeze, Lock, Confuse, Petrify, Icebound, Entangle, Forbidding Skill Use) and Weaken, gains 100 Accumulator, and then launches a single attack against the damage's origin. This attack deals 450% S-ATK damage, has all of Kane's skill effects apart from follow-up attacks, and comes with Hunter Focus. (Usable 1 time per battle, but being revived or rebirthed resets charges up to 3 times; triggers before Starcore Essence). If the S-ATK doesn't kill an enemy, 1 extra S-ATK is launched as a follow-up attack.

**Slot 3 — Stalker's Creed** (id 1591, unlocks at `+3`)
  - **Ⅰ** at `+3` — Stalker's CreedⅠ (卡因技能描述，无实际意义)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +60% S-ATK: +60% DMG Bonus (Absolute Value): +15% Crit ATK (Absolute Value) +15%
  - **Ⅱ** at `+8` — Stalker's CreedⅡ (卡因技能描述，无实际意义)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +90% S-ATK: +90% DMG Bonus (Absolute Value): +20% Crit ATK (Absolute Value) +20%
  - **Ⅲ** at `+13` — Stalker's CreedⅢ (卡因技能描述，无实际意义)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +120% S-ATK: +120% DMG Bonus (Absolute Value): +25% Crit ATK (Absolute Value) +25%
  - **Ⅳ** at `+T` — Stalker's CreedIV (卡因技能描述，无实际意义)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +150% S-ATK: +150% DMG Bonus (Absolute Value): +30% Crit ATK (Absolute Value) +30%

**Slot 4 — Deadly Lock-on** (id 1592, unlocks at `+10`)
  - **Ⅰ** at `+10` — Deadly Lock-onⅠ (卡因技能描述，无实际意义)
    (Takes effect at the start of battle) Lock-on (1 unit can be locked on to at a time) to the enemy with the least HP when using a skill until they are destroyed. Lock On: The enemy unit deals 75% reduced damage. When the target acts, Kane attacks it with a single-target skill attack (can trigger 1 time per round and target), dealing 450% S-ATK damage and has all of Kane's skill effects apart from follow-up attacks.
  - **Ⅱ** at `+T1` — Deadly Lock-onⅡ (卡因技能描述，无实际意义)
    (Takes effect at the start of battle) Lock-on (1 unit can be locked on to at a time) to the enemy with the least HP when using a skill until they are destroyed. Lock On: The enemy unit deals 75% reduced damage. When the target acts, Kane attacks it with a single-target skill attack (can trigger 1 time per round and target), dealing 450% S-ATK damage and has all of Kane's skill effects apart from follow-up attacks. When the locked-on target is destroyed, Kane immediately locks on to another enemy.
  - **Ⅲ** at `+T2` — Deadly Lock-onⅢ (卡因技能描述，无实际意义)
    (Takes effect at the start of battle) Lock-on (1 unit can be locked on to at a time) to the enemy with the least HP when using a skill until they are destroyed. Lock On: The enemy unit deals 75% reduced damage. When the target acts, Kane attacks it with a single-target skill attack (can trigger 1 time per round and target), dealing 450% S-ATK damage and has all of Kane's skill effects apart from follow-up attacks. When the locked-on target is destroyed, Kane immediately locks on to another enemy. An enemy locked on by Kane cannot target him with skills (including attacks and skill effects). Kane's S-ATK against the locked-on target deal True Damage equal to 100% of the initial hit.
  - **Ⅳ** at `+T4` — Deadly Lock-onIV (卡因技能描述，无实际意义)
    (Takes effect at the start of battle) Lock-on (1 unit can be locked on to at a time) to the enemy with the least HP when using a skill until they are destroyed. Lock On: The enemy unit deals 75% reduced damage. When the target acts, Kane attacks it with a single-target skill attack (can trigger 1 time per round and target), dealing 450% S-ATK damage and has all of Kane's skill effects apart from follow-up attacks. Kane's attacks against the locked-on enemy gain Hunter Focus. When the locked-on target is destroyed, Kane immediately locks on to another enemy. An enemy locked on by Kane cannot target him with skills (including attacks and skill effects). Kane's S-ATK against the locked-on target deal True Damage equal to 100% of the initial hit. When an enemy locked on by Kane is destroyed, Kane gains Hunter Focus for 2 rounds, and will be cleared of crowd-control effects (Freeze, Lock, Confuse, Petrify, Icebound, Entangle and Forbidding Skill Use) before acting on his next round. Hunter Focus: The attack always hits, ignores Dodge, Evasive and Time Ward.

### Augment cost (per step)
- `+1` — 5× Striker Chip · 100,000 money
- `+2` — 10× Striker Chip · 200,000 money
- `+3` — 21× Striker Chip · 300,000 money
- `+4` — 28× Striker Chip · 500,000 money
- `+5` — 35× Striker Chip · 800,000 money
- `+6` — 42× Striker Chip · 10× Pandora Power Core
- `+7` — 49× Striker Chip · 50× Pandora Power Core
- `+8` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Kane Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Kane Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Kane Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Kane Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Kane Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Kane Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 554 · Angelo 安杰罗
**Role** Striker · **Attack** physical · **Generation** latest
**Ratings** Damage 9/10 · Defence 8/10 · Assist 10/10

### Skill panels
**Slot 1 — Ashes of the Falling Sky** (id 1665, unlocks at `+0`)
  - **Ⅰ** at `+0` — Ashes of the Falling SkyⅠ (安杰罗技能描述)
    Angelo possesses the cataclysmic weapon "Meteor Cannon," which requires 3 "CHARGE" cycles to activate. The skill is "CHARGE" before the charges are complete, and it switches to "Meteor Cannon" once fully charged. At the start of the battle, Angelo gains Eye of True Sight, which lasts until the end of the battle. [Meteor Charge]: Enters a charging state and gains 1 Charge, increasing Accumulator by 25 without consuming any upon casting. Charge stacks up to 3 times. [Meteor Cannon]: Deals 1800% S-ATK damage to the 2 enemy units that were not untargetable and dealt the most damage last round. Finally, clears all CHARGE stacks, exits CHARGE state, and recovers 100 Accumulator.
  - **Ⅱ** at `+6` — Ashes of the Falling SkyⅡ (安杰罗技能描述)
    Angelo possesses the cataclysmic weapon "Meteor Cannon," which requires 3 "CHARGE" cycles to activate. The skill is "CHARGE" before the charges are complete, and it switches to "Meteor Cannon" once fully charged. At the start of the battle, Angelo gains Eye of True Sight, which lasts until the end of the battle. [Meteor Charge]: Enters a charging state and gains 1 Charge, increasing Accumulator by 50 without consuming any upon casting. Charge stacks up to 3 times. [Meteor Cannon]: Targets the 2 enemy units that were not untargetable last round and dealt the most damage, first clears their buffs, then deals 2200% S-ATK damage, and finally clears all Charge stacks, exits CHARGE state, and recovers 100 Accumulator.
  - **Ⅲ** at `+10` — Ashes of the Falling SkyⅢ (安杰罗技能描述)
    Angelo possesses the cataclysmic weapon "Meteor Cannon," which requires 3 "CHARGE" cycles to activate. The skill is "CHARGE" before the charges are complete, and it switches to "Meteor Cannon" once fully charged. At the start of the battle, Angelo gains Eye of True Sight, which lasts until the end of the battle. [Meteor Charge]: Enters a charging state and gains 1 Charge, increasing Accumulator by 75 without consuming any upon casting. Charge stacks up to 3 times. [Meteor Cannon]: Targets the 2 enemy units that were not untargetable last round and dealt the most damage, first clears their buffs, then deals 2600% S-ATK damage with guaranteed Penetration (cannot be Blocked), finally removes all CHARGE stacks, exits CHARGE state, and recovers 100 Accumulator.
  - **Ⅳ** at `+15` — Ashes of the Falling SkyⅣ (安杰罗技能描述)
    Angelo possesses the cataclysmic weapon "Meteor Cannon," which requires 3 "CHARGE" cycles to activate. The skill is "CHARGE" before the charges are complete, and it switches to "Meteor Cannon" once fully charged. At the start of the battle, Angelo gains Eye of True Sight, which lasts until the end of the battle. [Meteor Charge]: Enters a charging state and gains 1 Charge, increasing Accumulator by 100 without consuming any upon casting. Charge stacks up to 3 times. [Meteor Cannon]: Targets the two enemy units that were not untargetable last round and dealt the most damage, first clears their buffs, then deals 3000% S-ATK damage with guaranteed Penetration (cannot be Blocked), followed by dealing True Damage equal to 300% of the first phase S-ATK damage to the two enemies with the lowest HP. Finally, clears all CHARGE stacks, exits CHARGE state, and recovers 100 Accumulator.

**Slot 2 — Meteor Cannon** (id 1666, unlocks at `+2`)
  - **Ⅰ** at `+2` — Meteor CannonⅠ (安杰罗技能描述)
    (Takes effect at the start of battle) [Meteor Cannon] always deals critical damage.
  - **Ⅱ** at `+9` — Meteor CannonⅡ (安杰罗技能描述)
    (Takes effect at the start of battle) [Meteor Cannon] always deals critical damage. Upon reaching 3 Charges, if not incapacitated, immediately activates [Meteor Cannon].
  - **Ⅲ** at `+12` — Meteor CannonⅢ (安杰罗技能描述)
    (Takes effect at the start of battle) [Meteor Cannon] always deals critical damage. Upon reaching 3 Charges, if not incapacitated, immediately activates [Meteor Cannon]. When activating [Meteor Cannon], the skill's damage increases by 0.5% for each Accumulator above 100 spent during skill cast, up to a maximum of 200%.
  - **Ⅳ** at `+T3` — Meteor CannonⅣ (安杰罗技能描述)
    (Takes effect at the start of battle) [Meteor Cannon] always deals critical damage. Upon reaching 3 Charges, if not incapacitated, immediately activates [Meteor Cannon]. When activating [Meteor Cannon], the skill's damage increases by 0.5% for each Accumulator above 100 spent during skill cast, up to a maximum of 200%. Meteor Cannon's attack comes with the Hunter Focus effect and can ignore all immunity to lethal damage and resistance to lethal damage except for Starcore Essence.

**Slot 3 — Destructive Power** (id 1667, unlocks at `+4`)
  - **Ⅰ** at `+4` — Destructive PowerⅠ (安杰罗技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +60% ATK: +60% Crit ATK (Absolute Value): +30% DMG Bonus (Absolute Value): +15%
  - **Ⅱ** at `+8` — Destructive PowerⅡ (安杰罗技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +90% ATK: +90% Crit ATK (Absolute Value): +40% DMG Bonus (Absolute Value): +20%
  - **Ⅲ** at `+13` — Destructive PowerⅢ (安杰罗技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +120% ATK: +120% Crit ATK (Absolute Value): +50% DMG Bonus (Absolute Value): +25%
  - **Ⅳ** at `+T` — Destructive PowerⅣ (安杰罗技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +150% ATK: +150% Crit ATK (Absolute Value): +60% DMG Bonus (Absolute Value): +30%

**Slot 4 — Meteor Charge** (id 1668, unlocks at `+T`)
  - **Ⅰ** at `+T` — Meteor ChargeⅠ (安杰罗技能描述)
    (Takes effect at the start of battle) Angelo's custom energy defense device makes him immune to effects that reduce Accumulator (including those that ignore immunity and protection against Accumulator reduction, and this effect cannot be disabled by skills that prevent skill effects from activating).
  - **Ⅱ** at `+T1` — Meteor ChargeⅡ (安杰罗技能描述)
    (Takes effect at the start of battle) Angelo's custom energy defense device makes him immune to effects that reduce Accumulator (including those that ignore immunity and protection against Accumulator reduction, and this effect cannot be disabled by skills that prevent skill effects from activating). While in CHARGE state, for every additional 300 Accumulator gained, complete 1 CHARGE. For each friendly unit that dies, complete 1 CHARGE.
  - **Ⅲ** at `+T2` — Meteor ChargeⅢ (安杰罗技能描述)
    (Takes effect at the start of battle) Angelo's custom energy defense device makes him immune to effects that reduce Accumulator (including those that ignore immunity and protection against Accumulator reduction, and this effect cannot be disabled by skills that prevent skill effects from activating). While in CHARGE state, for every additional 300 Accumulator gained, complete 1 CHARGE. For each friendly unit that dies, complete 1 CHARGE. Every time a CHARGE skill is used, the Accumulator gained increases to 200.
  - **Ⅳ** at `+T4` — Meteor ChargeⅣ (安杰罗技能描述)
    (Takes effect at the start of battle) Angelo's custom energy defense device makes him immune to effects that reduce Accumulator (including those that ignore immunity and protection against Accumulator reduction, and this effect cannot be disabled by skills that prevent skill effects from activating). While in CHARGE state, for every additional 300 Accumulator gained, complete 1 CHARGE. For each friendly unit that dies, complete 1 CHARGE. Every time a CHARGE skill is used, the Accumulator gained increases to 200. At the start of battle, as well as after each revival or rebirth, you gain "Dark Conceal," making you untargetable by attacks and enemy skill effects for 3 rounds.

### Augment cost (per step)
- `+1` — 5× Striker Chip · 100,000 money
- `+2` — 10× Striker Chip · 200,000 money
- `+3` — 21× Striker Chip · 300,000 money
- `+4` — 28× Striker Chip · 500,000 money
- `+5` — 35× Striker Chip · 800,000 money
- `+6` — 42× Striker Chip · 10× Pandora Power Core
- `+7` — 49× Striker Chip · 50× Pandora Power Core
- `+8` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Angelo's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Angelo's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Angelo's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Angelo's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Angelo's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Angelo's Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 556 · Bebo 贝波
**Role** Striker · **Attack** physical · **Generation** old
**Ratings** Damage 9/10 · Defence 8/10 · Assist 10/10

### Signature skill
- **Ⅰ** at `+0` — Heat-seeking Missile (贝波)
  Cross Attack, deals 200% S-ATK damage to targets and finally recovers 100 Accumulator.

### Augment cost (per step)
- `+1` — 5× Striker Chip · 100,000 money
- `+2` — 10× Striker Chip · 200,000 money
- `+3` — 21× Striker Chip · 300,000 money
- `+4` — 28× Striker Chip · 500,000 money
- `+5` — 35× Striker Chip · 800,000 money
- `+6` — 42× Striker Chip · 10× Pandora Power Core
- `+7` — 49× Striker Chip · 50× Pandora Power Core
- `+8` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Bebo's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Bebo's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Bebo's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Bebo's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Bebo's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Bebo's Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 561 · Alana 阿兰
**Role** Striker · **Attack** physical · **Generation** latest
**Ratings** Damage 9/10 · Defence 5/10 · Assist 6/10

### Skill panels
**Slot 1 — Lethal Chord** (id 1700, unlocks at `+0`)
  - **Ⅰ** at `+0` — Lethal ChordⅠ (阿兰技能描述)
    Cross Attack, deals 320% S-ATK damage to targets. Has a 40% chance to lock all enemies (probability for each target is calculated independently) for 2 rounds. Increases your own ATK and S-ATK by 30%. When S-ATK is used on the Locked enemies, ignore 30% of the target's DEF and S-DEF (including the lock applied by this skill). Lastly, you recover 100 Accumulator.
  - **Ⅱ** at `+7` — Lethal ChordⅡ (阿兰技能描述)
    Cross Attack, deals 350% S-ATK damage to targets. Initially, there is a 40% chance to lock all enemies (probability for each target is calculated independently) for 2 rounds. After each skill use, the chance to Lock increases by 5% (the accumulated increase in Lock chance will not be Reset after revival), up to an additional 20% Lock chance.Increases your ATK and S-ATK by 40% for 2 rounds. When S-ATK is used on the Locked enemies, ignores 40% of the target's DEF and S-DEF (including the Lock applied by this skill). Lastly, you recover 100 Accumulator.
  - **Ⅲ** at `+13` — Lethal ChordⅢ (阿兰技能描述)
    Cross Attack, deals 380% S-ATK damage to targets. Initially, there is a 40% chance to lock all enemies (probability for each target is calculated independently) for 2 rounds. After each skill use, the chance to Lock increases by 10% (the accumulated increase in Lock chance will not be Reset after revival), up to an additional 30% Lock chance.Increases your ATK and S-ATK by 50% for 2 rounds. When S-ATK is used on the Locked enemies, it ignores 50% of the target's DEF and S-DEF (including Lock applied by this skill). Lastly, you recover 100 Accumulator.
  - **Ⅳ** at `+15` — Lethal ChordⅣ (阿兰技能描述)
    Cross Attack, plunders 50% Accumulator from the target, then deals 420% S-ATK damage to targets. Initially, there is a 40% chance to Lock all enemies (probability for each target is calculated independently) for 2 rounds. After each skill use, the chance to Lock increases by 20% (the accumulated Lock chance will not Reset after revival), up to an additional 40% Lock chance.Increases your ATK and S-ATK by 60% for 2 rounds. When S-ATK is used on the Locked enemies, it ignores 60% of the target's DEF and S-DEF (including Lock applied by this skill). Lastly, you recover 100 Accumulator.

**Slot 2 — Resonance** (id 1701, unlocks at `+3`)
  - **Ⅰ** at `+3` — ResonanceⅠ (阿兰技能描述)
    (Takes effect at the start of battle) When S-ATK is used on the Locked enemies, it will always be a critical hit, and the Crit ATK damage is increased by 30%.
  - **Ⅱ** at `+9` — ResonanceⅡ (阿兰技能描述)
    (Takes effect at the start of battle) When S-ATK is used on the Locked enemies, it will always be a critical hit, and the Crit ATK damage is increased by 30%. S-ATK deals 80% increased damage to enemies that are Locked.
  - **Ⅲ** at `+T1` — ResonanceⅢ (阿兰技能描述)
    (Takes effect at the start of battle) When S-ATK is used on the Locked enemies, it will always be a critical hit, and the Crit ATK damage is increased by 30%. S-ATK deals 80% increased damage to enemies that are Locked. Upon first skill cast, there's an additional 100% chance to Lock 3 random enemies for 2 rounds, ignoring their immunity and protection effects (can be Reset after each revival).
  - **Ⅳ** at `+T4` — ResonanceⅣ (阿兰技能描述)
    (Takes effect at the start of battle) When S-ATK is used on the Locked enemies, it will always be a critical hit, and the Crit ATK damage is increased by 30%. S-ATK deals 80% increased damage to enemies that are Locked. Upon first skill cast, there's an additional 100% chance to Lock 3 random enemies for 2 rounds, ignoring their immunity and protection effects (can be Reset after each revival). When Lock is applied to an enemy, there is an 80% chance (chance is calculated individually for each unit) to ignore the target's immunity and protection effects.

**Slot 3 — Blessing** (id 1702, unlocks at `+5`)
  - **Ⅰ** at `+5` — BlessingⅠ (阿兰技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +30% S-ATK: +30% DMG Bonus (Absolute Value): +15%
  - **Ⅱ** at `+11` — BlessingⅡ (阿兰技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +60% S-ATK: +60% DMG Bonus (Absolute Value): +20%
  - **Ⅲ** at `+T2` — BlessingⅢ (阿兰技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +90% S-ATK: +90% DMG Bonus (Absolute Value): +25%
  - **Ⅳ** at `+T3` — BlessingⅣ (阿兰技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +120% S-ATK: +120% DMG Bonus (Absolute Value): +30%

### Augment cost (per step)
- `+1` — 5× Striker Chip · 100,000 money
- `+2` — 10× Striker Chip · 200,000 money
- `+3` — 21× Striker Chip · 300,000 money
- `+4` — 28× Striker Chip · 500,000 money
- `+5` — 35× Striker Chip · 800,000 money
- `+6` — 42× Striker Chip · 10× Pandora Power Core
- `+7` — 49× Striker Chip · 50× Pandora Power Core
- `+8` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Alana's Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Alana's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Alana's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Alana's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Alana's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Alana's Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 568 · Yvonne 伊温
**Role** Striker · **Attack** physical · **Generation** old
**Ratings** Damage 9/10 · Defence 8/10 · Assist 10/10

### Signature skill
- **Ⅰ** at `+0` — Charged Strike (莱卡+0)
  Vertical Attack, deals 280% S-ATK damage to the target. Lastly, recovers 100 Accumulator.

### Augment cost (per step)
- `+1` — 5× Striker Chip · 100,000 money
- `+2` — 10× Striker Chip · 200,000 money
- `+3` — 21× Striker Chip · 300,000 money
- `+4` — 28× Striker Chip · 500,000 money
- `+5` — 35× Striker Chip · 800,000 money
- `+6` — 42× Striker Chip · 10× Pandora Power Core
- `+7` — 49× Striker Chip · 50× Pandora Power Core
- `+8` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Yvonne's Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Yvonne's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Yvonne's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Yvonne's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Yvonne's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Yvonne's Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 573 · Viollet Gray 维奥莱·格雷斯
**Role** Striker · **Attack** physical · **Generation** latest
**Ratings** Damage 10/10 · Defence 7/10 · Assist 8/10

### Skill panels
**Slot 1 — Best Forward** (id 1775, unlocks at `+0`)
  - **Ⅰ** at `+0` — Best ForwardⅠ (维奥莱·格雷斯技能描述)
    Vertical Attack, deals 340% S-ATK damage to targets. When the skill attack crits, there's a 100% chance to gain 1 stack of [Fearless Charge], up to 3 stacks, lasting 2 rounds. Lastly, recovers 100 Accumulator. [Fearless Charge]: Each stack increases damage dealt by 5% (in PVE battles, each stack increases damage by 10%).
  - **Ⅱ** at `+7` — Best ForwardⅡ (维奥莱·格雷斯技能描述)
    Vertical Attack, deals 370% S-ATK damage to targets. Reduces the target's DEF and S-DEF by 80% for 2 rounds. When the skill attack crits, there's a 100% chance to gain 1 stack of [Fearless Charge], up to 3 stacks, lasting 2 rounds. Lastly, recovers 100 Accumulator. [Fearless Charge]: Each stack increases damage dealt by 10% (in PVE battles, each stack increases damage by 20%).
  - **Ⅲ** at `+9` — Best ForwardⅢ (维奥莱·格雷斯技能描述)
    Vertical Attack, first removes the target's buffs, then deals 400% S-ATK damage to the target. Reduces the target's DEF and S-DEF by 80% for 2 rounds. When the skill attack crits, there's a 100% chance to gain 1 stack of [Fearless Charge], up to 3 stacks, lasting 2 rounds. Finally, recovers 100 Accumulator. [Fearless Charge]: Each stack increases damage dealt by 10% (in PVE battles, each stack increases damage by 20%).
  - **Ⅳ** at `+15` — Best ForwardIV (维奥莱·格雷斯技能描述)
    Vertical Attack, first removes the target's buffs, then deals 440% S-ATK damage to the target. Reduces the target's DEF and S-DEF by 80% for 2 rounds. When the skill attack crits, there's a 100% chance to gain 1 stack of [Fearless Charge], up to 3 stacks, lasting 2 rounds. Finally, recovers 100 Accumulator. 【Fearless Charge】: Each stack increases your damage dealt by 15% (in PVE battles, each stack increases damage by 30%). When casting a skill, each stack deals an additional instance of S-ATK damage.

**Slot 2 — Fearless Charge** (id 1776, unlocks at `+3`)
  - **Ⅰ** at `+3` — Fearless ChargeⅠ (维奥莱·格雷斯技能描述)
    (Takes effect at the start of battle) Each stack of [Fearless Charge] increases all allies' S-ATK by 30%.
  - **Ⅱ** at `+10` — Fearless ChargeⅡ (维奥莱·格雷斯技能描述)
    (Takes effect at the start of battle) Each stack of [Fearless Charge] increases all allies' S-ATK by 30%. Each stack of [Fearless Charge] increases the Crit ATK of all allies by 20%.
  - **Ⅲ** at `+T3` — Fearless ChargeⅢ (维奥莱·格雷斯技能描述)
    (Takes effect at the start of battle) Each stack of [Fearless Charge] increases all allies' S-ATK by 30%. Each stack of [Fearless Charge] increases the Crit ATK of all allies by 20%. Each stack of [Fearless Charge] increases the damage dealt by all allies to enemies under control by 10%.
  - **Ⅳ** at `+T4` — Fearless ChargeIV (维奥莱·格雷斯技能描述)
    (Takes effect at the start of battle) Each stack of [Fearless Charge] increases all allies' S-ATK by 30%. Each stack of [Fearless Charge] increases the Crit ATK of all allies by 20%. Each stack of [Fearless Charge] increases the damage dealt by all allies to enemies under control by 10%. When casting a skill, there is a 65% chance for the S-ATK to trigger a guaranteed critical hit. In PvE battles, this chance increases to 100%.

**Slot 3 — Physical Exercise** (id 1777, unlocks at `+5`)
  - **Ⅰ** at `+5` — Physical ExerciseⅠ (维奥莱·格雷斯技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +60% S-ATK: +60% DMG Bonus (Absolute Value): +15% Dodge (Absolute Value): +30%
  - **Ⅱ** at `+13` — Physical ExerciseⅡ (维奥莱·格雷斯技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +90% S-ATK: +90% DMG Bonus (Absolute Value): +20% Dodge (Absolute Value): +40%
  - **Ⅲ** at `+T` — Physical ExerciseⅢ (维奥莱·格雷斯技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +120% S-ATK: +120% DMG Bonus (Absolute Value): +25% Dodge (Absolute Value): +50%
  - **Ⅳ** at `+T2` — Physical ExerciseIV (维奥莱·格雷斯技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +150% S-ATK: +150% DMG Bonus (Absolute Value): +30% Dodge (Absolute Value): +60%

### Augment cost (per step)
- `+1` — 5× Striker Chip · 100,000 money
- `+2` — 10× Striker Chip · 200,000 money
- `+3` — 21× Striker Chip · 300,000 money
- `+4` — 28× Striker Chip · 500,000 money
- `+5` — 35× Striker Chip · 800,000 money
- `+6` — 42× Striker Chip · 10× Pandora Power Core
- `+7` — 49× Striker Chip · 50× Pandora Power Core
- `+8` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Viollet Gray's Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Viollet Gray's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Viollet Gray's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Viollet Gray's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Viollet Gray's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Viollet Gray's Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 574 · Woon Lionel 乌恩·莱奥尼尔
**Role** Striker · **Attack** physical · **Generation** latest
**Ratings** Damage 10/10 · Defence 7/10 · Assist 8/10

### Skill panels
**Slot 1 — M30 Piercing Beam** (id 1780, unlocks at `+0`)
  - **Ⅰ** at `+0` — M30 Piercing BeamⅠ (乌恩·莱奥尼尔技能描述)
    Vertical Attack, deals 350% S-ATK damage to targets hit. Gains Eye of True Sight for 2 rounds. When using skills, 20% of max HP (retaining at least 10% HP) is converted into a shield equal to 150% of the HP lost (persists through effects that clear buffs and can stack, not exceeding 300% of the HP at the start of the battle). Lastly, recovers 100 Accumulator.
  - **Ⅱ** at `+5` — M30 Piercing BeamⅡ (乌恩·莱奥尼尔技能描述)
    Vertical Attack, deals 390% S-ATK damage to targets hit. Gains Eye of True Sight for 2 rounds. When using skills, 30% of max HP (retaining at least 10% HP) is converted into a shield equal to 200% of the HP lost (persists through effects that clear buffs and can stack, not exceeding 350% of the HP at the start of the battle). Lastly, recovers 100 Accumulator.
  - **Ⅲ** at `+9` — M30 Piercing BeamⅢ (乌恩·莱奥尼尔技能描述)
    Vertical Attack, first absorbs 65% of the target's Accumulator, then deals 430% S-ATK damage to the target hit. Gains Eye of True Sight for 2 rounds.When using skills, 40% of max HP (retaining at least 10% HP) is converted into a shield equal to 250% of the HP lost (persists through effects that clear buffs and can stack, not exceeding 400% of the HP at the start of the battle). Lastly, recovers 100 Accumulator.
  - **Ⅳ** at `+15` — M30 Piercing BeamIV (乌恩·莱奥尼尔技能描述)
    Vertical Attack, first absorbs 65% of the target's Accumulator (ignores immunity), then deals 480% S-ATK damage to the target hit. Gains Eye of True Sight for 2 rounds.When using skills, 50% of max HP (retaining at least 10% HP) is converted into a shield equal to 300% of the HP lost (persists through effects that clear buffs and can stack, up to 500% of the HP at the start of the battle). Lastly, recovers 100 Accumulator.

**Slot 2 — Energy Conversion** (id 1781, unlocks at `+2`)
  - **Ⅰ** at `+2` — Energy ConversionⅠ (乌恩·莱奥尼尔技能描述)
    (Takes effect at the start of battle) When dealing S-ATK damage, additionally deals extra S-ATK damage equal to 100% of your current shield value.
  - **Ⅱ** at `+7` — Energy ConversionⅡ (乌恩·莱奥尼尔技能描述)
    (Takes effect at the start of battle) When dealing S-ATK damage, additionally deals extra S-ATK damage equal to 100% of your current shield value. When dealing skill damage, increases own shield value by 50% of the damage dealt.
  - **Ⅲ** at `+11` — Energy ConversionⅢ (乌恩·莱奥尼尔技能描述)
    (Takes effect at the start of battle) When dealing S-ATK damage, additionally deals extra S-ATK damage equal to 100% of your current shield value. When dealing skill damage, increases own shield value by 50% of the damage dealt. Damage dealt increases by 3% and damage reduction by 3% for every 1% HP lost.
  - **Ⅳ** at `+T3` — Energy ConversionIV (乌恩·莱奥尼尔技能描述)
    (Takes effect at the start of battle) When dealing S-ATK damage, additionally deals extra S-ATK damage equal to 100% of your current shield value. When dealing skill damage, increases own shield value by 50% of the damage dealt. Damage dealt increases by 3% and damage reduction by 3% for every 1% HP lost. If current HP is below 30% of Max HP, additionally gain: Evolved Eye of True Sight, allowing attacks on ships in Invisible and Dark Conceal states.

**Slot 3 — Awaken** (id 1782, unlocks at `+3`)
  - **Ⅰ** at `+3` — AwakenⅠ (乌恩·莱奥尼尔技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +60% ATK: +60% Crit ATK (Absolute Value): +30% DMG Bonus (Absolute Value): +15%
  - **Ⅱ** at `+8` — AwakenⅡ (乌恩·莱奥尼尔技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +90% ATK: +90% Crit ATK (Absolute Value): +40% DMG Bonus (Absolute Value): +20%
  - **Ⅲ** at `+13` — AwakenⅢ (乌恩·莱奥尼尔技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +120% ATK: +120% Crit ATK (Absolute Value): +50% DMG Bonus (Absolute Value): +25%
  - **Ⅳ** at `+T` — AwakenIV (乌恩·莱奥尼尔技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +150% ATK: +150% Crit ATK (Absolute Value): +60% DMG Bonus (Absolute Value): +30%

**Slot 4 — Adversity Resilience** (id 1783, unlocks at `+10`)
  - **Ⅰ** at `+10` — Adversity ResilienceⅠ (乌恩·莱奥尼尔技能描述)
    (Takes effect at the start of battle) If current HP is below 70% of Max HP, gains an additional 50% S-ATK damage.
  - **Ⅱ** at `+T1` — Adversity ResilienceⅡ (乌恩·莱奥尼尔技能描述)
    (Takes effect at the start of battle) If current HP is below 70% of Max HP, gains an additional 50% S-ATK damage. If current HP is below 50% of Max HP, gains: S-ATK is guaranteed to crit.
  - **Ⅲ** at `+T2` — Adversity ResilienceⅢ (乌恩·莱奥尼尔技能描述)
    (Takes effect at the start of battle) If current HP is below 70% of Max HP, gains an additional 50% S-ATK damage. If current HP is below 50% of Max HP, gains: S-ATK is guaranteed to crit. If current HP is below 30% of Max HP, gains an additional S-ATK.
  - **Ⅳ** at `+T4` — Adversity ResilienceIV (乌恩·莱奥尼尔技能描述)
    (Takes effect at the start of battle) If current HP is below 70% of Max HP, gains an additional 50% S-ATK damage. If current HP is below 50% of Max HP, gains: S-ATK is guaranteed to crit. If current HP is below 30% of Max HP, gains an additional S-ATK. If the HP condition for gaining additional skill effects is met, the additional skill effects will persist in subsequent battles (does not disappear upon death), and current HP does not need to remain below the required HP.

### Augment cost (per step)
- `+1` — 5× Striker Chip · 100,000 money
- `+2` — 10× Striker Chip · 200,000 money
- `+3` — 21× Striker Chip · 300,000 money
- `+4` — 28× Striker Chip · 500,000 money
- `+5` — 35× Striker Chip · 800,000 money
- `+6` — 42× Striker Chip · 10× Pandora Power Core
- `+7` — 49× Striker Chip · 50× Pandora Power Core
- `+8` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Woon Lionel Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Woon Lionel Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Woon Lionel Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Woon Lionel Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Woon Lionel Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Woon Lionel Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 575 · Mond 蒙德
**Role** Striker · **Attack** physical · **Generation** latest
**Ratings** Damage 10/10 · Defence 7/10 · Assist 8/10

### Skill panels
**Slot 1 — Blood Hunt** (id 1787, unlocks at `+0`)
  - **Ⅰ** at `+0` — Blood HuntⅠ (蒙德技能描述)
    Vertical Attack, deals 340% S-ATK damage to target. The S-ATK ignores 35% of the target's DEF and S-DEF. Lastly, recovers 100 Accumulator. At the start of the battle, gains the [Hunt] effect, lasting until the end of the battle. 【Hunt】: If the target's HP falls below 30% after the hero uses S-ATK, the hero will use an additional skill attack.
  - **Ⅱ** at `+7` — Blood HuntⅡ (蒙德技能描述)
    Vertical attack, steals 50% of the target's Accumulator, then deals 360% S-ATK damage to the target. The S-ATK ignores 45% of the target's DEF and S-DEF. Finally, recovers 100 Accumulator. At the start of the battle, gains the [Hunt] effect, lasting until the end of the battle. 【Hunt】: If the target's HP falls below 40% after the hero uses S-ATK, the hero will use an additional skill attack.
  - **Ⅲ** at `+9` — Blood HuntⅢ (蒙德技能描述)
    Vertical Attack, steals 50% of the target's Accumulator (ignores immunity effects), then deals 380% S-ATK damage to the target. The S-ATK ignores 55% of the target's DEF and S-DEF. Finally, recovers 100 Accumulator. At the start of the battle, gains the [Hunt] effect, lasting until the end of the battle. 【Hunt】: If the target's HP falls below 50% after the hero uses S-ATK, the hero will use an additional skill attack.
  - **Ⅳ** at `+15` — Blood HuntIV (蒙德技能描述)
    Vertical attack, steals 60% of the target's Accumulator (ignores immunity effects), then deals 410% S-ATK damage to the target hit. The S-ATK ignores 75% of the target's DEF and S-DEF.Has a 50% chance to instantly kill 2 random enemies. Lastly, recovers 100 Accumulator. At the start of the battle, gains the 【Hunt】 effect, lasting until the end of the battle. 【Hunt】: If the target's HP falls below 60% after the hero uses S-ATK, the hero will use an additional skill attack.

**Slot 2 — Bloodthirsty Instinct** (id 1788, unlocks at `+3`)
  - **Ⅰ** at `+3` — Bloodthirsty InstinctⅠ (蒙德技能描述)
    (Takes effect at the start of battle) When casting a skill, for every 1% of the target's max HP lost, your attack damage against them increases by 3%.
  - **Ⅱ** at `+11` — Bloodthirsty InstinctⅡ (蒙德技能描述)
    (Takes effect at the start of battle) When casting a skill, for every 1% of the target's max HP lost, your attack damage against them increases by 3%. Each time a skill is cast, increases own Crit Rate by 80% (absolute value) and Crit ATK by 60% (absolute value), stacking up to 4 times.
  - **Ⅲ** at `+T3` — Bloodthirsty InstinctⅢ (蒙德技能描述)
    (Takes effect at the start of battle) When casting a skill, for every 1% of the target's max HP lost, your attack damage against them increases by 3%. Each time a skill is cast, increases own Crit Rate by 80% (absolute value) and Crit ATK by 60% (absolute value), stacking up to 4 times. The instant destruction effect in the skill is enhanced: ignores the target's immunity to instant destruction, and the probability of instant destruction is increased to 60%.
  - **Ⅳ** at `+T4` — Bloodthirsty InstinctIV (蒙德技能描述)
    (Takes effect at the start of battle) When casting a skill, for every 1% of the target's max HP lost, your attack damage against them increases by 3%. Each time a skill is cast, increases own Crit Rate by 80% (absolute value) and Crit ATK by 60% (absolute value), stacking up to 4 times. The instant destruction effect in the skill is enhanced: ignores the target's immunity to instant destruction, and the probability of instant destruction is increased to 60%. If an S-ATK results in a kill, the hero gains Rebirth, reviving immediately upon death with 100% of initial HP and 150 Accumulator (unaffected by forbidding revival and rebirth effects).

**Slot 3 — Heart of the Hunt** (id 1789, unlocks at `+5`)
  - **Ⅰ** at `+5` — Heart of the HuntⅠ (蒙德技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +60% DEF: +30% S-DEF: +30% DMG Reduction (Absolute Value): +30%
  - **Ⅱ** at `+13` — Heart of the HuntⅡ (蒙德技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +90% DEF: +60% S-DEF: +60% DMG Reduction (Absolute Value): +40%
  - **Ⅲ** at `+T` — Heart of the HuntⅢ (蒙德技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +120% DEF: +90% S-DEF: +90% DMG Reduction (Absolute Value): +50%
  - **Ⅳ** at `+T2` — Heart of the HuntIV (蒙德技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +150% DEF: +120% S-DEF: +120% DMG Reduction (Absolute Value): +60%

### Augment cost (per step)
- `+1` — 5× Striker Chip · 100,000 money
- `+2` — 10× Striker Chip · 200,000 money
- `+3` — 21× Striker Chip · 300,000 money
- `+4` — 28× Striker Chip · 500,000 money
- `+5` — 35× Striker Chip · 800,000 money
- `+6` — 42× Striker Chip · 10× Pandora Power Core
- `+7` — 49× Striker Chip · 50× Pandora Power Core
- `+8` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Mond Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Mond Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Mond Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Mond Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Mond Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Mond Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 583 · Ignis 伊格尼斯
**Role** Striker · **Attack** physical · **Generation** latest
**Ratings** Damage 9/10 · Defence 8/10 · Assist 10/10

### Skill panels
**Slot 1 — Infernal Scorch** (id 1816, unlocks at `+0`)
  - **Ⅰ** at `+0` — Infernal ScorchⅠ (伊格尼斯+0)
    Cross Attack, deals 340% S-ATK damage to targets, with a 50% chance to apply Scorch to all enemies, lasting 99 rounds. Lastly, recovers 100 Accumulator. Scorch: Stacks up to 3 times. Deals True Damage equal to Stacks multiplied by 30% of S-ATK Damage before the target acts. (this damage ignores shields' damage reduction). Scorch stacks are cleared upon revival. (When multiple Scorch effects are applied simultaneously, only the latest recent Scorch will take effect and will be calculated its damage.)
  - **Ⅱ** at `+6` — Infernal ScorchⅡ (伊格尼斯+6)
    Cross Attack, deals 360% S-ATK damage to targets, with a 50% chance to apply Scorch to all enemies, lasting 99 rounds. Recovers 40% of maximum HP, and lastly, recovers 100 Accumulator. Scorch: Stacks up to 3 times. Deals True Damage equal to Stacks multiplied by 40% of S-ATK Damage before the target acts (this damage ignores shields' damage reduction). The healing effect on the target is reduced by 50%. Scorch stacks are cleared upon revival. (When multiple Scorch effects are applied simultaneously, only the latest recent Scorch will take effect and will be calculated its damage.)
  - **Ⅲ** at `+10` — Infernal ScorchⅢ (伊格尼斯+10)
    Cross attack, plunders 40% Accumulator from targets, deals 380% S-ATK damage to targets, with a 50% chance to apply Scorch to all enemies, lasting 99 rounds. Recovers 60% of maximum HP, and lastly, recovers 100 Accumulator. Scorch: Stacks up to 3 times. Deals True Damage equal to Stacks multiplied by 40% of S-ATK Damage before the target acts (this damage ignores shields' damage reduction). Also reduces Accumulator equal to Scorch stacks multiplied by 15. The healing effect on the target is reduced by 75%. Scorch stacks are cleared upon revival. (When multiple Scorch effects are applied simultaneously, only the latest recent Scorch will take effect and will be calculated its damage.)
  - **Ⅳ** at `+15` — Infernal ScorchIV (伊格尼斯+15)
    Cross Attack, plunders 50% Accumulator from targets, deals 400% S-ATK damage to targets, with a 75% chance to apply Scorch to all enemies, lasting 99 rounds. Recovers 80% of maximum HP, removes Freeze and Icebound status from allies, and lastly recovers 100 Accumulator. Scorch: Stacks up to 3 times. Deals True Damage equal to Stacks multiplied by 50% of S-ATK Damage before the target acts (this damage ignores shields' damage reduction). Also reduces Accumulator equal to Scorch stacks multiplied by 20. Targets with Scorch cannot be healed. If the target with Scorch is revived, the Scorch stacks are reduced to 1. (When multiple Scorch effects are applied simultaneously, only the latest recent Scorch will take effect and will be calculated its damage.)

**Slot 2 — Fire Crystal Core** (id 1817, unlocks at `+2`)
  - **Ⅰ** at `+2` — Fire Crystal CoreⅠ (伊格尼斯+2)
    (Takes effect at the start of battle) Ignis's Fire Crystal Core makes it immune to Freeze and Icebound effects (including control effects that ignore immunity and protection; this effect cannot be disabled by skills that prevent other skill effects from taking effect.). At the start of battle, gains Eye of True Sight for 99 rounds.
  - **Ⅱ** at `+9` — Fire Crystal CoreⅡ (伊格尼斯+9)
    (Takes effect at the start of battle) Ignis's Fire Crystal Core makes him immune to Freeze and Icebound effects (including control effects that ignore immunity and protection; this effect cannot be disabled by skills that prevent other skill effects from taking effect). At the start of battle, gains Eye of True Sight for 99 rounds. Upon death, reduces the HP of enemies with Scorch to 1, and dispels Rebirth effects from all enemies.
  - **Ⅲ** at `+13` — Fire Crystal CoreⅢ (伊格尼斯+13)
    (Takes effect at the start of battle) Ignis's Fire Crystal Core makes him immune to Freeze and Icebound effects (including control effects that ignore immunity and protection; this effect cannot be disabled by skills that prevent other skill effects from taking effect). At the start of battle, gains Eye of True Sight for 99 rounds. Upon death, reduces the HP of enemies with Scorch to 1, and dispels Rebirth effects from all enemies. When taking damage, if max HP falls below 40%, there is a 50% chance to gain a Rebirth effect, reviving immediately upon death with 100% HP and 150 Accumulator.
  - **Ⅳ** at `+T3` — Fire Crystal CoreIV (伊格尼斯+19)
    (Takes effect at the start of battle) Ignis's Fire Crystal Core makes it immune to Freeze and Icebound effects (including control effects that ignore immunity and protection; this effect cannot be disabled by skills that prevent other skill effects from taking effect). At the start of battle, applies Scorch to 2 random enemies and gains Eye of True Sight for 99 rounds. Upon death, reduces the HP of enemies with Scorch to 1, and dispels Rebirth effects from all enemies. When taking damage, if HP falls below 50%, there is a 50% chance to gain a Rebirth effect, reviving immediately upon death with 100% HP and 150 Accumulator. (the first Rebirth triggered by this effect in each battle is not affected by effects that forbid revival).

**Slot 3 — Will of Flame** (id 1818, unlocks at `+4`)
  - **Ⅰ** at `+4` — Will of FlameⅠ (伊格尼斯+4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +60% ATK: +60% Crit ATK (Absolute Value): +30% DMG Bonus (Absolute Value): +15%
  - **Ⅱ** at `+12` — Will of FlameⅡ (伊格尼斯+10)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +90% ATK: +90% Crit ATK (Absolute Value): +40% DMG Bonus (Absolute Value): +20%
  - **Ⅲ** at `+15` — Will of FlameⅢ (伊格尼斯+15)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +120% ATK: +120% Crit ATK (Absolute Value): +50% DMG Bonus (Absolute Value): +25%
  - **Ⅳ** at `+T2` — Will of FlameIV (伊格尼斯+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +150% ATK: +150% Crit ATK (Absolute Value): +60% DMG Bonus (Absolute Value): +30%

**Slot 4 — Absolute Scorch** (id 1819, unlocks at `+3`)
  - **Ⅰ** at `+3` — Absolute ScorchⅠ (伊格尼斯+3)
    (Takes effect at the start of battle) S-ATK will instantly kill enemies in a frozen state.
  - **Ⅱ** at `+9` — Absolute ScorchⅡ (伊格尼斯+9)
    (Takes effect at the start of battle) S-ATK will instantly kill enemies in a frozen state. S-ATK will remove Glacial Coating from ships with Scorch.
  - **Ⅲ** at `+T` — Absolute ScorchⅢ (伊格尼斯+16)
    (Takes effect at the start of battle) S-ATK will instantly kill enemies in a frozen state. S-ATK will remove Glacial Coating from ships with Scorch. Ships with Scorch will revive after death, losing 50% of their max HP and resetting their Accumulator.
  - **Ⅳ** at `+T4` — Absolute ScorchIV (伊格尼斯+20)
    (Takes effect at the start of battle) S-ATK will instantly kill enemies in a Frozen state (ignores immunity to lethal and instant destruction effects). S-ATK will remove Glacial Coating and Cryosleep effects from ships with Scorch. Ships with Scorch will revive after death, losing 50% of their max HP and resetting their Accumulator.

### Augment cost (per step)
- `+1` — 5× Striker Chip · 100,000 money
- `+2` — 10× Striker Chip · 200,000 money
- `+3` — 21× Striker Chip · 300,000 money
- `+4` — 28× Striker Chip · 500,000 money
- `+5` — 35× Striker Chip · 800,000 money
- `+6` — 42× Striker Chip · 10× Pandora Power Core
- `+7` — 49× Striker Chip · 50× Pandora Power Core
- `+8` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Ignis's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Ignis's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Ignis's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Ignis's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Ignis's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Ignis's Ship Part · 100× Alien Essence · 100× Transcendence Core

---

## 590 · Chun Hua 春华
**Role** Striker · **Attack** physical · **Generation** latest
**Ratings** Damage 9/10 · Defence 8/10 · Assist 10/10

### Skill panels
**Slot 1 — Petal Dart** (id 1845, unlocks at `+0`)
  - **Ⅰ** at `+0` — Petal DartⅠ (春华+0)
    Cross Attack, deals 280% S-ATK damage to targets, with a 50% chance (probability for each target is calculated independently) to apply Weakness to all enemies, reducing all their attributes by 50% for 2 rounds. Lastly, recovers 100 Accumulator.
  - **Ⅱ** at `+7` — Petal DartⅡ (春华+3)
    Cross Attack, deals 300% S-ATK damage to targets and additional S-ATK damage equal to 10% of their current Accumulator (up to 200 Accumulator). Has a 50% chance to apply Weakness to all enemies (probability for each target is calculated independently), reducing all their Attributes by 50% for 2 rounds. Lastly, recovers 100 Accumulator.
  - **Ⅲ** at `+15` — Petal DartⅢ (春华+7)
    Cross Attack, deals 320% S-ATK damage to targets and additional damage equal to 10% of their current Accumulator (up to 250 Accumulator). Has a 50% chance to apply Weakness to all enemies (probability calculated independently for each unit), reducing all their Attributes by 50% for 2 rounds. S-ATK will instantly kill any enemies with less than 40% HP. Lastly, recovers 100 Accumulator.
  - **Ⅳ** at `+T3` — Petal DartIV (春华+9)
    Cross Attack, first absorbs 60% of the target's ATK and S-ATK for 2 rounds. Deals 360% S-ATK damage to targets and additional S-ATK damage equal to 10% of their current Accumulator (up to 300 Accumulator). Has a 50% chance to apply Weakness to all enemies (probability calculated individually for each unit), reducing their Attributes by 50% for 2 rounds. S-ATK will instantly kill any enemies with less than 40% HP (ignores immunity to lethal and instant destruction effects). Finally, recovers 100 Accumulator.

**Slot 2 — Ensemble** (id 1846, unlocks at `+3`)
  - **Ⅰ** at `+3` — EnsembleⅠ (春华+3)
    (Takes effect at the start of battle) At the start of battle and when casting a skill, marks the ally with the highest ATK (excluding self) as the Assist Unit for 2 rounds (re-marks after each skill cast). After the Assist Unit casts its next skill, if the hero is not in a state of inability to act, he immediately takes an action.
  - **Ⅱ** at `+9` — EnsembleⅡ (春华+9)
    (Takes effect at the start of battle) At the start of battle and when casting a skill, marks the ally with the highest ATK (excluding self) as the Assist unit for 2 rounds (re-marked after each skill cast). After the Assist Unit casts its next skill, if the hero is not in a state of inability to act, he immediately takes an action. When casting a skill, there is a 50% chance to grant Rebirth to self and the assist unit. Upon death, revive immediately with 100% of initial HP and 150 Accumulator.
  - **Ⅲ** at `+T1` — EnsembleⅢ (春华+17)
    (Takes effect at the start of battle) At the start of battle and when casting a skill, marks the ally with the highest ATK (excluding self) as the Assist unit for 2 rounds (re-marked after each skill cast). After the Assist Unit casts its next skill, if the hero is not in a state of inability to act, he immediately takes an action. When casting a skill, there is a 50% chance to grant Rebirth to self and the assist unit. Upon death, revive immediately with 100% of initial HP and 150 Accumulator. If self and the Assist Unit target enemies with more than 50% of Max HP, the skill damage is increased by 60%.
  - **Ⅳ** at `+T4` — EnsembleIV (春华+20)
    (Takes effect at the start of battle) At the start of battle and when casting a skill, marks the ally with the highest ATK (excluding self) as the Assist unit for 2 rounds (re-marked after each skill cast). After the Assist Unit casts its next skill, if the hero is not in a state of inability to act, he immediately takes an action. When casting a skill, there is a 50% chance to grant Rebirth to self and the assist unit. Upon death, revive immediately with 100% of initial HP and 150 Accumulator (unaffected by forbidding revival and forbidden rebirth effects). If self and the Assist Unit target enemies with more than 50% of Max HP, the skill damage is increased by 80%. When any ally dies, all other allies' damage is increased by 100% (does not stack). Additionally, self immediately takes an action (this effect can trigger once for each ally. The trigger count resets each time self revives or Rebirths. If multiple allies die simultaneously, the immediate action only triggers once).

**Slot 3 — Lightness** (id 1847, unlocks at `+5`)
  - **Ⅰ** at `+5` — LightnessⅠ (春华+5)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +60% DEF: +30% S-DEF: +30% DMG Reduction (Absolute Value): +30%
  - **Ⅱ** at `+11` — LightnessⅡ (春华+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +90% DEF: +60% S-DEF: +60% DMG Reduction (Absolute Value): +40%
  - **Ⅲ** at `+T` — LightnessⅢ (春华+16)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +120% DEF: +90% S-DEF: +90% DMG Reduction (Absolute Value): +50%
  - **Ⅳ** at `+T2` — LightnessIV (春华+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +150% DEF: +120% S-DEF: +120% DMG Reduction (Absolute Value): +60%

### Augment cost (per step)
- `+1` — 5× Striker Chip · 100,000 money
- `+2` — 10× Striker Chip · 200,000 money
- `+3` — 21× Striker Chip · 300,000 money
- `+4` — 28× Striker Chip · 500,000 money
- `+5` — 35× Striker Chip · 800,000 money
- `+6` — 42× Striker Chip · 10× Pandora Power Core
- `+7` — 49× Striker Chip · 50× Pandora Power Core
- `+8` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Chun Hua's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Chun Hua's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Chun Hua's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Chun Hua's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Chun Hua's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Chun Hua's Ship Part · 100× Alien Essence · 100× Transcendence Core

---

## 597 · Eric Valk 艾瑞克·瓦尔克
**Role** Striker · **Attack** physical · **Generation** latest
**Ratings** Damage 10/10 · Defence 7/10 · Assist 8/10

### Skill panels
**Slot 1 — A20 Electromagnetic Penetration** (id 1864, unlocks at `+0`)
  - **Ⅰ** at `+0` — A20 Electromagnetic PenetrationⅠ (艾瑞克·瓦尔克+0)
    Vertical Attack, first plunders 30% of the target's Accumulator, then deals 350% S-ATK damage to the target. Lastly, recovers 100 Accumulator.
  - **Ⅱ** at `+6` — A20 Electromagnetic PenetrationⅡ (艾瑞克·瓦尔克+2（被动组合）)
    Vertical Attack, first plunders 50% of the target's Accumulator, then deals 400% S-ATK damage to the target. Gains Eye of True Sight for 2 rounds. Lastly, recovers 100 Accumulator.
  - **Ⅲ** at `+10` — A20 Electromagnetic PenetrationⅢ (艾瑞克·瓦尔克+6)
    Vertical Attack, first plunders 50% of the target's Accumulator, then deals 450% S-ATK damage to the target. Increases own ATK and S-ATK by 60% for 2 rounds. Gains Eye of True Sight for 2 rounds. Lastly, recovers 100 Accumulator.
  - **Ⅳ** at `+15` — A20 Electromagnetic PenetrationIV (艾瑞克·瓦尔克+9（被动组合）)
    Vertical Attack, first plunders 70% of the target's Accumulator, then deals 500% S-ATK damage to the target. Increases own ATK and S-ATK by 80% for 2 rounds. Gains Eye of True Sight for 2 rounds. Gains [Supercharged Accumulator] for 2 rounds. Lastly, recovers 200 Accumulator. <Supercharged Accumulator>: Each time damage taken, recovers an additional 75 Accumulator. When any allies (except self) uses a skill during battle, gains additional Accumulator equal to 20% of the Accumulator consumed. The maximum Accumulator gained through this effect per round is 200.

**Slot 2 — Precision Orbit Lock** (id 1865, unlocks at `+2`)
  - **Ⅰ** at `+2` — Precision Orbit LockⅠ (艾瑞克·瓦尔克+2)
    (Takes effect at the start of battle) When Eric Valk using a skill, additional effects are applied based on the current Accumulator. (Effects from each stage can be triggered cumulatively) Accumulator above 200: Increases own Penetration by 50% (absolute value) and Hit Rate by 50% (absolute value) for 2 rounds. Accumulator above 300: S-ATK is guaranteed to critically hit.
  - **Ⅱ** at `+9` — Precision Orbit LockⅡ (艾瑞克·瓦尔克+9)
    (Takes effect at the start of battle) When Eric Valk using a skill, additional effects are applied based on the current Accumulator. (Effects from each stage can be triggered cumulatively) Accumulator above 200: Increases own Penetration by 80%(absolute value) and Hit Rate by 80% (absolute value) for 2 rounds. Accumulator above 300: S-ATK is guaranteed to critically hit. Accumulator above 400: S-ATK ignores Stasis and immunity to lethal attacks.
  - **Ⅲ** at `+T` — Precision Orbit LockⅢ (艾瑞克·瓦尔克+16)
    (Takes effect at the start of battle) When Eric Valk using a skill, additional effects are applied based on the current Accumulator. (Effects from each stage can be triggered cumulatively) Accumulator above 200: Increases own Penetration by 100%(absolute value) and Hit Rate by 100% (absolute value) for 2 rounds. Accumulator above 300: S-ATK is guaranteed to critically hit.and increases own Crit ATK by 200% (absolute value) for 2 rounds. Accumulator above 400: S-ATK ignores Stasis and immunity to lethal attacks. And for each Accumulator point above 100 spent, the damage increases by an additional 0.2%.
  - **Ⅳ** at `+T3` — Precision Orbit LockIV (艾瑞克·瓦尔克+19)
    (Takes effect at the start of battle) When Eric Valk using a skill, additional effects are applied based on the current Accumulator. (Effects from each stage can be triggered cumulatively) Accumulator above 200: Increases own Penetration by 150%(absolute value) and Hit Rate by 150% (absolute value) for 2 rounds. Accumulator above 300: S-ATK is guaranteed to critically hit.and increases own Crit ATK by 200% (absolute value) for 2 rounds. Accumulator above 400: S-ATK ignores Stasis and immunity to lethal attacks. And for each Accumulator point above 100 spent, the damage increases by an additional 0.3%. S-ATK can target units in Dark Conceal. If the S-ATK hits only one enemy, it applies an additional effect: instantly destroys the targeted enemy. (Ignores immunity to lethal damage and instant destruction)

**Slot 3 — Will to Win** (id 1866, unlocks at `+4`)
  - **Ⅰ** at `+4` — Will to WinⅠ (艾瑞克·瓦尔克+4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +60% ATK: +60% Crit ATK (Absolute Value): +30% DMG Bonus (Absolute Value): +15%
  - **Ⅱ** at `+10` — Will to WinⅡ (艾瑞克·瓦尔克+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +90% ATK: +90% Crit ATK (Absolute Value): +40% DMG Bonus (Absolute Value): +20%
  - **Ⅲ** at `+14` — Will to WinⅢ (艾瑞克·瓦尔克+14)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +120% ATK: +120% Crit ATK (Absolute Value): +50% DMG Bonus (Absolute Value): +25%
  - **Ⅳ** at `+T2` — Will to WinIV (艾瑞克·瓦尔克+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +150% ATK: +150% Crit ATK (Absolute Value): +60% DMG Bonus (Absolute Value): +30%

**Slot 4 — Turn the Tide** (id 1867, unlocks at `+3`)
  - **Ⅰ** at `+3` — Turn the TideⅠ (艾瑞克·瓦尔克+3)
    (Takes effect at the start of battle) Eric Valk is immune to Accumulator Reduction effects.
  - **Ⅱ** at `+13` — Turn the TideⅡ (艾瑞克·瓦尔克+13)
    (Takes effect at the start of battle) Eric Valk is immune to Accumulator Reduction effects. When Eric Valk receives lethal damage or instant destruction effect, he immediately releases [Electromagnetic Surge]: A powerful electromagnetic pulse is instantly released, dealing devastating damage to the enemy before being destroyed. (Can take effect once per battle, can still release this skill while under control or with insufficient Accumulator) [Electromagnetic Surge]: Attacks all enemies, dealing 200% S-ATK damage to targets.
  - **Ⅲ** at `+T1` — Turn the TideⅢ (艾瑞克·瓦尔克+17)
    (Takes effect at the start of battle) Eric Valk is immune to Accumulator Reduction effects. At the start of battle, gains [Supercharged Accumulator] for 2 rounds. When receiving lethal damage or instant destruction effect, he immediately releases [Electromagnetic Surge]: A powerful electromagnetic pulse is instantly released, dealing devastating damage to the enemy before being destroyed. (Can take effect once per battle, can still release this skill while under control or with insufficient Accumulator) [Electromagnetic Surge]: Attacks all enemies, dealing 200% S-ATK damage to targets.
  - **Ⅳ** at `+T4` — Turn the TideIV (艾瑞克·瓦尔克+20)
    (Takes effect at the start of battle) Eric Valk is immune to Accumulator Reduction effects. At the start of battle, gains [Supercharged Accumulator] for 2 rounds. When receiving lethal damage or instant destruction effect, he immediately releases [Electromagnetic Surge]: A powerful electromagnetic pulse is instantly released, dealing devastating damage to the enemy before being destroyed. (Can take effect once per battle, can still release this skill while under control or with insufficient Accumulator) [Electromagnetic Surge]: Attacks all enemies, dealing 300% S-ATK damage to targets.This skill applies the effect of [Precision Orbit Lock] and triggers additional benefits without considering the current Accumulator value. Targets hit by [Electromagnetic Surge] have a 50% chance be locked for 2 rounds. (ignore immunity and protection effects)

### Augment cost (per step)
- `+1` — 5× Striker Chip · 100,000 money
- `+2` — 10× Striker Chip · 200,000 money
- `+3` — 21× Striker Chip · 300,000 money
- `+4` — 28× Striker Chip · 500,000 money
- `+5` — 35× Striker Chip · 800,000 money
- `+6` — 42× Striker Chip · 10× Pandora Power Core
- `+7` — 49× Striker Chip · 50× Pandora Power Core
- `+8` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Eric Valk's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Eric Valk's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Eric Valk's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Eric Valk's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Eric Valk's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Eric Valk's Ship Part · 100× Alien Essence · 100× Transcendence Core

---

## 603 · Karl Drakk 卡尔·德拉克
**Role** Striker · **Attack** physical · **Generation** latest
**Ratings** Damage 9/10 · Defence 8/10 · Assist 10/10

### Skill panels
**Slot 1 — Flame Roar** (id 1886, unlocks at `+0`)
  - **Ⅰ** at `+0` — Flame RoarⅠ (卡尔·德拉克+0)
    Cross Attack, plunders 50% S-DEF and 50% Accumulator from targets, then deals 300% S-ATK damage to targets. Lastly, recovers 100 Accumulator.
  - **Ⅱ** at `+7` — Flame RoarⅡ (卡尔·德拉克+3(被动))
    Cross Attack, plunders 50% S-DEF and 50% Accumulator from targets, then deals 320% S-ATK damage to targets. Increases all allies' S-ATK by 100%, Penetration by 75%, and Critical by 150% (absolute value) for 2 rounds. Lastly, recovers 100 Accumulator.
  - **Ⅲ** at `+15` — Flame RoarⅢ (卡尔·德拉克+7)
    Cross Attack, plunders 50% S-DEF and 50% Accumulator from targets, then deals 340% S-ATK damage to targets. Increases all allies' S-ATK by 150%, Penetration by 100%, and Critical by 200% (absolute value) for 2 rounds. If current HP is above 50% of max HP, consumes 50% of current HP when releasing the skill, instantly killing a random enemy. Lastly, recovers 100 Accumulator.
  - **Ⅳ** at `+T3` — Flame RoarIV (卡尔·德拉克+9(被动))
    Cross Attack, plunders 75% S-DEF and 75% Accumulator from targets, then deals 360% S-ATK damage to targets. Gains Eye of True Sight lasting until the end of the battle. Increases all allies' S-ATK by 150%, Penetration by 100%, and Critical by 200% (absolute value) for 2 rounds. If current HP is above 50% of max HP, consumes 30% of current HP when releasing the skill, instantly killing a random enemy. Lastly, recovers 100 Accumulator.

**Slot 2 — Annihilation Heavy Cannon** (id 1887, unlocks at `+3`)
  - **Ⅰ** at `+3` — Annihilation Heavy CannonⅠ (卡尔·德拉克+3)
    (Takes effect at the start of battle) Karl wields the ultimate weapon—Annihilation Heavy Cannon. However, to unleash its unparalleled power, he needs to gather scattered energy on the battlefield to awaken the absolute force hidden within the flames: At the start of battle and when using skills, CHARGE for the Annihilation Heavy Cannon. In this state, for every 1 point of Accumulator reduced by any units in any effect, the base S-ATK damage increases by 0.8%. Each time a skill is used, S-ATK damage increases by 300% (damage cap at 600%). When it is Karl turn to act, if the accumulated S-ATK damage reaches 600%, first recover 30% of maximum HP and 100 Accumulator, then launch the Annihilation Heavy Cannon vertical S-ATK, dealing the accumulated S-ATK damage to hit units and applying all skill effects of Flame Roar. After this skill is released, immediately perform one Flame Roar skill attack. (After releasing this skill, the accumulated S-ATK damage needs to be recalculated)
  - **Ⅱ** at `+9` — Annihilation Heavy CannonⅡ (卡尔·德拉克+9)
    (Takes effect at the start of battle) Karl wields the ultimate weapon—Annihilation Heavy Cannon. However, to unleash its unparalleled power, he needs to gather scattered energy on the battlefield to awaken the absolute force hidden within the flames: At the start of battle and when using skills, CHARGE for the Annihilation Heavy Cannon. In this state, for every 1 point of Accumulator reduced by any units in any effect, the base S-ATK damage increases by 1.0%. Each time a skill is used, S-ATK damage increases by 500% (damage cap at 1000%). When it is Karl turn to act, if the accumulated S-ATK damage reaches 1000%, first recover 30% of maximum HP and 100 Accumulator, then launch the Annihilation Heavy Cannon vertical S-ATK, dealing the accumulated S-ATK damage to hit units and applying all skill effects of Flame Roar. After this skill is released, immediately perform one Flame Roar skill attack. (After releasing this skill, the accumulated S-ATK damage needs to be recalculated) Karl S-ATK can ignore the effects of Stasis and immunity to lethal shield effect.
  - **Ⅲ** at `+T1` — Annihilation Heavy CannonⅢ (卡尔·德拉克+17)
    (Takes effect at the start of battle) Karl wields the ultimate weapon—Annihilation Heavy Cannon. However, to unleash its unparalleled power, he needs to gather scattered energy on the battlefield to awaken the absolute force hidden within the flames: At the start of battle and when using skills, CHARGE for the Annihilation Heavy Cannon. In this state, for every 1 point of Accumulator reduced by any units in any effect, the base S-ATK damage increases by 1.2%. Each time a skill is used, S-ATK damage increases by 750% (damage cap at 1500%). When it is Karl turn to act, if the accumulated S-ATK damage reaches 1500%, first recover 30% of maximum HP and 150 Accumulator, then launch the Annihilation Heavy Cannon vertical S-ATK, dealing the accumulated S-ATK damage to hit units and applying all skill effects of Flame Roar. After this skill is released, immediately perform one Flame Roar skill attack. (After releasing this skill, the accumulated S-ATK damage needs to be recalculated) Karl S-ATK can ignore the effects of Stasis and immunity to lethal shield effect. Killing an enemy with an S-ATK, Karl gains Rebirth, reviving immediately upon death with 100% of initial HP and 150 Accumulator (unaffected by forbidding revival and rebirth effects).
  - **Ⅳ** at `+T4` — Annihilation Heavy CannonIV (卡尔·德拉克+20)
    (Takes effect at the start of battle) Karl wields the ultimate weapon—Annihilation Heavy Cannon. However, to unleash its unparalleled power, he needs to gather scattered energy on the battlefield to awaken the absolute force hidden within the flames: At the start of battle and when using skills, CHARGE for the Annihilation Heavy Cannon. In this state, for every 1 point of Accumulator reduced by any units in any effect, the base S-ATK damage increases by 1.5%. Each time a skill is used, S-ATK damage increases by 1000% (damage cap at 2000%). When it is Karl turn to act, if the accumulated S-ATK damage reaches 2000%, first recover 50% of maximum HP and 200 Accumulator, then launch the Annihilation Heavy Cannon vertical S-ATK, dealing the accumulated S-ATK damage to hit units and applying all skill effects of Flame Roar. After this skill is released, immediately perform one Flame Roar skill attack. (After releasing this skill, the accumulated S-ATK damage needs to be recalculated) Karl S-ATK can ignore the effects of Stasis and immunity to lethal shield effect. If this skill kills an enemy, it deals True Damage to all enemies equal to 50% of the excess damage. Killing an enemy with an S-ATK, Karl gains Rebirth, reviving immediately upon death with 100% of initial HP and 150 Accumulator (unaffected by forbidding revival and rebirth effects). The instant destruction effect in the skill is enhanced: ignores the target's immunity to instant destruction.

**Slot 3 — Iron Will** (id 1888, unlocks at `+5`)
  - **Ⅰ** at `+5` — Iron WillⅠ (卡尔·德拉克+5)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +60% DEF: +30% S-DEF: +30% DMG Reduction (Absolute Value): +30%
  - **Ⅱ** at `+11` — Iron WillⅡ (卡尔·德拉克+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +90% DEF: +60% S-DEF: +60% DMG Reduction (Absolute Value): +40%
  - **Ⅲ** at `+T` — Iron WillⅢ (卡尔·德拉克+16)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +120% DEF: +90% S-DEF: +90% DMG Reduction (Absolute Value): +50%
  - **Ⅳ** at `+T2` — Iron WillIV (卡尔·德拉克+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +150% DEF: +120% S-DEF: +120% DMG Reduction (Absolute Value): +60%

### Augment cost (per step)
- `+1` — 5× Striker Chip · 100,000 money
- `+2` — 10× Striker Chip · 200,000 money
- `+3` — 21× Striker Chip · 300,000 money
- `+4` — 28× Striker Chip · 500,000 money
- `+5` — 35× Striker Chip · 800,000 money
- `+6` — 42× Striker Chip · 10× Pandora Power Core
- `+7` — 49× Striker Chip · 50× Pandora Power Core
- `+8` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Karl Drakk Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Karl Drakk Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Karl Drakk Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Karl Drakk Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Karl Drakk Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Karl Drakk Ship Part · 100× Alien Essence · 100× Transcendence Core

---

## 613 · Mu 穆
**Role** Striker · **Attack** physical · **Generation** latest
**Ratings** Damage 10/10 · Defence 6/10 · Assist 9/10

### Skill panels
**Slot 1 — OR-DX Heavy Cannon Crush Formation** (id 1921, unlocks at `+0`)
  - **Ⅰ** at `+0` — OR-DX Heavy Cannon Crush FormationⅠ (穆+0)
    Vertical Attack, deals 340% S-ATK damage to the target, then triggers [Pursuit]. Lastly, recovers 200 Accumulator. [Pursuit]: Each pursuit deals 260% S-ATK damage to a random enemy within the vertical range. Starts with 3 pursuits. For every 50 Accumulator consumed when casting the skill, gains 1 additional pursuit, up to a maximum of 5 additional pursuits.
  - **Ⅱ** at `+6` — OR-DX Heavy Cannon Crush FormationⅡ (穆+2)
    Vertical Attack, first removes buffs from targets, deals 360% S-ATK damage to the target, then triggers [Pursuit]. Lastly, recovers 200 Accumulator. [Pursuit]: Each pursuit deals 260% S-ATK damage to a random enemy within the vertical range. Starts with 3 pursuits. For every 50 Accumulator consumed when casting the skill, gains 1 additional pursuit, up to a maximum of 6 additional pursuits.
  - **Ⅲ** at `+10` — OR-DX Heavy Cannon Crush FormationⅢ (穆+6)
    Vertical Attack, first removes buffs from targets, reduces the target's S-DEF and DEF by 75% for 2 rounds, deals 380% S-ATK damage to the target, then triggers [Pursuit]. Lastly, recovers 200 Accumulator. [Pursuit]: Each pursuit deals 280% S-ATK damage to a random enemy within the vertical range. Starts with 3 pursuits. For every 50 Accumulator consumed when casting the skill, gains 1 additional pursuit, up to a maximum of 8 additional pursuits.
  - **Ⅳ** at `+15` — OR-DX Heavy Cannon Crush FormationIV (穆+9)
    Vertical Attack, first removes buffs from targets, reduces the target's S-DEF and DEF by 75% for 2 rounds, deals 400% S-ATK damage to the target, then triggers [Pursuit]. Increases Crit Rate of all allies by 150% (absolute value) for 2 rounds. Each time the skill is used, increases Crit ATK by 50%, stacking up to 10 times, lasting until the end of the battle. Lastly, recovers 200 Accumulator. [Pursuit]: Each pursuit deals 300% S-ATK damage to a random enemy within the vertical range. Starts with 3 pursuits. For every 50 Accumulator consumed when casting the skill, gains 1 additional pursuit, up to a maximum of 10 additional pursuits.

**Slot 2 — Desperate Charge** (id 1922, unlocks at `+2`)
  - **Ⅰ** at `+2` — Desperate ChargeⅠ (穆+2)
    (Takes effect at the start of battle) When using a skill, gains Eye of True Sight for 99 rounds.
  - **Ⅱ** at `+9` — Desperate ChargeⅡ (穆+9)
    (Takes effect at the start of battle) When using a skill, gains Eye of True Sight for 99 rounds. When dealing S-ATK damage, for every 1% of the target's max HP lost, damage dealt to them is increased by 2%.
  - **Ⅲ** at `+T` — Desperate ChargeⅢ (穆+16)
    (Takes effect at the start of battle) When using a skill, gains Eye of True Sight for 99 rounds. When dealing S-ATK damage, for every 1% of the target's max HP lost, damage dealt to them is increased by 3%. Each time Mu uses an S-ATK, the next skill used will additionally restore 20 Accumulator. (Stacks up to 5 times; stacks persists through death if revived.)
  - **Ⅳ** at `+T3` — Desperate ChargeIV (穆+19)
    (Takes effect at the start of battle) When using a skill, gains Eye of True Sight for 99 rounds, and S-ATK can target enemies in Dark Conceal. When dealing S-ATK damage, for every 1% of the target's max HP lost, damage dealt to them is increased by 3%. Each time Mu uses an S-ATK, the next skill used will additionally restore 20 Accumulator. (Stacks up to 10 times; stacks persists through death if revived.)

**Slot 3 — Falcon** (id 1923, unlocks at `+4`)
  - **Ⅰ** at `+4` — FalconⅠ (穆+4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +60% ATK: +60% Crit ATK (Absolute Value): +30% DMG Bonus (Absolute Value): +15%
  - **Ⅱ** at `+10` — FalconⅡ (穆+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +90% ATK: +90% Crit ATK (Absolute Value): +40% DMG Bonus (Absolute Value): +20%
  - **Ⅲ** at `+14` — FalconⅢ (穆+14)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +120% ATK: +120% Crit ATK (Absolute Value): +50% DMG Bonus (Absolute Value): +25%
  - **Ⅳ** at `+T2` — FalconIV (穆+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +150% ATK: +150% Crit ATK (Absolute Value): +60% DMG Bonus (Absolute Value): +30%

**Slot 4 — Supernova・Collapse Charge** (id 1924, unlocks at `+3`)
  - **Ⅰ** at `+3` — Supernova・Collapse ChargeⅠ (穆+3)
    (Takes effect at the start of battle) At the start of battle, gain an additional 300 Accumulator.
  - **Ⅱ** at `+13` — Supernova・Collapse ChargeⅡ (穆+13)
    (Takes effect at the start of battle) At the start of battle, gain an additional 300 Accumulator. All allies' damage dealt is increased by 120% until the end of the battle.
  - **Ⅲ** at `+T1` — Supernova・Collapse ChargeⅢ (穆+17)
    (Takes effect at the start of battle) At the start of battle, gain an additional 300 Accumulator. All allies' damage dealt is increased by 120% until the end of the battle. The skill's damage increases by 0.3% for each Accumulator above 100 spent during skill cast.
  - **Ⅳ** at `+T4` — Supernova・Collapse ChargeIV (穆+20)
    (Takes effect at the start of battle) At the start of battle, gain an additional 300 Accumulator. All allies' damage dealt is increased by 120% until the end of the battle. The skill's damage increases by 0.3% for each Accumulator above 100 spent during skill cast. If the S-ATK doesn't kill an enemy, immediately launch 1 extra S-ATK.(Effects of the same type do not stack) If there are other members of the Supernova Blades Fleet (Aiolia, Ouros, Karon, Teda) in the team, each time they cast a skill, Mu recovers 50 Accumulator. If it is Ulysses, Mu recovers 200 Accumulator instead, and all enemies take 30% more damage for 2 turns.

### Augment cost (per step)
- `+1` — 5× Striker Chip · 100,000 money
- `+2` — 10× Striker Chip · 200,000 money
- `+3` — 21× Striker Chip · 300,000 money
- `+4` — 28× Striker Chip · 500,000 money
- `+5` — 35× Striker Chip · 800,000 money
- `+6` — 42× Striker Chip · 10× Pandora Power Core
- `+7` — 49× Striker Chip · 50× Pandora Power Core
- `+8` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Elenia Exclusive Chip · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Elenia Exclusive Chip · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Elenia Exclusive Chip · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Elenia Exclusive Chip · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Elenia Exclusive Chip · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Elenia Exclusive Chip · 100× Alien Essence · 100× Transcendence Core

---

## 617 · Liser 利瑟
**Role** Striker · **Attack** physical · **Generation** latest
**Ratings** Damage 10/10 · Defence 7/10 · Assist 9/10

### Skill panels
**Slot 1 — Oblivion Brand** (id 1937, unlocks at `+0`)
  - **Ⅰ** at `+0` — Oblivion BrandⅠ (利瑟+0)
    Cross Attack, deals 280% S-ATK damage to target. Applies [Frenzy] on target hit for 99 rounds. Lastly, recovers 100 Accumulator. [Frenzy]: When the affected enemy use a skill, it will lose 40% of current HP and have a 40% chance to become Confused for 2 rounds.
  - **Ⅱ** at `+6` — Oblivion BrandⅡ (利瑟+3)
    Cross Attack, first removes buffs from the target, then deals 300% S-ATK damage to target. Applies [Frenzy] on target hit for 99 rounds. Lastly, recovers 100 Accumulator. [Frenzy]: When the affected enemy use a skill, it will lose 40% of current HP and have a 40% chance to become Confused for 2 rounds.
  - **Ⅲ** at `+10` — Oblivion BrandⅢ (利瑟+6)
    Cross Attack, first removes buffs from the target, then deals 320% S-ATK damage to target. Increases own Damage by 120% and Crit ATK by 200% for 2 rounds. Applies [Frenzy] on target hit for 99 rounds. Lastly, recovers 100 Accumulator. [Frenzy]: When the affected enemy use a skill, it will lose 40% of current HP and have a 40% chance to become Confused for 2 rounds.
  - **Ⅳ** at `+15` — Oblivion BrandIV (利瑟+10)
    Cross Attack, first removes buffs from the target, then deals 340% S-ATK damage to target. Increases all allies' ATK and S-ATK by 75% for 2 rounds. Increases own Damage by 120% and Crit ATK by 200% for 2 rounds. Applies [Frenzy] on target hit for 99 rounds. Lastly, recovers 100 Accumulator. [Frenzy]: When the affected enemy use a skill, it will lose 60% of current HP and have a 40% chance to become Confused for 2 rounds.Each time the affected enemy casts a skill, the chance of Confusion from this effect increases by 20%, up to a maximum of 100%.

**Slot 2 — Heart Devour** (id 1938, unlocks at `+2`)
  - **Ⅰ** at `+2` — Heart DevourⅠ (利瑟+2)
    (Takes effect at the start of battle) At the start of battle and each time resurrect rebirthed, if the damage taken exceeds 30% of your max HP, the excess is negated. Lasts for 2 rounds or is removed after casting a skill.
  - **Ⅱ** at `+9` — Heart DevourⅡ (利瑟+9)
    (Takes effect at the start of battle) At the start of battle and each time resurrect rebirthed, if the damage taken exceeds 20% of your max HP, the excess is negated. Lasts for 2 rounds or is removed after casting a skill. After death, when the ally with the highest S-ATK casts a skill, he/she will gain all skill effects provided by [Oblivion Brand] for 2 rounds.
  - **Ⅲ** at `+T` — Heart DevourⅢ (利瑟+16)
    (Takes effect at the start of battle) At the start of battle and each time resurrect rebirthed, if the damage taken exceeds 10% of your max HP, the excess is negated. Lasts for 2 rounds or is removed after casting a skill. After death, when the ally with the highest S-ATK casts a skill, he/she will gain all skill effects provided by [Oblivion Brand] for 2 rounds. Ally with the [Oblivion Brand] skill effect deal 80% increased damage until the end of battle.
  - **Ⅳ** at `+T3` — Heart DevourIV (利瑟+19)
    (Takes effect at the start of battle) At the start of battle and each time resurrect rebirthed, if the damage taken exceeds 5% of your max HP, the excess is negated. Lasts until removed after casting a skill. After death, when the ally with the highest S-ATK casts a skill, he/she will gain all skill effects provided by [Oblivion Brand] for 2 rounds. Ally with the [Oblivion Brand] skill effect deal 120% increased damage until the end of battle, and immediately take an extra action upon gaining this effect.

**Slot 3 — Collapse** (id 1939, unlocks at `+4`)
  - **Ⅰ** at `+4` — CollapseⅠ (利瑟+4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +60% ATK: +60% Crit ATK (Absolute Value): +30% DMG Bonus (Absolute Value): +15%
  - **Ⅱ** at `+10` — CollapseⅡ (利瑟+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +90% ATK: +90% Crit ATK (Absolute Value): +40% DMG Bonus (Absolute Value): +20%
  - **Ⅲ** at `+14` — CollapseⅢ (利瑟+14)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +120% ATK: +120% Crit ATK (Absolute Value): +50% DMG Bonus (Absolute Value): +25%
  - **Ⅳ** at `+T2` — CollapseIV (利瑟+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +150% ATK: +150% Crit ATK (Absolute Value): +60% DMG Bonus (Absolute Value): +30%

**Slot 4 — Dreamscape** (id 1940, unlocks at `+3`)
  - **Ⅰ** at `+3` — DreamscapeⅠ (利瑟+3)
    (Takes effect at the start of battle) When using a skill, gains Eye of True Sight for 99 rounds.
  - **Ⅱ** at `+13` — DreamscapeⅡ (利瑟+13)
    (Takes effect at the start of battle) When using a skill, gains Eye of True Sight for 99 rounds. After S-ATK is completed, deals True Damage equal to 300% of the first stage skill attack damage to the enemy ship with the lowest HP.
  - **Ⅲ** at `+T1` — DreamscapeⅢ (利瑟+17)
    (Takes effect at the start of battle) When using a skill, gains Eye of True Sight for 99 rounds. After S-ATK is completed, deals True Damage equal to 300% of the first stage skill attack damage to the enemy ship with the lowest HP. If the S-ATK hits only one enemy, applies an additional effect: after this enemy dies, it cannot be revivals or rebirths(including revivals and rebirths unaffected by revival prohibition), lasting until the end of battle.
  - **Ⅳ** at `+T4` — DreamscapeIV (利瑟+20)
    (Takes effect at the start of battle) When using a skill, gains Eye of True Sight for 99 rounds. After S-ATK is completed, deals True Damage equal to 300% of the first stage skill attack damage to the enemy ship with the lowest HP. If the S-ATK hits only one enemy, applies an additional effect: after this enemy dies, it cannot be revivals or rebirths(including revivals and rebirths unaffected by revival prohibition), lasting until the end of battle. When an enemy with [Frenzy] casts a skill, there is a 50% chance that [Pursuit] and [hit targets XXX times consecutively] effects will not activate.

### Augment cost (per step)
- `+1` — 5× Striker Chip · 100,000 money
- `+2` — 10× Striker Chip · 200,000 money
- `+3` — 21× Striker Chip · 300,000 money
- `+4` — 28× Striker Chip · 500,000 money
- `+5` — 35× Striker Chip · 800,000 money
- `+6` — 42× Striker Chip · 10× Pandora Power Core
- `+7` — 49× Striker Chip · 50× Pandora Power Core
- `+8` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Elenia Exclusive Chip · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Elenia Exclusive Chip · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Elenia Exclusive Chip · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Elenia Exclusive Chip · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Elenia Exclusive Chip · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Elenia Exclusive Chip · 100× Alien Essence · 100× Transcendence Core

---

## 620 · Welly 维利
**Role** Striker · **Attack** physical · **Generation** old
**Ratings** Damage 10/10 · Defence 7/10 · Assist 8/10

### Signature skill
- **Ⅰ** at `+0` — Tactical Strike (维利)
  Cross Attack, deals 200% S-ATK damage to targets. Lastly, you recover 100 Accumulator.

### Augment cost (per step)
- `+1` — 5× Striker Chip · 100,000 money
- `+2` — 10× Striker Chip · 200,000 money
- `+3` — 21× Striker Chip · 300,000 money
- `+4` — 28× Striker Chip · 500,000 money
- `+5` — 35× Striker Chip · 800,000 money
- `+6` — 42× Striker Chip · 10× Pandora Power Core
- `+7` — 49× Striker Chip · 50× Pandora Power Core
- `+8` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Welly Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Welly Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Welly Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Welly Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Welly Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Welly Ship Part · 100× Alien Essence · 100× Transcendence Core

---

## 623 · Zerina 泽瑞娜
**Role** Striker · **Attack** physical · **Generation** latest
**Ratings** Damage 10/10 · Defence 7/10 · Assist 8/10

### Skill panels
**Slot 1 — Frost Mist Burst** (id 1960, unlocks at `+0`)
  - **Ⅰ** at `+0` — Frost Mist BurstⅠ (泽瑞娜+0)
    Horizontal Attack, plunders 50% Accumulator and 50% S-ATK from the target, then deals 360% S-ATK damage to hit targets for 2 rounds. Lastly, recovers 100 Accumulator.
  - **Ⅱ** at `+6` — Frost Mist BurstⅡ (泽瑞娜+3)
    Horizontal Attack, plunders 50% Accumulator and 50% S-ATK from the target, then deals 360% S-ATK damage to the target for 2 rounds. Increases all allies' ATK and S-ATK by 80% for 2 rounds. Lastly, recovers 100 Accumulator.
  - **Ⅲ** at `+10` — Frost Mist BurstⅢ (泽瑞娜+6)
    Horizontal Attack, plunders 50% Accumulator and 50% S-ATK from the target, then deals 360% S-ATK damage to the target for 2 rounds. Increases all allies' ATK and S-ATK by 80% for 2 rounds. Has a 100% chance to Freeze 2 random enemies for 2 rounds. Lastly, recovers 100 Accumulator.
  - **Ⅳ** at `+15` — Frost Mist BurstIV (泽瑞娜+10)
    Horizontal Attack, plunders 50% Accumulator and 50% S-ATK from the target, then deals 360% S-ATK damage to the target for 2 rounds. Increases all allies' ATK and S-ATK by 80% for 2 rounds. Has a 100% chance to Brittle a random enemy within the attack range, increasing the damage he/she take by 80% for 2 rounds. Has a 100% chance to Freeze 2 random enemies for 2 rounds. Lastly, recovers 100 Accumulator.

**Slot 2 — Frost Star** (id 1961, unlocks at `+2`)
  - **Ⅰ** at `+2` — Frost StarⅠ (泽瑞娜+2)
    (Takes effect at the start of battle) At the start of battle, grants all allies immunity to Freeze until the end of battle.
  - **Ⅱ** at `+9` — Frost StarⅡ (泽瑞娜+9)
    (Takes effect at the start of battle) At the start of battle, grants all allies immunity to Freeze until the end of battle. At the start of battle, there is a 100% chance to Brittle 1 random enemy for 2 rounds.
  - **Ⅲ** at `+T` — Frost StarⅢ (泽瑞娜+16)
    (Takes effect at the start of battle) At the start of battle, grants all allies immunity to Freeze, Brittle, and Icebound until the end of battle. At the start of battle, there is a 100% chance to Brittle 1 random enemy, increasing the damage he/she take by 80%, lasting 2 rounds.
  - **Ⅳ** at `+T3` — Frost StarIV (泽瑞娜+19)
    (Takes effect at the start of battle) At the start of battle, grants all allies immunity to Freeze, Brittle, and Icebound until the end of battle. At the start of battle, there is a 100% chance to Brittle 1 random enemy, increasing the damage he/she take by 80%, lasting 2 rounds. While Zerina is alive, all allies gain the effect: Enemies they kill will be Frozen for 1 round upon revival. (If Zerina dies, the effect is removed.)

**Slot 3 — Winter's Vow** (id 1962, unlocks at `+4`)
  - **Ⅰ** at `+4` — Winter's VowⅠ (泽瑞娜+4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +60% DEF: +30% S-DEF: +30% DMG Reduction (Absolute Value): +30%
  - **Ⅱ** at `+10` — Winter's VowⅡ (泽瑞娜+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +90% DEF: +60% S-DEF: +60% DMG Reduction (Absolute Value): +40%
  - **Ⅲ** at `+14` — Winter's VowⅢ (泽瑞娜+14)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +120% DEF: +90% S-DEF: +90% DMG Reduction (Absolute Value): +50%
  - **Ⅳ** at `+T2` — Winter's VowIV (泽瑞娜+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +150% DEF: +120% S-DEF: +120% DMG Reduction (Absolute Value): +60%

**Slot 4 — Icicle Barrage** (id 1963, unlocks at `+3`)
  - **Ⅰ** at `+3` — Icicle BarrageⅠ (泽瑞娜+3)
    (Takes effect at the start of battle) When casting a skill, there is a 50% chance to instantly kill enemies in freezing, Brittle, or Icebound states. (Probability for each target calculated separately.)
  - **Ⅱ** at `+13` — Icicle BarrageⅡ (泽瑞娜+13)
    (Takes effect at the start of battle) When casting a skill, there is a 50% chance to instantly kill enemies in freezing, Brittle, or Icebound states. (Probability for each target calculated separately.) When S-ATK hits an enemy in freezing, Brittle, or Icebound states, increases own S-ATK by 100% and Crit ATK by 300% for 2 turns.
  - **Ⅲ** at `+T1` — Icicle BarrageⅢ (泽瑞娜+17)
    (Takes effect at the start of battle) When casting a skill, there is a 50% chance to instantly kill enemies in freezing, Brittle, or Icebound states. (Probability for each target calculated separately.) When S-ATK hits an enemy in freezing, Brittle, or Icebound states, increases own S-ATK by 100% and Crit ATK by 300% for 2 turns. Upon own death, there is a 100% chance to Icebound 2 random enemies for 2 turns.
  - **Ⅳ** at `+T4` — Icicle BarrageIV (泽瑞娜+20)
    (Takes effect at the start of battle) When casting a skill, there is a 50% chance to instantly kill enemies in freezing, Brittle, or Icebound states. (Probability for each target calculated separately.) When S-ATK hits an enemy in freezing, Brittle, or Icebound states, increases own S-ATK by 100% and Crit ATK by 300% for 2 turns. Upon own death, there is a 100% chance to Icebound 2 random enemies for 2 turns. Icebound effects applied by this ability ignore immunity and protection effects; units that die while Icebound cannot be reborn or revived.

### Augment cost (per step)
- `+1` — 5× Striker Chip · 100,000 money
- `+2` — 10× Striker Chip · 200,000 money
- `+3` — 21× Striker Chip · 300,000 money
- `+4` — 28× Striker Chip · 500,000 money
- `+5` — 35× Striker Chip · 800,000 money
- `+6` — 42× Striker Chip · 10× Pandora Power Core
- `+7` — 49× Striker Chip · 50× Pandora Power Core
- `+8` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Zerina Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Zerina Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Zerina Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Zerina Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Zerina Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Zerina Ship Part · 100× Alien Essence · 100× Transcendence Core

---

## 627 · Lin Xingyao 林星遥
**Role** Striker · **Attack** physical · **Generation** latest
**Ratings** Damage 10/10 · Defence 7/10 · Assist 10/10

### Skill panels
**Slot 1 — Zero-Point Fission** (id 1972, unlocks at `+0`)
  - **Ⅰ** at `+0` — Zero-Point FissionⅠ (林星遥+0)
    Cross Attack, plunders 50% Accumulator and 75% S-ATK from the target for 2 rounds, then deals 220% S-ATK damage to the target. Lastly, recovers 100 Accumulator.
  - **Ⅱ** at `+6` — Zero-Point FissionⅡ (林星遥+2)
    Cross Attack, plunders 50% Accumulator and 75% S-ATK from the target for 2 rounds, then deals 240% S-ATK damage to the target. This S-ATK is guaranteed to Penetrate (ignores Block). Lastly, recovers 100 Accumulator.
  - **Ⅲ** at `+10` — Zero-Point FissionⅢ (林星遥+6)
    Cross Attack, plunders 50% Accumulator and 75% S-ATK from the target for 2 rounds, then deals 260% S-ATK damage to the target. This S-ATK is guaranteed to Penetrate (ignores Block). Gains Eye of True Sight for 99 rounds. Lastly, recovers 100 Accumulator.
  - **Ⅳ** at `+15` — Zero-Point FissionIV (林星遥+9)
    Cross Attack, first removes the target's buffs, then plunders 50% Accumulator and 75% S-ATK from the target for 2 rounds, then deals 300% S-ATK damage to the target. This S-ATK is guaranteed to Penetrate (ignores Block). Increases own Crit Rate by 150% and Crit ATK by 300% for 99 rounds. Gains Eye of True Sight for 99 rounds. Lastly, recovers 200 Accumulator.

**Slot 2 — Hyperionic Cannon** (id 1973, unlocks at `+2`)
  - **Ⅰ** at `+2` — Hyperionic CannonⅠ (林星遥+2)
    (Takes effect at the start of battle) At the start of battle, charges [Hyperionic Cannon], starting at 0 stack and up to a maximum of 3 stacks. Each time a skill is cast, gains 1 stack. Upon reaching 3 stacks, if not in a state of inability to act, immediately triggers an additional vertical attack from [Hyperionic Barrage]. This skill effect is the same as [Zero-Point Fission], and S-ATK is increased to 300%.
  - **Ⅱ** at `+9` — Hyperionic CannonⅡ (林星遥+9)
    (Takes effect at the start of battle) At the start of battle, charges [Hyperionic Cannon], starting at 0 stack and up to a maximum of 3 stacks. Each time a skill is cast, gains 1 stack. Upon reaching 3 stacks, if not in a state of inability to act, immediately triggers an additional vertical attack from [Hyperionic Barrage]. This skill effect is the same as [Zero-Point Fission], and S-ATK is increased to 350%. [Hyperionic Barrage] will remove the Rebirth effect from the target and has a 100% chance to instantly destroy a random enemy.
  - **Ⅲ** at `+T` — Hyperionic CannonⅢ (林星遥+16)
    (Takes effect at the start of battle) At the start of battle, charges [Hyperionic Cannon], starting at 0 stack and up to a maximum of 3 stacks. Each time a skill is cast, gains 1 stack. Upon reaching 3 stacks, if not in a state of inability to act, immediately triggers an additional vertical attack from [Hyperionic Barrage]. This skill effect is the same as [Zero-Point Fission], and S-ATK is increased to 400%. [Hyperionic Barrage] will remove the Rebirth effect from the target and has a 100% chance to instantly destroy a random enemy. [Hyperionic Barrage] will remove Eye of True Sight from all enemies, and enemies hit cannot gain Eye of True Sight for 2 rounds.
  - **Ⅳ** at `+T3` — Hyperionic CannonIV (林星遥+19)
    (Takes effect at the start of battle) At the start of battle, charges [Hyperionic Cannon], starting at 0 stack and up to a maximum of 3 stacks. Each time a skill is cast, gains 1 stack. Upon reaching 3 stacks, if not in a state of inability to act, immediately triggers an additional vertical attack from [Hyperionic Barrage]. This skill effect is the same as [Zero-Point Fission], and S-ATK is increased to 500%. [Hyperionic Barrage] will remove the Rebirth effect from the target and has a 100% chance to instantly destroy a random enemy. (Ignores immunity to instant destruction) [Hyperionic Barrage] will remove Eye of True Sight from all enemies, and enemies hit cannot gain Eye of True Sight for 2 rounds. Own S-ATK can ignore the effects of Stasis and immunity to lethal shield effect. Using [Zero-Point Fission] does not consume Accumulator. ([Hyperionic Barrage] cannot gain this effect)

**Slot 3 — Valiant Creed** (id 1974, unlocks at `+4`)
  - **Ⅰ** at `+4` — Valiant CreedⅠ (林星遥+4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +60% ATK: +60% Crit ATK (Absolute Value): +30% DMG Bonus (Absolute Value): +15%
  - **Ⅱ** at `+10` — Valiant CreedⅡ (林星遥+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +90% ATK: +90% Crit ATK (Absolute Value): +40% DMG Bonus (Absolute Value): +20%
  - **Ⅲ** at `+14` — Valiant CreedⅢ (林星遥+14)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +120% ATK: +120% Crit ATK (Absolute Value): +50% DMG Bonus (Absolute Value): +25%
  - **Ⅳ** at `+T2` — Valiant CreedIV (林星遥+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +150% ATK: +150% Crit ATK (Absolute Value): +60% DMG Bonus (Absolute Value): +30%

**Slot 4 — Ionic Surge** (id 1975, unlocks at `+3`)
  - **Ⅰ** at `+3` — Ionic SurgeⅠ (林星遥+3)
    (Takes effect at the start of battle) At the start of battle, self gains 3 rounds of invisibility.
  - **Ⅱ** at `+13` — Ionic SurgeⅡ (林星遥+13)
    (Takes effect at the start of battle) At the start of battle, self gains 3 rounds of invisibility. At the start of battle, charges [Hyperionic Cannon] with 2 stacks. For each allies that dies, charges [Hyperionic Cannon] with 1 stack.
  - **Ⅲ** at `+T1` — Ionic SurgeⅢ (林星遥+17)
    (Takes effect at the start of battle) At the start of battle, self gains 3 rounds of invisibility. At the start of battle, charges [Hyperionic Cannon] with 2 stacks. For each allies that dies, charges [Hyperionic Cannon] with 1 stack. [Zero-Point Fission] deals damage 1 additional time, [Hyperionic Barrage] deals damage 2 additional times. (Additional damage are based on the corresponding skill’s damage.)
  - **Ⅳ** at `+T4` — Ionic SurgeIV (林星遥+20)
    (Takes effect at the start of battle) At the start of battle, self gains 3 rounds of invisibility. At the start of battle, charges [Hyperionic Cannon] with 2 stacks. For each allies that dies, charges [Hyperionic Cannon] with 1 stack. [Zero-Point Fission] deals damage 2 additional times, [Hyperionic Barrage] deals damage 3 additional times. (Additional damage are based on the corresponding skill’s damage.) When receiving lethal damage (including ignores immunity to lethal attacks and instant destruction effects), all stacks of [Hyperionic Cannon] are removed to block this lethal damage, can only trigger up to 2 times per battle.

### Augment cost (per step)
- `+1` — 5× Striker Chip · 100,000 money
- `+2` — 10× Striker Chip · 200,000 money
- `+3` — 21× Striker Chip · 300,000 money
- `+4` — 28× Striker Chip · 500,000 money
- `+5` — 35× Striker Chip · 800,000 money
- `+6` — 42× Striker Chip · 10× Pandora Power Core
- `+7` — 49× Striker Chip · 50× Pandora Power Core
- `+8` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Lin Xingyao's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Lin Xingyao's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Lin Xingyao's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Lin Xingyao's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Lin Xingyao's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Lin Xingyao's Ship Part · 100× Alien Essence · 100× Transcendence Core

---

## 636 · Kaelum 凯勒姆
**Role** Striker · **Attack** physical · **Generation** latest
**Ratings** Damage 9/10 · Defence 7/10 · Assist 9/10

### Skill panels
**Slot 1 — Propelling Cannonade** (id 2004, unlocks at `+0`)
  - **Ⅰ** at `+0` — Propelling CannonadeⅠ (凯勒姆+0)
    Vertical Attack, deals 350% S-ATK damage to targets hit. Gains Eye of True Sight until the end of battle. Lastly, recovers 100 Accumulator.
  - **Ⅱ** at `+6` — Propelling CannonadeⅡ (凯勒姆+6)
    Vertical Attack, deals 400% S-ATK damage to targets hit. Gains Eye of True Sight until the end of battle. Gains a Shield equal to 80% of max HP (cannot stack, repeated use refreshes the Shield). Lastly, recovers 100 Accumulator.
  - **Ⅲ** at `+10` — Propelling CannonadeⅢ (凯勒姆+9)
    Vertical Attack, deals 450% S-ATK damage to targets hit. Gains Eye of True Sight until the end of battle. Gains a Shield equal to 80% of max HP (cannot stack, repeated use refreshes the Shield). All allies gain 90% S-ATK and 60% crit ATK until the end of battle. Lastly, recovers 100 Accumulator.
  - **Ⅳ** at `+15` — Propelling CannonadeIV (凯勒姆+15)
    Vertical Attack, first plunders 80% of the target's Accumulator (ignores immunity), deals 500% S-ATK damage to targets hit. Gains Eye of True Sight until the end of battle. Gains a Shield equal to 80% of max HP (cannot stack, repeated use refreshes the Shield). All allies gain 90% S-ATK and 60% crit ATK until the end of battle. Lastly, recovers 100 Accumulator.

**Slot 2 — Combat Command** (id 2005, unlocks at `+2`)
  - **Ⅰ** at `+2` — Combat CommandⅠ (凯勒姆+2)
    (Takes effect at the start of battle) During battle preparation, Kaelum determines the battle style based on position. If placed in the 1st or 2nd row, [Destruction Mode] is activated; if placed in the 3rd row, [Synchronization Mode] is activated. Different modes grant different skill effects. (Takes effect at the start of battle and each time a unit is resurrect rebirthed.) [Destruction Mode]: The damage taken from a single hit will not exceed 20% of max HP, lasting for 5 rounds. [Synchronization Mode]: At the start of battle, all allies' damage dealt is increased by 60%, lasting until the end of battle.
  - **Ⅱ** at `+9` — Combat CommandⅡ (凯勒姆+9)
    (Takes effect at the start of battle) During battle preparation, Kaelum determines the battle style based on position. If placed in the 1st or 2nd row, [Destruction Mode] is activated; if placed in the 3rd row, [Synchronization Mode] is activated. Different modes grant different skill effects. (Takes effect at the start of battle and each time a unit is resurrect rebirthed.) [Destruction Mode]: The damage taken from a single hit will not exceed 15% of max HP, lasting for 5 rounds. When using a skill, additionally recover 300 Accumulator. [Synchronization Mode]: At the start of battle, all allies' damage dealt is increased by 120%, lasting until the end of battle.
  - **Ⅲ** at `+T` — Combat CommandⅢ (凯勒姆+16)
    (Takes effect at the start of battle) During battle preparation, Kaelum determines the battle style based on position. If placed in the 1st or 2nd row, [Destruction Mode] is activated; if placed in the 3rd row, [Synchronization Mode] is activated. Different modes grant different skill effects. (Takes effect at the start of battle and each time a unit is resurrect rebirthed.) [Destruction Mode]: The damage taken from a single hit will not exceed 15% of max HP, lasting for 5 rounds. When using a skill, additionally recover 300 Accumulator, and S-ATK deal 4 extra hits. [Synchronization Mode]: At the start of battle, all allies' damage dealt is increased by 120%, lasting until the end of battle. While Kaelum is alive, whenever any ally uses a skill, cleanse all allies’ control effects.
  - **Ⅳ** at `+T3` — Combat CommandIV (凯勒姆+19)
    (Takes effect at the start of battle) During battle preparation, Kaelum determines the battle style based on position. If placed in the 1st or 2nd row, [Destruction Mode] is activated; if placed in the 3rd row, [Synchronization Mode] is activated. Different modes grant different skill effects. (Takes effect at the start of battle and each time a unit is resurrect rebirthed.) [Destruction Mode]: The damage taken from a single hit will not exceed 15% of max HP, lasting for 5 rounds. When using a skill, additionally recover 300 Accumulator, and S-ATK deal 5 extra hits. When taking lethal damage (including ignores immunity to lethal attacks and instant destruction effects), the damage is blocked and Kaelum immediately acts once. (Can only activate once per battle) [Synchronization Mode]: At the start of battle, all allies' damage dealt is increased by 120%, lasting until the end of battle. While Kaelum is alive, whenever any ally uses a skill, cleanse all allies’ control effects, and all allies’ S-ATK can target units in Conceal and Dark Conceal states. (If Kaelum dies, the effect disappears)

**Slot 3 — Imperial Guard** (id 2006, unlocks at `+4`)
  - **Ⅰ** at `+4` — Imperial GuardⅠ (凯勒姆+4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +60% DEF: +30% S-DEF: +30% DMG Reduction (Absolute Value): +30%
  - **Ⅱ** at `+10` — Imperial GuardⅡ (凯勒姆+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +90% DEF: +60% S-DEF: +60% DMG Reduction (Absolute Value): +40%
  - **Ⅲ** at `+14` — Imperial GuardⅢ (凯勒姆+14)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +120% DEF: +90% S-DEF: +90% DMG Reduction (Absolute Value): +50%
  - **Ⅳ** at `+T2` — Imperial GuardIV (凯勒姆+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +150% DEF: +120% S-DEF: +120% DMG Reduction (Absolute Value): +60%

**Slot 4 — Combat Endurance** (id 2007, unlocks at `+3`)
  - **Ⅰ** at `+3` — Combat EnduranceⅠ (凯勒姆+3)
    (Takes effect at the start of battle) Upon death, deal true damage equal to 40% of your max HP to each enemy unit.
  - **Ⅱ** at `+13` — Combat EnduranceⅡ (凯勒姆+13)
    (Takes effect at the start of battle) Upon death, deal true damage equal to 40% of your max HP to each enemy unit. [Destruction Mode]: When casting a skill, restores 50% of own max HP. [Synchronization Mode]: Each time a skill is cast, all Enemies take 50% increased damage for 2 rounds.
  - **Ⅲ** at `+T1` — Combat EnduranceⅢ (凯勒姆+17)
    (Takes effect at the start of battle) Upon death, deal true damage equal to 40% of your max HP to each enemy unit, and the ally unit with the highest S-ATK at the start of battle will act immediately once. [Destruction Mode]: When casting a skill, restores 50% of her max HP. [Synchronization Mode]: Each time a skill is cast, all Enemy units take 50% more damage for 2 rounds.
  - **Ⅳ** at `+T4` — Combat EnduranceIV (凯勒姆+20)
    (Takes effect at the start of battle) Upon death, deal true damage equal to 40% of your max HP to each enemy unit, and the ally unit with the highest S-ATK at the start of battle will act immediately once. [Destruction Mode]: When casting a skill, restores 50% of her max HP. If an S-ATK results in a kill, perform an additional S-ATK. [Synchronization Mode]: Each time a skill is cast, all Enemy units take 50% more damage for 2 rounds, and the ally unit with the highest S-ATK at the start of BATTLE will act immediately once. (Cannot target self.)

### Augment cost (per step)
- `+1` — 5× Striker Chip · 100,000 money
- `+2` — 10× Striker Chip · 200,000 money
- `+3` — 21× Striker Chip · 300,000 money
- `+4` — 28× Striker Chip · 500,000 money
- `+5` — 35× Striker Chip · 800,000 money
- `+6` — 42× Striker Chip · 10× Pandora Power Core
- `+7` — 49× Striker Chip · 50× Pandora Power Core
- `+8` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Kaelum's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Kaelum's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Kaelum's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Kaelum's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Kaelum's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Kaelum's Ship Part · 100× Alien Essence · 100× Transcendence Core

---

## 637 · Darius 达里厄
**Role** Striker · **Attack** physical · **Generation** old
**Ratings** Damage 7/10 · Defence 7/10 · Assist 9/10

### Signature skill
- **Ⅰ** at `+0` — Worldie (达里厄+0)
  Cross Attack, deals 200% S-ATK damage to targets. Lastly, you recover 100 Accumulator.

### Augment cost (per step)
- `+1` — 5× Striker Chip · 100,000 money
- `+2` — 10× Striker Chip · 200,000 money
- `+3` — 21× Striker Chip · 300,000 money
- `+4` — 28× Striker Chip · 500,000 money
- `+5` — 35× Striker Chip · 800,000 money
- `+6` — 42× Striker Chip · 10× Pandora Power Core
- `+7` — 49× Striker Chip · 50× Pandora Power Core
- `+8` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Striker Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Striker Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Darius's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Darius's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Darius's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Darius's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Darius's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Darius's Ship Part · 100× Alien Essence · 100× Transcendence Core

---
