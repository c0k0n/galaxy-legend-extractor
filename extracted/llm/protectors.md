# Galaxy Legends — SSS Protectors (26 heroes)

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
| 420 | Buzzer | 巴斯尔 | 3 | 9 | 7 | old |
| 439 | Diesel | 迪塞尔 | 6 | 9 | 7 | old |
| 446 | Galaxy Huntress | 星河猎手 | 7 | 9 | 8 | old |
| 457 | Osmond | 奥斯蒙 | 5 | 10 | 8 | old |
| 467 | Edith Hineston | 伊蒂斯·海因斯顿 | 4 | 8 | 10 | old |
| 478 | Rasyon | 拉西昂 | 4 | 8 | 10 | old |
| 500 | Ulrich | 乌德维克 | 5 | 10 | 8 | old |
| 521 | DeRosa | 德罗萨 | 4 | 8 | 10 | old |
| 541 | Andrea | 安德莉亚 | 4 | 8 | 10 | latest |
| 544 | Flora | 芙兰 | 4 | 8 | 10 | latest |
| 555 | Selika | 瑟莉卡 | 4 | 8 | 10 | latest |
| 559 | Bonnie | 波妮 | 5 | 10 | 8 | old |
| 560 | Valghar | 瓦格哈尔 | 5 | 10 | 8 | latest |
| 572 | Sorrento | 索伦托 | 5 | 10 | 8 | latest |
| 576 | Eldran | 艾尔德兰 | 7 | 9 | 8 | latest |
| 584 | Interstellar Chef: Porter | 星际大厨：波特 | 4 | 8 | 10 | latest |
| 591 | Amber | 琥珀 | 5 | 10 | 8 | old |
| 594 | Kaelmor | 凯尔莫尔 | 5 | 10 | 8 | latest |
| 598 | Knightley | 奈特莉 | 7 | 10 | 8 | latest |
| 608 | Ironwall Prototype: Serratine | 铁壁原型机：塞拉汀 | 6 | 10 | 10 | latest |
| 615 | Teda | 泰达 | 4 | 10 | 10 | latest |
| 621 | Roche | 洛希 | 4 | 8 | 10 | latest |
| 624 | Vid | 维迪 | 7 | 9 | 8 | old |
| 625 | Brianna | 布里安娜 | 5 | 10 | 8 | latest |
| 634 | Kolossos | 科洛索斯 | 7 | 10 | 9 | latest |
| 639 | Javier | 哈维尔 | 7 | 10 | 9 | latest |

---

## 420 · Buzzer 巴斯尔
**Role** Protector · **Attack** physical · **Generation** old
**Ratings** Damage 3/10 · Defence 9/10 · Assist 7/10

### Signature skill
- **Ⅰ** at `+0` — Shining Shield (巴斯尔，闪光护盾)
  Vertical attack, deals 220% S-ATK damage to targets which get hit; increases 50% Crit Rate for the team for 1 round and activate shields for self and two teammates with the lowest HP; the shield can reduce 80% received damage for 2 rounds. It can also recover 50 Accumulator for all teammates and recover 100 Accumulator for self. If Buzzer has less than 70% HP when releases this skill, it will become invisible for 1 round, and increase DEF and S-DEF by 300% for 1 round; in addition, heal self by 30% of the S-ATK damage dealt.
- **Ⅱ** at `+T2` — Shining Shield Ⅱ (巴斯尔+T2)
  Vertical attack, deals 250% S-ATK damage to targets which get hit; increases 60% Crit Rate for the team for 1 round and activate shields for self and two teammates with the lowest HP; the shield can reduce 85% received damage for 2 rounds. It can also recover 50 Accumulator for all teammates and recover 100 Accumulator for self. If Buzzer has less than 70% HP when releases this skill, it will become invisible for 1 round, and increase DEF and S-DEF by 300% for 1 round; in addition, heal self by 30% of the S-ATK damage dealt.
- **III** at `+T4` — Shining Shield III (巴斯尔+T4)
  Vertical attack, deals 300% S-ATK damage to targets which get hit; increases 80% Crit Rate for the team for 1 round and activate shields for all allies; the shield can reduce 85% received damage for 2 rounds. It can also recover 65 Accumulator for all teammates and recover 100 Accumulator for self. If Buzzer has less than 80% HP when releases this skill, it will become invisible for 1 round, and increase DEF and S-DEF by 450% for 1 round; in addition, heal self by 50% of the S-ATK damage dealt.

### Augment cost (per step)
- `+1` — 5× Protector Chip · 100,000 money
- `+2` — 10× Protector Chip · 200,000 money
- `+3` — 21× Protector Chip · 300,000 money
- `+4` — 28× Protector Chip · 500,000 money
- `+5` — 35× Protector Chip · 800,000 money
- `+6` — 42× Protector Chip · 10× Pandora Power Core
- `+7` — 49× Protector Chip · 50× Pandora Power Core
- `+8` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Buzzer’s Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Buzzer’s Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Buzzer’s Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Buzzer’s Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Buzzer’s Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Buzzer’s Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 439 · Diesel 迪塞尔
**Role** Protector · **Attack** physical · **Generation** old
**Ratings** Damage 6/10 · Defence 9/10 · Assist 7/10

### Signature skill
- **Ⅰ** at `+0` — Universal NatureⅠ (迪赛尔，森罗万象)
  Cross attack, deals 300% S-ATK damage to targets which get hit. opens the Eye of True Sight for self and two teammates with the lowest HP percentage so they can attack invisible enemies and the effect will last until the end of the battle. It will trigger a Deflection Force Field for self. The field can resist 250% vertical damage dealt by vertical and cross attacks for self and the teammate behind for 1 round. The damage to resist is determined by Diesel’s ATK, S-ATK and Accumulator when releasing the skill. It can also increase 80% S-ATK, 80% S-DEF, 50% Block (percentage) for the team for 1 round. Meanwhile, Diesel will become immune to Weaken, Lock and Freeze for 1 round. In addition, restore 50 Accumulator for all teammates and 100 Accumulator for self.
- **Ⅱ** at `+T` — Universal NatureⅡ (迪赛尔，森罗万象)
  Cross attack, deals 320% S-ATK damage to targets which get hit. Opens the Eye of True Sight for self and two teammates with the lowest HP percentage so they can attack invisible enemies and the effect will last until the end of the battle. It will trigger a Deflection Force Field for self. The field can resist 300% vertical damage dealt by vertical and cross attacks for self and the teammate behind for 1 round. The damage to resist is determined by Diesel’s ATK, S-ATK and Accumulator when releasing the skill. It can also increase 85% S-ATK, 85% S-DEF, 80% Block (percentage) for the team for 1 round. Meanwhile, Diesel will become immune to Weaken, Lock and Freeze for 1 round. In addition, restore 70 Accumulator for all teammates and 100 Accumulator for self.
- **Ⅲ** at `+T3` — Universal NatureⅢ (迪赛尔，森罗万象)
  Cross attack, deals 320% S-ATK damage to targets which get hit. Opens the Eye of True Sight for self and two teammates with the lowest HP percentage so they can attack invisible enemies and the effect will last until the end of the battle. It will trigger a Deflection Force Field for self. The field can resist 300% vertical damage dealt by vertical and cross attacks for self and the teammate behind for 1 round. The damage to resist is determined by Diesel’s ATK, S-ATK and Accumulator when releasing the skill. It can also increase 85% S-ATK, 85% S-DEF, 80% Block (percentage) for the team for 1 round. Meanwhile, Diesel will become immune to Weaken, Lock and Freeze for 1 round.Activates an 80% damage reflect effect for all friendly ships for 1 round.Activates a shield that can absorb 50 million damage for all friendly ships for 1 round. In addition, restore 70 Accumulator for all teammates and 100 Accumulator for self.
- **Ⅳ** at `+T4` — Universal NatureⅣ (迪赛尔，森罗万象)
  Cross attack, deals 340% S-ATK damage to targets which get hit. Opens the Eye of True Sight for all allies so they can attack invisible enemies and the effect will last until the end of the battle. It will trigger a Deflection Force Field for self. The field can resist 350% vertical damage dealt by vertical and cross attacks for self and the teammate behind for 1 round. The damage to resist is determined by Diesel’s ATK, S-ATK and Accumulator when releasing the skill. It can also increase 100% S-ATK, 100% S-DEF, 100% Block (percentage) for the team for 1 round. Has an 80% chance (probability for each target is calculated independently) to cleanse the stat debuffs (including Weaken) of all allies and some crowd-control effects (Freeze, Lock, Confuse, Petrify and Forbidding Skill Use). Meanwhile, all allies will become immune to Weaken, Lock, Forbidding Skill Use, Confuse and Freeze for 1 round. Activates a 90% damage reflect effect for all friendly ships for 1 round. Activates a shield that can absorb 80 million damage for all friendly ships for 1 round. In addition, restore 80 Accumulator for all teammates and 100 Accumulator for self.

### Augment cost (per step)
- `+1` — 5× Protector Chip · 100,000 money
- `+2` — 10× Protector Chip · 200,000 money
- `+3` — 21× Protector Chip · 300,000 money
- `+4` — 28× Protector Chip · 500,000 money
- `+5` — 35× Protector Chip · 800,000 money
- `+6` — 42× Protector Chip · 10× Pandora Power Core
- `+7` — 49× Protector Chip · 50× Pandora Power Core
- `+8` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Diesel's Ship Parts · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Diesel's Ship Parts · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Diesel's Ship Parts · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Diesel's Ship Parts · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Diesel's Ship Parts · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Diesel's Ship Parts · 140× Alien Essence · 140× Transcendence Core

---

## 446 · Galaxy Huntress 星河猎手
**Role** Protector · **Attack** physical · **Generation** old
**Ratings** Damage 7/10 · Defence 9/10 · Assist 8/10

### Signature skill
- **Ⅰ** at `+0` — Space FortressⅠ (星河猎手，空间堡垒)
  Cross attack, deals 300% S-ATK damage to the targets. Releases a shield that can absorb 150 million damage for all friendly ships for 2 rounds (only the latest shield generated by the same skill can exist, and the effects cannot be stacked). Additionally, the skill will clear all buffs on the targets and allow self and two friendly ships with the lowest HP (percentage) to become immune to Lock and Freeze for 1 round. It has a 80% chance (the rate for each target will be settled independently) to make all friendly ships enter stasis status for 1 round. When in stasis state, it can withstand lethal damage one time for 1 round. It has a 80% chance (the rate for each target will be settled independently) to expose invisible enemies and clear the target's Accumulator obtained from this attack (DEF Accumulator Recovery). Recovers 100 Accumulator for self.
- **Ⅱ** at `+T` — Space FortressⅡ (星河猎手，空间堡垒 I)
  Cross Attack, deals 320% S-ATK damage to the targets. Releases a shield that can absorb 200 million damage for all friendly ships for 2 rounds (only the latest shield generated by the same skill can exist, and the effects cannot be stacked). Additionally, the skill will clear all buffs on the targets and grant you and all friendly ships immunity to Lock and Freeze for 1 round. It has a 80% chance (probability for each target is calculated independently) to make all friendly ships enter stasis status for 1 round. When in the stasis state, they can withstand lethal damage one time for 1 round. It has a 100% chance to expose invisible enemies and clear the target's Accumulator obtained from this attack (DEF Accumulator Recovery). Grants you 100 Accumulator.
- **Ⅲ** at `+T3` — Space FortressⅢ (星河猎手，空间堡垒 II)
  Cross Attack, deals 340% S-ATK damage to the targets. Releases a shield that can absorb 300 million damage for all friendly ships for 2 rounds (only the latest shield generated by the same skill can exist, and the effects cannot be stacked). If the Galaxy Huntress' shield provided to all allies is still in effect when an enemy attacks, friendly ships defended by the shield cannot receive any debuffs, control effects or stat debuffs (including Weaken) for 2 rounds (this shield persists through effects that clear buffs). Additionally, the skill will clear all buffs on the targets and grant you and all friendly ships immunity to Lock and Freeze for 1 round. It has an 80% chance (probability for each target is calculated independently) to make all friendly ships enter stasis status for 1 round. When in the stasis state, they can withstand lethal damage one time for 1 round. It has a 100% chance to expose invisible enemies and clear the target's Accumulator obtained from this attack (DEF Accumulator Recovery). Grants you 100 Accumulator.
- **IV** at `+T4` — Space FortressIV (星河猎手T4，空间堡垒 III)
  Cross Attack, deals 360% S-ATK damage to the targets. Releases a shield that can absorb 400 million damage for all friendly ships for 2 rounds (only the latest shield generated by the same skill can exist, and the effects cannot be stacked). If the Galaxy Huntress' shield provided to all allies is still in effect when an enemy attacks, friendly ships defended by the shield cannot receive any debuffs, control effects or stat debuffs (including Weaken) for 2 rounds (this shield persists through effects that clear buffs). When the shield is broken, a total of 400 million skill damage will be dealt to the enemy. The damage will be affected by the damage increase and damage reduction attributes, and the damage will be shared equally among the currently surviving enemy units. Additionally, the skill will clear all buffs on the targets and grant you and all friendly ships immunity to Lock and Freeze for 1 round. It has a 100% chance (probability for each target is calculated independently) to make all friendly ships enter stasis status for 1 round. When in the stasis state, they can withstand lethal damage one time for 1 round. It has a 100% chance to expose invisible enemies and clear the target's Accumulator. Grants you 100 Accumulator. At the start of battle, releases a shield that can absorb 400 million damage for all friendly ships for 2 rounds (only the latest shield generated by the same skill can exist, and the effects cannot be stacked). If the Galaxy Huntress' shield provided to all allies is still in effect when an enemy attacks, friendly ships defended by the shield cannot receive any debuffs, control effects or stat debuffs (including Weaken) for 2 rounds (this shield persists through effects that clear buffs). When the shield is broken, a total of 400 million skill damage will be dealt to the enemy. The damage will be affected by the damage increase and damage reduction attributes, and the damage will be shared equally among the currently surviving enemy units.

### Augment cost (per step)
- `+1` — 5× Protector Chip · 100,000 money
- `+2` — 10× Protector Chip · 200,000 money
- `+3` — 21× Protector Chip · 300,000 money
- `+4` — 28× Protector Chip · 500,000 money
- `+5` — 35× Protector Chip · 800,000 money
- `+6` — 42× Protector Chip · 10× Pandora Power Core
- `+7` — 49× Protector Chip · 50× Pandora Power Core
- `+8` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Galaxy Huntress's Ship Parts · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Galaxy Huntress's Ship Parts · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Galaxy Huntress's Ship Parts · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Galaxy Huntress's Ship Parts · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Galaxy Huntress's Ship Parts · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Galaxy Huntress's Ship Parts · 140× Alien Essence · 140× Transcendence Core

---

## 457 · Osmond 奥斯蒙
**Role** Protector · **Attack** physical · **Generation** old
**Ratings** Damage 5/10 · Defence 10/10 · Assist 8/10

### Signature skill
- **Ⅰ** at `+0` — Fortress of MeteorsⅠ (陨星之垒)
  Vertical attack, deals 200% S-ATK Damage, and each target will take additional S-ATK damage equal to (target's current Accumulator x 1)%, the max Accumulator is 300. It also links with all friendly ships, taking 90% of the team's damage, and activates a buff for self to reduce Damage received by 90%, for 2 rounds. It makes self immune to Lock, Freeze, instant destruction, forbidding skill use, and Accumulator Reduce effects, for 2 rounds. Finally, it recovers 100 Accumulator for self. Osmond can also recover an additional 75 Accumulator with DEF Accumulator Recovery, check Attributes for details.
- **Ⅱ** at `+T` — Fortress of MeteorsⅡ (奥斯蒙，陨星壁垒Ⅱ)
  Vertical attack, deals 220% S-ATK Damage, and each target will take additional S-ATK damage equal to (target's current Accumulator x 2)%, the max Accumulator is 300. It also links with all friendly ships, taking 90% of the team's damage, and activates a buff for self to reduce Damage received by 90%, for 2 rounds. It makes self immune to Lock, Freeze, instant destruction, forbidding skill use, and Accumulator Reduce effects, for 2 rounds. Finally, it recovers 100 Accumulator for self. Osmond can also recover an additional 75 Accumulator with DEF Accumulator Recovery, check Attributes for details.
- **Ⅲ** at `+T3` — Fortress of MeteorsⅢ (奥斯蒙，陨星壁垒Ⅲ)
  Vertical attack, deals 240% S-ATK Damage, and each target will take additional S-ATK damage equal to (target's current Accumulator x 3)%, the max Accumulator is 300. It also links with all friendly ships, taking 90% of the team's damage, and activates a buff for self to reduce Damage received by 90%, for 2 rounds.After casting a skill, increases its DEF and S-DEF by 800K (stackable, lasting until the end of the battle). Makes all friendly units immune to Freeze, Lock, Instant Destruction, Weaken, and Forbidding Skill Use for 2 rounds. It makes self immune to Lock, Freeze, instant destruction, forbidding skill use, and Accumulator Reduce effects, for 2 rounds. Finally, it recovers 100 Accumulator for self. Osmond can also recover an additional 75 Accumulator with DEF Accumulator Recovery, check Attributes for details.
- **Ⅳ** at `+T4` — Fortress of MeteorsⅣ (奥斯蒙T4，陨星壁垒Ⅲ)
  Vertical attack, deals 270% S-ATK Damage, and each target will take additional S-ATK damage equal to (target's current Accumulator x 5)%, the max Accumulator is 300. It also links with all friendly ships, taking 90% of the team's damage, and activates a buff for self to reduce Damage received by 90%, for 2 rounds. Each skill use will increase self's DEF and S-DEF by 1.2 million (stackable, lasts until Battle Over). It makes all allies immune to Freeze, Lock, Confusion, instant destruction, Weakening, forbidding skill use, Petrification, Ice Seal, and Entanglement, for 2 rounds. It makes self immune to Freeze, Confusion, Lock, instant destruction, Petrification, Ice Seal, Entanglement, forbidding skill use, and Accumulator Reduce effects, for 2 rounds. Finally, it recovers 100 Accumulator for self. Osmond can also recover an additional 75 Accumulator with DEF Accumulator Recovery, check Attributes for details.

### Augment cost (per step)
- `+1` — 5× Protector Chip · 100,000 money
- `+2` — 10× Protector Chip · 200,000 money
- `+3` — 21× Protector Chip · 300,000 money
- `+4` — 28× Protector Chip · 500,000 money
- `+5` — 35× Protector Chip · 800,000 money
- `+6` — 42× Protector Chip · 10× Pandora Power Core
- `+7` — 49× Protector Chip · 50× Pandora Power Core
- `+8` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Osmond Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Osmond Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Osmond Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Osmond Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Osmond Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Osmond Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 467 · Edith Hineston 伊蒂斯·海因斯顿
**Role** Protector · **Attack** physical · **Generation** old
**Ratings** Damage 4/10 · Defence 8/10 · Assist 10/10

### Signature skill
- **Ⅰ** at `+0` — Divine PunishmentⅠ (神罚领域Ⅰ)
  All attack, dealing 250% S-ATK damage to targets and releasing a halo that temporarily deactivates the Eye of True Sight of all enemies. Then, clears most of the debuffs from all friendly ships (Lock, Confuse, Freeze, Poison, and Curse), and dispels stat debuffs (including Weaken;Does not include debuffs from Legendary Equipment) from all friendly ships； Dispels the forbidding skill use debuff from all friendly ships. Activates Stardust Shield for all friendly ships, which reduces any damage taken by 75% for 1 round. Then, makes self immune to Confuse, Freeze, Lock, instant destruction, forbidding skill use, and Accumulator Reduce effects, for 2 rounds. Finally, recovers 100 Accumulator for self. Note: The ship's receiving S-ATK damage will be reduced by 50%.
- **Ⅱ** at `+T` — Divine PunishmentⅡ (神罚领域Ⅱ)
  All attack, dealing 260% S-ATK damage to targets and releasing a halo that temporarily deactivates the Eye of True Sight of all enemies. Then, clears most of the debuffs from all friendly ships (Lock, Confuse, Freeze, Poison, and Curse), and dispels stat debuffs (including Weaken;Does not include debuffs from Legendary Equipment) from all friendly ships； Dispels the forbidding skill use debuff from all friendly ships. Activates Stardust Shield for all friendly ships, which reduces any damage taken by 75% for 1 round. Then, makes self immune to Confuse, Freeze, Lock, instant destruction, forbidding skill use, and Accumulator Reduce effects, for 2 rounds. Finally, recovers 100 Accumulator for self. Note: The ship's receiving S-ATK damage will be reduced by 55%.
- **Ⅲ** at `+T3` — Divine PunishmentⅢ (神罚领域Ⅲ)
  All attack, dealing 280% S-ATK damage to targets and releasing a halo that temporarily deactivates the Eye of True Sight of all enemies. Then, clears most of the debuffs from all friendly ships (Lock, Confuse, Freeze, Poison, and Curse), and dispels stat debuffs (including Weaken;Does not include debuffs from Legendary Equipment) from all friendly ships； Dispels the forbidding skill use debuff from all friendly ships. Activates Stardust Shield for all friendly ships, which reduces any damage taken by 85% for 1 round.Applies a 40% reduction in S-ATK damage taken by all friendly units (except self), and increases Block by 60%, for 2 rounds. Then, makes self immune to Confuse, Freeze, Lock, instant destruction, forbidding skill use, and Accumulator Reduce effects, for 2 rounds.Revives all friendly units to 100% of their initial HP and 150 Accumulator. Revive only takes effect in the first three rounds and can be added to skill buffs of the current round. Finally, recovers 100 Accumulator for self. Note: The ship's receiving S-ATK damage will be reduced by 60%.
- **IV** at `+T4` — Divine PunishmentIV (神罚领域IV)
  All attack, dealing 300% S-ATK damage to targets and releasing a halo that temporarily deactivates the Eye of True Sight of all enemies. Then, clears most of the debuffs from all friendly ships (Lock, Confuse, Freeze, Poison, Curse, Petrify, Icebound and Entangle), and dispels stat debuffs (including Weaken; does not include debuffs from Legendary Equipment) from all friendly ships; dispels the forbidding skill use debuff from all friendly ships. Activates Stardust Shield for all friendly ships, which reduces any damage taken by 90% for 1 round. Applies a 50% reduction in S-ATK damage taken by all friendly units (except self), and increases Block by 80%, for 2 rounds. Also grants immunity to Confuse, Freeze, Lock, Instant Destruction, Forbidding Skill Use and Accumulator Reduction effects to all allies, and makes self immune to Petrify, Entangle and Icebound for 2 rounds. Revives all friendly units (unaffected by forbidding revival effects) to 100% of their initial HP and 180 Accumulator. Revive only takes effect in the first five rounds and can be added to the skill's buffs. Finally, recovers 100 Accumulator for self. Note: The ship's receiving S-ATK damage will be reduced by 65%. Gains Rebirth for 3 rounds at the start of battle, reviving upon death with 100% HP and 100 Accumulator.

### Augment cost (per step)
- `+1` — 5× Protector Chip · 100,000 money
- `+2` — 10× Protector Chip · 200,000 money
- `+3` — 21× Protector Chip · 300,000 money
- `+4` — 28× Protector Chip · 500,000 money
- `+5` — 35× Protector Chip · 800,000 money
- `+6` — 42× Protector Chip · 10× Pandora Power Core
- `+7` — 49× Protector Chip · 50× Pandora Power Core
- `+8` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Edith Hineston Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Edith Hineston Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Edith Hineston Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Edith Hineston Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Edith Hineston Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Edith Hineston Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 478 · Rasyon 拉西昂
**Role** Protector · **Attack** physical · **Generation** old
**Ratings** Damage 4/10 · Defence 8/10 · Assist 10/10

### Signature skill
- **I** at `+0` — Final Glory I (拉西昂)
  Cross attack; deals 220% S-ATK damage to targets. After casting a skill, Rasyon has a 50% chance to become Unyielding. When Unyielding is in effect, Rasyon will become the target of enemy attacks (Including the lieutenant) and take on all debuffs except for [Petrify] and [estrange] (Freeze, Lock, Confuse, Poison, Curse), stat debuffs, Weaken, Forbidding Skill Use, and Accumulator Reduction effects inflicted on friendly ships (i.e. Rasyon's allies will not be affected by these effects, but Rasyon himself will be affected).And Rasyon's allies will become immune to attack damage(Not immune to subsequent damage), all the above effects last for 2 rounds. Also, activates a shield for all friendly ships that reduces 70% of damage received, for 2 rounds. There's also a 50% chance to apply a Rebirth effect for himself that allows Rasyon to revive immediately upon death, recovering 100% HP and 100 Accumulator, for 1 round. Finally, recovers 100 Accumulator.
- **II** at `+T` — Final Glory II (拉西昂)
  Cross attack; deals 230% S-ATK damage to targets. After casting a skill, Rasyon has a 60% chance to become Unyielding. When Unyielding is in effect, Rasyon will become the target of enemy attacks (Including the lieutenant) and take on all debuffs (Freeze, Lock, Confuse, Poison, Curse), stat debuffs, Weaken, Forbidding Skill Use, and Accumulator Reduction effects inflicted on friendly ships (i.e. Rasyon's allies will not be affected by these effects, but Rasyon himself will be affected). And Rasyon's allies will become immune to attack damage (not immune to subsequent damage), all the above effects last for 2 rounds. Also, activates a shield for all friendly ships that reduces 70% of damage received, for 2 rounds. There's also a 60% chance to apply a Rebirth effect for himself that allows Rasyon to revive immediately upon death, recovering 100% HP and 100 Accumulator, for 1 round. Finally, recovers 100 Accumulator.
- **III** at `+T3` — Final Glory III (拉西昂)
  Cross attack; deals 240% S-ATK damage to targets. After casting a skill, Rasyon has a 100% chance to become Unyielding. When Unyielding is in effect, Rasyon will become the target of enemy attacks (Including the lieutenant) and take on all debuffs (Freeze, Lock, Confuse, Poison, Curse), stat debuffs, Weaken, Forbidding Skill Use, and Accumulator Reduction effects inflicted on friendly ships (i.e. Rasyon's allies will not be affected by these effects, but Rasyon himself will be affected). And Rasyon's allies will become immune to attack damage (not immune to subsequent damage), all the above effects last for 2 rounds. Also, activates a shield for all friendly ships that reduces 70% of damage received, for 2 rounds. There's also a 70% chance to apply a Rebirth effect for himself that allows Rasyon to revive immediately upon death, recovering 100% HP and 100 Accumulator, for 1 round. Finally, recovers 100 Accumulator.Has a 100% chance of gaining Unyielding for 1 round at the start of battle.
- **IV** at `+T4` — Final Glory IV (拉西昂T4)
  Cross attack; deals 260% S-ATK damage to targets. After casting a skill, Rasyon has a 100% chance to become Unyielding. When Unyielding is in effect, Rasyon will become the target of enemy attacks (Including the lieutenant) and take on all debuffs (Freeze, Lock, Confuse, Poison, Curse, Petrify, Entangle, and Icebound), stat debuffs, Weaken, Forbidding Skill Use, and Accumulator Reduction effects inflicted on friendly ships (i.e. Rasyon's allies will not be affected by these effects, but Rasyon himself will be affected). And Rasyon's allies will become immune to attack damage (not immune to subsequent damage), all the above effects last for 2 rounds. Also, activates a shield for all friendly ships that reduces 80% of damage received, for 2 rounds. There's also a 75% chance to apply a Rebirth effect for himself that allows Rasyon to revive immediately upon death, recovering 100% HP and 100 Accumulator, for 1 round. Gains 100% damage reflection for 2 rounds and heals 40% of max HP when takes damage in 2 rounds. Finally, recovers 100 Accumulator. Has a 100% chance of gaining Unyielding for 1 round and 100% damage reflection for 2 rounds at the start of battle.
- **Ⅴ** at `Awaken` — — (拉西昂T4触发技能)
  _(no English description shipped)_

### Augment cost (per step)
- `+1` — 5× Protector Chip · 100,000 money
- `+2` — 10× Protector Chip · 200,000 money
- `+3` — 21× Protector Chip · 300,000 money
- `+4` — 28× Protector Chip · 500,000 money
- `+5` — 35× Protector Chip · 800,000 money
- `+6` — 42× Protector Chip · 10× Pandora Power Core
- `+7` — 49× Protector Chip · 50× Pandora Power Core
- `+8` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Rasyon Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Rasyon Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Rasyon Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Rasyon Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Rasyon Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Rasyon Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 500 · Ulrich 乌德维克
**Role** Protector · **Attack** physical · **Generation** old
**Ratings** Damage 5/10 · Defence 10/10 · Assist 8/10

### Signature skill
- **Ⅰ** at `+0` — BlizzardⅠ (乌德维克，极冰风暴)
  Cross Attack; deals 240% S-ATK damage to targets. Has a 100% chance to apply Glacial Coating to all allies for 2 rounds. Glacial Coating prevents damage equal to 50% of Ulrich's maximum HP, while also reducing damage taken by 40%. Once the coating breaks, it shatters into pieces and has a 75% chance to IceBound 1 random enemy for 1 round. IceBound units cannot act and take 20% increased damage. Units killed while IceBound cannot be reborn or resurrected. Units with Glacial Coating become immune to Freeze, Lock, Confusion, and Instant Destruction. Also increases the S-DEF and DEF of all allies by 100%. Has an 80% chance to expose invisible enemies (probability for each target calculated separately). Finally, recovers 100 Accumulator for self. Self starts each battle with Glacial Coating lasting 2 rounds.
- **Ⅱ** at `+T` — BlizzardⅡ (乌德维克，极冰风暴)
  Cross Attack; deals 280% S-ATK damage to targets. Has a 100% chance to apply Glacial Coating to all allies for 2 rounds. Glacial Coating prevents damage equal to 70% of Ulrich's maximum HP, while also reducing damage taken by 45%. Once the coating breaks, it shatters into pieces and has a 75% chance to IceBound 1 random enemy for 1 round. IceBound units cannot act and take 25% increased damage. Units killed while IceBound cannot be reborn or resurrected. Units with Glacial Coating become immune to Freeze, Lock, Confusion, and Instant Destruction. Also increases the S-DEF and DEF of all allies by 120%. Has an 100% chance to expose invisible enemies (probability for each target calculated separately). Finally, recovers 100 Accumulator for self. Self starts each battle with Glacial Coating lasting 2 rounds.
- **Ⅲ** at `+T3` — BlizzardⅢ (乌德维克，极冰风暴)
  Cross Attack; deals 280% S-ATK damage to targets. Has a 100% chance to apply Glacial Coating to all allies for 2 rounds. Glacial Coating prevents damage equal to 70% of Ulrich's maximum HP, while also reducing damage taken by 45%. Once the coating breaks, it shatters into pieces and has a 75% chance to IceBound 1 random enemy for 1 round. IceBound units cannot act and take 25% increased damage. Units killed while IceBound cannot be reborn or resurrected. Units with Glacial Coating are immune to Freeze, Lock, Confuse, Forbidding Skill Use, Petrify, Entangle, and Instant Destruction. Also increases the S-DEF and DEF of all allies by 120%. Has an 100% chance to expose invisible enemies (probability for each target calculated separately). Finally, recovers 100 Accumulator for self. Applies Glacial Coating to all allied units for 2 Rounds at the start of battle.
- **IV** at `+T4` — BlizzardIV (乌德维克T4，极冰风暴)
  Cross Attack; deals 320% S-ATK damage to targets. Has a 100% chance to apply Glacial Coating to all allies for 2 rounds. Glacial Coating prevents damage equal to 100% of Ulrich's maximum HP, while also reducing damage taken by 55%. Once the coating breaks, it shatters into pieces and has a 100% chance to IceBound (ignores immunity and protection effects) 1 random enemy for 2 rounds. IceBound units cannot act and take 35% increased damage. Units killed while IceBound cannot be reborn or resurrected. Units with Glacial Coating become immune to Freeze, Lock, Confusion, Forbidding Skill Use, Petrify, Entangle and Instant Destruction. Also increases the S-DEF and DEF of all allies by 150%. When all the allies receive fatal damage within 2 rounds, they will be immune to this fatal damage, purify all their debuffs and control effects, and restore 100% of their max HP and 150 Accumulator, and gain 3 rounds of Glacial Coating, and finally make them Icebound for 1 round, during the Icebound: unable to move or be targeted (this effect has 2 rounds of CD after each trigger of each unit, and cannot be effective again during the CD) (this effect takes effect has a lower priority than Time Reversal, and shares a CD round, this effect can't be triggered during the CD of Time Reversal). Has a 100% chance (probability calculated for each unit individually) to reveal enemy invisible units. Has an 100% chance to expose invisible enemies (probability for each target calculated separately). Finally, recovers 100 Accumulator for self. Applies Glacial Coating to all allied units for 2 Rounds at the start of battle. When all the allies receive fatal damage within 2 rounds, they will be immune to this fatal damage, purify all their debuffs and control effects, and restore 100% of their max HP and 100 Accumulator, and gain 3 rounds of Glacial Coating, and finally make them Icebound for 1 round, during the Icebound: unable to move or be targeted (this effect has 2 rounds of CD after each trigger of each unit, and cannot be effective again during the CD) (this effect takes effect has a lower priority than Time Reversal, and shares a CD round, this effect can't be triggered during the CD of Time Reversal).

### Augment cost (per step)
- `+1` — 5× Protector Chip · 100,000 money
- `+2` — 10× Protector Chip · 200,000 money
- `+3` — 21× Protector Chip · 300,000 money
- `+4` — 28× Protector Chip · 500,000 money
- `+5` — 35× Protector Chip · 800,000 money
- `+6` — 42× Protector Chip · 10× Pandora Power Core
- `+7` — 49× Protector Chip · 50× Pandora Power Core
- `+8` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Ulrich Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Ulrich Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Ulrich Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Ulrich Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Ulrich Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Ulrich Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 521 · DeRosa 德罗萨
**Role** Protector · **Attack** physical · **Generation** old
**Ratings** Damage 4/10 · Defence 8/10 · Assist 10/10

### Signature skill
- **Ⅰ** at `+0` — Vengeful CounterⅠ (驰援反击)
  Vertical attack, deal 240% S-ATK damage, and Protects all allies for 2 rounds. Protect: Increases damage reduction by 35% and DEF and S-DEF equal to 40% of DeRosa's initial defenses. 40% of damage taken (excluding instant death) is transferred to DeRosa (damage reduction effects work on damage sustained this way; instant death effects and damage taken by DeRosa cannot be transferred to other units). The damage DeRosa takes for others and his HP will be recorded (resets to 0 upon death or when triggering explosion damage) up to 75% of DeRosa's max HP. Upon stacking up to 75%, an explosion is triggered that deals S-ATK damage equal to the accrued value to all enemy units (explosion damage is affected by damage boosts and damage reduction). The effect of Protect does not work when DeRosa is Confused or crowd-controlled (e.g., Locked, Frozen, Petrified, etc.). Also heals DeRosa and all allies for 25% of DeRosa's max HP and renders all allies immune to instant death for 2 rounds. Lastly, you recover 100 Accumulator. At the start of battle, DeRosa's max HP is increased by 25% and DEF and S-DEF by 15% for the remainder of the battle.
- **Ⅱ** at `+T` — Vengeful CounterⅡ (驰援反击)
  Vertical attack, deal 260% S-ATK damage, and Protects all allies for 2 rounds. Protect: Increases damage reduction by 45% and DEF and S-DEF equal to 55% of DeRosa's initial defenses. 50% of damage taken (excluding instant death) is transferred to DeRosa (damage reduction effects work on damage sustained this way; instant death effects and damage taken by DeRosa cannot be transferred to other units). The damage DeRosa takes for others and his HP will be recorded (resets to 0 upon death or when triggering explosion damage) up to 80% of DeRosa's max HP. Upon stacking up to 80%, an explosion is triggered that deals S-ATK damage equal to the accrued value to all enemy units (explosion damage is affected by damage boosts and damage reduction). The effect of Protect does not work when DeRosa is Confused or crowd-controlled (e.g., Locked, Frozen, Petrified, etc.). Also heals DeRosa and all allies for 30% of DeRosa's max HP and renders all allies immune to instant death for 2 rounds. Lastly, you recover 100 Accumulator. At the start of battle, DeRosa's max HP is increased by 30% and DEF and S-DEF by 20% for the remainder of the battle.
- **Ⅲ** at `+T3` — Vengeful CounterⅢ (驰援反击)
  Vertical attack, deal 280% S-ATK damage, and Protects all allies for 2 rounds. Protect: Increases damage reduction by 65% and DEF and S-DEF equal to 75% of DeRosa's initial defenses. 65% of damage taken (excluding instant death) is transferred to DeRosa (damage reduction effects work on damage sustained this way; instant death effects and damage taken by DeRosa cannot be transferred to other units). The damage DeRosa takes for others and his HP will be recorded (resets to 0 upon death or when triggering explosion damage) up to 100% of DeRosa's max HP. Upon stacking up to 100%, an explosion is triggered that deals S-ATK damage equal to the accrued value to all enemy units (explosion damage is affected by damage boosts and damage reduction). When a protected unit takes lethal damage, there is a 75% chance for that damage to be nullified and the ally is healed for 55% of DeRosa's max HP and cleared of all crowd-control effects and debuffs, whereupon the ally loses the Protect effect (may only trigger up to 2 times per unit in each battle). The effect of Protect does not work when DeRosa is Confused or crowd-controlled (e.g., Locked, Frozen, Petrified, etc.). Also heals DeRosa and all allies for 40% of DeRosa's max HP and renders all allies immune to instant death for 2 rounds. Lastly, you recover 100 Accumulator. At the start of battle, DeRosa's max HP is increased by 35% and DEF and S-DEF by 30% for the remainder of the battle. Also Protects all allies for 2 rounds.
- **IV** at `+T4` — Vengeful CounterIV (驰援反击)
  Vertical attack, deal 280% S-ATK damage, and Protects all allies for 2 rounds. Protect: Increases damage reduction by 75% and DEF and S-DEF equal to 100% of DeRosa's initial defenses. 75% of damage taken (excluding instant death) is transferred to DeRosa (damage reduction effects work on damage sustained this way; instant death effects and damage taken by DeRosa cannot be transferred to other units). The damage DeRosa takes for others and his HP will be recorded (resets to 0 upon death or when triggering explosion damage) up to 150% of DeRosa's max HP. Upon stacking up to 150%, an explosion is triggered that deals S-ATK damage equal to the accrued value to all enemy units (explosion damage is affected by damage boosts and damage reduction). When a protected unit takes lethal damage, there is a 100% chance for that damage to be nullified and the ally is healed for 55% of DeRosa's max HP and cleared of all crowd-control effects and debuffs, whereupon the ally loses the Protect effect (may only trigger up to 2 times per unit in each battle). The effect of Protect does not work when DeRosa is Confused or crowd-controlled (e.g., Locked, Frozen, Petrified, etc.). Also heals DeRosa and all allies for 40% of DeRosa's max HP and renders all allies immune to instant death for 2 rounds. Lastly, you recover 100 Accumulator. At the start of battle, DeRosa's max HP is increased by 35% and DEF and S-DEF by 30% for the remainder of the battle. Also Protects all allies for 2 rounds.

### Augment cost (per step)
- `+1` — 5× Protector Chip · 100,000 money
- `+2` — 10× Protector Chip · 200,000 money
- `+3` — 21× Protector Chip · 300,000 money
- `+4` — 28× Protector Chip · 500,000 money
- `+5` — 35× Protector Chip · 800,000 money
- `+6` — 42× Protector Chip · 10× Pandora Power Core
- `+7` — 49× Protector Chip · 50× Pandora Power Core
- `+8` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× DeRosa Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× DeRosa Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× DeRosa Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× DeRosa Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× DeRosa Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× DeRosa Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 541 · Andrea 安德莉亚
**Role** Protector · **Attack** physical · **Generation** latest
**Ratings** Damage 4/10 · Defence 8/10 · Assist 10/10

### Skill panels
**Slot 1 — Astral Chains** (id 1574, unlocks at `+0`)
  - **Ⅰ** at `+0` — Astral ChainsⅠ (安德莉亚技能描述)
    Cross Attack, deals 280% S-ATK damage to targets. Also links all allied ships and intercepts 50% of attack damage dealt to allies (effect is lost when Andrea transforms to Starcore Essence) for 2 rounds. Has a 50% chance to Starbind 1 random enemy, rendering them unable to act until the target is destroyed (this effect cannot be cleansed, isn't affected by immunity, and cannot be overridden by other crowd-control effects; up to 1 enemy can be Starbound at any time). Lastly, you recover 100 Accumulator.
  - **Ⅱ** at `+5` — Astral ChainsⅡ (安德莉亚技能描述)
    Cross Attack, deals 300% S-ATK damage to targets. Also links all allied ships and intercepts 60% of attack damage dealt to allies (effect is lost when Andrea transforms to Starcore Essence) for 2 rounds. Andrea is healed for 20% of the S-ATK damage dealt by linked allies. Has a 60% chance to Starbind 1 random enemy, rendering them unable to act until the target is destroyed (this effect cannot be cleansed, isn't affected by immunity, and cannot be overridden by other crowd-control effects; up to 1 enemy can be Starbound at any time). Lastly, you recover 100 Accumulator.
  - **Ⅲ** at `+9` — Astral ChainsⅢ (安德莉亚技能描述)
    Cross Attack, deals 320% S-ATK damage to targets. Also links all allied ships and intercepts 70% of attack damage dealt to allies (effect is lost when Andrea transforms to Starcore Essence) for 2 rounds. Andrea is healed for 30% of the S-ATK damage dealt by linked allies. Has a 75% chance to Starbind 1 random enemy, rendering them unable to act until the target is destroyed (this effect cannot be cleansed, isn't affected by immunity, and cannot be overridden by other crowd-control effects; up to 1 enemy can be Starbound at any time). All allies gain immunity to Freeze, Lock, Confuse, Forbidding Skill Use and Weaken for 2 rounds. Lastly, you recover 100 Accumulator.
  - **Ⅳ** at `+15` — Astral ChainsIV (安德莉亚技能描述)
    Cross Attack, deals 350% S-ATK damage to targets. Also links all allied ships and intercepts 80% of attack damage dealt to allies (effect is lost when Andrea transforms to Starcore Essence) for 2 rounds. Andrea is healed for 40% of the S-ATK damage dealt by linked allies. Has a 100% chance to Starbind 1 random enemy, rendering them unable to act until the target is destroyed (this effect cannot be cleansed, isn't affected by immunity, and cannot be overridden by other crowd-control effects; up to 1 enemy can be Starbound at any time). All allies gain immunity to Freeze, Lock, Confuse, Petrify, Icebound, Entangle, Forbidding Skill Use, Weaken and Instant Destruction for 2 rounds. Lastly, you recover 100 Accumulator.

**Slot 2 — Astral Refinement** (id 1575, unlocks at `+2`)
  - **Ⅰ** at `+2` — Astral RefinementⅠ (安德莉亚技能描述)
    (Takes effect at the start of battle) Andrea cannot take more than 60% of her max HP as damage from a single attack (including when intercepting damage for allies) (this does not work when Andrea's in Starcore Essence).
  - **Ⅱ** at `+7` — Astral RefinementⅡ (安德莉亚技能描述)
    (Takes effect at the start of battle) Andrea cannot take more than 50% of her max HP as damage from a single attack (including when intercepting damage for allies) (this does not work when Andrea's in Starcore Essence). 20% of the damage Andrea intercepts is transferred to the Starbound target.
  - **Ⅲ** at `+11` — Astral RefinementⅢ (安德莉亚技能描述)
    (Takes effect at the start of battle) Andrea cannot take more than 40% of her max HP as damage from a single attack (including when intercepting damage for allies) (this does not work when Andrea's in Starcore Essence). 30% of the damage Andrea intercepts is transferred to the Starbound target. Links with all allies at the start of battle for 2 rounds, intercepting 70% of any attack damage they take. Andrea is healed for 30% of the S-ATK damage dealt by linked allies.
  - **Ⅳ** at `+T3` — Astral RefinementIV (安德莉亚技能描述)
    (Takes effect at the start of battle) Andrea cannot take more than 30% of her max HP as damage from a single attack (including when intercepting damage for allies) (this does not work when Andrea's in Starcore Essence). 40% of the damage Andrea intercepts is transferred to the Starbound target. Links with all allies at the start of battle for 2 rounds, intercepting 80% of any attack damage they take. Andrea is healed for 40% of the S-ATK damage dealt by linked allies. Upon transforming to Starcore Essence, Andrea cleanses the debuffs and crowd-control effects (Freeze, Lock, Confuse, Petrify, Icebound, Entangle, Forbidding Skill Use and Weaken) of all allies, heals them for 100% of max HP, and boosts their damage by 30% for 5 rounds.

**Slot 3 — Astral Blessing** (id 1576, unlocks at `+3`)
  - **Ⅰ** at `+3` — Astral BlessingⅠ (安德莉亚技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +60% DEF: +30% S-DEF: +30% DMG Reduction (Absolute Value): +30%
  - **Ⅱ** at `+8` — Astral BlessingⅡ (安德莉亚技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +90% DEF: +60% S-DEF: +60% DMG Reduction (Absolute Value): +40%
  - **Ⅲ** at `+13` — Astral BlessingⅢ (安德莉亚技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +120% DEF: +90% S-DEF: +90% DMG Reduction (Absolute Value): +50%
  - **Ⅳ** at `+T` — Astral BlessingIV (安德莉亚技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +150% DEF: +120% S-DEF: +120% DMG Reduction (Absolute Value): +60%

**Slot 4 — Creation Making** (id 1577, unlocks at `+10`)
  - **Ⅰ** at `+10` — Creation MakingⅠ (安德莉亚技能描述)
    (Takes effect at the start of battle) When allies are targeted by Instant Destruction (including those that ignore Instant Destruction immunity), the effect is instead transferred to Andrea.
  - **Ⅱ** at `+T1` — Creation MakingⅡ (安德莉亚技能描述)
    (Takes effect at the start of battle) When allies are targeted by Instant Destruction (including those that ignore Instant Destruction immunity), the effect is instead transferred to Andrea, and she transforms into Starcore Essence (Instant Destruction effects do not transfer to Andrea while she's in Starcore Essence). Andrea transforms into Starcore Essence when taking lethal damage or is affected by an Instant Destruction effect (including those that ignore Instant Destruction immunity) (she is also cleared of all buffs except for Rebirth) (this effect may trigger up to 3 times per battle). Andrea returns to the battle with 100% of initial HP and 150 Accumulator if her Starcore Essence is not destroyed before her next action. Starcore Essence: Has HP equal to 150% of Andrea's initial HP and 100% of Andrea's other initial attributes (Andrea dies if the Starcore Essence is destroyed).
  - **Ⅲ** at `+T2` — Creation MakingⅢ (安德莉亚技能描述)
    (Takes effect at the start of battle) When allies are targeted by Instant Destruction (including those that ignore Instant Destruction immunity), the effect is instead transferred to Andrea, and she transforms into Starcore Essence (Instant Destruction effects do not transfer to Andrea while she's in Starcore Essence). Andrea transforms into Starcore Essence when taking lethal damage or is affected by an Instant Destruction effect (including those that ignore Instant Destruction immunity) (she is also cleared of all buffs except for Rebirth) (this effect may trigger up to 3 times per battle). Andrea returns to the battle with 100% of initial HP and 150 Accumulator if her Starcore Essence is not destroyed before her next action. Starcore Essence: Has HP equal to 200% of Andrea's initial HP, 100% of Andrea's other initial attributes, and 50% damage reduction (absolute value) (Andrea dies if the Starcore Essence is destroyed). All enemies are forced to attack the Starcore Essence (Unyielding's Taunt effect still takes precedence), and when the Starcore Essence is targeted by an attack, Andrea's allies are immune to attack damage (except for subsequent damage).
  - **Ⅳ** at `+T4` — Creation MakingIV (安德莉亚技能描述)
    (Takes effect at the start of battle) When allies are targeted by Instant Destruction (including those that ignore Instant Destruction immunity), the effect is instead transferred to Andrea, and she transforms into Starcore Essence (Instant Destruction effects do not transfer to Andrea while she's in Starcore Essence). Andrea transforms into Starcore Essence when taking lethal damage or is affected by an Instant Destruction effect (including those that ignore Instant Destruction immunity) (she is also cleared of all buffs except for Rebirth) (this effect may trigger up to 3 times per battle). Andrea returns to the battle with 100% of initial HP and 150 Accumulator if her Starcore Essence is not destroyed before her next action. Starcore Essence: Has HP equal to 300% of Andrea's initial HP, 100% of Andrea's other initial attributes, 80% damage reduction (absolute value), and 1,000% Crit ATK RED (Absolute Value) (Andrea dies if the Starcore Essence is destroyed). All enemies are forced to attack the Starcore Essence (Unyielding's Taunt effect still takes precedence), and when the Starcore Essence is targeted by an attack, Andrea's allies are immune to attack damage (except for subsequent damage). Andrea revives all dead allies to 100% of their initial HP and 150 Accumulator upon transforming into Starcore Essence (unaffected by forbidding revival effects).

### Augment cost (per step)
- `+1` — 5× Protector Chip · 100,000 money
- `+2` — 10× Protector Chip · 200,000 money
- `+3` — 21× Protector Chip · 300,000 money
- `+4` — 28× Protector Chip · 500,000 money
- `+5` — 35× Protector Chip · 800,000 money
- `+6` — 42× Protector Chip · 10× Pandora Power Core
- `+7` — 49× Protector Chip · 50× Pandora Power Core
- `+8` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Andrea Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Andrea Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Andrea Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Andrea Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Andrea Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Andrea Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 544 · Flora 芙兰
**Role** Protector · **Attack** physical · **Generation** latest
**Ratings** Damage 4/10 · Defence 8/10 · Assist 10/10

### Skill panels
**Slot 1 — Guardian Field** (id 1594, unlocks at `+0`)
  - **Ⅰ** at `+0` — Guardian FieldⅠ (芙兰技能描述，无实际意义)
    Vertical attack, deals 260% S-ATK damage to targets. Increases all allies' S-ATK by 40%, S-DEF by 40%, Penetration by 40% for 2 rounds and reduces damage taken by 40% for 2 rounds. All allies also gain 40% damage reflection for 2 rounds. For the next 2 rounds, before an ally acts, they first gain 15% damage (absolute value). Also applies Deflection Force Field to self, which resists 200% incoming horizontal and vertical damage from enemies' skill attacks for self and allied units behind and in horizontal range (effective when enemies attack units with the Deflection Force Field). The damage it can resist is related to Flora's ATK, S-ATK, and Accumulator when casting the skill. Lastly, you recover 100 Accumulator.
  - **Ⅱ** at `+7` — Guardian FieldⅡ (芙兰技能描述，无实际意义)
    Vertical attack, deals 280% S-ATK damage to targets. Increases all allies' S-ATK by 50%, S-DEF by 50%, Penetration by 50% for 2 rounds and reduces damage taken by 50% for 2 rounds. All allies also gain 50% damage reflection for 2 rounds. For the next 2 rounds, before an ally acts, they first gain 20% damage (absolute value) and whenever an ally takes damage, they recover 20% of max HP. Also applies Deflection Force Field to self, which resists 250% incoming horizontal and vertical damage from enemies' skill attacks for self and allied units behind and in horizontal range (effective when enemies attack units with the Deflection Force Field). The damage it can resist is related to Flora's ATK, S-ATK, and Accumulator when casting the skill. Lastly, you recover 100 Accumulator.
  - **Ⅲ** at `+13` — Guardian FieldⅢ (芙兰技能描述，无实际意义)
    Vertical attack, deals 300% S-ATK damage to targets. Increases all allies' S-ATK by 60%, S-DEF by 60%, Penetration by 60% for 2 rounds and reduces damage taken by 60% for 2 rounds. All allies also gain 60% damage reflection for 2 rounds. For the next 2 rounds, before an ally acts, they first gain 25% damage (absolute value) and whenever an ally takes damage, they absorb 40 of the attacker's Accumulator and recover 25% of max HP. Also applies Deflection Force Field to self, which resists 300% incoming horizontal and vertical damage from enemies' skill attacks for self and allied units behind and in horizontal range (effective when enemies attack units with the Deflection Force Field). The damage it can resist is related to Flora's ATK, S-ATK, and Accumulator when casting the skill. Lastly, you recover 100 Accumulator.
  - **Ⅳ** at `+15` — Guardian FieldIV (芙兰技能描述，无实际意义)
    Vertical attack, deals 340% S-ATK damage to targets. Increases all allies' S-ATK by 80%, S-DEF by 80%, Penetration by 80% for 2 rounds and reduces damage taken by 80% for 2 rounds. All allies also gain 80% damage reflection for 2 rounds. For the next 2 rounds, before an ally acts, they first gain 30% damage (absolute value) and whenever an ally takes damage, they absorb 60 of the attacker's Accumulator (ignores immunity and protection effects), increasing the damage the attacker takes by 40% and recover 30% of max HP. Also applies Deflection Force Field to self, which resists 350% incoming horizontal and vertical damage from enemies' skill attacks for self and allied units behind and in horizontal range (effective when enemies attack units with the Deflection Force Field). The damage it can resist is related to Flora's ATK, S-ATK, and Accumulator when casting the skill. Lastly, you recover 100 Accumulator.

**Slot 2 — Guardian Blessing** (id 1595, unlocks at `+3`)
  - **Ⅰ** at `+3` — Guardian BlessingⅠ (弗兰+7，触发回血)
    (Takes effect at the start of battle) Grants all allies immunity to Freeze, Lock, Confuse, Petrify, Icebound, Entangle and Forbidding Skill Use for 99 rounds.
  - **Ⅱ** at `+9` — Guardian BlessingⅡ (弗兰+13，触发回血)
    (Takes effect at the start of battle) Grants all allies immunity to Freeze, Lock, Confuse, Petrify, Icebound, Entangle and Forbidding Skill Use for 99 rounds. Applies a shield to all allies at the start of battle that blocks 1 attack, lasting 2 rounds.
  - **Ⅲ** at `+T1` — Guardian BlessingⅢ (弗兰+15，触发回血)
    (Takes effect at the start of battle) Grants all allies immunity to Freeze, Lock, Confuse, Petrify, Icebound, Entangle and Forbidding Skill Use for 99 rounds. Applies a shield to all allies at the start of battle that blocks 1 attack, lasting 2 rounds. Whenever an ally takes damage (triggers individually for each ally that takes damage), they have a 60% chance to gain an empowered Lock for 1 round that ignores all immunity and protection effects, and a 75% chance to Lock the enemy attacker for 1 round.
  - **Ⅳ** at `+T4` — Guardian BlessingIV (弗兰+17，触发回血)
    (Takes effect at the start of battle) Grants all allies immunity to Freeze, Lock, Confuse, Petrify, Icebound, Entangle and Forbidding Skill Use for 99 rounds. Applies a shield to all allies at the start of battle that blocks 1 attack, lasting 2 rounds. Whenever an ally takes damage (triggers individually for each ally that takes damage), they have a 60% chance to gain an empowered Lock for 1 round that ignores all immunity and protection effects, and a 75% chance to Lock the enemy attacker for 1 round. Flora revives all dead allies (unaffected by forbidding revival effects) with 100% of their initial HP and 100 Accumulator before her first 5 skill casts.

**Slot 3 — Guardian Will** (id 1596, unlocks at `+5`)
  - **Ⅰ** at `+5` — Guardian WillⅠ (芙兰技能描述，无实际意义)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +60% DEF: +30% S-DEF: +30%
  - **Ⅱ** at `+11` — Guardian WillⅡ (芙兰技能描述，无实际意义)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +90% DEF: +60% S-DEF: +60%
  - **Ⅲ** at `+T2` — Guardian WillⅢ (芙兰技能描述，无实际意义)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +120% DEF: +90% S-DEF: +90%
  - **Ⅳ** at `+T3` — Guardian WillIV (芙兰技能描述，无实际意义)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +150% DEF: +120% S-DEF: +120%

### Augment cost (per step)
- `+1` — 5× Protector Chip · 100,000 money
- `+2` — 10× Protector Chip · 200,000 money
- `+3` — 21× Protector Chip · 300,000 money
- `+4` — 28× Protector Chip · 500,000 money
- `+5` — 35× Protector Chip · 800,000 money
- `+6` — 42× Protector Chip · 10× Pandora Power Core
- `+7` — 49× Protector Chip · 50× Pandora Power Core
- `+8` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Flora Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Flora Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Flora Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Flora Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Flora Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Flora Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 555 · Selika 瑟莉卡
**Role** Protector · **Attack** physical · **Generation** latest
**Ratings** Damage 4/10 · Defence 8/10 · Assist 10/10

### Skill panels
**Slot 1 — Guardian's Will** (id 1674, unlocks at `+0`)
  - **Ⅰ** at `+0` — Guardian's WillⅠ (瑟莉卡技能描述)
    Cross Attack, deals 260% S-ATK damage to targets. There is a 50% chance to taunt, lasting for 2 rounds, forcing all enemies to target Selika as their attack (higher priority than the Unyielding and Starcore Essence's taunt effects). All allies gain an 80% reflect damage for 2 rounds. Lastly, recover 100 Accumulator.
  - **Ⅱ** at `+7` — Guardian's WillⅡ (瑟莉卡技能描述)
    Cross Attack, deals 280% S-ATK damage to targets. Has a 75% chance to taunt, lasting for 2 rounds, forcing all enemies to target Selika as their attack (priority is higher than the taunt effects of Unyielding and Starcore Essence's taunt effects).All allies gain 80% reflect damage for 2 rounds. When taking skill damage, there is a 30% chance to lock a random enemy for 2 rounds. Lastly, recover 100 Accumulator.
  - **Ⅲ** at `+13` — Guardian's WillⅢ (瑟莉卡技能描述)
    Cross Attack, deals 300% S-ATK damage to targets. There's a 100% chance to taunt, lasting for 2 rounds, forcing all enemies to target Selika as their attack (higher priority than the Unyielding and Starcore Essence's taunt effects)All allies gain 80% reflect damage for 2 rounds. When an ally takes skill damage, there is a 50% chance to lock a random enemy for 2 rounds. All allies are immunity to destroy for 99 rounds. Lastly, recover 100 Accumulator.
  - **Ⅳ** at `+15` — Guardian's WillⅣ (瑟莉卡技能描述)
    Cross Attack, deals 320% S-ATK damage to targets. There's a 100% chance to taunt, lasting for 2 rounds, forcing all enemies to target Selika as their attack (higher priority than the Unyielding and Starcore Essence's taunt effects)All allies gain 80% reflect damage for 2 rounds. When an ally takes skill damage, there is a 50% chance to lock a random enemy for 2 rounds. All allies are immune to destroy for 99 rounds. Lastly, recover 100 Accumulator.At the start of battle and upon revive or rebirth, launches Taunt for 2 rounds. When Selika is taunting, the final damage of all damage received by all allies is reduced by 55%.

**Slot 2 — Revive Domain** (id 1675, unlocks at `+3`)
  - **Ⅰ** at `+3` — Revive DomainⅠ (瑟莉卡技能描述)
    (Takes effect at the start of battle) (Takes effect at the start of battle) When dealing S-ATK damage, reсovers HP equal to 30% of the damage dealt, the part exceeding max HP is converted into Shield value (Shield cap is 150% of the afflicted target's Max HP).
  - **Ⅱ** at `+9` — Revive DomainⅡ (瑟莉卡技能描述)
    (Takes effect at the start of battle) (Takes effect at the start of battle) When dealing S-ATK damage, reсovers HP equal to 30% of the damage dealt, the part exceeding max HP is converted into Shield value (Shield cap is 150% of the afflicted target's Max HP). When all allies are hit by S-ATK damage, the triggered Lock can ignore the target's immunity and protection effects.
  - **Ⅲ** at `+T3` — Revive DomainⅢ (瑟莉卡技能描述)
    (Takes effect at the start of battle) (Takes effect at the start of battle) When dealing S-ATK damage, reсovers HP equal to 30% of the damage dealt, the part exceeding max HP is converted into Shield value (Shield cap is 150% of the afflicted target's Max HP). When all allies are hit by S-ATK damage, the triggered Lock can ignore the target's immunity and protection effects. At the start of BATTLE, each time Selika is revive or rebirth, and all allies making a kill, she grants a 70% chance for rebirth, prioritizing herself. If Selika already has reborn, a random ally without rebirth is chosen instead. The rebirth effect lasts for 99 rounds.
  - **Ⅳ** at `+T4` — Revive DomainⅣ (瑟莉卡技能描述)
    (Takes effect at the start of battle) (Takes effect at the start of battle) When dealing S-ATK damage, reсovers HP equal to 30% of the damage dealt, the part exceeding max HP is converted into Shield value (Shield cap is 150% of the afflicted target's Max HP). When all allies are hit by S-ATK damage, the triggered Lock can ignore the target's immunity and protection effects. At the start of BATTLE, each time Selika is revive or rebirth, and all allies making a kill, she grants a 70% chance for rebirth, prioritizing herself. If Selika already has reborn, a random ally without rebirth is chosen instead. The rebirth effect lasts for 99 rounds. Selika triggers "Revive" each time she is revive or rebirth: Cleanses all allies of crowd-control effects (Freeze, Lock, Confuse, Petrify, Icebound, Entangle, Forbidding Skill Use and Weaken); all allies heal for 80% of max HP;Revives all dead allies (unaffected by forbidding revival or Rebirth effects) with 100% of Max HP and Accumulator (revival effect can trigger 3 times).

**Slot 3 — Resolute Will** (id 1676, unlocks at `+5`)
  - **Ⅰ** at `+5` — Resolute WillⅠ (瑟莉卡技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +60% Block (Absolute Value): +30% DMG Reduction (Absolute Value): +15%
  - **Ⅱ** at `+11` — Resolute WillⅡ (瑟莉卡技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +90% Block (Absolute Value): +40% DMG Reduction (Absolute Value): +20%
  - **Ⅲ** at `+T1` — Resolute WillⅢ (瑟莉卡技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +120% Block (Absolute Value): +50% DMG Reduction (Absolute Value): +25%
  - **Ⅳ** at `+T2` — Resolute WillⅣ (瑟莉卡技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +150% Block (Absolute Value): +60% DMG Reduction (Absolute Value): +30%

### Augment cost (per step)
- `+1` — 5× Protector Chip · 100,000 money
- `+2` — 10× Protector Chip · 200,000 money
- `+3` — 21× Protector Chip · 300,000 money
- `+4` — 28× Protector Chip · 500,000 money
- `+5` — 35× Protector Chip · 800,000 money
- `+6` — 42× Protector Chip · 10× Pandora Power Core
- `+7` — 49× Protector Chip · 50× Pandora Power Core
- `+8` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Selika Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Selika Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Selika Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Selika Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Selika Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Selika Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 559 · Bonnie 波妮
**Role** Protector · **Attack** physical · **Generation** old
**Ratings** Damage 5/10 · Defence 10/10 · Assist 8/10

### Signature skill
- **Ⅰ** at `+0` — Quantum Bomb (波尼)
  Cross Attack, deals 350% S-ATK damage to targets. Lastly, you recover 100 Accumulator.

### Augment cost (per step)
- `+1` — 5× Protector Chip · 100,000 money
- `+2` — 10× Protector Chip · 200,000 money
- `+3` — 21× Protector Chip · 300,000 money
- `+4` — 28× Protector Chip · 500,000 money
- `+5` — 35× Protector Chip · 800,000 money
- `+6` — 42× Protector Chip · 10× Pandora Power Core
- `+7` — 49× Protector Chip · 50× Pandora Power Core
- `+8` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Bonnie's Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Bonnie's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Bonnie's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Bonnie's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Bonnie's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Bonnie's Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 560 · Valghar 瓦格哈尔
**Role** Protector · **Attack** physical · **Generation** latest
**Ratings** Damage 5/10 · Defence 10/10 · Assist 8/10

### Skill panels
**Slot 1 — Energy Blast** (id 1695, unlocks at `+0`)
  - **Ⅰ** at `+0` — Energy BlastⅠ (瓦格哈尔技能描述)
    Cross Attack, deals 280% S-ATK damage to targets. Grants self 15 stacks of [Defensive Energy] for 2 rounds, up to a maximum of 15 stacks. Increases own DMG Reduction (Absolute Value) by 40% for 2 rounds. All allies gain 30% S-ATK and S-DEF for 2 rounds. Lastly, recovers 100 Accumulator.[Defensive Energy] : Whenever any ally is targeted by a skill attack or normal attack that inflicts damage exceeding 10% of their Max HP, they will consume stacks to block the damage, with each stack blocking damage equal to 10% of Valghar's Max HP. In a single attack, each ally can consume up to 5 stacks to block attack damage, and any overflow damage after blocking is reduced by 20% (when multiple allies are attacked at the same time, priority is given to the ally with forward positions to block the damage).
  - **Ⅱ** at `+5` — Energy BlastⅡ (瓦格哈尔技能描述)
    Cross Attack, deals 300% S-ATK damage to targets. Grants self 15 stacks of [Defensive Energy] for 2 rounds, up to a maximum of 15 stacks. Increases own DMG Reduction (Absolute Value) by 50% for 2 rounds. All allies gain 40% S-ATK and S-DEF for 2 rounds. Lastly, recovers 100 Accumulator.[Defensive Energy] : Whenever any ally is targeted by a skill attack or normal attack that inflicts damage exceeding 10% of their Max HP, they will consume stacks to block the damage, with each stack blocking damage equal to 15% of Valghar's Max HP. In a single attack, each ally can consume up to 5 stacks to block attack damage, and any overflow damage after blocking is reduced by 30% (when multiple allies are attacked at the same time, priority is given to the ally with forward positions to block the damage).
  - **Ⅲ** at `+9` — Energy BlastⅢ (瓦格哈尔技能描述)
    Cross Attack, deals 320% S-ATK damage to targets. You gain 15 stacks of [Defensive Energy] for 2 rounds, up to a maximum of 15 stacks. There's a 50% chance to apply Binding to a random enemy, rendering it unable to act for 1 round (this effect cannot be cleansed, isn't affected by immunity) (it cannot be overridden by other control effects, and reapplication will not refresh the duration).Grants self 60% DMG Reduction (Absolute Value) for 2 rounds. Increases all allies' S-ATK and S-DEF by 50% for 2 rounds. Lastly, recovers 100 Accumulator. At the start of battle, increases own Max HP by 30% until the end.[Defensive Energy] : Whenever any ally is targeted by a skill attack or normal attack that inflicts damage exceeding 10% of their Max HP, they will consume stacks to block the damage, with each stack blocking damage equal to 20% of Valghar's Max HP. In a single attack, each ally can consume up to 5 stacks to block attack damage, and any overflow damage after blocking is reduced by 40% (when multiple allies are attacked at the same time, priority is given to the ally with forward positions to block the damage).
  - **Ⅳ** at `+15` — Energy BlastⅣ (瓦格哈尔技能描述)
    Cross Attack, deals 350% S-ATK damage to targets. You gain 15 stacks of [Defensive Energy] for 2 rounds, up to a maximum of 15 stacks. There's a 100% chance to apply Binding to a random enemy, rendering it unable to act for 1 round (this effect cannot be cleansed, isn't affected by immunity) (it cannot be overridden by other control effects, and reapplication will not refresh the duration). Gains 80% DMG Reduction (Absolute Value) for 2 rounds.All allies gain 75% S-ATK and S-DEF for 2 rounds. Recovers 100 Accumulator at the end. At the start of battle, increases own max HP by 40% until the end.At the start of battle and with each skill cast, applies Deflection Force Field to itself for 2 Rounds, which resists 420% incoming horizontal and vertical damage from enemies' S-ATK for itself and allied units behind it and in its horizontal range. The damage it can resist is related to ATK, S-ATK, and Accumulator when casting the skill.[Defensive Energy] : Whenever any ally is targeted by a skill attack or normal attack that inflicts damage exceeding 10% of their Max HP, they will consume stacks to block the damage, with each stack blocking damage equal to 20% of Valghar's Max HP. In a single attack, each ally can consume up to 5 stacks to block attack damage, and any overflow damage after blocking is reduced by 50% (when multiple allies are attacked at the same time, priority is given to the ally with forward positions to block the damage).

**Slot 2 — Defensive Energy** (id 1696, unlocks at `+2`)
  - **Ⅰ** at `+2` — Defensive EnergyⅠ (瓦格哈尔技能描述)
    (Takes effect at the start of battle) If at least 5 stacks of [[Defensive Energy] ] are present, when allies are targeted by Instant Destruction (including those that ignore Instant Destruction immunity), 5 stacks will be consumed to negate the instant destruction.
  - **Ⅱ** at `+7` — Defensive EnergyⅡ (瓦格哈尔技能描述)
    (Takes effect at the start of battle) If at least 5 stacks of [[Defensive Energy] ] are present, when allies are targeted by Instant Destruction (including those that ignore Instant Destruction immunity), 5 stacks will be consumed to negate the instant destruction. At the start of battle, immediately gains 15 stacks of [Defensive Energy].
  - **Ⅲ** at `+11` — Defensive EnergyⅢ (瓦格哈尔技能描述)
    (Takes effect at the start of battle) If at least 5 stacks of [[Defensive Energy] ] are present, when allies are targeted by Instant Destruction (including those that ignore Instant Destruction immunity), 5 stacks will be consumed to negate the instant destruction. At the start of battle, immediately gains 15 stacks of [Defensive Energy]. When Valghar is affected by a buff that prevents skill effects (such as the buff from Energy Block that prevents skill effects), [Defensive Energy] can still apply to our allies.
  - **Ⅳ** at `+T3` — Defensive EnergyⅣ (瓦格哈尔技能描述)
    (Takes effect at the start of battle) If at least 5 stacks of [[Defensive Energy] ] are present, when allies are targeted by Instant Destruction (including those that ignore Instant Destruction immunity), 5 stacks will be consumed to negate the instant destruction. At the start of battle, immediately gains 15 stacks of [Defensive Energy]. When Valghar is affected by a buff that prevents skill effects (such as the buff from Energy Block that prevents skill effects), [Defensive Energy] can still apply to our allies. Each stack of [Defensive Energy] can now block damage up to 35% of Valghar's max HP.

**Slot 3 — Sacred Armor** (id 1697, unlocks at `+3`)
  - **Ⅰ** at `+3` — Sacred ArmorⅠ (瓦格哈尔技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +60% DEF: +30% S-DEF: +30% DMG Reduction (Absolute Value): +30%
  - **Ⅱ** at `+8` — Sacred ArmorⅡ (瓦格哈尔技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +90% DEF: +60% S-DEF: +60% DMG Reduction (Absolute Value): +40%
  - **Ⅲ** at `+13` — Sacred ArmorⅢ (瓦格哈尔技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +120% DEF: +90% S-DEF: +90% DMG Reduction (Absolute Value): +50%
  - **Ⅳ** at `+T` — Sacred ArmorⅣ (瓦格哈尔技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +150% DEF: +120% S-DEF: +120% DMG Reduction (Absolute Value): +60%

**Slot 4 — Binding** (id 1698, unlocks at `+10`)
  - **Ⅰ** at `+10` — BindingⅠ (瓦格哈尔技能描述)
    (Takes effect at the start of battle) When all allied use their skills, they will deal additional damage based on the number of Valghar's [Defensive Energy] stacks, with each stack dealing an extra 5% of Valghar's Max HP as S-ATK damage.
  - **Ⅱ** at `+T1` — BindingⅡ (瓦格哈尔技能描述)
    (Takes effect at the start of battle) When all allied use their skills, they will deal additional damage based on the number of Valghar's [Defensive Energy] stacks, with each stack dealing an extra 5% of Valghar's Max HP as S-ATK damage. When the [Binding] ends, it deals damage equal to 25% of the total damage taken by the target during the effect's duration.
  - **Ⅲ** at `+T2` — BindingⅢ (瓦格哈尔技能描述)
    (Takes effect at the start of battle) When all allied use their skills, they will deal additional damage based on the number of Valghar's [Defensive Energy] stacks, with each stack dealing an extra 5% of Valghar's Max HP as S-ATK damage. When the [Binding] ends, it deals damage equal to 25% of the total damage taken by the target during the effect's duration. During the [Binding], the affected target takes 30% increased damage.
  - **Ⅳ** at `+T4` — BindingⅣ (瓦格哈尔技能描述)
    (Takes effect at the start of battle) When all allied use their skills, they will deal additional damage based on the number of Valghar's [Defensive Energy] stacks, with each stack dealing an extra 5% of Valghar's Max HP as S-ATK damage. When the [Binding] ends, it deals damage equal to 25% of the total damage taken by the target during the effect's duration. During the [Binding], the affected target takes 30% increased damage. When casting a skill, if the stacks of [Defensive Energy] are not less than 5, it will clears control effects from all friendly ships (Freeze, Lock, Confuse, Petrify, Icebound, Entangle, Forbidding Skill Use and Weaken), recovers 40% of max HP to all allies, and has a 50% chance to revive all dead allies (probability for each unit calculated separately) with HP and Accumulator equal to 100% of their initial status.

### Augment cost (per step)
- `+1` — 5× Protector Chip · 100,000 money
- `+2` — 10× Protector Chip · 200,000 money
- `+3` — 21× Protector Chip · 300,000 money
- `+4` — 28× Protector Chip · 500,000 money
- `+5` — 35× Protector Chip · 800,000 money
- `+6` — 42× Protector Chip · 10× Pandora Power Core
- `+7` — 49× Protector Chip · 50× Pandora Power Core
- `+8` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Valghar Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Valghar Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Valghar Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Valghar Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Valghar Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Valghar Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 572 · Sorrento 索伦托
**Role** Protector · **Attack** physical · **Generation** latest
**Ratings** Damage 5/10 · Defence 10/10 · Assist 8/10

### Skill panels
**Slot 1 — Heavy Quantum Cannon** (id 1768, unlocks at `+0`)
  - **Ⅰ** at `+0` — Heavy Quantum CannonⅠ (索伦托技能描述)
    Cross Attack, deals 260% S-ATK damage to targets. Applies [Buffer Barrier] to all allies for 2 rounds. Increases all allies' S-DEF and DEF by 50% for 2 rounds. Lastly, recovers 100 Accumulator. [Buffer Barrier]: During its duration, 20% of damage from normal attacks and skills is stored, with a storage limit of 150% of Sorrento's max HP (The storage limit of each hero with the barrier is calculated separately). The stored damage is settled with a delay: before each turn, 60% of the current stored value is settled as damage. At the end of the duration, the remaining stored value is settled immediately.
  - **Ⅱ** at `+7` — Heavy Quantum CannonⅡ (索伦托技能描述)
    Cross Attack, deals 280% S-ATK damage to targets. Applies [Buffer Barrier] to all allies for 2 rounds. Increases all allies' S-DEF and DEF by 70% for 2 rounds. Grants all allies Eye of True Sight for 2 rounds. Lastly, recovers 100 Accumulator. [Buffer Barrier]: During its duration, 30% of damage from normal attacks and skills is stored, with a storage limit of 200% of Sorrento's max HP (The storage limit of each hero with the barrier is calculated separately). The stored damage is settled with a delay: before each turn, 50% of the current stored value is settled as damage. At the end of the duration, the remaining stored value is settled immediately.
  - **Ⅲ** at `+9` — Heavy Quantum CannonⅢ (索伦托技能描述)
    Cross Attack, deals 300% S-ATK damage to targets. Applies [Buffer Barrier] to all allies for 2 rounds. Increases all allies' S-DEF and DEF by 90% for 2 rounds. Increases 30 Accumulator for all allies. Grants all allies Eye of True Sight for 2 rounds. Lastly, recovers 100 Accumulator. [Buffer Barrier]: During its duration, 40% of damage from normal attacks and skills is stored, with a storage limit of 250% of Sorrento's max HP (The storage limit of each hero with the barrier is calculated separately). The stored damage is settled with a delay: before each turn, 40% of the current stored value is settled as damage. At the end of the duration, the remaining stored value is settled immediately.
  - **Ⅳ** at `+15` — Heavy Quantum CannonIV (索伦托技能描述)
    Cross Attack, deals 330% S-ATK damage to targets. Applies [Buffer Barrier] to all allies for 2 rounds. Increases all allies' S-DEF and DEF by 120% for 2 rounds.Increases 50 Accumulator for all allies. Grants all allies Eye of True Sight for 2 rounds. Grants all allies immunity to Freeze, Lock, Confuse, Petrify, Icebound, Entangle, Forbidding Skill Use, and Weaken for 2 rounds. Lastly, recovers 100 Accumulator. [Buffer Barrier]: During its duration, 50% of damage from normal attacks and skills is stored, with a storage limit of 300% of Sorrento's max HP (The storage limit of each hero with the barrier is calculated separately). The stored damage is settled with a delay: before each turn, 30% of the current stored value is settled as damage. At the end of the duration, the remaining stored value is settled immediately.

**Slot 2 — Buffer Barrier** (id 1769, unlocks at `+3`)
  - **Ⅰ** at `+3` — Buffer BarrierⅠ (索伦托技能描述)
    (Takes effect at the start of battle) At the start of battle, all allies' max HP is increased by 30% until the end of the battle (disappears upon death).
  - **Ⅱ** at `+11` — Buffer BarrierⅡ (索伦托技能描述)
    (Takes effect at the start of battle) At the start of battle, all allies' max HP is increased by 30% until the end of the battle (disappears upon death). Each time all allies calculate the stored damage of the [Buffer Barrier], the calculated damage received is reduced by 20%.
  - **Ⅲ** at `+T3` — Buffer BarrierⅢ (索伦托技能描述)
    (Takes effect at the start of battle) At the start of battle, all allies' max HP is increased by 30% until the end of the battle (disappears upon death). Each time all allies calculate the stored damage of the [Buffer Barrier], the calculated damage received is reduced by 20%. If a kill is made during the duration of [Buffer Barrier], 50% of the stored damage will be cleared.
  - **Ⅳ** at `+T4` — Buffer BarrierIV (索伦托技能描述)
    (Takes effect at the start of battle) At the start of battle, all allies' max HP is increased by 30% until the end of the battle (disappears upon death). Each time all allies calculate the stored damage of the [Buffer Barrier], the calculated damage received is reduced by 20%. If a kill is made during the duration of [Buffer Barrier], 50% of the stored damage will be cleared. At the start of battle, applies [Buffer Barrier] to all allies, lasting 2 rounds.

**Slot 3 — Armed Reinforcement** (id 1770, unlocks at `+5`)
  - **Ⅰ** at `+5` — Armed ReinforcementⅠ (索伦托技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +60% DEF: +30% S-DEF: +30%
  - **Ⅱ** at `+13` — Armed ReinforcementⅡ (索伦托技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +90% DEF: +60% S-DEF: +60%
  - **Ⅲ** at `+T` — Armed ReinforcementⅢ (索伦托技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +120% DEF: +90% S-DEF: +90%
  - **Ⅳ** at `+T2` — Armed ReinforcementIV (索伦托技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +150% DEF: +120% S-DEF: +120%

### Augment cost (per step)
- `+1` — 5× Protector Chip · 100,000 money
- `+2` — 10× Protector Chip · 200,000 money
- `+3` — 21× Protector Chip · 300,000 money
- `+4` — 28× Protector Chip · 500,000 money
- `+5` — 35× Protector Chip · 800,000 money
- `+6` — 42× Protector Chip · 10× Pandora Power Core
- `+7` — 49× Protector Chip · 50× Pandora Power Core
- `+8` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Sorrento Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Sorrento Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Sorrento Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Sorrento Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Sorrento Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Sorrento Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 576 · Eldran 艾尔德兰
**Role** Protector · **Attack** physical · **Generation** latest
**Ratings** Damage 7/10 · Defence 9/10 · Assist 8/10

### Skill panels
**Slot 1 — Vine Binding** (id 1791, unlocks at `+0`)
  - **Ⅰ** at `+0` — Vine BindingⅠ (古木+0)
    Cross Attack, deals 280% S-ATK damage to targets. Has a 100% chance to Entangle a random enemy for 2 rounds, preventing them from acting. Lastly, recovers 100 Accumulator.
  - **Ⅱ** at `+5` — Vine BindingⅡ (古木+5)
    Cross Attack, deals 300% S-ATK damage to targets. Has a 100% chance to Entangle a random enemy for 2 rounds, preventing them from acting. Grants all allies immunity to Freeze, Lock, Confuse, Petrify, Icebound, Entangle, Forbidding Skill Use, and Weaken, as well as immunity to instant destruction, for 2 rounds. Lastly, recovers 100 Accumulator.
  - **Ⅲ** at `+9` — Vine BindingⅢ (古木+9)
    Cross Attack, deals 320% S-ATK damage to targets. Other friendly ships recover HP equal to 40% of their max HP when attacked, lasting for 99 rounds. Has a 100% chance to Entangle a random enemy for 2 rounds, preventing them from acting. Grants all allies immunity to Freeze, Lock, Confuse, Petrify, Icebound, Entangle, Forbidding Skill Use, and Weaken, as well as immunity to instant destruction, lasting for 2 rounds. Lastly, recovers 100 Accumulator.
  - **Ⅳ** at `+15` — Vine BindingIV (古木+10)
    Cross Attack, deals 350% S-ATK damage to targets. Other friendly ships recover HP equal to 40% of their max HP when attacked, and all allies take 70% less damage. Has a 100% chance to Entangle a random enemy for 2 rounds, preventing them from acting. Grants all allies immunity to Freeze, Lock, Confuse, Petrify, Icebound, Entangle, Forbidding Skill Use, and Weaken, as well as immunity to instant destruction, for 2 rounds. Lastly, recovers 100 Accumulator.

**Slot 2 — Tree Shadow's Protection** (id 1792, unlocks at `+7`)
  - **Ⅰ** at `+7` — Tree Shadow's ProtectionⅠ (被动技能描述)
    (Takes effect at the start of battle) When our ships deal skill damage, they recover HP equal to 30% of the damage dealt, and all friendly ships' damage is increased by 50%.
  - **Ⅱ** at `+15` — Tree Shadow's ProtectionⅡ (被动技能描述)
    (Takes effect at the start of battle) The hero cannot take more than 40% of his max HP as damage from a single attack. When a friendly ship deals skill damage, it recovers HP equal to 30% of the damage dealt, and all friendly ships' damage dealt is increased by 50%. The applied entangle effect is empowered, ignoring all immunity and protection effects.
  - **Ⅲ** at `+T1` — Tree Shadow's ProtectionⅢ (被动技能描述)
    (Takes effect at the start of battle) The hero cannot take more than 30% of his max HP as damage from a single attack. When a friendly ship deals skill damage, it recovers HP equal to 30% of the damage dealt, and all friendly ships' damage dealt is increased by 50%. Upon death, entangles a random enemy for 1 round. The applied entangle effect is empowered, ignoring all immunity and protection effects.
  - **Ⅳ** at `+T3` — Tree Shadow's ProtectionIV (被动技能描述)
    (Takes effect at the start of battle) The hero cannot take more than 20% of his max HP as damage from a single attack. When a friendly ship deals skill damage, it recovers HP equal to 40% of the damage dealt, and all friendly ships' damage dealt is increased by 60%. Upon death, entangles a random enemy for 1 round. At the start of battle, randomly selects an enemy to entangle for 1 round. The applied entangle effect is empowered, ignoring all immunity and protection effects, and cannot be cleansed.

**Slot 3 — Tree Shadow Buff** (id 1794, unlocks at `+3`)
  - **Ⅰ** at `+3` — Tree Shadow BuffⅠ (被动技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +60% DEF: +30% S-DEF: +30% DMG Reduction (Absolute Value): +30%
  - **Ⅱ** at `+8` — Tree Shadow BuffⅡ (被动技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +90% DEF: +60% S-DEF: +60% DMG Reduction (Absolute Value): +40%
  - **Ⅲ** at `+13` — Tree Shadow BuffⅢ (被动技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +120% DEF: +90% S-DEF: +90% DMG Reduction (Absolute Value): +50%
  - **Ⅳ** at `+T` — Tree Shadow BuffIV (被动技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +150% DEF: +120% S-DEF: +120% DMG Reduction (Absolute Value): +60%

**Slot 4 — Withered Vine Curse** (id 1793, unlocks at `+10`)
  - **Ⅰ** at `+10` — Withered Vine CurseⅠ (古木死亡触发技能)
    (Takes effect at the start of battle) Entangled enemies gain the [Withered Vine Curse] status. If they die within 2 rounds, the following effects are triggered: cleanse all allies of abnormal statuses and crowd-control effects (Freeze, Lock, Confuse, Petrify, Icebound, Entangle, Forbidding Skill Use and Weaken), and heal all allies for 50% of their max HP.
  - **Ⅱ** at `+T1` — Withered Vine CurseⅡ (被缠绕单位死亡触发)
    (Takes effect at the start of battle) Entangled enemies gain the [Withered Vine Curse] status. If they die within 2 rounds, the following effects occur: Upon revival, they will be Entangled for 2 rounds, all allies will be cleansed of abnormal statuses and crowd-control effects (Freeze, Lock, Confuse, Petrify, Icebound, Entangle, Forbidding Skill Use and Weaken), and all allies will be healed for 100% of their max HP.
  - **Ⅲ** at `+T2` — Withered Vine CurseⅢ (被缠绕单位死亡触发)
    (Takes effect at the start of battle) Enemies affected by Entangle gain the [Withered Vine Curse] status. If they die within 2 rounds, the following effects occur: Upon revival, they will be Entangled for 2 rounds. All allies will be cleansed of abnormal statuses and crowd-control effects (Freeze, Lock, Confuse, Petrify, Icebound, Entangle, Forbidding Skill Use and Weaken), and all allies will be healed for 100% of their max HP for 1 round. Eldran's Entangle will prioritize ships that are not already Entangled.
  - **Ⅳ** at `+T4` — Withered Vine CurseIV (被缠绕单位死亡触发)
    (Takes effect at the start of battle) Enemies affected by Entangle gain the [Withered Vine Curse] status. If they die within 2 rounds, the following effects occur: Upon revival, they will be Entangled for 2 rounds. All allies will be cleansed of abnormal statuses and crowd-control effects (Freeze, Lock, Confuse, Petrify, Icebound, Entangle, Forbidding Skill Use and Weaken), and all allies will be healed for 100% of their max HP for 1 round. Additionally, the Entangle effect will be transferred to 2 random enemies for 1 round. Eldran's Entangle will prioritize ships that are not already Entangled.

### Augment cost (per step)
- `+1` — 5× Protector Chip · 100,000 money
- `+2` — 10× Protector Chip · 200,000 money
- `+3` — 21× Protector Chip · 300,000 money
- `+4` — 28× Protector Chip · 500,000 money
- `+5` — 35× Protector Chip · 800,000 money
- `+6` — 42× Protector Chip · 10× Pandora Power Core
- `+7` — 49× Protector Chip · 50× Pandora Power Core
- `+8` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Eldran Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Eldran Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Eldran Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Eldran Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Eldran Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Eldran Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 584 · Interstellar Chef: Porter 星际大厨：波特
**Role** Protector · **Attack** physical · **Generation** latest
**Ratings** Damage 4/10 · Defence 8/10 · Assist 10/10

### Skill panels
**Slot 1 — Meteor Stew** (id 1821, unlocks at `+0`)
  - **Ⅰ** at `+0` — Meteor StewⅠ (星际大厨：波特+0)
    Cross Attack, deals 280% S-ATK damage to targets. Applies a shield to all allies, reducing any damage taken by 60% for 2 rounds. Lastly, recovers 100 Accumulator.
  - **Ⅱ** at `+7` — Meteor StewⅡ (星际大厨：波特+7)
    Cross Attack, deals 300% S-ATK damage to targets. Applies a shield to all allies, reducing any damage taken by 60% for 2 rounds. When using the skill, increases DEF and S-DEF by 100% for all allies with HP below 70%. Lastly, recovers 100 Accumulator.
  - **Ⅲ** at `+14` — Meteor StewⅢ (星际大厨：波特+15)
    Cross Attack, deals 320% S-ATK damage to targets. Applies a shield to all allies, reducing any damage taken by 75% for 2 rounds. Increases all allies' damage by 60%. When using the skill, increases DEF and S-DEF by 200% for all allies with HP below 70%, and grants a Rebirth effect to those with less than 30% HP, allowing them to revive immediately upon death with 100% of their initial HP and Accumulator, lasting for 99 rounds. Lastly, recovers 100 Accumulator.
  - **Ⅳ** at `+T3` — Meteor StewIV (星际大厨：波特+18)
    Cross Attack, deals 350% S-ATK damage to targets. Applies a shield to all allies, reducing any damage taken by 90% for 2 rounds. Increases all allies' damage by 80%. When using the skill, increases DEF and S-DEF by 300% for all allies with HP below 90%, and grants a Rebirth effect to those with less than 50% HP, allowing them to revive immediately upon death with 100% of their initial HP and Accumulator, lasting for 99 rounds. Lastly, recovers 100 Accumulator. Porter can revive all allies (unaffected by forbidding revival effects) with 100% of their initial HP and Accumulator for the first 5 times he uses a skill.

**Slot 2 — Fresh Green Salad** (id 1822, unlocks at `+2`)
  - **Ⅰ** at `+2` — Fresh Green SaladⅠ (星际大厨：波特+3)
    (Takes effect at the start of battle) Grants all allies immunity to Freeze, Lock, Confuse, Petrify, Icebound, Entangle, and Forbidding Skill Use for 99 rounds.
  - **Ⅱ** at `+10` — Fresh Green SaladⅡ (星际大厨：波特+9)
    (Takes effect at the start of battle) Grants all allies immunity to Freeze, Lock, Confuse, Petrify, Icebound, Entangle, and Forbidding Skill Use for 99 rounds. At the start of battle and each time revived or reborn, all allies gain the effect: If they are under a control effect, there is a 30% chance to clear the control effect before acting, lasting for 2 rounds.
  - **Ⅲ** at `+T1` — Fresh Green SaladⅢ (星际大厨：波特+17)
    (Takes effect at the start of battle) Grants all allies immunity to Freeze, Lock, Confuse, Petrify, Icebound, Entangle, and Forbidding Skill Use for 99 rounds. At the start of battle and each time revived or reborn, all allies gain the effect: If they are under a control effect, there is a 30% chance to clear the control effect before acting, lasting for 2 rounds. When all allies use skill attacks on enemies under these control (Lock, Confuse, Freeze, Forbidding Skill Use), there is a 20% chance to trigger the following effects. (probability for each effect is calculated independently, and multiple effects can be triggered.) - Heals all allies for 80% of their HP. - All allies gain: Immunity to one lethal attack, lasting for 2 rounds. - The ship that triggers this effect gains a Rebirth effect, reviving immediately upon death with 100% of its initial HP and 150 Accumulator.
  - **Ⅳ** at `+T4` — Fresh Green SaladIV (星际大厨：波特+20)
    (Takes effect at the start of battle) Grants all allies immunity to Freeze, Lock, Confuse, Petrify, Icebound, Entangle, and Forbidding Skill Use for 99 rounds. At the start of battle and each time revived or reborn, all allies gain the effect: If they are under a control effect, there is a 50% chance to clear the control effect before acting, lasting for 2 rounds. When all allies use skill attacks on enemies under these control (Lock, Confuse, Freeze, Forbidding Skill Use), there is a 30% chance to trigger the following effects. (probability for each effect is calculated independently, and multiple effects can be triggered.) - Heals all allies for 100% of their HP. - All allies gain: Immunity to one lethal attack, lasting for 2 rounds. - The ship that triggers this effect gains a Rebirth effect, reviving immediately upon death with 100% of its initial HP and 150 Accumulator. (unaffected by forbidding revival effects) - Skill attacks instantly kill all enemies in a straight line. (Ignores immunity to lethal and instant destruction effects)

**Slot 3 — Inspiring Snack** (id 1823, unlocks at `+5`)
  - **Ⅰ** at `+5` — Inspiring SnackⅠ (星际大厨：波特+5)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +60% DEF: +30% S-DEF: +30%
  - **Ⅱ** at `+11` — Inspiring SnackⅡ (星际大厨：波特+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +90% DEF: +60% S-DEF: +60%
  - **Ⅲ** at `+T` — Inspiring SnackⅢ (星际大厨：波特+16)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +120% DEF: +90% S-DEF: +90%
  - **Ⅳ** at `+T2` — Inspiring SnackIV (星际大厨：波特+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +150% DEF: +120% S-DEF: +120%

### Augment cost (per step)
- `+1` — 5× Protector Chip · 100,000 money
- `+2` — 10× Protector Chip · 200,000 money
- `+3` — 21× Protector Chip · 300,000 money
- `+4` — 28× Protector Chip · 500,000 money
- `+5` — 35× Protector Chip · 800,000 money
- `+6` — 42× Protector Chip · 10× Pandora Power Core
- `+7` — 49× Protector Chip · 50× Pandora Power Core
- `+8` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Interstellar Chef: Porter's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Interstellar Chef: Porter's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Interstellar Chef: Porter's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Interstellar Chef: Porter's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Interstellar Chef: Porter's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Interstellar Chef: Porter's Ship Part · 100× Alien Essence · 100× Transcendence Core

---

## 591 · Amber 琥珀
**Role** Protector · **Attack** physical · **Generation** old
**Ratings** Damage 5/10 · Defence 10/10 · Assist 8/10

### Signature skill
- **Ⅰ** at `+0` — Seismic Wave (琥珀+0)
  Cross Attack, deals 200% S-ATK damage to targets. Lastly, you recover 100 Accumulator.

### Augment cost (per step)
- `+1` — 5× Protector Chip · 100,000 money
- `+2` — 10× Protector Chip · 200,000 money
- `+3` — 21× Protector Chip · 300,000 money
- `+4` — 28× Protector Chip · 500,000 money
- `+5` — 35× Protector Chip · 800,000 money
- `+6` — 42× Protector Chip · 10× Pandora Power Core
- `+7` — 49× Protector Chip · 50× Pandora Power Core
- `+8` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Red Envelope Refresh Coupon · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Red Envelope Refresh Coupon · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Red Envelope Refresh Coupon · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Red Envelope Refresh Coupon · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Red Envelope Refresh Coupon · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Red Envelope Refresh Coupon · 100× Alien Essence · 100× Transcendence Core

---

## 594 · Kaelmor 凯尔莫尔
**Role** Protector · **Attack** physical · **Generation** latest
**Ratings** Damage 5/10 · Defence 10/10 · Assist 8/10

### Skill panels
**Slot 1 — Eco Barrier** (id 1859, unlocks at `+0`)
  - **Ⅰ** at `+0` — Eco BarrierⅠ (凯尔莫尔+0)
    Cross Attack, deals 280% S-ATK damage to targets, with a 25% chance to Taunt for 2 rounds. Makes all allies immune to freezing, locking, confusion, petrification, freezing, entangling, instant destruction, prohibiting the use of skills and weakening, lasting for 99 rounds. Finally restore 100 points of energy.
  - **Ⅱ** at `+6` — Eco BarrierⅡ (凯尔莫尔+6)
    Cross Attack, deals 300% S-ATK damage to targets, with a 50% chance to Taunt for 2 rounds. Increases all allies' S-DEF by 30% and makes all allies immune to freezing, locking, confusion, petrification, freezing, entangling, instant destruction, prohibiting the use of skills and weakening, lasting for 99 rounds. Finally restore 100 points of energy.
  - **Ⅲ** at `+10` — Eco BarrierⅢ (凯尔莫尔+10)
    Cross Attack, deals 320% S-ATK damage to targets with a 75% chance to Taunt for 2 rounds. Increases all allies' S-DEF by 50% and makes all allies immune to freezing, locking, confusion, petrification, freezing, entangling, instant destruction, prohibiting the use of skills and weakening, lasting for 99 rounds. All allies gain a Shield equal to 500% of your S-ATK for 2 rounds. Lastly, you recover 100 Accumulator.
  - **Ⅳ** at `+15` — Eco BarrierIV (凯尔莫尔+15)
    Cross Attack, deals 360% S-ATK damage to targets and has a 100% chance to Taunt for 2 rounds. Increases all allies' S-DEF by 75% and makes all allies immune to freezing, locking, confusion, petrification, freezing, entangling, instant destruction, prohibiting the use of skills and weakening, lasting for 99 rounds. All allies gain a Shield equal to 800% of your S-ATK for 2 rounds. There is a 70% chance to gain Rebirth, reviving immediately upon death with 100% HP and Accumulator as at the start of the battle. Lastly, you recover 100 Accumulator.

**Slot 2 — Gene Resonance** (id 1856, unlocks at `+2`)
  - **Ⅰ** at `+2` — Gene ResonanceⅠ (凯尔莫尔+2)
    (Takes effect at the start of battle) At the start of battle and each time a unit is resurrect rebirthed, Taunt is activated for 2 rounds.
  - **Ⅱ** at `+9` — Gene ResonanceⅡ (凯尔莫尔+9)
    (Takes effect at the start of battle) At the start of battle and each time a unit is resurrect rebirthed, Taunt is activated for 2 rounds. At the start of battle, all allies' Max HP is increased by 60%, but damage taken is increased by 20%, lasting until the end of battle (disappears on death).
  - **Ⅲ** at `+T` — Gene ResonanceⅢ (凯尔莫尔+16)
    (Takes effect at the start of battle) At the start of battle and each time a unit is resurrect rebirthed, Taunt is activated for 2 rounds. At the start of battle, all allies' max HP is increased by 80%, but damage taken is increased by 25% until the end of battle (disappears on death). When any ally uses a skill, if Kaelmor was dead, there is a 25% chance to revive Kaelmor with 100% max HP and Accumulator. (which isn't affected by forbidding revival effects)
  - **Ⅳ** at `+T4` — Gene ResonanceIV (凯尔莫尔+20)
    (Takes effect at the start of battle) At the start of battle and each time a unit is resurrect rebirthed, Taunt is activated for 2 rounds. At the start of battle, all allies' max HP is increased by 120%, but damage taken is increased by 30% until the end of battle (disappears on death). When any ally uses a skill, if Kaelmor was dead, there is a 25% chance to revive Kaelmor with 100% max HP and Accumulator. (which isn't affected by forbidding revival effects) Each time Kaelmor is rebirthed or revived, [Gene Resonance] will be triggered: all allies recover 100% max HP and Accumulator, purifies all allies' control effects, and randomly revive 2 dead allies with 100% max HP and Accumulator (not affected by revive prohibition).

**Slot 3 — Gene Enhancement** (id 1857, unlocks at `+4`)
  - **Ⅰ** at `+4` — Gene EnhancementⅠ (凯尔莫尔+4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +60% DEF: +30% S-DEF: +30% DMG Reduction (Absolute Value): +30%
  - **Ⅱ** at `+10` — Gene EnhancementⅡ (凯尔莫尔+10)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +90% DEF: +60% S-DEF: +60% DMG Reduction (Absolute Value): +40%
  - **Ⅲ** at `+14` — Gene EnhancementⅢ (凯尔莫尔+14)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +120% DEF: +90% S-DEF: +90% DMG Reduction (Absolute Value): +50%
  - **Ⅳ** at `+T2` — Gene EnhancementIV (凯尔莫尔+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +150% DEF: +120% S-DEF: +120% DMG Reduction (Absolute Value): +60%

**Slot 4 — Gene Mutation** (id 1858, unlocks at `+3`)
  - **Ⅰ** at `+3` — Gene MutationⅠ (凯尔莫尔+3)
    (Takes effect at the start of battle) While you are Taunting, all allies take 40% less final damage.
  - **Ⅱ** at `+13` — Gene MutationⅡ (凯尔莫尔+13)
    (Takes effect at the start of battle) When Taunting, all allies take 40% less final damage. When attacked by a Ranger, Striker, or Destroyer, gain the effect: damage taken from a single attack does not exceed 60% of Max HP for 1 round. (Effect activates after taking damage)
  - **Ⅲ** at `+T1` — Gene MutationⅢ (凯尔莫尔+17)
    (Takes effect at the start of battle) When Taunting, all allies take 60% less final damage. When attacked by Rangers, Strikers, or Destroyers, gain the effect: damage taken from a single attack does not exceed 40% of Max HP for 1 round. (Effect activates after taking damage) S-ATK deals additional damage to all enemy Flagships, Rovers, and Protectors, equal to 60% of the their maximum HP. When enemy Flagships, Rovers, or Protectors are revived after death, they will lose 50% of Max HP and their Accumulator is reset.
  - **Ⅳ** at `+T3` — Gene MutationIV (凯尔莫尔+19)
    (Takes effect at the start of battle) When Taunting, all allies take 60% less final damage. When attacked by Rangers, Strikers, or Destroyers, gain the effect: damage taken from a single attack does not exceed 25% of Max HP for 1 round. (Effect activates after taking damage) S-ATK deals additional damage to all enemy Flagships, Rovers, and Protectors, equal to 60% of the their maximum HP. When enemy Flagships, Rovers, or Protectors are revived after death, they will lose 50% of Max HP and their Accumulator is reset. Upon death, other allies gain his skill effect for 1 round.

### Augment cost (per step)
- `+1` — 5× Protector Chip · 100,000 money
- `+2` — 10× Protector Chip · 200,000 money
- `+3` — 21× Protector Chip · 300,000 money
- `+4` — 28× Protector Chip · 500,000 money
- `+5` — 35× Protector Chip · 800,000 money
- `+6` — 42× Protector Chip · 10× Pandora Power Core
- `+7` — 49× Protector Chip · 50× Pandora Power Core
- `+8` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Kaelmor's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Kaelmor's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Kaelmor's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Kaelmor's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Kaelmor's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Kaelmor's Ship Part · 100× Alien Essence · 100× Transcendence Core

---

## 598 · Knightley 奈特莉
**Role** Protector · **Attack** physical · **Generation** latest
**Ratings** Damage 7/10 · Defence 10/10 · Assist 8/10

### Skill panels
**Slot 1 — Liberation Oath** (id 1868, unlocks at `+0`)
  - **Ⅰ** at `+0` — Liberation OathⅠ (奈特莉+0)
    Cross Attack, deals 280% S-ATK damage to targets. Links with all allies ships, taking 50% of the allies damage(shared damage cannot exceed 50% of own max HP), and reduces damage taken by all allies by 50% for 2 rounds. Recovers 40 Accumulator for all allies except self, and finally she recovers herself 100 Accumulator.
  - **Ⅱ** at `+7` — Liberation OathⅡ (奈特莉+3(被动))
    Cross Attack, deals 300% S-ATK damage to targets. Links with all allies ships, taking 70% of the allies damage(shared damage cannot exceed 40% of own max HP), and reduces damage taken by all allies by 70% for 2 rounds. All allies gain Eye of True Sight, lasts until Battle Over. Recovers 50 Accumulator for all allies except self, and finally she recovers herself 100 Accumulator.
  - **Ⅲ** at `+15` — Liberation OathⅢ (奈特莉+7)
    Cross Attack, deals 320% S-ATK damage to targets. Links with all allies ships, taking 80% of the allies damage(shared damage cannot exceed 35% of own max HP), and reduces damage taken by all allies by 80% for 2 rounds. All allies gain Eye of True Sight, lasts until Battle Over. When the linked allies ships release skills, Knightley restores 30% of her max HP. Recovers 60 Accumulator for all allies except self, and finally she recovers herself 100 Accumulator.
  - **Ⅳ** at `+T3` — Liberation OathIV (奈特莉+9(被动))
    Cross Attack, deals 360% S-ATK damage to targets. Links with all allies ships, taking 90% of the allies damage(shared damage cannot exceed 30% of own max HP), and reduces damage taken by all allies by 90% for 2 rounds. All allies gain Eye of True Sight, lasts until Battle Over. When the linked allies ships release skills, Knightley restores 30% of her max HP and gains Liberation Oath, lasting for 2 rounds. Recovers 80 Accumulator for all allies except self, and finally she recovers herself 100 Accumulator. <Liberation Oath>: When affected by Lock, Freeze, Confuse, or Entangle, clears the corresponding debuff and immediately acts once. (Cannot be triggered if the ship is under other control effects).

**Slot 2 — Protector's Embrace** (id 1869, unlocks at `+3`)
  - **Ⅰ** at `+3` — Protector's EmbraceⅠ (奈特莉+3)
    (Takes effect at the start of battle) If current HP is above 50% of Max HP, casting a skill will consume 30% of current HP, cleans all allies' abnormal statuses and crowd-control effects. If current HP is below 50% of Max HP, casting a skill grants a rebirth, reviving immediately upon death with 100% HP and Accumulator as at the start of the battle, lasting for 99 rounds.
  - **Ⅱ** at `+9` — Protector's EmbraceⅡ (奈特莉+9)
    (Takes effect at the start of battle) If current HP is above 50% of Max HP, casting a skill will consume 30% of current HP, cleans all allies' abnormal statuses and crowd-control effects, and restore 60% of Max HP to all allies except herself. If current HP is below 50% of Max HP, casting a skill grants a rebirth, reviving immediately upon death with 100% HP and Accumulator as at the start of the battle, lasting for 99 rounds, and she cannot take more than 40% of max HP as damage from a single attack, lasting for 1 round.
  - **Ⅲ** at `+T1` — Protector's EmbraceⅢ (奈特莉+17)
    (Takes effect at the start of battle) If current HP is above 50% of Max HP, casting a skill will consume 30% of current HP, cleans all allies' abnormal statuses and crowd-control effects, and restore 100% of Max HP to all allies except herself. If current HP is below 50% of Max HP, casting a skill grants a rebirth, reviving immediately upon death with 100% HP and Accumulator as at the start of the battle, lasting for 99 rounds, and she cannot take more than 40% of max HP as damage from a single attack, lasting for 1 round. When any ally dies, she restore 100% of Max HP.
  - **Ⅳ** at `+T4` — Protector's EmbraceIV (奈特莉+20)
    (Takes effect at the start of battle) If current HP is above 50% of Max HP, casting a skill will consume 30% of current HP, cleans all allies' abnormal statuses and crowd-control effects, and restore 100% of Max HP to all allies except herself. If current HP is below 50% of Max HP, casting a skill grants a rebirth, reviving immediately upon death with 100% HP and Accumulator as at the start of the battle (unaffected by forbidding revival effects), lasting for 99 rounds, and she cannot take more than 25% of max HP as damage from a single attack, lasting for 1 round. When any ally dies, she restores 100% of Max HP, and her next skill cast will randomly revive 1 dead ally (unaffected by forbidding revival effects), revive his/her with 100% max HP and Accumulator. When an ally takes lethal damage, there is a 100% chance that Knightley will block this lethal damage for the ally, but will lose 70% of current HP (can only take effect once per battle).

**Slot 3 — Noble Conviction** (id 1870, unlocks at `+5`)
  - **Ⅰ** at `+5` — Noble ConvictionⅠ (奈特莉+5)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +60% DEF: +30% S-DEF: +30%
  - **Ⅱ** at `+11` — Noble ConvictionⅡ (奈特莉+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +90% DEF: +60% S-DEF: +60%
  - **Ⅲ** at `+T` — Noble ConvictionⅢ (奈特莉+16)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +120% DEF: +90% S-DEF: +90%
  - **Ⅳ** at `+T2` — Noble ConvictionIV (奈特莉+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +150% DEF: +120% S-DEF: +120%

### Augment cost (per step)
- `+1` — 5× Protector Chip · 100,000 money
- `+2` — 10× Protector Chip · 200,000 money
- `+3` — 21× Protector Chip · 300,000 money
- `+4` — 28× Protector Chip · 500,000 money
- `+5` — 35× Protector Chip · 800,000 money
- `+6` — 42× Protector Chip · 10× Pandora Power Core
- `+7` — 49× Protector Chip · 50× Pandora Power Core
- `+8` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Knightley's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Knightley's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Knightley's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Knightley's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Knightley's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Knightley's Ship Part · 100× Alien Essence · 100× Transcendence Core

---

## 608 · Ironwall Prototype: Serratine 铁壁原型机：塞拉汀
**Role** Protector · **Attack** physical · **Generation** latest
**Ratings** Damage 6/10 · Defence 10/10 · Assist 10/10

### Skill panels
**Slot 1 — Astral Bastion** (id 1902, unlocks at `+0`)
  - **Ⅰ** at `+0` — Astral BastionⅠ (铁壁原型机：塞拉汀+0)
    Vertical Attack, plunders 75% of the target's S-DEF, then deals 300% S-ATK damage to targets. Makes all allies immune to freezing, locking, confusion, petrification, freezing, entangling, instant destruction, prohibiting the use of skills and weakening, lasting for 99 rounds. Finally restore 100 Accumulator.
  - **Ⅱ** at `+6` — Astral BastionⅡ (铁壁原型机：塞拉汀+6)
    Vertical Attack, plunders 75% of the target's S-DEF, then deals 320% S-ATK damage to targets. All allies gain 100% S-ATK damage reduction for 2 rounds. Makes all allies immune to freezing, locking, confusion, petrification, freezing, entangling, instant destruction, prohibiting the use of skills and weakening, lasting for 99 rounds. Finally restore 100 Accumulator.
  - **Ⅲ** at `+10` — Astral BastionⅢ (铁壁原型机：塞拉汀+10)
    Vertical Attack, plunders 75% of the target's S-DEF, then deals 340% S-ATK damage to targets. All allies gain 100% S-ATK damage reduction for 2 rounds. Makes all allies immune to freezing, locking, confusion, petrification, freezing, entangling, instant destruction, prohibiting the use of skills and weakening, lasting for 99 rounds. Gains [Astral Bastion] for 2 rounds. Finally restore 100 Accumulator. [Astral Bastion]: While active, if damage taken exceeds 30% of Max HP, the excess damage is negated, the effect can trigger up to 2 times. During the effect period, enemies will select Serratine as target priority. (takes precedence over Unyielding and Taunt; Repeated applied will reset the effect's times; Similar effects cannot be stacked.)
  - **Ⅳ** at `+15` — Astral BastionIV (铁壁原型机：塞拉汀+15)
    Vertical Attack, plunders 75% of the target's S-DEF, then deals 380% S-ATK damage to targets. All allies gain 120% S-ATK damage reduction for 2 rounds. Makes all allies immune to freezing, locking, confusion, petrification, freezing, entangling, instant destruction, prohibiting the use of skills and weakening, lasting for 99 rounds. Enemies cannot land critical hits when dealing damage for 2 rounds (takes priority over guaranteed critical hits). Recovers 80% of maximum HP and gains [Astral Bastion] for 2 rounds. Finally restore 100 Accumulator. [Astral Bastion]: While active, if damage taken exceeds 20% of Max HP, the excess damage is negated, the effect can trigger up to 2 times. During the effect period, enemies will select Serratine as target priority. (takes precedence over Unyielding and Taunt; Repeated applied will reset the effect's times; Similar effects cannot be stacked.)

**Slot 2 — Core Transference** (id 1903, unlocks at `+2`)
  - **Ⅰ** at `+2` — Core TransferenceⅠ (铁壁原型机：塞拉汀+2)
    (Takes effect at the start of battle) Each time takes damage, reduce all enemies' S-ATK by 60% for 99 rounds, stacking up to 5 times.
  - **Ⅱ** at `+12` — Core TransferenceⅡ (铁壁原型机：塞拉汀+12)
    (Takes effect at the start of battle) At the start of battle, gain [Astral Bastion], lasting 2 rounds. Each time takes damage, reduce all enemies' S-ATK by 60% for 99 rounds, stacking up to 5 times.
  - **Ⅲ** at `+T` — Core TransferenceⅢ (铁壁原型机：塞拉汀+16)
    (Takes effect at the start of battle) At the start of battle, gain [Astral Bastion], lasting 2 rounds. Each time takes damage, reduce all enemies' S-ATK by 60% for 99 rounds, stacking up to 5 times. At the start of battle, gain [Core Transference]. When attacked by specified Classes, trigger the corresponding effect. When attacked by Rangers/Protectors/Rovers, gain the effect: Recover 40% of Max HP.
  - **Ⅳ** at `+T3` — Core TransferenceIV (铁壁原型机：塞拉汀+19)
    (Takes effect at the start of battle) At the start of battle, gain [Astral Bastion], lasting 2 rounds. Each time takes damage, reduce all enemies' S-ATK by 60% for 99 rounds, stacking up to 5 times. At the start of battle, gain [Core Transference]. When attacked by specified Classes, trigger the corresponding effect. When attacked by Flagships/Strikers/Destroyers, gain the effect: immune to damage and abnormal statuses from that Class for 1 round. (Effect activates after taking damage, except for subsequent damage.) When attacked by Rangers/Protectors/Rovers, gain the effect: Recover 40% of Max HP and purifies all allies' abnormal statuses and control effects.

**Slot 3 — Ironwall** (id 1904, unlocks at `+4`)
  - **Ⅰ** at `+4` — IronwallⅠ (铁壁原型机：塞拉汀+4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +60% DEF: +30% S-DEF: +30% DMG Reduction (Absolute Value): +30%
  - **Ⅱ** at `+10` — IronwallⅡ (铁壁原型机：塞拉汀+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +90% DEF: +60% S-DEF: +60% DMG Reduction (Absolute Value): +40%
  - **Ⅲ** at `+14` — IronwallⅢ (铁壁原型机：塞拉汀+14)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +120% DEF: +90% S-DEF: +90% DMG Reduction (Absolute Value): +50%
  - **Ⅳ** at `+T2` — IronwallIV (铁壁原型机：塞拉汀+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +150% DEF: +120% S-DEF: +120% DMG Reduction (Absolute Value): +60%

**Slot 4 — Astral Reforge** (id 1905, unlocks at `+0`)
  - **Ⅰ** at `+0` — Astral ReforgeⅠ (铁壁原型机：塞拉汀+0)
    (Takes effect at the start of battle) Serratine's Astralsteel body makes it immune to the effects that prohibit skill activation and effects that reduce healing, but it cannot gain Rebirth, and upon death, it cannot be revived by any means (including revivals and rebirths unaffected by revival prohibition). When Serratine takes lethal damage, it will not die but instead triggers [Astral Reforge]. (Can only activate once per battle) [Astral Reforge]: Revives all dead allies to 100% of their initial HP and 150 Accumulator (unaffected by forbidding revival effects).
  - **Ⅱ** at `+13` — Astral ReforgeⅡ (铁壁原型机：塞拉汀+13)
    (Takes effect at the start of battle) Serratine's Astralsteel body makes it immune to the effects that prohibit skill activation and effects that reduce healing, but it cannot gain Rebirth, and upon death, it cannot be revived by any means (including revivals and rebirths unaffected by revival prohibition). When Serratine takes lethal damage, it will not die but instead triggers [Astral Reforge]. (Can activate up to 2 times per battle) [Astral Reforge]: Restores 100% of max HP, revives all dead allies to 100% of their initial HP and 150 Accumulator (unaffected by forbidding revival effects).
  - **Ⅲ** at `+T1` — Astral ReforgeⅢ (铁壁原型机：塞拉汀+17)
    (Takes effect at the start of battle) Serratine's Astralsteel body makes it immune to the effects that prohibit skill activation and effects that reduce healing, but it cannot gain Rebirth, and upon death, it cannot be revived by any means (including revivals and rebirths unaffected by revival prohibition). When Serratine takes lethal damage (Ignores immunity to lethal damage and instant destruction), it will not die but instead triggers [Astral Reforge]. (Can activate up to 2 times per battle) [Astral Reforge]: Restores 100% of max HP, revives all dead allies to 100% of their initial HP and 150 Accumulator (unaffected by forbidding revival effects).
  - **Ⅳ** at `+T4` — Astral ReforgeIV (铁壁原型机：塞拉汀+20)
    (Takes effect at the start of battle) Serratine's Astralsteel body makes it immune to the effects that prohibit skill activation and effects that reduce healing, but it cannot gain Rebirth, and upon death, it cannot be revived by any means (including revivals and rebirths unaffected by revival prohibition). When Serratine takes lethal damage (Ignores immunity to lethal damage and instant destruction), it will not die but instead triggers [Astral Reforge]. (Can activate up to 3 times per battle.) [Astral Reforge]: Restores 100% of max HP, revives all dead allies to 100% of their initial HP and 150 Accumulator (unaffected by forbidding revival effects). Additional effects are gained based on the number of times [Astral Reforge] is triggered. (Effects stack with each trigger) First trigger: Grants all allies 120% S-ATK damage reduction for 2 rounds. Second trigger: Immediately gains [Astral Bastion], increasing block count to 5 times, which will reset to 2 times after the next skill is used. Third trigger: Ignores trigger conditions and immediately activates all effects of [Core Transference] once.

### Augment cost (per step)
- `+1` — 5× Protector Chip · 100,000 money
- `+2` — 10× Protector Chip · 200,000 money
- `+3` — 21× Protector Chip · 300,000 money
- `+4` — 28× Protector Chip · 500,000 money
- `+5` — 35× Protector Chip · 800,000 money
- `+6` — 42× Protector Chip · 10× Pandora Power Core
- `+7` — 49× Protector Chip · 50× Pandora Power Core
- `+8` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Elenia Exclusive Chip · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Elenia Exclusive Chip · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Elenia Exclusive Chip · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Elenia Exclusive Chip · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Elenia Exclusive Chip · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Elenia Exclusive Chip · 100× Alien Essence · 100× Transcendence Core

---

## 615 · Teda 泰达
**Role** Protector · **Attack** physical · **Generation** latest
**Ratings** Damage 4/10 · Defence 10/10 · Assist 10/10

### Skill panels
**Slot 1 — Oath of the Boulder** (id 1929, unlocks at `+0`)
  - **Ⅰ** at `+0` — Oath of the BoulderⅠ (泰达+0)
    Cross Attack, deals 280% S-ATK damage to targets. Grants [Boulder] to all allies for 2 rounds. Lastly, recovers 100 Accumulator. [Boulder]: While active, records specific negative effects received in battle (freezing, locking, confusion, petrification, freezing, entangling, weakening, prohibiting the use of skills). If the same negative effect is received again while this buff is present, it will be blocked.
  - **Ⅱ** at `+6` — Oath of the BoulderⅡ (泰达+3)
    Cross Attack, deals 300% S-ATK damage to targets. Grants [Boulder] to all allies for 2 rounds. Increases all allies' Accumulator by 50, and finally recovers 100 Accumulator. [Boulder]: While active, records specific negative effects received in battle (freezing, locking, confusion, petrification, freezing, entangling, weakening, prohibiting the use of skills). If the same negative effect is received again while this buff is present, it will be blocked.
  - **Ⅲ** at `+10` — Oath of the BoulderⅢ (泰达+6)
    Cross Attack, deals 320% S-ATK damage to targets. Grants [Boulder] to all allies for 2 rounds. Increases all allies' S-DEF and DEF by 120%. Increases all allies' Accumulator by 50, and finally recovers 100 Accumulator. [Boulder]: While active, records specific negative effects received in battle (freezing, locking, confusion, petrification, freezing, entangling, weakening, prohibiting the use of skills). If the same negative effect is received again while this buff is present, it will be blocked.
  - **Ⅳ** at `+15` — Oath of the BoulderIV (泰达+10)
    Cross Attack, deals 340% S-ATK damage to targets. Grants [Boulder] to all allies for 2 rounds. Increases all allies' S-DEF and DEF by 120%. Increases all allies' Accumulator by 50, cleanse all allies of abnormal statuses and crowd-control effects, and finally recovers 100 Accumulator. [Boulder]: While active, records specific negative effects received in battle (freezing, locking, confusion, petrification, freezing, entangling, weakening, prohibiting the use of skills). If the same negative effect is received again while this buff is present, it will be blocked.

**Slot 2 — W60 Stance** (id 1930, unlocks at `+2`)
  - **Ⅰ** at `+2` — W60 StanceⅠ (泰达+2)
    (Takes effect at the start of battle) At the start of battle, gain [W60 Stance]: the damage taken from a single hit will not exceed 50% of your max HP, lasting until the end of battle (effects of the same type do not stack).
  - **Ⅱ** at `+9` — W60 StanceⅡ (泰达+9)
    (Takes effect at the start of battle) At the start of battle, gain [W60 Stance]: the damage taken from a single hit will not exceed 50% of your max HP, lasting until the end of battle (effects of the same type do not stack). During battle preparation, different skill effects are activated based on the formation ship's placement. (Takes effect at the start of battle and each time it revives or rebirths.) [Front Row]: The [W60 Stance] provided by own, the damage taken from a single hit will not exceed 30% of your max HP. [Second Row]: Grants [W60 Stance] to all allies in the front row at the start of battle (effect is removed upon death). [Back Row]: Grants [W60 Stance] to all allies in the front and second rows at the start of battle, but the duration is reduced to 1 round.
  - **Ⅲ** at `+T` — W60 StanceⅢ (泰达+16)
    (Takes effect at the start of battle) At the start of battle, gain [W60 Stance]: the damage taken from a single hit will not exceed 40% of your max HP, lasting until the end of battle (effects of the same type do not stack). During battle preparation, different skill effects are activated based on the formation ship's placement. (Takes effect at the start of battle and each time it revives or rebirths.) [Front Row]: The [W60 Stance] provided by own, the damage taken from a single hit will not exceed 20% of your max HP. [Second Row]: Grants [W60 Stance] to all allies in the front row at the start of battle (effect is removed upon death), gain a Rebirth effect, reviving immediately upon death with 100% HP and 150 Accumulator. [Back Row]: Grants [W60 Stance] to all allies in the front and second rows at the start of battle, but the duration is reduced to 1 round.
  - **Ⅳ** at `+T3` — W60 StanceIV (泰达+19)
    (Takes effect at the start of battle) When using a skill, there is a 75% chance to revive dead allies (unaffected by forbidding revival effects), revive 100% of their initial HP and Accumulator as at the start of battle. [Boulder] can now block additional negative effects: Energy Block, Magnetic Hyperspace Bomb, and Shadow Veil. It can also block effects that ignore immunity. At the start of battle and when casting a skill, grants [Guardian Stance] to allies with [W60 Stance] for 2 rounds. [Guardian Stance]: When taking S-ATK, different skill effects are activated based on the his placement. If there is any ally in the Front Row, Teda becomes immune to this damage and skill effect, and the skill effect is transferred to an ally in the front row (transfer priority follows position order; this effect has lower priority than Taunt, except for subsequent damage). If there are other members of the Supernova Blades Fleet (Aiolia, Ouros, Mu, Karon, Ulysses) in the formation, they gain [W60 Stance] and [Guardian Stance] at the start of battle, lasting for 99 rounds.

**Slot 3 — Barrier** (id 1931, unlocks at `+4`)
  - **Ⅰ** at `+4` — BarrierⅠ (泰达+4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +60% DEF: +30% S-DEF: +30% DMG Reduction (Absolute Value): +30%
  - **Ⅱ** at `+10` — BarrierⅡ (泰达+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +90% DEF: +60% S-DEF: +60% DMG Reduction (Absolute Value): +40%
  - **Ⅲ** at `+14` — BarrierⅢ (泰达+14)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +120% DEF: +90% S-DEF: +90% DMG Reduction (Absolute Value): +50%
  - **Ⅳ** at `+T2` — BarrierIV (泰达+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +150% DEF: +120% S-DEF: +120% DMG Reduction (Absolute Value): +60%

**Slot 4 — Supernova: Guardian Stance** (id 1932, unlocks at `+3`)
  - **Ⅰ** at `+3` — Supernova: Guardian StanceⅠ (泰达+3)
    (Takes effect at the start of battle) When using a skill, there is a 50% chance to revive dead allies, revive 100% of their initial HP and Accumulator as at the start of battle.
  - **Ⅱ** at `+13` — Supernova: Guardian StanceⅡ (泰达+13)
    (Takes effect at the start of battle) When using a skill, there is a 75% chance to revive dead allies (unaffected by forbidding revival effects), revive 100% of their initial HP and Accumulator as at the start of battle.
  - **Ⅲ** at `+T1` — Supernova: Guardian StanceⅢ (泰达+17)
    (Takes effect at the start of battle) When using a skill, there is a 75% chance to revive dead allies (unaffected by forbidding revival effects), revive 100% of their initial HP and Accumulator as at the start of battle. [Boulder] can now block additional negative effects: Energy Block, Magnetic Hyperspace Bomb, and Shadow Veil. It can also block effects that ignore immunity.
  - **Ⅳ** at `+T4` — Supernova: Guardian StanceIV (泰达+20)
    (Takes effect at the start of battle) When using a skill, there is a 75% chance to revive dead allies (unaffected by forbidding revival effects), revive 100% of their initial HP and Accumulator as at the start of battle. [Boulder] can now block additional negative effects: Energy Block, Magnetic Hyperspace Bomb, and Shadow Veil. It can also block effects that ignore immunity. At the start of battle and when casting a skill, grants [Guardian Stance] to allies with [W60 Stance] for 2 rounds. [Guardian Stance]: When taking S-ATK, different skill effects are activated based on the his placement. If there is any ally in the Front Row, Teda becomes immune to this damage and skill effect, and the skill effect is transferred to an ally in the front row (transfer priority follows position order; this effect has lower priority than Taunt, except for subsequent damage). If there are other members of the Supernova Blades Fleet (Aiolia, Ouros, Mu, Karon, Teda, Ulysses) in the team, they gain [W60 Stance] and [Guardian Stance] at the start of battle, lasting for 99 rounds.

### Augment cost (per step)
- `+1` — 5× Protector Chip · 100,000 money
- `+2` — 10× Protector Chip · 200,000 money
- `+3` — 21× Protector Chip · 300,000 money
- `+4` — 28× Protector Chip · 500,000 money
- `+5` — 35× Protector Chip · 800,000 money
- `+6` — 42× Protector Chip · 10× Pandora Power Core
- `+7` — 49× Protector Chip · 50× Pandora Power Core
- `+8` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Elenia Exclusive Chip · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Elenia Exclusive Chip · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Elenia Exclusive Chip · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Elenia Exclusive Chip · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Elenia Exclusive Chip · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Elenia Exclusive Chip · 100× Alien Essence · 100× Transcendence Core

---

## 621 · Roche 洛希
**Role** Protector · **Attack** physical · **Generation** latest
**Ratings** Damage 4/10 · Defence 8/10 · Assist 10/10

### Skill panels
**Slot 1 — Nebula Lash** (id 1949, unlocks at `+0`)
  - **Ⅰ** at `+0` — Nebula LashⅠ (洛希+0)
    Cross Attack, deals 300% S-ATK damage to targets. Has a 100% chance to Taunt for 2 rounds. All allies take 60% less final damage. All allies gain [Nebula Lash] for 2 rounds. Lastly, recovers 100 Accumulator. [Nebula Lash]: While active, when taking attack damage, there is a 30% chance to Entangle a random enemy for 2 rounds.
  - **Ⅱ** at `+6` — Nebula LashⅡ (洛希+2)
    Cross Attack, deals 320% S-ATK damage to targets with a 100% chance to Taunt for 2 rounds. Reduces all allies' final damage taken by 60%. Purifies all allies of control effects (freezing, locking, confusion, petrification, Icebound, entangling, prohibiting the use of skills and weakening). All allies gain [Nebula Lash] for 2 rounds. Lastly, restore 100 points of energy. [Nebula Lash]: While active, when taking attack damage, there is a 30% chance to entangle 1 random enemy unit for 2 rounds.
  - **Ⅲ** at `+10` — Nebula LashⅢ (洛希+3)
    Cross Attack, deals 340% S-ATK damage to targets with a 100% chance to Taunt for 2 rounds. Reduces all allies' final damage taken by 60%. Purifies all allies of control effects (freezing, locking, confusion, petrification, Icebound, entangling, prohibiting the use of skills and weakening), and all allies recover HP equal to 80% of their max HP. All allies gain [Nebula Lash] for 2 rounds. Lastly, restore 100 points of energy. [Nebula Lash]: While active, when taking attack damage, there is a 30% chance to entangle 1 random enemy unit for 2 rounds.
  - **Ⅳ** at `+15` — Nebula LashIV (洛希+6)
    Cross Attack, deals 360% S-ATK damage to targets with a 100% chance to Taunt for 2 rounds. Reduces all allies' final damage taken by 60%. Purifies all allies of control effects (freezing, locking, confusion, petrification, Icebound, entangling, prohibiting the use of skills and weakening), and all allies recover HP equal to 80% of their max HP. Has a 100% chance to entangle 1 enemy unit for 1 round, and all allies gain [Nebula Lash] for 2 rounds. Lastly, restore 100 points of energy. [Nebula Lash]: While active, when taking attack damage, there is a 30% chance to entangle 1 random enemy unit for 2 rounds, and it can block 1 instance of any type of damage. Reapplying refreshes the number of blocks.

**Slot 2 — Cornucopia Blessing** (id 1950, unlocks at `+2`)
  - **Ⅰ** at `+2` — Cornucopia BlessingⅠ (洛希+2)
    (Takes effect at the start of battle) Each time [Nebula Lash] is applied, the holder's S-ATK increases by 40%, lasting until the end of battle. (Stacks up to 5 times)
  - **Ⅱ** at `+9` — Cornucopia BlessingⅡ (洛希+9)
    (Takes effect at the start of battle) Each time [Nebula Lash] is applied, the holder's S-ATK is increased by 40%, lasting until the end of battle. (Stacks up to 5 times) At the start of battle and upon each revival or rebirth, Taunt is activated for 2 rounds.
  - **Ⅲ** at `+T` — Cornucopia BlessingⅢ (洛希+16)
    (Takes effect at the start of battle) Each time [Nebula Lash] is applied, the holder's S-ATK is increased by 40%, lasting until the end of battle. (Stacks up to 5 times) At the start of battle and upon each revival or rebirth, Taunt is activated for 2 rounds. At the start of battle, all allies gain [Nebula Lash] for 2 rounds.
  - **Ⅳ** at `+T3` — Cornucopia BlessingIV (洛希+19)
    (Takes effect at the start of battle) Each time [Nebula Lash] is applied, the holder's S-ATK is increased by 40%, lasting until the end of battle. (Stacks up to 5 times) At the start of battle and upon each revival or rebirth, Taunt is activated for 2 rounds. At the start of battle, all allies gain [Nebula Lash] for 2 rounds. The chance for Entangle applied by [Nebula Lash] is increased to 50%.

**Slot 3 — Dew** (id 1951, unlocks at `+4`)
  - **Ⅰ** at `+4` — DewⅠ (洛希+4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +60% DEF: +30% S-DEF: +30%
  - **Ⅱ** at `+10` — DewⅡ (洛希+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +90% DEF: +60% S-DEF: +60%
  - **Ⅲ** at `+14` — DewⅢ (洛希+14)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +120% DEF: +90% S-DEF: +90%
  - **Ⅳ** at `+T2` — DewIV (洛希+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +150% DEF: +120% S-DEF: +120%

**Slot 4 — Verdant Gift** (id 1952, unlocks at `+3`)
  - **Ⅰ** at `+3` — Verdant GiftⅠ (洛希+3)
    (Takes effect at the start of battle) At the start of battle and when casting a skill, all allies gain [Verdant Gift] until the end of the battle. [Verdant Gift]: The holder's S-DMG Reduction increases by 60%, and DEF and S-DEF increase by 90%.
  - **Ⅱ** at `+13` — Verdant GiftⅡ (洛希+13)
    (Takes effect at the start of battle) At the start of battle and when casting a skill, all allies gain [Verdant Gift] until the end of the battle. [Verdant Gift]: The holder's S-DMG Reduction increases by 60%, and DEF and S-DEF increase by 90%. Grants immunity to freezing, locking, confusion, petrification, Icebound, entangling, prohibiting the use of skills, and weakening.
  - **Ⅲ** at `+T1` — Verdant GiftⅢ (洛希+17)
    (Takes effect at the start of battle) At the start of battle and when casting a skill, all allies gain [Verdant Gift] until the end of the battle. [Verdant Gift]: The holder's S-DMG Reduction increases by 60%, and DEF and S-DEF increase by 90%. Grants immunity to freezing, locking, confusion, petrification, Icebound, entangling, prohibiting the use of skills, and weakening, lasting until the end of battle. When an ally with [Verdant Gift] casts a skill, there is a 30% chance to grant itself a Rebirth effect; upon death, reviving immediately upon death with 100% HP and Accumulator as at the start of the battle. (which isn't affected by forbidding revival effects.)
  - **Ⅳ** at `+T4` — Verdant GiftIV (洛希+20)
    (Takes effect at the start of battle) At the start of battle and when casting a skill, all allies gain [Verdant Gift] until the end of the battle. [Verdant Gift]: The holder's S-DMG Reduction increases by 60%, and DEF and S-DEF increase by 90%. Grants immunity to freezing, locking, confusion, petrification, Icebound, entangling, prohibiting the use of skills, and weakening, lasting until the end of battle. When an ally with [Verdant Gift] casts a skill, there is a 30% chance to grant itself a Rebirth effect; upon death, reviving immediately upon death with 100% HP and Accumulator as at the start of the battle. (which isn't affected by forbidding revival effects.) When the holder dies, all allies gain [Nebula Lash] for 2 rounds, and there is a 100% chance to Entangle 2 random enemies for 2 rounds. (Entangle from this effect, ignoring immunity and protection effects, and will prioritize enemies not already Entangled)

### Augment cost (per step)
- `+1` — 5× Protector Chip · 100,000 money
- `+2` — 10× Protector Chip · 200,000 money
- `+3` — 21× Protector Chip · 300,000 money
- `+4` — 28× Protector Chip · 500,000 money
- `+5` — 35× Protector Chip · 800,000 money
- `+6` — 42× Protector Chip · 10× Pandora Power Core
- `+7` — 49× Protector Chip · 50× Pandora Power Core
- `+8` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Roche Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Roche Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Roche Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Roche Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Roche Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Roche Ship Part · 100× Alien Essence · 100× Transcendence Core

---

## 624 · Vid 维迪
**Role** Protector · **Attack** physical · **Generation** old
**Ratings** Damage 7/10 · Defence 9/10 · Assist 8/10

### Signature skill
- **Ⅰ** at `+0` — Repost (维迪+0)
  Cross Attack, deals 200% S-ATK damage to targets. Lastly, you recover 100 Accumulator.

### Augment cost (per step)
- `+1` — 5× Protector Chip · 100,000 money
- `+2` — 10× Protector Chip · 200,000 money
- `+3` — 21× Protector Chip · 300,000 money
- `+4` — 28× Protector Chip · 500,000 money
- `+5` — 35× Protector Chip · 800,000 money
- `+6` — 42× Protector Chip · 10× Pandora Power Core
- `+7` — 49× Protector Chip · 50× Pandora Power Core
- `+8` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Vid Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Vid Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Vid Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Vid Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Vid Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Vid Ship Part · 100× Alien Essence · 100× Transcendence Core

---

## 625 · Brianna 布里安娜
**Role** Protector · **Attack** physical · **Generation** latest
**Ratings** Damage 5/10 · Defence 10/10 · Assist 8/10

### Skill panels
**Slot 1 — Starborn Chrono Arrow** (id 1964, unlocks at `+0`)
  - **Ⅰ** at `+0` — Starborn Chrono ArrowⅠ (布里安娜+0)
    All Attack, deals 340% S-ATK damage to hit targets. Purifies all allies of abnormal statuses and attribute debuffs. Lastly, recovers 100 Accumulator.
  - **Ⅱ** at `+6` — Starborn Chrono ArrowⅡ (布里安娜+3)
    All Attack, deals 360% S-ATK damage to hit targets. Purifies all allies of abnormal statuses and attribute debuffs. Applies a shield to all allies, reducing any damage taken by 90% for 99 rounds. Lastly, recovers 100 Accumulator.
  - **Ⅲ** at `+10` — Starborn Chrono ArrowⅢ (布里安娜+6)
    All Attack, deals 380% S-ATK damage to hit targets. Removes Eye of True Sight from all enemies and purifies all allies of abnormal statuses and attribute debuffs. Applies a shield to all allies, reducing any damage taken by 90% for 99 rounds. Increases all allies' damage dealt by 30%, stacking up to 3 times, lasting until the end of the battle. Lastly, recovers 100 Accumulator.
  - **Ⅳ** at `+15` — Starborn Chrono ArrowIV (布里安娜+10)
    All Attack, first clears all buffs from the target, then deals 400% S-ATK damage to hit targets. Removes Eye of True Sight from all enemies and purifies all allies of abnormal statuses and attribute debuffs. Applies a shield to all allies, reducing any damage taken by 90% for 99 rounds. Increases all allies' damage dealt by 30% and S-ATK by 20%, stacking up to 3 times, lasting until the end of the battle. Lastly, recovers 100 Accumulator.

**Slot 2 — Everbright Aegis** (id 1965, unlocks at `+2`)
  - **Ⅰ** at `+2` — Everbright AegisⅠ (布里安娜+2)
    (Начинает действовать в начале боя) В начале битвы все союзники получают невосприимчивыми к замораживанию, блокировке, ошеломлению, окаменению, сковывание льдом, Хрупкость, запутыванию, запрету использования навыков, ослаблению, а также иммунитет к мгновенному уничтожению, действующий до конца битвы. (Эффект снимается при смерти)
  - **Ⅱ** at `+9` — Everbright AegisⅡ (布里安娜+9)
    (Takes effect at the start of battle) At the start of battle, grants all allies immune to freezing, locking, confusion, petrification, Icebound, Brittle, entangling, prohibiting the use of skills, weakening, as well as immunity to instant destruction, lasting until the end of battle. (Effect is removed upon death) When any ally dies, all other allies deal 100% more damage (not stackable), lasting for 1 round.
  - **Ⅲ** at `+T` — Everbright AegisⅢ (布里安娜+16)
    (Takes effect at the start of battle) At the start of battle, grants all allies immune to freezing, locking, confusion, petrification, Icebound, Brittle, entangling, prohibiting the use of skills, weakening, as well as immunity to instant destruction, lasting until the end of battle. (Effect is removed upon death) When any ally dies, all other allies deal 120% more damage (not stackable), lasting for 1 round. At the start of battle, applies Ward to all allies. Allies under Ward will block the damage from an enemy skill attack and will not be affected by the skill’s effects (except for subsequent damage). Ward is removed after blocking one attack and lasts for 2 rounds.
  - **Ⅳ** at `+T3` — Everbright AegisIV (布里安娜+19)
    (Takes effect at the start of battle) At the start of battle, grants all allies immune to freezing, locking, confusion, petrification, Icebound, Brittle, entangling, prohibiting the use of skills, weakening, as well as immunity to instant destruction, lasting until the end of battle. (Effect is removed upon death) When any ally dies, all other allies deal 120% more damage (not stackable), lasting for 1 round. At the start of battle, applies Ward to all allies. Allies under Ward will block the damage from an enemy skill attack and will not be affected by the skill’s effects (except for subsequent damage). Ward is removed after blocking one attack and lasts for 2 rounds. When casting a skill, increases damage taken by all enemies by 15%, stacking up to 3 times, lasting until the end of battle.

**Slot 3 — Chrono-Boon** (id 1966, unlocks at `+4`)
  - **Ⅰ** at `+4` — Chrono-BoonⅠ (布里安娜+4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +60% DEF: +30% S-DEF: +30% DMG Reduction (Absolute Value): +30%
  - **Ⅱ** at `+10` — Chrono-BoonⅡ (布里安娜+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +90% DEF: +60% S-DEF: +60% DMG Reduction (Absolute Value): +40%
  - **Ⅲ** at `+14` — Chrono-BoonⅢ (布里安娜+14)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +120% DEF: +90% S-DEF: +90% DMG Reduction (Absolute Value): +50%
  - **Ⅳ** at `+T2` — Chrono-BoonIV (布里安娜+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +150% DEF: +120% S-DEF: +120% DMG Reduction (Absolute Value): +60%

**Slot 4 — Sequencing Echo** (id 1967, unlocks at `+3`)
  - **Ⅰ** at `+3` — Sequencing EchoⅠ (布里安娜+3)
    (Takes effect at the start of battle) Each time a skill is cast, increases all allies' Crit ATK by 15%, stacking up to 3 times and lasting until the end of battle.
  - **Ⅱ** at `+13` — Sequencing EchoⅡ (布里安娜+13)
    (Takes effect at the start of battle) Each time a skill is cast, increases all allies' Crit ATK by 15%, stacking up to 3 times and lasting until the end of battle. When casting a skill, grants all allies Ward for 2 rounds.
  - **Ⅲ** at `+T1` — Sequencing EchoⅢ (布里安娜+17)
    (Takes effect at the start of battle) Each time a skill is cast, increases all allies' Crit ATK by 15%, stacking up to 3 times and lasting until the end of battle. When casting a skill, grants all allies Ward for 2 rounds. When casting a skill, revives all dead allies, restoring them to 100% of their initial HP and 100 Accumulator. The revival effect is only valid for the first 5 rounds.
  - **Ⅳ** at `+T4` — Sequencing EchoIV (布里安娜+20)
    (Takes effect at the start of battle) Each time a skill is cast, increases all allies' Crit ATK by 30%, stacking up to 3 times and lasting until the end of battle. When casting a skill, grants all allies Ward for 2 rounds. When casting a skill, revives all dead allies (not affected by effects that prevent revival), restoring them to 100% of their initial HP and 100 Accumulator. The revival effect is only valid for the first 5 rounds.

### Augment cost (per step)
- `+1` — 5× Protector Chip · 100,000 money
- `+2` — 10× Protector Chip · 200,000 money
- `+3` — 21× Protector Chip · 300,000 money
- `+4` — 28× Protector Chip · 500,000 money
- `+5` — 35× Protector Chip · 800,000 money
- `+6` — 42× Protector Chip · 10× Pandora Power Core
- `+7` — 49× Protector Chip · 50× Pandora Power Core
- `+8` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Brianna's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Brianna's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Brianna's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Brianna's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Brianna's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Brianna's Ship Part · 100× Alien Essence · 100× Transcendence Core

---

## 634 · Kolossos 科洛索斯
**Role** Protector · **Attack** physical · **Generation** latest
**Ratings** Damage 7/10 · Defence 10/10 · Assist 9/10

### Skill panels
**Slot 1 — Starfall Strike** (id 1996, unlocks at `+0`)
  - **Ⅰ** at `+0` — Starfall StrikeⅠ (科洛索斯+0)
    Cross Attack, deals 280% S-ATK damage to targets. Reduces all damage taken by Us by 90%. Lastly, recovers 100 Accumulator.
  - **Ⅱ** at `+6` — Starfall StrikeⅡ (科洛索斯+6)
    Cross Attack, deals 300% S-ATK damage to targets. Reduces all damage taken by Us by 90%. Purifies all allies' control effects.(Freeze, Lock, Confuse, Petrify, Icebound, Entangle, Brittle, Forbidding Skill Use and Weaken.) Lastly, recovers 100 Accumulator.
  - **Ⅲ** at `+10` — Starfall StrikeⅢ (科洛索斯+9)
    Cross Attack, deals 320% S-ATK damage to targets. Reduces all damage taken by Us by 90%. Purifies all allies' control effects.(Freeze, Lock, Confuse, Petrify, Icebound, Entangle, Brittle, Forbidding Skill Use and Weaken.) Expose all Enemy ships that are invisible. Lastly, recovers 100 Accumulator.
  - **Ⅳ** at `+15` — Starfall StrikeIV (科洛索斯+10)
    Cross Attack, deals 350% S-ATK damage to targets. Reduces all damage taken by Us by 90%. Purifies all allies' control effects.(Freeze, Lock, Confuse, Petrify, Icebound, Entangle, Brittle, Forbidding Skill Use and Weaken.) Expose all Enemy ships that are invisible, reduces the current HP of attack targets by 80%. Lastly, recovers 100 Accumulator.

**Slot 2 — Eternal Stonify** (id 1997, unlocks at `+2`)
  - **Ⅰ** at `+2` — Eternal StonifyⅠ (科洛索斯+2)
    (Takes effect at the start of battle) Increases the damage dealt of all allies by 40% until the end of the battle.
  - **Ⅱ** at `+9` — Eternal StonifyⅡ (科洛索斯+9)
    (Takes effect at the start of battle) Increases the damage dealt of all allies by 60% until the end of the battle. When using a skill, there is a 100% chance to inflict [Stonify] on attacked enemy for 2 rounds.
  - **Ⅲ** at `+T` — Eternal StonifyⅢ (科洛索斯+16)
    (Takes effect at the start of battle) Increases the damage dealt of all allies by 80% until the end of the battle. When using a skill, there is a 100% chance to inflict [Stonify] on attacked enemy for 2 rounds. When using a skill, if damage taken exceeds 30% of max HP, the excess is nullified for 2 rounds.
  - **Ⅳ** at `+T3` — Eternal StonifyIV (科洛索斯+19)
    (Takes effect at the start of battle) Increases the damage dealt of all allies by 120% until the end of the battle. When using a skill, there is a 100% chance to inflict [Stonify] on attacked enemy for 2 rounds. When using a skill, if damage taken exceeds 20% of max HP, the excess is nullified for 2 rounds. When using a skill, the first unit in the vertical line gains [Disruption] for 2 rounds. While holding this effect, when the unit uses a skill, its attack range changes to Single attack and can only target the first unit in the vertical line. (Lower priority than Taunt)

**Slot 3 — Primordial** (id 1998, unlocks at `+4`)
  - **Ⅰ** at `+4` — PrimordialⅠ (科洛索斯+4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +60% DEF: +30% S-DEF: +30%
  - **Ⅱ** at `+10` — PrimordialⅡ (科洛索斯+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +90% DEF: +60% S-DEF: +60%
  - **Ⅲ** at `+14` — PrimordialⅢ (科洛索斯+14)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +120% DEF: +90% S-DEF: +90%
  - **Ⅳ** at `+T2` — PrimordialIV (科洛索斯+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +150% DEF: +120% S-DEF: +120%

**Slot 4 — Sacred Gift** (id 1999, unlocks at `+3`)
  - **Ⅰ** at `+3` — Sacred GiftⅠ (科洛索斯+4)
    (Takes effect at the start of battle) At the start of battle, grants all allies immunity to Freeze, Lock, Confuse, Petrify, Icebound, Brittle, Entangle, Forbidding Skill Use, Weakening, and immunity to instant destruction, lasting until the end of battle. (Effect disappears upon death) When Kolossos is owned, player gains additional rewards in Daily [Stellar Territory] and [Galaxy Trial]. (Effect takes place without Deploying the hero; Daily Rewards counts reset at UTC 0:00; different tiers cannot trigger rewards repeatedly) [Stellar Territory]: The amount of Dark Aerosiderite obtained from Occupy any planet is increased by 30%, and the first 2 Quick Occupy each day will not consume Credits. [Galaxy Trial]: Upon successfully clearing a stage, you receive an extra OS Chip Random Pack*1, up to 3 times per day.
  - **Ⅱ** at `+13` — Sacred GiftⅡ (科洛索斯+11)
    (Takes effect at the start of battle) At the start of battle, grants all allies immunity to Freeze, Lock, Confuse, Petrify, Icebound, Brittle, Entangle, Forbidding Skill Use, Weakening, and immunity to instant destruction, lasting until the end of battle. (Effect disappears upon death) All allies gain an additional 75 Accumulator after taking damage, lasting until the end of battle. (Effect disappears upon death) When Kolossos is owned, player gains additional rewards in Daily [Stellar Territory] and [Galaxy Trial]. (Effect takes place without Deploying the hero; Daily Rewards counts reset at UTC 0:00; different tiers cannot trigger rewards repeatedly) [Stellar Territory]: The amount of Dark Aerosiderite obtained from Occupy any planet is increased by 40%, and the first 2 Quick Occupy each day will not consume Credits. [Galaxy Trial]: Upon successfully clearing a stage, you receive an extra OS Chip Random Pack*1, up to 5 times per day.
  - **Ⅲ** at `+T1` — Sacred GiftⅢ (科洛索斯+14)
    (Takes effect at the start of battle) At the start of battle, grants all allies immunity to Freeze, Lock, Confuse, Petrify, Icebound, Brittle, Entangle, Forbidding Skill Use, Weakening, and immunity to instant destruction, lasting until the end of battle. (Effect disappears upon death) All allies gain an additional 75 Accumulator after taking damage, lasting until the end of battle. (Effect disappears upon death) At the start of battle and upon each revival or rebirth, grants all allies (excluding self) a Rebirth effect: upon death, immediately revive and restore to 100% HP and Accumulator as at the start of battle. (Unaffected by forbidding revival effects) When Kolossos is owned, player gains additional rewards in Daily [Stellar Territory] and [Galaxy Trial]. (Effect takes place without Deploying the hero; Daily Rewards counts reset at UTC 0:00; different tiers cannot trigger rewards repeatedly) [Stellar Territory]: The amount of Dark Aerosiderite obtained from Occupy any planet is increased by 60%, and the first 3 Quick Occupy each day will not consume Credits. [Galaxy Trial]: Upon successfully clearing a stage, you receive an extra OS Chip Random Pack*1, Potential Material Optional Pack*1, up to 5 times per day.
  - **Ⅳ** at `+T4` — Sacred GiftIV (科洛索斯+18)
    (Takes effect at the start of battle) At the start of battle, grants all allies immunity to Freeze, Lock, Confuse, Petrify, Icebound, Brittle, Entangle, Forbidding Skill Use, Weakening, and immunity to instant destruction, lasting until the end of battle. (Effect disappears upon death) All allies gain an additional 75 Accumulator after taking damage, lasting until the end of battle. (Effect disappears upon death) At the start of battle and upon each revival or rebirth, grants all allies (excluding self) a Rebirth effect: upon death, immediately revive and restore to 100% HP and Accumulator as at the start of battle. (Unaffected by forbidding revival effects) Each time revived or rebirth, self will Taunt for 2 rounds or until a skill is used. When Kolossos is owned, player gains additional rewards in Daily [Stellar Territory] and [Galaxy Trial]. (Effect takes place without Deploying the hero; Daily Rewards counts reset at UTC 0:00; different tiers cannot trigger rewards repeatedly) [Stellar Territory]: The amount of Dark Aerosiderite obtained from Occupy any planet is increased by 100%, and the first 3 Quick Occupy each day will not consume Credits. [Galaxy Trial]: Upon successfully clearing a stage, you receive an extra OS Chip Random Pack*2, Potential Material Optional Pack*2, up to 5 times per day.

### Augment cost (per step)
- `+1` — 5× Protector Chip · 100,000 money
- `+2` — 10× Protector Chip · 200,000 money
- `+3` — 21× Protector Chip · 300,000 money
- `+4` — 28× Protector Chip · 500,000 money
- `+5` — 35× Protector Chip · 800,000 money
- `+6` — 42× Protector Chip · 10× Pandora Power Core
- `+7` — 49× Protector Chip · 50× Pandora Power Core
- `+8` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Kolossos's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Kolossos's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Kolossos's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Kolossos's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Kolossos's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Kolossos's Ship Part · 100× Alien Essence · 100× Transcendence Core

---

## 639 · Javier 哈维尔
**Role** Protector · **Attack** physical · **Generation** latest
**Ratings** Damage 7/10 · Defence 10/10 · Assist 9/10

### Skill panels
**Slot 1 — Guardian Shield** (id 2013, unlocks at `+0`)
  - **Ⅰ** at `+0` — Guardian ShieldⅠ (哈维尔+0)
    Cross Attack, deals 320% S-ATK damage to targets, applies Guardian Shield to all allies for 2 rounds, and lastly recovers 100 Accumulator. [Guardian Shield]: While active, when taking any damage, only 1% of max HP is lost from that instance, then the effect is removed. Reapplying refreshes the block count. (Cannot stack with similar effects)
  - **Ⅱ** at `+6` — Guardian ShieldⅡ (哈维尔+6)
    Cross Attack, first plunders 75% of the target's S-DEF, deals 340% S-ATK damage to targets, applies Guardian Shield to all allies for 2 rounds, and lastly recovers 100 Accumulator. [Guardian Shield]: While active, when taking any damage, only 1% of max HP is lost from that instance, then the effect is removed. Reapplying refreshes the block count. (Cannot stack with similar effects)
  - **Ⅲ** at `+10` — Guardian ShieldⅢ (哈维尔+10)
    Cross Attack, first plunders 75% of the target's S-DEF, deals 360% S-ATK damage to targets. Increases all allies' S-DEF damage reduction by 200%, lasting until the end of the battle. Applies Guardian Shield to all allies for 2 rounds, and lastly recovers 100 Accumulator. [Guardian Shield]: While active, when taking any damage, only 1% of max HP is lost from that instance, then the effect is removed. Reapplying refreshes the block count. (Cannot stack with similar effects)
  - **Ⅳ** at `+T` — Guardian ShieldIV (哈维尔+15)
    Cross Attack, first plunders 75% of the target's S-DEF, deals 380% S-ATK damage to targets. Increases all allies' S-DEF damage reduction by 200%, lasting until the end of the battle. Has a 100% chance to inflict [Binding] on all enemy non-biological units and gender-neutral characters for 2 rounds. Applies Guardian Shield to all allies for 2 rounds, and lastly recovers 100 Accumulator. [Guardian Shield]: While active, when taking any damage, only 1% of max HP is lost from that instance, then the effect is removed. Reapplying refreshes the block count. (Cannot stack with similar effects)

**Slot 2 — Cross Intercept** (id 2014, unlocks at `+2`)
  - **Ⅰ** at `+2` — Cross InterceptⅠ (哈维尔+2)
    (Takes effect at the start of battle) At the start of battle, applies [Guardian Shield] to all allies, lasting 2 rounds.
  - **Ⅱ** at `+9` — Cross InterceptⅡ (哈维尔+9)
    (Takes effect at the start of battle) At the start of battle, applies [Guardian Shield] to all allies, lasting 2 rounds. At the start of battle, activates Taunt and reduces allies' final damage taken by 65% until the end of battle.
  - **Ⅲ** at `+15` — Cross InterceptⅢ (哈维尔+16)
    (Takes effect at the start of battle) At the start of battle, applies [Guardian Shield] to all allies, lasting 2 rounds. At the start of battle, activates Taunt and reduces allies' final damage taken by 65% until the end of battle. While self is alive, whenever allies uses S-ATK that includes healing or HP recovery, [Guardian Shield] is additionally granted, lasting 2 rounds. (This effect is removed upon self's death and does not include healing effects from Legendary Equipment.)
  - **Ⅳ** at `+T3` — Cross InterceptIV (哈维尔+19)
    (Takes effect at the start of battle) At the start of battle, applies [Guardian Shield] to all allies, lasting 2 rounds. At the start of battle, activates Taunt and reduces allies' final damage taken by 65% until the end of battle. While self is alive, whenever allies uses S-ATK that includes healing or HP recovery, [Guardian Shield] is additionally granted, lasting 2 rounds. (This effect is removed upon self's death and does not include healing effects from Legendary Equipment.) When any unit in allies dies, all remaining units in allies gain [Guardian Shield] for 2 rounds and their HP increases by 100%. (If multiple units die in the same round, this effect only triggers once.)

**Slot 3 — Landing Prediction** (id 2015, unlocks at `+4`)
  - **Ⅰ** at `+4` — Landing PredictionⅠ (哈维尔+4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +60% DEF: +30% S-DEF: +30% DMG Reduction (Absolute Value): +30%
  - **Ⅱ** at `+10` — Landing PredictionⅡ (哈维尔+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +90% DEF: +60% S-DEF: +60% DMG Reduction (Absolute Value): +40%
  - **Ⅲ** at `+14` — Landing PredictionⅢ (哈维尔+14)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +120% DEF: +90% S-DEF: +90% DMG Reduction (Absolute Value): +50%
  - **Ⅳ** at `+T2` — Landing PredictionIV (哈维尔+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +150% DEF: +120% S-DEF: +120% DMG Reduction (Absolute Value): +60%

**Slot 4 — Last Defense** (id 2016, unlocks at `+3`)
  - **Ⅰ** at `+3` — Last DefenseⅠ (哈维尔+3)
    (Takes effect at the start of battle) After taking damage, if max HP is below 75%, gain [Guardian Shield] for 2 rounds. If max HP is below 50%, there is a 50% chance to gain a Rebirth effect, reviving immediately upon death and restoring HP and Accumulator to 100% of the value at the start of battle. (Each effect can stack and be triggered repeatedly)
  - **Ⅱ** at `+13` — Last DefenseⅡ (哈维尔+13)
    (Takes effect at the start of battle) After taking damage, if max HP is below 75%, gain [Guardian Shield] for 2 rounds. If max HP is below 50%, there is a 50% chance to gain a Rebirth effect, reviving immediately upon death and restoring HP and Accumulator to 100% of the value at the start of battle. If max HP is below 25%, immediately take 1 extra action. (Each effect can stack and be triggered repeatedly)
  - **Ⅲ** at `+T1` — Last DefenseⅢ (哈维尔+17)
    (Takes effect at the start of battle) After taking damage, if max HP is below 75%, gain [Guardian Shield] for 2 rounds. If max HP is below 50%, there is a 50% chance to gain a Rebirth effect, reviving immediately upon death and restoring HP and Accumulator to 100% of the value at the start of battle. If max HP is below 25%, immediately take 1 extra action. (Each effect can stack and be triggered repeatedly) When taking lethal damage (including ignores immunity to lethal attacks and instant destruction effects), will not die, but instead trigger [Last Defense]. (Can be triggered once per survival; resets after revival or rebirth) [Last Defense]: restores all allies' HP to 100% of Max HP and 200 Accumulator, and removes own Taunt effect. Taunt will reactivate after next skill use or being attacked by an enemy.
  - **Ⅳ** at `+T4` — Last DefenseIV (哈维尔+20)
    (Takes effect at the start of battle) After taking damage, if max HP is below 75%, gain [Guardian Shield] for 2 rounds. If max HP is below 50%, there is a 50% chance to gain a Rebirth effect, reviving immediately upon death and restoring HP and Accumulator to 100% of the value at the start of battle. If max HP is below 25%, immediately take 1 extra action. (Each effect can stack and be triggered repeatedly) When taking lethal damage (including ignores immunity to lethal attacks and instant destruction effects), will not die, but instead trigger [Last Defense]. (Can be triggered once per survival; resets after revival or rebirth) [Last Defense]: restores all allies' HP to 100% of Max HP and 200 Accumulator, removes all effects that prohibit or limit revival from all allies (this effect does not work on already fallen units). Revives all allies (ignoring effects that prohibit revival), restoring them to 100% HP and Accumulator as at the start of the battle. Removes own Taunt effect. Taunt will reactivate after next skill use or being attacked by an enemy.

### Augment cost (per step)
- `+1` — 5× Protector Chip · 100,000 money
- `+2` — 10× Protector Chip · 200,000 money
- `+3` — 21× Protector Chip · 300,000 money
- `+4` — 28× Protector Chip · 500,000 money
- `+5` — 35× Protector Chip · 800,000 money
- `+6` — 42× Protector Chip · 10× Pandora Power Core
- `+7` — 49× Protector Chip · 50× Pandora Power Core
- `+8` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Protector Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Protector Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Javier's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Javier's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Javier's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Javier's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Javier's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Javier's Ship Part · 100× Alien Essence · 100× Transcendence Core

---
