# Galaxy Legends — SSS Destroyers (30 heroes)

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
| 373 | Freddy | 弗瑞 | 9 | 6 | 2 | old |
| 396 | Snowden | 斯诺登 | 9 | 6 | 5 | old |
| 413 | Floop | 霍普 | 9 | 5 | 4 | old |
| 443 | Nu'zogh | 恩索斯 | 9 | 6 | 5 | old |
| 454 | K | K | 10 | 6 | 6 | old |
| 465 | Deena Hineston | 蒂娜·海因斯顿 | 10 | 6 | 6 | old |
| 482 | Chaos | 混沌 | 10 | 6 | 6 | old |
| 499 | Rachel | 瑞秋 | 10 | 6 | 6 | old |
| 506 | Leith | 莱斯 | 10 | 6 | 6 | old |
| 517 | Kristen | 克里斯汀 | 10 | 6 | 6 | old |
| 523 | De Faust | 德瓦斯特 | 10 | 6 | 6 | old |
| 534 | Helena | 海伦娜 | 9 | 6 | 5 | latest |
| 535 | Phoenix | 菲尼克斯 | 10 | 6 | 6 | latest |
| 547 | Selene | 瑟琳娜 | 10 | 6 | 6 | latest |
| 551 | Tyrone | 泰隆 | 10 | 6 | 6 | latest |
| 557 | Catherine | 凯瑟琳 | 10 | 6 | 6 | latest |
| 567 | Vrabel | 芙拉贝尔 | 10 | 6 | 6 | latest |
| 571 | Viperian | 维珀里安 | 10 | 6 | 6 | latest |
| 581 | Jack's Pumpkin | 杰克的南瓜 | 10 | 6 | 6 | latest |
| 582 | Adele | 阿黛尔 | 9 | 6 | 5 | old |
| 589 | Nacali | 娜卡莉 | 10 | 6 | 6 | latest |
| 595 | Sylvina | 西尔维娜 | 9 | 9 | 6 | latest |
| 602 | Grusen | 格鲁瑟恩 | 10 | 8 | 7 | latest |
| 607 | Liora | 莉奥拉 | 10 | 9 | 8 | latest |
| 609 | Ariya | 艾瑞娅 | 10 | 6 | 6 | latest |
| 614 | Karon | 卡隆 | 10 | 6 | 6 | latest |
| 619 | Tagnias | 塔格尼亚斯 | 10 | 8 | 6 | latest |
| 628 | Qin Yue | 秦月 | 10 | 6 | 6 | latest |
| 630 | Jiang Changxing | 江长行 | 9 | 8 | 10 | old |
| 633 | Joe Lever | 乔・雷弗 | 10 | 6 | 6 | latest |

---

## 373 · Freddy 弗瑞
**Role** Destroyer · **Attack** energy · **Generation** old
**Ratings** Damage 9/10 · Defence 6/10 · Assist 2/10

### Signature skill
- **Ⅰ** at `+0` — Open Fire (11月wd)
  Single attack. After hitting a main target, the attack will create a chain of lightning. The lightning will jump to enemy targets in proximity of the main target. The lightning will successively deal 400%, 380%, 360% S-ATK damage to each target it jumps to, and it can also plunder 40% Dodge (absolute value) from all enemies for 1 round. Additionally, increases 100 Accumulator for the ship itself.
- **II** at `+T4` — Open Fire II (弗瑞+T4)
  Single attack. After hitting the main target, forms a chain lightning attack on enemy units in proximity to the main target, dealing 450%, 420%, and 390% damage to each unit in sequence. At the same time, it drains 50% [absolute value] of the Dodge level from all units (lasts for 1 round), and has a 50% chance to weaken all attributes of the hit target by 50% for 1 round. Lastly, recovers 100 Accumulator for self.

### Augment cost (per step)
- `+1` — 5× Destroyer Chip · 100,000 money
- `+2` — 10× Destroyer Chip · 200,000 money
- `+3` — 21× Destroyer Chip · 300,000 money
- `+4` — 28× Destroyer Chip · 500,000 money
- `+5` — 35× Destroyer Chip · 800,000 money
- `+6` — 42× Destroyer Chip · 10× Pandora Power Core
- `+7` — 49× Destroyer Chip · 50× Pandora Power Core
- `+8` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Freddy Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Freddy Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Freddy Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Freddy Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Freddy Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Freddy Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 396 · Snowden 斯诺登
**Role** Destroyer · **Attack** energy · **Generation** old
**Ratings** Damage 9/10 · Defence 6/10 · Assist 5/10

### Signature skill
- **I** at `+0` — Chaos Card I (斯诺登)
  Cross Attack, plunders 40% of Accumulator from targets and then deals 210% S-ATK damage. Ice Cards have a 50% chance to freeze targets for 1 round; Mind Cards have a 50% chance to confuse targets for 1 round; Truth Cards have a 70% chance to expose invisible targets (the rate for each target will be settled independently), finally, recover 100 Accumulators for self.
- **II** at `+T2` — Chaos Card II (斯诺登+T2)
  Cross Attack, plunders 50% of Accumulator from targets and then deals 300% S-ATK damage. Ice Cards have a 50% chance to freeze targets for 1 round; Mind Cards have a 50% chance to confuse targets for 1 round; Truth Cards have a 70% chance to expose invisible targets (the rate for each target will be settled independently), finally, recover 100 Accumulators for self.
- **III** at `+T4` — Chaos Card III (斯诺登+T4)
  Cross Attack, plunders 70% of Accumulator from targets and then deals 380% S-ATK damage. Ice Cards have an 80% chance to freeze targets for 1 round; Mind Cards have an 80% chance to confuse targets for 1 round; Truth Cards have a 100% chance to expose invisible targets (the rate for each target will be settled independently) and self gains 1 round of Invisibility. Finally, recover 100 Accumulators for self.

### Augment cost (per step)
- `+1` — 5× Destroyer Chip · 100,000 money
- `+2` — 10× Destroyer Chip · 200,000 money
- `+3` — 21× Destroyer Chip · 300,000 money
- `+4` — 28× Destroyer Chip · 500,000 money
- `+5` — 35× Destroyer Chip · 800,000 money
- `+6` — 42× Destroyer Chip · 10× Pandora Power Core
- `+7` — 49× Destroyer Chip · 50× Pandora Power Core
- `+8` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Snowden's Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Snowden's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Snowden's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Snowden's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Snowden's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Snowden's Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 413 · Floop 霍普
**Role** Destroyer · **Attack** energy · **Generation** old
**Ratings** Damage 9/10 · Defence 5/10 · Assist 4/10

### Signature skill
- **Ⅰ** at `+0` — Fatal Sting (霍普，致命毒刺)
  Single attack, attack 4 times and each attack can deal 200% S-ATK damage. And then deals 50% of the previous total damage (True Damage) to enemies with 60% or above HP. It can also activate a shield for self which can withstand the damage of one attack for one round, increase 80% Crit and 80% Hit for the team for 1 round. In addition, recover 100 Accumulator for self.
- **Ⅱ** at `+T2` — Fatal Sting Ⅱ (霍普+T2)
  Single attack, attack 4 times and each attack can deal 230% S-ATK damage. And then deals 50% of the previous total damage (True Damage) to enemies with 50% or above HP. It can also activate a shield for self which can withstand the damage of one attack for one round, increase 85% Crit and 85% Hit for the team for 1 round. In addition, recover 100 Accumulator for self.
- **III** at `+T2` — Fatal Sting III (霍普+T2)
  Single attack, attack 5 times and each attack can deal 250% S-ATK damage plus 8M True Damage. And then deals 60% of the previous total damage (True Damage) to enemies with 35% or above HP. It can also activate a shield for self which can withstand the damage of one attack for one round, increase 100% Crit and 100% Hit for the team for 1 round. In addition, recover 100 Accumulator for self.

### Augment cost (per step)
- `+1` — 5× Destroyer Chip · 100,000 money
- `+2` — 10× Destroyer Chip · 200,000 money
- `+3` — 21× Destroyer Chip · 300,000 money
- `+4` — 28× Destroyer Chip · 500,000 money
- `+5` — 35× Destroyer Chip · 800,000 money
- `+6` — 42× Destroyer Chip · 10× Pandora Power Core
- `+7` — 49× Destroyer Chip · 50× Pandora Power Core
- `+8` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Floop’s Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Floop’s Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Floop’s Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Floop’s Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Floop’s Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Floop’s Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 443 · Nu'zogh 恩索斯
**Role** Destroyer · **Attack** energy · **Generation** old
**Ratings** Damage 9/10 · Defence 6/10 · Assist 5/10

### Signature skill
- **Ⅰ** at `+0` — Wrath of the Old Gods (索恩斯，古神之殇)
  Cross attack, plunders 20% Hit Rate from all enemies for 1 round and then deals 250% S-ATK damage and 3M True Damage. Targets hit by the skill will be poisoned for 2 rounds and they will receive 150% S-ATK damage each round. The skill will randomly clear an enemy unit's Accumulator. Receive a shield that can reduce all damage by 60% for 2 rounds. Has a 50% chance to confuse the targets for 1 round. If the skill kills an enemy, then you have a 70% chance to perform an additional skill attack. This can be triggered at least once in a single battle. Recovers 100 Accumulator for self.
- **Ⅱ** at `+T` — Wrath of the Old Gods Ⅱ (索恩斯，古神之殇Ⅱ)
  Cross attack, plunders 50% Hit Rate and 50% Penetration from all enemies for 1 round and then deals 300% S-ATK damage and 5M True Damage. Targets hit by the skill will be poisoned for 2 rounds and they will receive 200% S-ATK damage each round. The skill will randomly clear an enemy unit's Accumulator. Receive a shield that can reduce all damage by 80% for 2 rounds. Has a 60% chance to confuse the targets for 1 round. If the skill kills an enemy, then you have a 80% chance to perform an additional skill attack. This can be triggered at least once in a single battle. Recovers 100 Accumulator for self.
- **Ⅲ** at `+T3` — Wrath of the Old Gods Ⅲ (索恩斯，古神之殇Ⅲ)
  Cross attack, plunders 50% Hit Rate and 50% Penetration from all enemies, and plunder 50% Accumulator from the target, for 1 round and then deals 350% S-ATK damage and 10M True Damage. Targets hit by the skill will be poisoned for 2 rounds and they will receive 250% S-ATK damage each round. The skill will randomly clear an enemy unit's Accumulator. Receive a shield that can reduce all damage by 80% for 2 rounds. Has a 60% chance to confuse the targets for 1 round. If the skill kills an enemy, then you have a 100% chance to perform an additional skill attack. This can be triggered at least once in a single battle. Recovers 100 Accumulator for self.
- **IV** at `+T4` — Wrath of the Old GodsIV (索恩斯，古神之殇Ⅲ)
  Cross attack, plunders 70% Hit Rate and 70% Penetration from all enemies, and plunder 70% Accumulator from the target, for 1 round and then deals 380% S-ATK damage and 12M True Damage. Targets hit by the skill will be poisoned for 2 rounds and they will receive 300% S-ATK damage each round. The skill will randomly clear an enemy unit's Accumulator. Receive a shield that can reduce all damage by 80% for 2 rounds. Has a 100% chance to confuse the targets for 1 round. If the skill kills an enemy, then you have a 100% chance to perform an additional skill attack. If the additional skill attack kills an enemy, you perform a second extra skill attack dealing 80% damage. Recovers 100 Accumulator for self.

### Augment cost (per step)
- `+1` — 5× Destroyer Chip · 100,000 money
- `+2` — 10× Destroyer Chip · 200,000 money
- `+3` — 21× Destroyer Chip · 300,000 money
- `+4` — 28× Destroyer Chip · 500,000 money
- `+5` — 35× Destroyer Chip · 800,000 money
- `+6` — 42× Destroyer Chip · 10× Pandora Power Core
- `+7` — 49× Destroyer Chip · 50× Pandora Power Core
- `+8` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Nu'zogh's Ship Parts · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Nu'zogh's Ship Parts · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Nu'zogh's Ship Parts · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Nu'zogh's Ship Parts · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Nu'zogh's Ship Parts · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Nu'zogh's Ship Parts · 140× Alien Essence · 140× Transcendence Core

---

## 454 · K K
**Role** Destroyer · **Attack** energy · **Generation** old
**Ratings** Damage 10/10 · Defence 6/10 · Assist 6/10

### Signature skill
- **Ⅰ** at `+0` — Death NoticeⅠ (K,死亡宣告)
  Cross attack, deals 300% S-ATK damage and an additional 3M true damage (ignores defense), hit targets cannot be healed, for 2 rounds. There's also a 50% chance of cursing all enemy units (probability for each unit calculated separately) for 2 rounds. When the curse ends, hit targets will suffer 10000% S-ATK damage. After the attack is complete, there's a 100% chance of becoming invisible for 1 round. Finally, recovers 100 Accumulator for self.
- **Ⅱ** at `+T` — Death NoticeⅡ (K,死亡宣告Ⅱ)
  Cross attack, deals 330% S-ATK damage and an additional 5M true damage (ignores defense), hit targets cannot be healed, for 2 rounds. There's also a 60% chance of cursing all enemy units (probability for each unit calculated separately) for 2 rounds. When the curse ends, hit targets will suffer 12000% S-ATK damage. After the attack is complete, there's a 100% chance of becoming invisible for 1 round. Finally, recovers 100 Accumulator for self.
- **Ⅲ** at `+T3` — Death NoticeⅢ (K,死亡宣告Ⅲ)
  Cross attack, deals 380% S-ATK damage and an additional 8M true damage (ignores defense), hit targets cannot be healed, for 2 rounds. There's also a 60% chance of cursing all enemy units (probability for each unit calculated separately) for 2 rounds. When the curse ends, hit targets will suffer 12000% S-ATK damage. There's a 100% chance to confuse targets for 1 round.There's a 100% chance to expose invisible enemies.After the attack is complete, there's a 100% chance of becoming invisible for 1 round. Finally, recovers 100 Accumulator for self.
- **Ⅳ** at `+T4` — Death NoticeⅣ (K,死亡宣告Ⅲ)
  Cross attack, deals 380% S-ATK damage and an additional 10M true damage (ignores defense), hit targets cannot be healed, for 2 rounds. There's also a 75% chance of cursing all enemy units (probability for each unit calculated separately) for 2 rounds. When the curse ends, hit targets will suffer 15000% S-ATK damage. There's a 100% chance to confuse targets for 1 round.There's a 100% chance to expose invisible enemies. After the attack is complete, there's a 100% chance of becoming invisible for 1 round. Finally, recovers 100 Accumulator for self.

### Augment cost (per step)
- `+1` — 5× Destroyer Chip · 100,000 money
- `+2` — 10× Destroyer Chip · 200,000 money
- `+3` — 21× Destroyer Chip · 300,000 money
- `+4` — 28× Destroyer Chip · 500,000 money
- `+5` — 35× Destroyer Chip · 800,000 money
- `+6` — 42× Destroyer Chip · 10× Pandora Power Core
- `+7` — 49× Destroyer Chip · 50× Pandora Power Core
- `+8` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× K Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× K Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× K Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× K Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× K Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× K Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 465 · Deena Hineston 蒂娜·海因斯顿
**Role** Destroyer · **Attack** energy · **Generation** old
**Ratings** Damage 10/10 · Defence 6/10 · Assist 6/10

### Signature skill
- **Ⅰ** at `+0` — Radiation BombⅠ (辐射光弹)
  Cross attack, deals 350% S-ATK damage and 5M True Damage. It has a 100% chance to apply Forbid Revive on enemy bound Heroes with reviving skills, for 1 round (on enemy ships with reviving skills (not including lieutenants)). In addition, it has a 50% chance to lock all enemies (probability calculated separately for each target), for 1 round. Then, becomes invisible for 1 round. Finally, recovers 100 Accumulator for self.
- **Ⅱ** at `+T` — Radiation BombⅡ (蒂娜，辐射光弹Ⅱ)
  Cross attack, plunders 30% Crit and 30% Penetration from all enemies before dealing 380% S-ATK damage and 8M True Damage. It has a 100% chance to apply Forbid Revive on enemy bound Heroes with reviving skills, for 1 round (while the debuff is in effect, the bound Hero will not be able to resurrect friendly units). In addition, it has a 75% chance to lock all enemies (probability calculated separately for each target), for 1 round. Then, becomes invisible for 1 round. Finally, recovers 100 Accumulator for self.
- **Ⅲ** at `+T3` — Radiation BombⅢ (蒂娜，辐射光弹Ⅲ)
  Cross attack, plunders 50% Crit and 50% Penetration from all enemies before dealing 400% S-ATK damage and 10M True Damage. It has a 100% chance to apply Forbid Revive on enemy bound Heroes with reviving skills, for 1 round (while the debuff is in effect, the bound Hero will not be able to resurrect friendly units).Has a 60% chance (probability for each target calculated separately) to apply Forbid Revive on all enemy Lieutenants with reviving skills, for 2 rounds (prevents at least one Lieutenant from reviving each time this skill is cast).Clears all buffs (including stat boosts, shields, immunity skill effects) from targets. Then, has a 50% chance to forbid all enemy units (probability calculated separately for each unit) from using their skill for 1 round. In addition, it has a 75% chance to lock all enemies (probability calculated separately for each target), for 1 round. Then, becomes invisible for 1 round. Finally, recovers 100 Accumulator for self.
- **IV** at `+T4` — Radiation BombIV (蒂娜，辐射光弹IV)
  Cross attack, plunders 80% Crit and 80% Penetration from all enemies and 50% Accumulator from targets, before dealing 450% S-ATK damage and 15M True Damage. It has a 100% chance to apply Forbid Revive on enemy bound Heroes with reviving skills, for 1 round (while the debuff is in effect, the bound Hero will not be able to resurrect friendly units). Has a 100% chance (probability for each target calculated separately) to apply Forbid Revive on all enemy Lieutenants with reviving skills, for 2 rounds (prevents at least one Lieutenant from reviving each time this skill is cast). Enemies that are revived become Locked for 2 rounds. Clears all buffs (including stat boosts, shields and immunity skill effects) from targets. Then, has a 65% chance to forbid all enemy units (probability calculated separately for each unit) from using their skill for 1 round. In addition, it has a 75% chance to lock all enemies (probability calculated separately for each target) for 1 round. Then, becomes invisible for 1 round and will not lose invisibility for as long as there is another allied unit alive (can be seen by Eye of True Sight). Finally, recovers 100 Accumulator for self. At the start of the battle, self becomes invisible for 1 round, and will not lose invisibility for as long as there is another allied unit alive (can be seen by Eye of True Sight).
- **6** at `Awaken` — — (蒂娜，敌方复活触发)
  _(no English description shipped)_

### Augment cost (per step)
- `+1` — 5× Destroyer Chip · 100,000 money
- `+2` — 10× Destroyer Chip · 200,000 money
- `+3` — 21× Destroyer Chip · 300,000 money
- `+4` — 28× Destroyer Chip · 500,000 money
- `+5` — 35× Destroyer Chip · 800,000 money
- `+6` — 42× Destroyer Chip · 10× Pandora Power Core
- `+7` — 49× Destroyer Chip · 50× Pandora Power Core
- `+8` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Deena Hineston Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Deena Hineston Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Deena Hineston Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Deena Hineston Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Deena Hineston Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Deena Hineston Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 482 · Chaos 混沌
**Role** Destroyer · **Attack** energy · **Generation** old
**Ratings** Damage 10/10 · Defence 6/10 · Assist 6/10

### Signature skill
- **I** at `+0` — Plague I (混沌，瘟疫)
  Cross attack; deals 350% S-ATK damage to targets and there is a 50% chance to applies 3 stacks of Plague effects to 1 random target (if target is already plagued, then add 3 additional stack) for 99 rounds. Also, makes self immune to [Plague] for 2 rounds. Whenever a plagued target casts a skill, normal attack, or restores 100 Accumulator, it will be inflicted with 3, 1, and 1 Plague stacks, respectively (max 12 stacks). For every 1 Plague stack it has, the target receives a 5% reduction in damage dealt, 5% increase in damage taken, and [1M x number of stacks] True Damage at the end of each of its turns. If the target dies with 6 or more Plague stacks, then Forbidding Skill Use will be applied to all enemies for 1 round; in addition, 2 Plague stacks will be transmitted to the target's adjacent units (if there are no adjacent enemy units, then transmission will not occur). When a target has 12 Plague stacks, it will die immediately and cannot be revived by any means. Meanwhile, recovers 100 Accumulator for self.
- **II** at `+T` — Plague II (混沌T，瘟疫)
  Cross attack; deals 360% S-ATK damage to targets and there is a 60% chance to apply 3 stacks of Plague effects to 1 random target (if target is already plagued, then add 3 additional stacks) for 99 rounds. Also, makes self immune to [Plague] for 2 rounds. Whenever a plagued target casts a skill, normal attack, or restores 100 Accumulator, it will be inflicted with 3, 1, and 1 Plague stacks, respectively (max 12 stacks). For every 1 Plague stack it has, the target receives a 8% reduction in damage dealt, 8% increase in damage taken, and [2M x number of stacks] True Damage at the end of each of its turns. If the target dies with 6 or more Plague stacks, then Forbidding Skill Use will be applied to all enemies for 1 round; in addition, 2 Plague stacks will be transmitted to the target's adjacent units (if there are no adjacent enemy units, then transmission will not occur). When a target has 12 Plague stacks, it will die immediately and cannot be revived by any means. Meanwhile, recovers 100 Accumulator for self.
- **III** at `+T3` — Plague III (混沌T3，瘟疫)
  Cross attack; deals 360% S-ATK damage to targets and there is a 100% chance to apply 4 stacks of Plague effects to 2 random target (if target is already plagued, then add 4 additional stacks) for 99 rounds. Also, makes self immune to [Plague] for 2 rounds. Whenever a plagued target casts a skill, normal attack, or restores 100 Accumulator, it will be inflicted with 3, 1, and 1 Plague stacks, respectively (max 12 stacks). For every 1 Plague stack it has, the target receives a 8% reduction in damage dealt, 8% increase in damage taken, and [2M x number of stacks] True Damage at the end of each of its turns. If the target dies with 6 or more Plague stacks, then Forbidding Skill Use will be applied to all enemies for 1 round; in addition, 2 Plague stacks will be transmitted to the target's adjacent units (if there are no adjacent enemy units, then transmission will not occur). When a target has 12 Plague stacks, it will die immediately and cannot be revived by any means. Meanwhile, recovers 100 Accumulator for self.
- **IV** at `+T4` — Plague IV (混沌T4，瘟疫)
  Cross attack; deals 380% S-ATK damage to targets and there is a 100% chance to apply 4 stacks of Plague effects to 2 random targets (if target is already plagued, then add 4 additional stacks) for 99 rounds. Also, makes self immune to [Plague] for 2 rounds. Whenever a plagued target casts a skill, normal attack, or restores 100 Accumulator, it will be inflicted with 4, 2, and 2 Plague stacks, respectively (max 12 stacks). For every 1 Plague stack it has, the target receives an 8% reduction in damage dealt, 8% increase in damage taken, and [3M x number of stacks] True Damage at the end of each of its turns. If the target dies with 6 or more Plague stacks, then deal S-ATK damage to all enemies equal to 60% of the killed unit's max HP and apply Forbidding Skill Use to all enemies for 1 round; in addition, 4 Plague stacks will be transmitted to the target's adjacent units (if there are no adjacent enemy units, then transmission will not occur). When a target has 12 Plague stacks, it will die (ignores immunity to lethal attacks and instant destruction) after its next action and cannot be revived by any means. Meanwhile, recovers 100 Accumulator for self. Apply 4 stacks of Plague to 2 random targets at the start of each battle.

### Augment cost (per step)
- `+1` — 5× Destroyer Chip · 100,000 money
- `+2` — 10× Destroyer Chip · 200,000 money
- `+3` — 21× Destroyer Chip · 300,000 money
- `+4` — 28× Destroyer Chip · 500,000 money
- `+5` — 35× Destroyer Chip · 800,000 money
- `+6` — 42× Destroyer Chip · 10× Pandora Power Core
- `+7` — 49× Destroyer Chip · 50× Pandora Power Core
- `+8` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Chaos Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Chaos Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Chaos Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Chaos Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Chaos Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Chaos Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 499 · Rachel 瑞秋
**Role** Destroyer · **Attack** energy · **Generation** old
**Ratings** Damage 10/10 · Defence 6/10 · Assist 6/10

### Signature skill
- **I** at `+0` — Lightfusion Blaster I (聚合光炮Ⅰ)
  Launches a Single Attack against the enemy with the lowest HP%, dealing 260% S-ATK damage, with an extra 1% damage for each 1% HP the target is missing. Each time this skill kills an enemy, it will attack again but the damage is reduced by 50% per new attack (each attack deals 50% less damage than the last). Grants self Eye of True Sight for 2 rounds. Finally, recovers 100 Accumulator for self. Note: comes with 30% extra Penetration.
- **II** at `+T` — Lightfusion Blaster II (聚合光炮Ⅱ)
  Launches a Single Attack against the enemy with the lowest HP%, dealing 280% S-ATK damage, with an extra 2% damage for each 1% HP the target is missing. Each time this skill kills an enemy, it will attack again but the damage is reduced by 40% per new attack (each attack deals 40% less damage than the last). Grants self Eye of True Sight for 2 rounds. Add a Guaranteed Hit to yourself for 2 round. Finally, recovers 100 Accumulator for self. Note: comes with 50% extra Penetration.
- **III** at `+T3` — Lightfusion Blaster III (聚合光炮Ⅲ)
  Launches a Single Attack against the enemy with the lowest HP%. Starts by stealing 100% of the target's Accumulator before dealing 300% S-ATK damage, with an extra 3% damage for each 1% HP the target is missing. Each time this skill kills an enemy, it will attack again but the damage is reduced by 30% per new attack (each attack deals 30% less damage than the last). Grants self Eye of True Sight for 2 rounds. Add a Guaranteed Hit to yourself for 2 round. Finally, recovers 100 Accumulator for self. Note: comes with 80% extra Penetration.
- **IV** at `+T4` — Lightfusion BlasterIV (聚合光炮IV)
  Launches a Single Attack against the enemy with the lowest HP%. Starts by stealing 100% of the target's Accumulator before dealing 360% S-ATK damage, with an extra 4% damage for each 1% HP the target is missing. Grants self Eye of True Sight and Guaranteed Hit for 2 rounds. Finally, recovers 100 Accumulator for self. Note: comes with 80% extra Penetration.

### Augment cost (per step)
- `+1` — 5× Destroyer Chip · 100,000 money
- `+2` — 10× Destroyer Chip · 200,000 money
- `+3` — 21× Destroyer Chip · 300,000 money
- `+4` — 28× Destroyer Chip · 500,000 money
- `+5` — 35× Destroyer Chip · 800,000 money
- `+6` — 42× Destroyer Chip · 10× Pandora Power Core
- `+7` — 49× Destroyer Chip · 50× Pandora Power Core
- `+8` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Rachel Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Rachel Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Rachel Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Rachel Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Rachel Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Rachel Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 506 · Leith 莱斯
**Role** Destroyer · **Attack** energy · **Generation** old
**Ratings** Damage 10/10 · Defence 6/10 · Assist 6/10

### Signature skill
- **Ⅰ** at `+0` — Fury of BloodⅠ (莱斯，浴血之怒Ⅰ)
  Cross Attack, leeches 30% Penetration from all enemies and inflicts 380% S-ATK damage to the target. Leith's skills are all Crit hits and deal 50% extra damage to shields. Gains a stack of [Fury] (stacks up to 3 times) when an ally dies, he doesn't get a kill in a round, or an enemy uses a skill. Loses a stack of [Fury] when he kills an enemy. Every stack of [Fury] increases Crit ATK by 60% and True Damage by 5M, and grants the following extra skill effects: 1-Stack: Leeches 30% Accumulator from the target before attack. 2-Stack: Skills ignore Lethal Attack Immunity and Stasis and have 100% accuracy. 3-Stack: Enemies killed by Leith have a 40% chance of being locked for 1 round after revival. Gains Invisibility for 1 round. Gains Eye of True Sight for 1 round. Deals True Damage equal to 150% of the total previous S-ATK damage dealt. Has a 50% chance to inflict Weaken on all enemies (probability differs among units), reducing all stats by 50% for a round. Lastly, recovers 100 Accumulator. When battle begins or Leith revives, gains 3 stacks of [Fury].
- **Ⅱ** at `+T` — Fury of BloodⅡ (莱斯，浴血之怒Ⅱ)
  Cross Attack , leeches 50% Penetration from all enemies and inflicts 410% S-ATK damage to the target. Leith's skills are all Crit hits and deal 80% extra damage to shields. Gains a stack of [Fury] (stacks up to 3 times) when an ally dies, he doesn't get a kill in a round, or an enemy uses a skill. Loses a stack of [Fury] when he kills an enemy. Every stack of [Fury] increases Crit ATK by 90% and True Damage by 6M, and grants the following extra skill effects: 1-Stack: Clears the target's buffs and leeches 40% Accumulator from it before attack. 2-Stack: Skills ignore Lethal Attack Immunity and Stasis and have 100% accuracy. 3-Stack: Enemies killed by Leith have a 50% chance of being locked for 1 round after revival. Gains Invisibility for 1 round. Gains Eye of True Sight for 1 round. Deals True Damage equal to 180% of the total previous S-ATK damage dealt. Has a 50% chance to inflict Weaken on all enemies (probability differs among units), reducing all stats by 50% for a round. Lastly, recovers 100 Accumulator. When battle begins or Leith revives, gains 3 stacks of [Fury].
- **Ⅲ** at `+T3` — Fury of BloodⅢ (莱斯，浴血之怒Ⅲ)
  Cross Attack , leeches 50% Penetration from all enemies and inflicts 450% S-ATK damage to the target. Leith's skills are all Crit hits and deal 100% extra damage to shields. Gains a stack of [Fury] (stacks up to 3 times) when an ally dies, he doesn't get a kill in a round, or an enemy uses a skill. Loses a stack of [Fury] when he kills an enemy. Every stack of [Fury] increases Crit ATK by 130% and True Damage by 8M, and grants the following extra skill effects: 1-Stack: Clears the target's buffs and leeches 50% Accumulator from it. 2-Stack: Skills ignore Lethal Attack Immunity and Stasis and have 100% accuracy. 3-Stack: There's a 50% chance that enemies killed by Leith won't be able to revive or rebirth. Gains Invisibility for 1 round. Gains Eye of True Sight for 1 round. Deals True Damage equal to 210% of the total previous S-ATK damage dealt. Has a 50% chance to inflict Weaken on all enemies (probability differs among units), reducing all stats by 50% for a round. Lastly, recovers 100 Accumulator. When battle begins or Leith revives, gains 3 stacks of [Fury].
- **IV** at `+T4` — Fury of Blood IV (莱斯T4，浴血之怒IV)
  Cross Attack, leeches 80% Penetration from all enemies and inflicts 480% S-ATK damage to the target. Leith's skills are all Crit hits and deal 150% extra damage to shields. Gains a stack of [Fury] (stacks up to 3 times) when an ally dies, he doesn't get a kill in a round, or an enemy uses a skill. Loses a stack of [Fury] when he kills an enemy. Every stack of [Fury] increases Crit ATK by 150% and True Damage by 12M, and grants the following extra skill effects: 1-Stack: Clears the target's buffs and leeches 70% Accumulator from it. 2-Stack: Skills ignore Lethal Attack Immunity and Stasis and have 100% accuracy. 3-Stack: There's a 70% chance that enemies killed by Leith won't be able to revive or rebirth. Gains Invisibility for 1 round. Gains Eye of True Sight for 1 round. Deals True Damage equal to 260% of the total previous S-ATK damage dealt. If the skill kills an enemy, Leith deals True Damage equal to 100% of the damage dealt to all enemies. Has a 50% chance to inflict Weaken on all enemies (probability differs among units), reducing all stats by 50% for a round. Lastly, recovers 100 Accumulator. When battle begins or Leith revives, gains 3 stacks of [Fury].

### Augment cost (per step)
- `+1` — 5× Destroyer Chip · 100,000 money
- `+2` — 10× Destroyer Chip · 200,000 money
- `+3` — 21× Destroyer Chip · 300,000 money
- `+4` — 28× Destroyer Chip · 500,000 money
- `+5` — 35× Destroyer Chip · 800,000 money
- `+6` — 42× Destroyer Chip · 10× Pandora Power Core
- `+7` — 49× Destroyer Chip · 50× Pandora Power Core
- `+8` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Leith Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Leith Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Leith Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Leith Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Leith Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Leith Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 517 · Kristen 克里斯汀
**Role** Destroyer · **Attack** energy · **Generation** old
**Ratings** Damage 10/10 · Defence 6/10 · Assist 6/10

### Signature skill
- **Ⅰ** at `+0` — Doom Force (克里斯汀)
  Cross attack, deals 300% S-ATK damage and boosts the E-ATK of allied Destroyers by 80% for 2 rounds. Lastly, you recover 100 Accumulator.

### Augment cost (per step)
- `+1` — 5× Destroyer Chip · 100,000 money
- `+2` — 10× Destroyer Chip · 200,000 money
- `+3` — 21× Destroyer Chip · 300,000 money
- `+4` — 28× Destroyer Chip · 500,000 money
- `+5` — 35× Destroyer Chip · 800,000 money
- `+6` — 42× Destroyer Chip · 10× Pandora Power Core
- `+7` — 49× Destroyer Chip · 50× Pandora Power Core
- `+8` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Kristen Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Kristen Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Kristen Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Kristen Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Kristen Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Kristen Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 523 · De Faust 德瓦斯特
**Role** Destroyer · **Attack** energy · **Generation** old
**Ratings** Damage 10/10 · Defence 6/10 · Assist 6/10

### Signature skill
- **Ⅰ** at `+0` — Night CurseⅠ (德瓦斯特，暗夜诅咒)
  Cross Attack, deals 260% S-ATK damage and applies the enemy with the highest S-ATK with Dark Curse for 2 rounds. Dark Curse: Reduces damage by 20%. When an enemy loses HP, they deal 20% extra link damage (True Damage that ignores shields' damage reduction) to other enemies applied with Dark Curse. When using skills, clears all Dark Curse effects on enemies and reselects a target to apply Dark Curse to. Applies all enemies with Night Curse for 2 rounds, making them take True Damage equal to 40% of De Faust's S-ATK when taking action, and the damage is not affected by shields that resist damage. Lastly, recovers 100 Accumulator.
- **Ⅱ** at `+T` — Night CurseⅡ (德瓦斯特，暗夜诅咒)
  Cross Attack, deals 280% S-ATK damage and applies the enemy with the highest S-ATK and another random enemy with Dark Curse for 1 round. Dark Curse: Reduces damage by 25%. When an enemy loses HP, they deal 25% extra link damage (True Damage that ignores shields' damage reduction) to other enemies applied with Dark Curse. When using skills, clears all Dark Curse effects on enemies and reselects a target to apply Dark Curse to. Applies all enemies with Night Curse for 2 rounds, making them take True Damage equal to 50% of De Faust's S-ATK when taking action, and the damage is not affected by shields that resist damage. Lastly, recovers 100 Accumulator.
- **Ⅲ** at `+T3` — Night CurseⅢ (德瓦斯特，暗夜诅咒)
  Cross Attack, deals 300% S-ATK damage and applies the enemy with the highest S-ATK and another random enemy with Dark Curse for 1 round. Dark Curse: Reduces damage by 30%. When an enemy loses HP, they deal 30% extra link damage (True Damage that ignores shields' damage reduction) to other enemies applied with Dark Curse. When an enemy applied with Dark Curse receives any debuffs, stat debuffs, control effects and Instant Destruction, the other enemies with Dark Curse receive the same effects (ignores immunity and protection). When using skills, clears all Dark Curse effects on enemies and reselects a target to apply Dark Curse to. Applies all enemies with Night Curse for 2 rounds, making them take True Damage equal to 80% of De Faust's S-ATK when taking action, and the damage is not affected by shields that resist damage. When an enemy applied with Night Curse gains or recovers Accumulator through skills, has a 50% chance to reduce the increased Accumulator by 35%. Lastly, recovers 100 Accumulator.
- **IV** at `+T4` — Night CurseIV (德瓦斯特，暗夜诅咒)
  Cross Attack, deals 340% S-ATK damage and applies the enemy with the highest S-ATK and 2 other random enemies with Dark Curse for 2 rounds. Dark Curse: Reduces damage by 40%. When an enemy loses HP, they deal 35% extra link damage (True Damage that ignores shields' damage reduction) to other enemies applied with Dark Curse. When an enemy applied with Dark Curse receives any debuffs, stat debuffs, control effects and Instant Destruction, the other enemies with Dark Curse receive the same effects (ignores immunity and protection). When an enemy applied with Dark Curse dies, De Faust gains S-ATK equal to 100% of the enemy's S-ATK upon death (stackable, lasts until death or the end of the battle) and Dark Conceal, becoming unable to be attacked or targeted by skill effects for 1 round. When using skills, clears all Dark Curse effects on enemies and reselects a target to apply Dark Curse to. Applies all enemies with Night Curse for 2 rounds, making them take True Damage equal to 100% of De Faust's S-ATK when taking action, and the damage is not affected by shields that resist damage. When an enemy applied with Night Curse gains or recovers Accumulator through skills, has a 65% chance to reduce the increased Accumulator by 50%. Lastly, recovers 100 Accumulator. At the start of battle, applies the enemy with the highest S-ATK and 2 other random enemies with Dark Curse and all enemies with Night Curse for 2 rounds.

### Augment cost (per step)
- `+1` — 5× Destroyer Chip · 100,000 money
- `+2` — 10× Destroyer Chip · 200,000 money
- `+3` — 21× Destroyer Chip · 300,000 money
- `+4` — 28× Destroyer Chip · 500,000 money
- `+5` — 35× Destroyer Chip · 800,000 money
- `+6` — 42× Destroyer Chip · 10× Pandora Power Core
- `+7` — 49× Destroyer Chip · 50× Pandora Power Core
- `+8` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× De Faust Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× De Faust Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× De Faust Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× De Faust Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× De Faust Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× De Faust Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 534 · Helena 海伦娜
**Role** Destroyer · **Attack** energy · **Generation** latest
**Ratings** Damage 9/10 · Defence 6/10 · Assist 5/10

### Skill panels
**Slot 1 — Doom Storm** (id 1548, unlocks at `+0`)
  - **Ⅰ** at `+0` — Doom StormⅠ (海伦娜，改造+0)
    Vertical Attack, attacks the target hit 4 times, each attack dealing 180% S-ATK damage. You also gain Damage Boost (lasting 2 rounds) and 40% Crit Rate (absolute value, lasting 2 rounds). The attacks ignore 35% of the enemy's S-DEF. Each cast also increases your E-ATK by 400K, stacking up to 3.2M. Lastly, you recover 100 Accumulator. Damage Boost: For every 1% of max HP the target lost, you deal 1% increased S-ATK damage (effect stacks with similar buffs).
  - **Ⅱ** at `+7` — Doom StormⅡ (海伦娜，改造+7)
    Vertical Attack, attacks the target hit 4 times, each attack dealing 200% S-ATK damage. You also gain Damage Boost (lasting 2 rounds) and 60% Crit Rate (absolute value, lasting 2 rounds). The attacks ignore 45% of the enemy's S-DEF. Each cast also increases your E-ATK by 600K, stacking up to 4.8M. Lastly, you recover 100 Accumulator. Damage Boost: For every 1% of max HP the target lost, you deal 2% increased S-ATK damage (effect stacks with similar buffs).
  - **Ⅲ** at `+13` — Doom StormⅢ (海伦娜，改造+13)
    Vertical Attack, attacks the target hit 4 times, each attack dealing 220% S-ATK damage. You also gain Damage Boost (lasting 2 rounds) and 80% Crit Rate (absolute value, lasting 2 rounds). The attacks ignore 55% of the enemy's S-DEF. Each cast also increases your E-ATK by 800K, stacking up to 6.4M. Lastly, you recover 100 Accumulator. Damage Boost: For every 1% of max HP the target lost, you deal 3% increased S-ATK damage (effect stacks with similar buffs).
  - **Ⅳ** at `+T` — Doom StormIV (海伦娜，改造+16)
    Vertical Attack, attacks the target hit 4 times, each attack dealing 240% S-ATK damage and inflicting Shield Shatter. You also gain Damage Boost (lasting 2 rounds) and 80% Crit Rate (absolute value, lasting 2 rounds). The attacks ignore 75% of the enemy's S-DEF. Each cast also increases your E-ATK by 1M, stacking up to 8M. Lastly, you recover 100 Accumulator. Damage Boost: For every 1% of max HP the target lost, you deal 4% increased S-ATK damage (effect stacks with similar buffs). Shield Shatter (only works during PvE encounters): Shatters the target's damage shields, whether applied to that target specifically or to the entire enemy formation.

**Slot 2 — Doom Nova** (id 1549, unlocks at `+3`)
  - **Ⅰ** at `+3` — Doom NovaⅠ (海伦娜技能2，LV1)
    (Takes effect at the start of battle; only works during PvE encounters) Deals 50% increased damage. You have a 35% chance when acting each turn to be able to act again.
  - **Ⅱ** at `+9` — Doom NovaⅡ (海伦娜技能2，LV2)
    (Takes effect at the start of battle; only works during PvE encounters) Deals 100% increased damage. You have a 45% chance when acting each turn to be able to act again.
  - **Ⅲ** at `+15` — Doom NovaⅢ (海伦娜技能2，LV3)
    (Takes effect at the start of battle; only works during PvE encounters) Deals 150% increased damage. You have a 55% chance when acting each turn to be able to act again, while dealing 10% increased damage.
  - **Ⅳ** at `+T4` — Doom NovaIV (海伦娜技能2，LV4)
    (Takes effect at the start of battle; only works during PvE encounters) Deals 300% increased damage. You have a 65% chance when acting each turn to be able to act again, while dealing 20% increased damage.

**Slot 3 — Doom Force** (id 1550, unlocks at `+5`)
  - **Ⅰ** at `+5` — Doom ForceⅠ (海伦娜技能3，LV1)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): E-ATK: +40% S-ATK: +30% Crit ATK (Absolute Value): +20%
  - **Ⅱ** at `+11` — Doom ForceⅡ (海伦娜技能3，LV2)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): E-ATK: +70% S-ATK: +60% Crit ATK (Absolute Value): +30%
  - **Ⅲ** at `+T1` — Doom ForceⅢ (海伦娜技能3，LV3)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): E-ATK: +100% S-ATK: +90% Crit ATK (Absolute Value): +40%
  - **Ⅳ** at `+T3` — Doom ForceIV (海伦娜技能3，LV4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): E-ATK: +150% S-ATK: +120% Crit ATK (Absolute Value): +60%

### Augment cost (per step)
- `+1` — 5× Destroyer Chip · 100,000 money
- `+2` — 10× Destroyer Chip · 200,000 money
- `+3` — 21× Destroyer Chip · 300,000 money
- `+4` — 28× Destroyer Chip · 500,000 money
- `+5` — 35× Destroyer Chip · 800,000 money
- `+6` — 42× Destroyer Chip · 10× Pandora Power Core
- `+7` — 49× Destroyer Chip · 50× Pandora Power Core
- `+8` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Helena Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Helena Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Helena Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Helena Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Helena Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Helena Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 535 · Phoenix 菲尼克斯
**Role** Destroyer · **Attack** energy · **Generation** latest
**Ratings** Damage 10/10 · Defence 6/10 · Assist 6/10

### Skill panels
**Slot 1 — Doom of Ruin** (id 1554, unlocks at `+0`)
  - **Ⅰ** at `+0` — Doom of RuinⅠ (菲尼克斯技能1)
    Scorch of Ruin (Starblaze Form): Cross Attack, deals 320% S-ATK damage to targets, with a 40% chance (probability for each target is calculated independently) to apply 1 stack of Scorch. Scorch lasts 99 rounds. You also gain Eye of True Sight for 99 rounds. Lastly, you recover 100 Accumulator. Doom Meteora (Doom Form): Cross attack; plunders 20% Accumulator and 50% Penetration (Absolute value; lasts 1 round) from targets before dealing 360% S-ATK damage to targets. All targets with Scorch also take True Damage equal to 10% of the Total S-ATK Damage of the initial hit multiplied by their Scorch stacks. After this, the skill has a 45% chance to trigger Scorch damage (probability calculated individually for each unit), dealing True Damage equal to Scorch stacks multiplied by 40% of S-ATK damage. Lastly, you recover 100 Accumulator. Scorch: Stacks up to 3 times. Deals True Damage equal to Stacks multiplied by 20% of S-ATK Damage before the target acts. This damage ignores shields' damage reduction. Also reduces the healing recovery and healing effect of affected targets by 45%. Scorch stacks are cleansed upon revival.
  - **Ⅱ** at `+5` — Doom of RuinⅡ (菲尼克斯技能1)
    Scorch of Ruin (Starblaze Form): Cross Attack, deals 340% S-ATK damage to targets, with a 50% chance (probability for each target is calculated independently) to apply 1 stack of Scorch. Scorch lasts 99 rounds. You also gain Eye of True Sight for 99 rounds. Lastly, you recover 100 Accumulator. Doom Meteora (Doom Form): Cross attack; plunders 30% Accumulator and 60% Penetration (Absolute value; lasts 1 round) from targets before dealing 400% S-ATK damage to targets. All targets with Scorch also take True Damage equal to 15% of the Total S-ATK Damage of the initial hit multiplied by their Scorch stacks, while healing you for 30% of S-ATK damage. After this, the skill has a 55% chance to trigger Scorch damage and Accumulator reduction (probability calculated individually for each unit), dealing True Damage equal to Scorch stacks multiplied by 60% of S-ATK damage and reducing Accumulator equal to Scorch stacks multiplied by 20. Lastly, you recover 100 Accumulator. Scorch: Stacks up to 3 times. Deals True Damage equal to Stacks multiplied by 30% of S-ATK Damage before the target acts. This damage ignores shields' damage reduction. Also reduces Accumulator equal to Scorch stacks multiplied by 10 (not affected by immunity). Also reduces the healing recovery and healing effect of affected targets by 55%. Scorch stacks are cleansed upon revival.
  - **Ⅲ** at `+12` — Doom of RuinⅢ (菲尼克斯技能1)
    Scorch of Ruin (Starblaze Form): Cross Attack, deals 360% S-ATK damage to targets, with a 60% chance (probability for each target is calculated independently) to apply Scorch. Scorch lasts 99 rounds. You also gain Eye of True Sight for 99 rounds. Lastly, you recover 100 Accumulator. Doom Meteora (Doom Form): Cross attack; plunders 40% Accumulator (not affected by immunity) and 80% Penetration (Absolute value; lasts 1 round) from targets before dealing 440% S-ATK damage to targets. All targets with Scorch also take True Damage equal to 20% of the Total S-ATK Damage of the initial hit multiplied by their Scorch stacks, while healing you for 40% of S-ATK damage. After this, the skill has a 65% chance to trigger Scorch damage and Accumulator reduction (probability calculated individually for each unit), dealing True Damage equal to Scorch stacks multiplied by 80% of S-ATK damage and reducing Accumulator equal to Scorch stacks multiplied by 25. Lastly, you recover 100 Accumulator. Scorch: Stacks up to 3 times. Deals True Damage equal to Stacks multiplied by 40% of S-ATK Damage before the target acts. This damage ignores shields' damage reduction. Also reduces Accumulator equal to Scorch stacks multiplied by 15 (not affected by immunity). Also reduces the healing recovery and healing effect of affected targets by 65%. Scorch stacks are cleansed upon revival.
  - **Ⅳ** at `+15` — Doom of RuinIV (菲尼克斯技能1)
    Scorch of Ruin (Starblaze Form): Cross Attack, deals 380% S-ATK damage to targets, with a 75% chance (probability for each target is calculated independently) to apply Scorch. Scorch lasts 99 rounds. You also gain Eye of True Sight for 99 rounds. Lastly, you recover 100 Accumulator. Doom Meteora (Doom Form): Cross attack; plunders 50% Accumulator (not affected by immunity) and 100% Penetration (Absolute value; lasts 1 round) from targets before dealing 480% S-ATK damage to targets. All targets with Scorch also take True Damage equal to 25% of the Total S-ATK Damage of the initial hit multiplied by their Scorch stacks, while healing you for 50% of S-ATK damage. After this, the skill has a 75% chance to trigger Scorch damage and Accumulator reduction (probability calculated individually for each unit), dealing True Damage equal to Scorch stacks multiplied by 100% of S-ATK damage and reducing Accumulator equal to Scorch stacks multiplied by 30. Lastly, you recover 100 Accumulator. Scorch: Stacks up to 3 times. Deals True Damage equal to Stacks multiplied by 50% of S-ATK Damage before the target acts. This damage ignores shields' damage reduction. Also reduces Accumulator equal to Scorch stacks multiplied by 20 (not affected by immunity). Also reduces the healing recovery and healing effect of affected targets by 75%. Scorch stacks reduce to 1 upon revival.

**Slot 2 — Flames of Ruin** (id 1556, unlocks at `+1`)
  - **Ⅰ** at `+1` — Flames of RuinⅠ (菲尼克斯技能3)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +60% E-ATK: +60% Penetration (Absolute Value): +30% Crit Rate (Absolute Value): +30%
  - **Ⅱ** at `+7` — Flames of RuinⅡ (菲尼克斯技能3)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +90% E-ATK: +90% Penetration (Absolute Value): +50% Crit Rate (Absolute Value): +50%
  - **Ⅲ** at `+13` — Flames of RuinⅢ (菲尼克斯技能3)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +120% E-ATK: +120% Penetration (Absolute Value): +70% Crit Rate (Absolute Value): +70%
  - **Ⅳ** at `+T3` — Flames of RuinIV (菲尼克斯技能3)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +150% E-ATK: +150% Penetration (Absolute Value): +90% Crit Rate (Absolute Value): +90%

**Slot 3 — Doom Flames** (id 1555, unlocks at `+3`)
  - **Ⅰ** at `+3` — Doom FlamesⅠ (菲尼克斯技能2)
    (Takes effect at the start of battle) Starblaze Form: Has a 50% chance (probability for each target is calculated independently) to apply 1 stack of Scorch to all enemies on death. Healing received and health recovery reduced by 75%. Doom Form: Gains True Sight for 99 rounds. Each active skill cast has a 45% chance to apply Scorch to all enemies (probability for each target is calculated independently). When enemies apply control (Freeze, Lock, Confuse) to Phoenix on their round, Phoenix has a 100% chance to gain Scorch, lose 15% of max HP, and be cleansed of control (Freeze, Lock, Confuse).
  - **Ⅱ** at `+8` — Doom FlamesⅡ (菲尼克斯技能2)
    (Takes effect at the start of battle) Starblaze Form: Has a 75% chance (probability for each target is calculated independently) to apply 1 stack of Scorch to all enemies on death. Healing received and health recovery reduced by 75%. Doom Form: Gains True Sight for 99 rounds. Each active skill cast has a 55% chance to apply Scorch to all enemies (probability for each target is calculated independently). When enemies apply control (Freeze, Lock, Confuse, Forbidding Skill Use) to Phoenix on their round, Phoenix has a 100% chance to gain Scorch, lose 12% of max HP, and be cleansed of control (Freeze, Lock, Confuse, Forbidding Skill Use).
  - **Ⅲ** at `+14` — Doom FlamesⅢ (菲尼克斯技能2)
    (Takes effect at the start of battle) Starblaze Form: Has a 30% chance to apply Scorch to 3 random targets (probability for each target is calculated independently). Has a 100% chance (probability for each target is calculated independently) to apply 1 stack of Scorch to all enemies on death. Healing received and health recovery reduced by 75%. Doom Form: Gains True Sight for 99 rounds. Each active skill cast has a 65% chance to apply Scorch to all enemies (probability for each target is calculated independently). When enemies apply control (Freeze, Lock, Confuse, Forbidding Skill Use) and Weaken to Phoenix on their round, Phoenix has a 100% chance to gain Scorch, lose 9% of max HP, and be cleansed of control (Freeze, Lock, Confuse, Forbidding Skill Use) and Weaken.
  - **Ⅳ** at `+T` — Doom FlamesIV (菲尼克斯技能2)
    (Takes effect at the start of battle) Starblaze Form: Has a 50% chance to apply Scorch to 3 random targets (probability for each target is calculated independently) each time an active skill is used. Has a 100% chance (probability for each target is calculated independently) to apply 1 stack of Scorch to all enemies on death. Healing received and health recovery reduced by 75%. Doom Form: Gains True Sight for 99 rounds. Each active skill cast has a 75% chance to apply Scorch to all enemies (probability for each target is calculated independently). When enemies apply crowd-control (Freeze, Lock, Confuse, Petrify, Icebound, Entangle, Forbidding Skill Use) and Weaken to Phoenix on their round, Phoenix has a 100% chance to gain Scorch, lose 5% of max HP, and be cleansed of crowd-control (Freeze, Lock, Confuse, Petrify, Icebound, Entangle, Forbidding Skill Use) and Weaken.

**Slot 4 — Fiery Rebirth** (id 1557, unlocks at `+6`)
  - **Ⅰ** at `+6` — Fiery RebirthⅠ (菲尼克斯技能4)
    (Takes effect at the start of battle) [Phoenix] always enters battle in Starblaze Form, but is reborn into Doom Form upon death (unaffected by forbidding revival effects; revives into Doom Form even when dying in Doom Form). Starblaze Form: Active skill: Scorch of Ruin. Applies 1 stack of Scorch to all enemies and gains 3% S-ATK. Enemies deal 6% less damage for each stack of Scorch. Doom Form: Active skill: Doom Meteora. Applies 1 stack of Scorch to all enemies when casting skills, and increases the S-ATK damage of that cast by 3%. Enemies take 6% more damage for each stack of Scorch.
  - **Ⅱ** at `+10` — Fiery RebirthⅡ (菲尼克斯技能4)
    (Takes effect at the start of battle) [Phoenix] always enters battle in Starblaze Form, but is reborn into Doom Form upon death (unaffected by forbidding revival effects; revives into Doom Form even when dying in Doom Form). Starblaze Form: Active skill: Scorch of Ruin. Applies 1 stack of Scorch to all enemies and gains 5% S-ATK. Enemies deal 8% less damage for each stack of Scorch. Doom Form: Active skill: Doom Meteora. Applies 1 stack of Scorch to all enemies when casting skills, and increases the S-ATK damage of that cast by 5%. Enemies take 8% more damage for each stack of Scorch.
  - **Ⅲ** at `+T1` — Fiery RebirthⅢ (菲尼克斯技能4)
    (Takes effect at the start of battle) [Phoenix] always enters battle in Starblaze Form, but is reborn into Doom Form upon death (unaffected by forbidding revival effects; revives into Doom Form even when dying in Doom Form). Starblaze Form: Active skill: Scorch of Ruin. Applies 1 stack of Scorch to all enemies and gains 7% S-ATK. Enemies deal 10% less damage for each stack of Scorch. Doom Form: Active skill: Doom Meteora. Applies 1 stack of Scorch to all enemies when casting skills, and increases the S-ATK damage of that cast by 7%. Enemies take 10% more damage for each stack of Scorch.
  - **Ⅳ** at `+T4` — Fiery RebirthIV (菲尼克斯技能4)
    (Takes effect at the start of battle) [Phoenix] always enters battle in Starblaze Form, but is reborn into Doom Form upon death and immediately acts (unaffected by forbidding revival effects; revives into Doom Form even when dying in Doom Form). Starblaze Form: Active skill: Scorch of Ruin. Applies 1 stack of Scorch to all enemies and gains 12% S-ATK. Enemies deal 15% less damage for each stack of Scorch. Doom Form: Active skill: Doom Meteora. Applies 1 stack of Scorch to all enemies when casting skills, and increases the S-ATK damage of that cast by 12%. Enemies take 15% more damage for each stack of Scorch.

### Transform form (536 · 菲尼克斯（变身后）)
- **Ⅰ** at `+0` — Doom MeteoraⅠ (菲尼克斯，灭世星火lv1（灭世主动）；)
  _(no English description shipped)_
- **Ⅱ** at `Awaken` — Doom MeteoraⅡ (菲尼克斯，灭世星火lv2（灭世主动）；)
  _(no English description shipped)_
- **Ⅲ** at `Second Awaken` — Doom MeteoraⅢ (菲尼克斯，灭世星火lv3（灭世主动）；)
  _(no English description shipped)_
- **IV** at `Awaken +3` — Doom MeteoraIV (菲尼克斯，灭世星火lv4（灭世主动）；)
  _(no English description shipped)_

### Augment cost (per step)
- `+1` — 5× Destroyer Chip · 100,000 money
- `+2` — 10× Destroyer Chip · 200,000 money
- `+3` — 21× Destroyer Chip · 300,000 money
- `+4` — 28× Destroyer Chip · 500,000 money
- `+5` — 35× Destroyer Chip · 800,000 money
- `+6` — 42× Destroyer Chip · 10× Pandora Power Core
- `+7` — 49× Destroyer Chip · 50× Pandora Power Core
- `+8` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Phoenix Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Phoenix Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Phoenix Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Phoenix Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Phoenix Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Phoenix Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 547 · Selene 瑟琳娜
**Role** Destroyer · **Attack** energy · **Generation** latest
**Ratings** Damage 10/10 · Defence 6/10 · Assist 6/10

### Skill panels
**Slot 1 — Magnetic Hyperspace Bomb** (id 1618, unlocks at `+0`)
  - **Ⅰ** at `+0` — Magnetic Hyperspace BombⅠ (瑟琳娜技能描述)
    Cross Attack, deals 360% S-ATK damage to targets. Applies [Magnetic Hyperspace Bomb] to 1 random enemy lasting 99 rounds. Whenever any ally uses a skill, enemies with a [Magnetic Hyperspace Bomb] take 200% S-ATK damage. This damage is then logged, and when the bomb explodes (bombs explode before each time Selene uses a skill, when Selene dies, or when the affected target dies), every enemy unit takes S-ATK damage equal to the logged damage. The [Magnetic Hyperspace Bomb] is removed upon exploding, and the damage it causes cannot be transferred to other units. Lastly, you recover 100 Accumulator.
  - **Ⅱ** at `+6` — Magnetic Hyperspace BombⅡ (瑟琳娜技能描述)
    Cross Attack, starts by stealing 50% of the target's Penetration (absolute value) before dealing 380% S-ATK damage to targets. Applies [Magnetic Hyperspace Bomb] to 1 random enemy lasting 99 rounds. Whenever any ally uses a skill, enemies with a [Magnetic Hyperspace Bomb] take 240% S-ATK damage. This damage is then logged, and when the bomb explodes (bombs explode before each time Selene uses a skill, when Selene dies, or when the affected target dies), every enemy unit takes S-ATK damage equal to the logged damage. The [Magnetic Hyperspace Bomb] is removed upon exploding, and the damage it causes cannot be transferred to other units. Lastly, you recover 100 Accumulator.
  - **Ⅲ** at `+9` — Magnetic Hyperspace BombⅢ (瑟琳娜技能描述)
    Cross Attack, starts by stealing 60% of the target's Penetration and Hit Rate (absolute value) before dealing 400% S-ATK damage to targets. Applies [Magnetic Hyperspace Bomb] to 1 random enemy lasting 99 rounds. Whenever any ally uses a skill, enemies with a [Magnetic Hyperspace Bomb] take 280% S-ATK damage. This damage is then logged, and when the bomb explodes (bombs explode before each time Selene uses a skill, when Selene dies, or when the affected target dies), every enemy unit takes S-ATK damage equal to the logged damage. The [Magnetic Hyperspace Bomb] is removed upon exploding, and the damage it causes cannot be transferred to other units. Lastly, you recover 100 Accumulator.
  - **Ⅳ** at `+15` — Magnetic Hyperspace BombIV (瑟琳娜技能描述)
    Cross Attack, starts by stealing 70% of the target's Penetration and Hit Rate (absolute value) before dealing 450% S-ATK damage to targets. Applies [Magnetic Hyperspace Bomb] to 1 random enemy lasting 99 rounds. Whenever any ally uses a skill, enemies with a [Magnetic Hyperspace Bomb] take 330% S-ATK damage. This damage is then logged, and when the bomb explodes (bombs explode before each time Selene uses a skill, when Selene dies, or when the affected target dies), every enemy unit takes S-ATK damage equal to the logged damage. The [Magnetic Hyperspace Bomb] is removed upon exploding, and the damage it causes cannot be transferred to other units. Lastly, you recover 100 Accumulator. Applies [Magnetic Hyperspace Bomb] to 1 random enemy at the start of battle.

**Slot 2 — Hyperspace Seal** (id 1619, unlocks at `+2`)
  - **Ⅰ** at `+2` — Hyperspace SealⅠ (瑟琳娜技能描述)
    (Takes effect at the start of battle) When using skills, 24% of current HP is converted into a shield (persists through effects that clear buffs) equal to 150% of the HP lost and 1 stack of [Hyperspace Seal] is gained, which reduces HP recovery and healing effects from other sources than self by 75%. [Hyperspace Seal]: Stacks up to 3 times. Each stack increases E-ATK by 15% and increases the damage of [Magnetic Hyperspace Bomb] by 15%.
  - **Ⅱ** at `+7` — Hyperspace SealⅡ (瑟琳娜技能描述)
    (Takes effect at the start of battle) When using skills, 24% of current HP is converted into a shield (persists through effects that clear buffs) equal to 180% of the HP lost and 1 stack of [Hyperspace Seal] is gained, which reduces HP recovery and healing effects from other sources than self by 75%. [Hyperspace Seal]: Stacks up to 3 times. Each stack increases E-ATK by 20% and increases the damage of [Magnetic Hyperspace Bomb] by 20%. Damage dealt increases by 1% and damage reduction by 1% for every 1% HP lost.
  - **Ⅲ** at `+11` — Hyperspace SealⅢ (瑟琳娜技能描述)
    (Takes effect at the start of battle) When using skills, 24% of current HP is converted into a shield (persists through effects that clear buffs) equal to 210% of the HP lost and 1 stack of [Hyperspace Seal] is gained, which reduces HP recovery and healing effects from other sources than self by 75%. [Hyperspace Seal]: Stacks up to 3 times. Each stack increases E-ATK by 25% and increases the damage of [Magnetic Hyperspace Bomb] by 25%. Damage dealt increases by 2% and damage reduction by 2% for every 1% HP lost. After each [Hyperspace Seal] gained, the next lethal damage taken will be prevented and Selene will instead recover max HP equal to [Hyperspace Seal] stacks * 35% (this effect does not stack and you can only have 1 chance at a time).
  - **Ⅳ** at `+T3` — Hyperspace SealIV (瑟琳娜技能描述)
    (Takes effect at the start of battle) When using skills, 24% of current HP is converted into a shield (persists through effects that clear buffs) equal to 240% of the HP lost and 1 stack of [Hyperspace Seal] is gained, which reduces HP recovery and healing effects from other sources than self by 75%. [Hyperspace Seal]: Stacks up to 3 times. Each stack increases E-ATK by 30% and increases the damage of [Magnetic Hyperspace Bomb] by 30%. Damage dealt increases by 3% and damage reduction by 3% for every 1% HP lost. After each [Hyperspace Seal] gained, the next lethal damage taken will be prevented and Selene will instead recover max HP equal to [Hyperspace Seal] stacks * 35% (this effect does not stack and you can only have 1 chance at a time). Gained at the start of battle: You cannot critical hit; instead, each 1% of Crit ATK above 100% will be converted into 1% S-ATK damage, up to a maximum of 400%.

**Slot 3 — Hyperspace Power** (id 1620, unlocks at `+3`)
  - **Ⅰ** at `+3` — Hyperspace PowerⅠ (瑟琳娜技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +60% E-ATK: +60% Penetration (Absolute Value): +60% Hit Rate (Absolute Value): +60%
  - **Ⅱ** at `+8` — Hyperspace PowerⅡ (瑟琳娜技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +90% E-ATK: +90% Penetration (Absolute Value): +70% Hit Rate (Absolute Value): +70%
  - **Ⅲ** at `+13` — Hyperspace PowerⅢ (瑟琳娜技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +120% E-ATK: +120% Penetration (Absolute Value): +80% Hit Rate (Absolute Value): +80%
  - **Ⅳ** at `+T` — Hyperspace PowerIV (瑟琳娜技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +150% E-ATK: +150% Penetration (Absolute Value): +90% Hit Rate (Absolute Value): +90%

**Slot 4 — Magnetic Bomb Reinforcement** (id 1621, unlocks at `+10`)
  - **Ⅰ** at `+10` — Magnetic Bomb ReinforcementⅠ (瑟琳娜技能描述)
    (Takes effect at the start of battle) Enemies destroyed by [Magnetic Hyperspace Bomb] damage cannot revive or rebirth.
  - **Ⅱ** at `+T1` — Magnetic Bomb ReinforcementⅡ (瑟琳娜技能描述)
    (Takes effect at the start of battle) Enemies destroyed by [Magnetic Hyperspace Bomb] damage cannot revive or rebirth. When using a skill, applies 1 extra [Magnetic Hyperspace Bomb] to a random target based on the following priority: Destroyer, Striker, Flagship, Ranger, Rover and Protector.
  - **Ⅲ** at `+T2` — Magnetic Bomb ReinforcementⅢ (瑟琳娜技能描述)
    (Takes effect at the start of battle) Enemies destroyed by [Magnetic Hyperspace Bomb] damage cannot revive or rebirth. When using a skill, applies 1 extra [Magnetic Hyperspace Bomb] to a random target based on the following priority: Destroyer, Striker, Flagship, Ranger, Rover and Protector. Enemies with [Magnetic Hyperspace Bomb] must consume an extra 100% Accumulator to use skills, and their skill damage is reduced by 70%.
  - **Ⅳ** at `+T4` — Magnetic Bomb ReinforcementIV (瑟琳娜技能描述)
    (Takes effect at the start of battle) Enemies destroyed by [Magnetic Hyperspace Bomb] damage cannot revive or rebirth. When using a skill, applies 1 extra [Magnetic Hyperspace Bomb] to a random target based on the following priority: Destroyer, Striker, Flagship, Ranger, Rover and Protector. Enemies with [Magnetic Hyperspace Bomb] must consume an extra 100% Accumulator to use skills, and their skill damage is reduced by 70%. [Magnetic Hyperspace Bomb] interferes with the affected target, rendering all buffs and skill effects applied to it by itself and allies invalid.

### Augment cost (per step)
- `+1` — 5× Destroyer Chip · 100,000 money
- `+2` — 10× Destroyer Chip · 200,000 money
- `+3` — 21× Destroyer Chip · 300,000 money
- `+4` — 28× Destroyer Chip · 500,000 money
- `+5` — 35× Destroyer Chip · 800,000 money
- `+6` — 42× Destroyer Chip · 10× Pandora Power Core
- `+7` — 49× Destroyer Chip · 50× Pandora Power Core
- `+8` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Selene Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Selene Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Selene Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Selene Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Selene Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Selene Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 551 · Tyrone 泰隆
**Role** Destroyer · **Attack** energy · **Generation** latest
**Ratings** Damage 10/10 · Defence 6/10 · Assist 6/10

### Skill panels
**Slot 1 — Oblivion Beam** (id 1646, unlocks at `+0`)
  - **Ⅰ** at `+0` — Oblivion BeamⅠ (泰隆)
    Cross Attack, deals 320% S-ATK damage to targets. Has a 40% chance to apply the [Annihilation Curse] to 2 random enemy units, lasting for 3 rounds. Lastly, you recover 100 Accumulator. [Annihilation Curse]: Initially at 3 stacks, the target will lose one stack when hit by a normal attack or skill attack, and will lose another stack after the affected target's action ends. When the stacks are reduced to 0, it will immediately deal 4000% S-ATK damage to the affected target by the caster, and this damage cannot be shared. Annihilation Curse will be cleared after dealing damage.
  - **Ⅱ** at `+7` — Oblivion BeamⅡ (泰隆)
    Cross Attack, deals 340% S-ATK damage to targets. Has a 60% chance to apply the [Annihilation Curse] to 2 random enemy units, lasting for 3 rounds. After the attack, there's a 100% chance to become invisible for 2 rounds. Lastly, you recover 100 Accumulator. [Annihilation Curse]: Initially at 3 stacks, the target will lose one stack when hit by a normal attack or skill attack, and will lose another stack after the affected target's action ends. When the stacks are reduced to 0, it will immediately deal 6000% S-ATK damage to the affected target by the caster, and this damage cannot be shared. Annihilation Curse will be cleared after dealing damage.
  - **Ⅲ** at `+13` — Oblivion BeamⅢ (泰隆)
    Cross Attack, deals 360% S-ATK damage to targets. Has an 80% chance to apply the [Annihilation Curse] to 2 random enemy units, lasting for 3 rounds. After the attack, there's a 100% chance to become invisible for 2 rounds. Increases your own E-ATK and S-ATK by 80% for 2 rounds. Lastly, you recover 100 Accumulator. [Annihilation Curse]: Initially at 3 stacks, the target will lose one stack when hit by a normal attack or skill attack, and will lose another stack after the affected target's action ends. When the stacks are reduced to 0, it will immediately deal 8000% S-ATK damage to the affected target by the caster, and this damage cannot be shared. Annihilation Curse will be cleared after causing damage.
  - **Ⅳ** at `+15` — Oblivion BeamⅣ (泰隆)
    Cross Attack, deals 400% S-ATK damage to targets. Has a 100% chance to apply the [Annihilation Curse] to 2 random enemy units, lasting for 3 rounds. After the attack, there's a 100% chance to become invisible for 2 rounds. Increases your own E-ATK and S-ATK by 80% for 2 rounds. There's a 75% chance to confuse the targets, lasting for 2 rounds. Lastly, you recover 100 Accumulator. [Annihilation Curse]: Initially at 3 stacks, the target will lose one stack when hit by a normal attack or skill attack, and will lose another stack after the affected target's action ends. When the stacks are reduced to 0, it will immediately deal 10000% S-ATK damage to the affected target by the caster, and this damage cannot be shared. Annihilation Curse will be cleared after causing damage.

**Slot 2 — Oblivion Curse** (id 1647, unlocks at `+3`)
  - **Ⅰ** at `+3` — Oblivion CurseⅠ (泰隆)
    (Takes effect at the start of battle) Units under the "Annihilation Curse" will not be able to activate their immunity to control and debuffs (Freeze, Lock, Confuse, Forbidding Skill use, Petrify, Icebound, Entangle).
  - **Ⅱ** at `+9` — Oblivion CurseⅡ (泰隆)
    (Takes effect at the start of battle) Units under the "Annihilation Curse" will not be able to activate their immunity to control and debuffs (Freeze, Lock, Confuse, Forbidding Skill use, Petrify, Icebound, Entangle). Each time instance of casting [Annihilation Curse] will affect 3 random enemies instead.
  - **Ⅲ** at `+T1` — Oblivion CurseⅢ (泰隆)
    (Takes effect at the start of battle) Units under the "Annihilation Curse" will not be able to activate their immunity to control and debuffs (Freeze, Lock, Confuse, Forbidding Skill use, Petrify, Icebound, Entangle). Each time instance of casting [Annihilation Curse] will affect 3 random enemies instead. The damage caused by [Annihilation Curse] can ignore effects that grant immunity to lethal damage and block lethal damage, except for Starcore Essence.
  - **Ⅳ** at `+T4` — Oblivion CurseⅣ (泰隆)
    (Takes effect at the start of battle) Units under the "Annihilation Curse" will not be able to activate their immunity to control and debuffs (Freeze, Lock, Confuse, Forbidding Skill use, Petrify, Icebound, Entangle). Each time instance of casting [Annihilation Curse] will affect 3 random enemies instead. The damage caused by [Annihilation Curse] can ignore effects that grant immunity to lethal damage and block lethal damage, except for Starcore Essence. The damage caused by [Annihilation Curse] is increased to 12000% S-ATK. When Tyrone casts a skill, he will first settle the damage caused by the [Annihilation Curse] on all enemies, and then proceed with subsequent actions.

**Slot 3 — Oblivion Trial** (id 1648, unlocks at `+5`)
  - **Ⅰ** at `+5` — Oblivion TrialⅠ (泰隆)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): E-ATK: +40% S-ATK: +30% Penetration (absolute value): +20%
  - **Ⅱ** at `+11` — Oblivion TrialⅡ (泰隆)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): E-ATK: +70% S-ATK: +60% Penetration (absolute value): +30%
  - **Ⅲ** at `+T2` — Oblivion TrialⅢ (泰隆)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): E-ATK: +100% S-ATK: +90% Penetration (absolute value): +40%
  - **Ⅳ** at `+T3` — Oblivion TrialⅣ (泰隆)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): E-ATK: +150% S-ATK: +120% Penetration (absolute value): +50%

### Augment cost (per step)
- `+1` — 5× Destroyer Chip · 100,000 money
- `+2` — 10× Destroyer Chip · 200,000 money
- `+3` — 21× Destroyer Chip · 300,000 money
- `+4` — 28× Destroyer Chip · 500,000 money
- `+5` — 35× Destroyer Chip · 800,000 money
- `+6` — 42× Destroyer Chip · 10× Pandora Power Core
- `+7` — 49× Destroyer Chip · 50× Pandora Power Core
- `+8` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Tyrone's Parts · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Tyrone's Parts · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Tyrone's Parts · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Tyrone's Parts · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Tyrone's Parts · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Tyrone's Parts · 140× Alien Essence · 140× Transcendence Core

---

## 557 · Catherine 凯瑟琳
**Role** Destroyer · **Attack** energy · **Generation** latest
**Ratings** Damage 10/10 · Defence 6/10 · Assist 6/10

### Skill panels
**Slot 1 — Cross Judgment** (id 1682, unlocks at `+0`)
  - **Ⅰ** at `+0` — Cross JudgmentⅠ (凯瑟琳技能描述)
    Cross Attack, attacks the target hit 3 times, each attack dealing 120% S-ATK damage. Each skill use increases self's Crit ATK by 20% (absolute value), stackable up to 100% Crit ATK (absolute value), lasting 99 rounds. Gains Eye of True Sight for 99 rounds. Lastly, recovers 100 Accumulator.
  - **Ⅱ** at `+5` — Cross JudgmentⅡ (凯瑟琳技能描述)
    Cross Attack, attacks the target hit 3 times, each attack dealing 140% S-ATK damage. Each skill use increases self's Crit ATK by 40% (absolute value), stackable up to 200% Crit ATK (absolute value), lasting 99 rounds. Each kill grants an additional 60% Crit ATK (absolute value) to self, stackable up to 180% Crit ATK (absolute value), lasting 99 rounds. Grants Eye of True Sight for self for 99 rounds. Finally, recovers 100 Accumulator.
  - **Ⅲ** at `+9` — Cross JudgmentⅢ (凯瑟琳技能描述)
    Cross Attack, attacks the target hit 3 times, each attack dealing 160% S-ATK damage. Each skill use increases self's Crit ATK by 60% (absolute value), stackable up to 300% Crit ATK (absolute value), lasting 99 rounds.Each kill grants an additional 80% Crit ATK (absolute value) to self, stackable up to a maximum of 240% Crit ATK (absolute value), lasting 99 rounds. Deals true damage equal to 120% of the first attack's S-ATK damage to all enemy ships with HP below 40%. Grants Eye of True Sight for self for 99 rounds. Finally, recovers 100 Accumulator.
  - **Ⅳ** at `+15` — Cross JudgmentⅣ (凯瑟琳技能描述)
    Cross Attack, first clears all buffs from the target, then plunders 50% of the target's Accumulator and 70% of their S-ATK, followed by 3 consecutive hits to the target, each dealing 180% S-ATK damage.Each skill use increases self's Crit ATK by 60% (absolute value), stackable up to 300% Crit ATK (absolute value), lasting 99 rounds; Each kill grants an additional 100% Crit ATK (absolute value) to self, stackable up to a maximum of 300% Crit ATK (absolute value), lasting 99 roundsDeals true damage equal to 150% of the first attack's S-ATK damage to all enemy ships with HP below 50%. Grants Eye of True Sight for self for 99 rounds. Finally, recovers 100 Accumulator.

**Slot 2 — Silver Crossbow** (id 1683, unlocks at `+2`)
  - **Ⅰ** at `+2` — Silver CrossbowⅠ (凯瑟琳技能描述)
    (Takes effect at the start of battle) S-ATK ignores 80% of the target's Crit Damage Reduce (absolute value)
  - **Ⅱ** at `+7` — Silver CrossbowⅡ (凯瑟琳技能描述)
    (Takes effect at the start of battle) S-ATK ignores 80% of the target's Crit Damage Reduce (absolute value) When dealing S-ATK damage, if the target's HP is above 50%, the damage dealt is increased by 60%.
  - **Ⅲ** at `+11` — Silver CrossbowⅢ (凯瑟琳技能描述)
    (Takes effect at the start of battle) S-ATK ignores 80% of the target's Crit Damage Reduce (absolute value) When dealing S-ATK damage, if the target's HP is above 50%, the damage dealt is increased by 60%. Skills always critical hit.
  - **Ⅳ** at `+T4` — Silver CrossbowⅣ (凯瑟琳技能描述)
    (Takes effect at the start of battle) S-ATK ignores 80% of the target's Crit Damage Reduce (absolute value) When dealing S-ATK damage, if the target's HP is above 50%, the damage dealt is increased by 60%. Skills always critical hit. Catherine's S-ATK has a 75% chance to gain Hunter Focus. (The attack always hits, ignores Dodge, Evasive and Time Ward).

**Slot 3 — Sensory Pursuit** (id 1684, unlocks at `+3`)
  - **Ⅰ** at `+3` — Sensory PursuitⅠ (凯瑟琳技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +60% E-ATK: +60% Penetration (Absolute Value): +60% Hit Rate (Absolute Value): +60%
  - **Ⅱ** at `+8` — Sensory PursuitⅡ (凯瑟琳技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +90% E-ATK: +90% Penetration (Absolute Value): +70% Hit Rate (Absolute Value): +70%
  - **Ⅲ** at `+13` — Sensory PursuitⅢ (凯瑟琳技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +120% E-ATK: +120% Penetration (Absolute Value): +80% Hit Rate (Absolute Value): +80%
  - **Ⅳ** at `+T` — Sensory PursuitⅣ (凯瑟琳技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +150% E-ATK: +150% Penetration (Absolute Value): +90% Hit Rate (Absolute Value): +90%

**Slot 4 — Judgment Pursuit** (id 1685, unlocks at `+10`)
  - **Ⅰ** at `+10` — Judgment PursuitⅠ (凯瑟琳技能描述)
    (Takes effect at the start of battle) S-ATK will always penetrate (cannot be blocked).
  - **Ⅱ** at `+T1` — Judgment PursuitⅡ (凯瑟琳技能描述)
    (Takes effect at the start of battle) S-ATK will always penetrate (cannot be blocked). At the start of battle and each time you are revived or reborn, gain Dark Conceal for 2 rounds, becoming unable to be attacked or targeted by skill effects.
  - **Ⅲ** at `+T2` — Judgment PursuitⅢ (凯瑟琳技能描述)
    (Takes effect at the start of battle) S-ATK will always penetrate (cannot be blocked). At the start of battle and each time you are revived or reborn, gain Dark Conceal for 2 rounds, becoming unable to be attacked or targeted by skill effects. When casting a skill, dispel and remove the Rebirth effect from all enemies, and units killed by Catherine will be locked for 1 round upon revival.
  - **Ⅳ** at `+T3` — Judgment PursuitⅣ (凯瑟琳技能描述)
    (Takes effect at the start of battle) S-ATK will always penetrate (cannot be blocked). At the start of battle and each time you are revived or reborn, gain Dark Conceal for 2 rounds, becoming unable to be attacked or targeted by skill effects. When casting a skill, dispel and remove the Rebirth effect from all enemies, and units killed by Catherine will be locked for 1 round upon revival. If Catherine's Cross S-ATK kills the target, 1 extra S-ATK is launched.

### Augment cost (per step)
- `+1` — 5× Destroyer Chip · 100,000 money
- `+2` — 10× Destroyer Chip · 200,000 money
- `+3` — 21× Destroyer Chip · 300,000 money
- `+4` — 28× Destroyer Chip · 500,000 money
- `+5` — 35× Destroyer Chip · 800,000 money
- `+6` — 42× Destroyer Chip · 10× Pandora Power Core
- `+7` — 49× Destroyer Chip · 50× Pandora Power Core
- `+8` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Catherine's Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Catherine's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Catherine's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Catherine's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Catherine's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Catherine's Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 567 · Vrabel 芙拉贝尔
**Role** Destroyer · **Attack** energy · **Generation** latest
**Ratings** Damage 10/10 · Defence 6/10 · Assist 6/10

### Skill panels
**Slot 1 — Data Turbulence** (id 1738, unlocks at `+0`)
  - **Ⅰ** at `+0` — Data TurbulenceⅠ (辛西娅技能描述)
    Cross Attack, plunders 20% of the target's S-ATK for 2 rounds, then deals 320% S-ATK damage to the hit target. Applies Erosion Virus to 1 random enemy that is not already affected by it, lasting for 2 rounds. Lastly, recovers 100 Accumulator. [Erosion Virus]: Affected targets lose HP equal to 240% S-ATK damage each round.
  - **Ⅱ** at `+7` — Data TurbulenceⅡ (辛西娅技能描述)
    Cross Attack, plunders 30% of the target's S-ATK for 2 rounds, then deals 340% S-ATK damage to the hit target. Applies Erosion Virus to 1 random enemy that is not already affected by it, lasting for 2 rounds. Lastly, recovers 100 Accumulator. [Erosion Virus]: Affected targets lose HP equal to 280% S-ATK damage each round, and each time they take S-ATK damage, Erosion Virus explodes, causing an additional True Damage equal to 20% of that damage.
  - **Ⅲ** at `+13` — Data TurbulenceⅢ (辛西娅技能描述)
    Cross Attack, plunders 40% of the target's S-ATK and Accumulator for 2 rounds, then deals 360% S-ATK damage to the hit target. Applies Erosion Virus to 1 random enemy that is not already affected by it, lasting for 2 rounds. Gains Eye of True Sight for 2 rounds. Lastly, recovers 100 Accumulator. [Erosion Virus]: Affected targets lose HP equal to 320% S-ATK damage each round, and each time they take S-ATK damage, Erosion Virus explodes, causing an additional True Damage equal to 25% of that damage.
  - **Ⅳ** at `+15` — Data TurbulenceIV (辛西娅技能描述)
    Cross Attack, plunders 50% of the target's S-ATK and Accumulator (ignores immunity) for 2 rounds, then deals 400% S-ATK damage to hit targets. Applies Erosion Virus to 1 random enemy that is not already affected by it, lasting for 2 rounds. Has a 50% chance to Weaken attack targets (reducing all Attributes by 50%), lasting for 2 rounds. Gains Eye of True Sight for 2 rounds. Lastly, recovers 100 Accumulator. [Erosion Virus]: Affected targets lose HP equal to 360% S-ATK damage each round, and each time they take S-ATK damage, Erosion Virus explodes, causing an additional True Damage equal to 35% of that damage.

**Slot 2 — Erosion Virus** (id 1739, unlocks at `+3`)
  - **Ⅰ** at `+3` — Erosion VirusⅠ (辛西娅技能描述)
    (Takes effect at the start of battle) The continuous damage caused by [Erosion Virus] and the damage exploded by S-ATK will be logged. At the end of the duration, [Erosion Virus] Bursts, dealing true damage equal to 100% of the logged damage to the affected target.
  - **Ⅱ** at `+9` — Erosion VirusⅡ (辛西娅技能描述)
    (Takes effect at the start of battle) The continuous damage caused by [Erosion Virus] and the damage exploded by S-ATK will be logged. At the end of the duration, [Erosion Virus] Bursts, dealing true damage equal to 100% of the logged damage to the affected target. [Erosion Virus] The continuous damage caused by [Erosion Virus], the damage exploded by S-ATK, and burst damage are increased by 20%. In PVE battles, this is increased to 30%.
  - **Ⅲ** at `+T3` — Erosion VirusⅢ (辛西娅技能描述)
    (Takes effect at the start of battle) The continuous damage caused by [Erosion Virus] and the damage exploded by S-ATK will be logged. At the end of the duration, [Erosion Virus] Bursts, dealing true damage equal to 100% of the logged damage to the affected target. [Erosion Virus] The continuous damage caused by [Erosion Virus], the damage exploded by S-ATK, and burst damage are increased by 20%. In PVE battles, this is increased to 30%. During the [Erosion Virus], the affected target's DEF and S-DEF are reduced to 80%.
  - **Ⅳ** at `+T4` — Erosion VirusIV (辛西娅技能描述)
    (Takes effect at the start of battle) The continuous damage caused by [Erosion Virus] and the damage exploded by S-ATK will be logged. At the end of the duration, [Erosion Virus] Bursts, dealing true damage equal to 100% of the logged damage to the affected target. [Erosion Virus] The continuous damage caused by [Erosion Virus], the damage exploded by S-ATK, and burst damage are increased by 20%. In PVE battles, this is increased to 30%. During the [Erosion Virus], the affected target's DEF and S-DEF are reduced to 80%. When Vrabel uses a skill, it triggers an outbreak of [Erosion Virus] on all enemies, dealing True Damage equal to 100% of the logged damage to the affected targets and resetting the logged damage. Then, it refreshes the duration of [Erosion Virus] on all enemies to 2 rounds.

**Slot 3 — Data Enhancement** (id 1740, unlocks at `+5`)
  - **Ⅰ** at `+5` — Data EnhancementⅠ (辛西娅技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): E-ATK: +40% S-ATK: +30% Crit ATK (Absolute Value): +20%
  - **Ⅱ** at `+11` — Data EnhancementⅡ (辛西娅技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): E-ATK: +70% S-ATK: +60% Crit ATK (Absolute Value): +30%
  - **Ⅲ** at `+T1` — Data EnhancementⅢ (辛西娅技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): E-ATK: +100% S-ATK: +90% Crit ATK (Absolute Value): +40%
  - **Ⅳ** at `+T2` — Data EnhancementIV (辛西娅技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): E-ATK: +150% S-ATK: +120% Crit ATK (Absolute Value): +60%

### Augment cost (per step)
- `+1` — 5× Destroyer Chip · 100,000 money
- `+2` — 10× Destroyer Chip · 200,000 money
- `+3` — 21× Destroyer Chip · 300,000 money
- `+4` — 28× Destroyer Chip · 500,000 money
- `+5` — 35× Destroyer Chip · 800,000 money
- `+6` — 42× Destroyer Chip · 10× Pandora Power Core
- `+7` — 49× Destroyer Chip · 50× Pandora Power Core
- `+8` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Vrabel's Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Vrabel's Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Vrabel's Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Vrabel's Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Vrabel's Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Vrabel's Part · 140× Alien Essence · 140× Transcendence Core

---

## 571 · Viperian 维珀里安
**Role** Destroyer · **Attack** energy · **Generation** latest
**Ratings** Damage 10/10 · Defence 6/10 · Assist 6/10

### Skill panels
**Slot 1 — M-02 Seeker Dagger** (id 1762, unlocks at `+0`)
  - **Ⅰ** at `+0` — M-02 Seeker DaggerⅠ (维珀里安技能描述)
    Cross Attack, deals 350% S-ATK damage to targets. Gains a shield that can block 1 attack for 2 rounds. Increases own Penetration and Hit Rate by 150% (absolute value) for 2 rounds. Prevents all enemies from being healed for 2 rounds. Lastly, recovers 100 Accumulator.
  - **Ⅱ** at `+5` — M-02 Seeker DaggerⅡ (维珀里安技能描述)
    Cross Attack, steals 50% Accumulator from the target and deals 380% S-ATK damage. Gains a shield that can block 1 attack for 2 rounds. Increases own Penetration and Hit Rate by 150% (absolute value) for 2 rounds. Prevents all enemies from being healed for 2 rounds. Lastly, recovers 100 Accumulator.
  - **Ⅲ** at `+9` — M-02 Seeker DaggerⅢ (维珀里安技能描述)
    Cross Attack, steals 50% Accumulator from the target and deals 410% S-ATK damage. Gains a shield that can block 1 attack for 2 rounds.Increases own Penetration and Hit Rate by 150% (absolute value) for 2 rounds. Prevents all enemies from being healed for 2 rounds. S-ATK cannot be blocked until the end of the battle. Lastly, recovers 100 Accumulator.
  - **Ⅳ** at `+15` — M-02 Seeker DaggerIV (维珀里安技能描述)
    Cross Attack, first clears all buffs from the target, then plunders 50% of their Accumulator and 50% of their S-DEF (lasts for 2 rounds), and deals 450% S-ATK damage to the targets. Gains a shield that can block 1 attack for 2 rounds.Increases own Penetration and Hit Rate by 150% (absolute value) for 2 rounds. Prevents all enemies from being healed for 2 rounds. S-ATK cannot be blocked until the end of the battle. Lastly, recovers 100 Accumulator.

**Slot 2 — Void Hunter** (id 1763, unlocks at `+2`)
  - **Ⅰ** at `+2` — Void HunterⅠ (维珀里安技能描述)
    (Takes effect at the start of battle) If the target's HP is above 70% of Max HP, this skill's damage is increased by 60%.
  - **Ⅱ** at `+7` — Void HunterⅡ (维珀里安技能描述)
    (Takes effect at the start of battle) If the target's HP is above 70% of Max HP, this skill's damage is increased by 60%. When casting an S-ATK, additionally deals True Damage equal to 230% of the first attack's S-ATK damage to the enemy with the highest current S-ATK.
  - **Ⅲ** at `+11` — Void HunterⅢ (维珀里安技能描述)
    (Takes effect at the start of battle) If the target's HP is above 70% of Max HP, this skill's damage is increased by 60%. When casting an S-ATK, additionally deals True Damage equal to 230% of the first attack's S-ATK damage to the enemy with the highest current S-ATK. Viperian's skill attacks have a 75% chance to gain Hunter Focus (the attack always hits, ignores Dodge, Evasive and Time Ward).
  - **Ⅳ** at `+T3` — Void HunterIV (维珀里安技能描述)
    (Takes effect at the start of battle) If the target's HP is above 70% of Max HP, this skill's damage is increased by 60%. When casting an S-ATK, additionally deals True Damage equal to 230% of the first attack's S-ATK damage to the enemy with the highest current S-ATK. Viperian's skill attacks have a 75% chance to gain Hunter Focus (the attack always hits, ignores Dodge, Evasive and Time Ward). When casting a skill, first removes all enemies' Invisible and Dark Conceal states, then proceeds with the follow-up actions.

**Slot 3 — Heart of the Hunt** (id 1764, unlocks at `+3`)
  - **Ⅰ** at `+3` — Heart of the HuntⅠ (维珀里安技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +60% E-ATK: +60% Penetration (Absolute Value): +30% Crit Rate (Absolute Value): +30%
  - **Ⅱ** at `+8` — Heart of the HuntⅡ (维珀里安技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +90% E-ATK: +90% Penetration (Absolute Value): +50% Crit Rate (Absolute Value): +50%
  - **Ⅲ** at `+13` — Heart of the HuntⅢ (维珀里安技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +120% E-ATK: +120% Penetration (Absolute Value): +70% Crit Rate (Absolute Value): +70%
  - **Ⅳ** at `+T` — Heart of the HuntIV (维珀里安技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +150% E-ATK: +150% Penetration (Absolute Value): +90% Crit Rate (Absolute Value): +90%

**Slot 4 — Hunting Rhythm** (id 1765, unlocks at `+10`)
  - **Ⅰ** at `+10` — Hunting RhythmⅠ (维珀里安技能描述)
    (Takes effect at the start of battle) At the start of battle, absorb 25% of all enemies' S-ATK, lasting until the end of the battle.
  - **Ⅱ** at `+T1` — Hunting RhythmⅡ (维珀里安技能描述)
    (Takes effect at the start of battle) At the start of battle, absorb 25% of all enemies' S-ATK, lasting until the end of the battle. Killing an enemy with an S-ATK increases damage by 30% (stacks up to 150%, lasts until the end of battle; disappears on death) and restores 80% of max HP, gaining 50 Accumulator.
  - **Ⅲ** at `+T2` — Hunting RhythmⅢ (维珀里安技能描述)
    (Takes effect at the start of battle) At the start of battle, absorb 25% of all enemies' S-ATK, lasting until the end of the battle. Killing an enemy with an S-ATK increases damage by 30% (stacks up to 150%, lasts until the end of battle; disappears on death) and restores 80% of max HP, gaining 50 Accumulator. If the S-ATK results in a kill, all enemies are forbidden from using skills for 1 round.
  - **Ⅳ** at `+T4` — Hunting RhythmIV (维珀里安技能描述)
    (Takes effect at the start of battle) At the start of battle, absorb 25% of all enemies' S-ATK, lasting until the end of the battle. Killing an enemy with an S-ATK increases damage by 30% (stacks up to 150%, lasts until the end of battle; disappears on death) and restores 80% of max HP, gaining 50 Accumulator. If the S-ATK results in a kill, all enemies are forbidden from using skills for 1 round. When casting a skill, all enemies can only revive once (including rebirth) after being destroyed. Once the revival limit is reached, they cannot revive or rebirth by any means until the end of the battle.

### Augment cost (per step)
- `+1` — 5× Destroyer Chip · 100,000 money
- `+2` — 10× Destroyer Chip · 200,000 money
- `+3` — 21× Destroyer Chip · 300,000 money
- `+4` — 28× Destroyer Chip · 500,000 money
- `+5` — 35× Destroyer Chip · 800,000 money
- `+6` — 42× Destroyer Chip · 10× Pandora Power Core
- `+7` — 49× Destroyer Chip · 50× Pandora Power Core
- `+8` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Viperian Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Viperian Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Viperian Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Viperian Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Viperian Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Viperian Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 581 · Jack's Pumpkin 杰克的南瓜
**Role** Destroyer · **Attack** energy · **Generation** latest
**Ratings** Damage 10/10 · Defence 6/10 · Assist 6/10

### Skill panels
**Slot 1 — Jack's Curse** (id 1812, unlocks at `+0`)
  - **Ⅰ** at `+0` — Jack's CurseⅠ (杰克的南瓜+0)
    Cross Attack, deals 320% S-ATK damage to targets. Curses the targets hit for 2 rounds. When the curse ends, targets take 4000% S-ATK damage. Lastly, recovers 100 Accumulator.
  - **Ⅱ** at `+7` — Jack's CurseⅡ (杰克的南瓜+7)
    Cross Attack, deals 340% S-ATK damage to targets. Instantly kills ships with less than 30% HP. Curses hit targets for 2 rounds, dealing 6000% S-ATK damage when the curse ends. Lastly, recovers 100 Accumulator.
  - **Ⅲ** at `+15` — Jack's CurseⅢ (杰克的南瓜+15)
    Cross Attack, deals 360% S-ATK damage to targets. Instantly kills ships with less than 40% HP. Curses hit targets for 2 rounds, dealing 8000% S-ATK damage when the curse ends. Gains invisibility for 1 round. Lastly, recovers 100 Accumulator.
  - **Ⅳ** at `+T3` — Jack's CurseIV (杰克的南瓜+17（回合数缩短）)
    Cross Attack, deals 400% S-ATK damage to targets. Instantly kills ships with less than 40% HP (ignores immunity to lethal and instant destruction effects). Curses hit targets for 2 rounds, dealing 10000% S-ATK damage when the curse ends. Gains invisibility for 1 round. Lastly, recovers 100 Accumulator.

**Slot 2 — Shadow Tear** (id 1813, unlocks at `+2`)
  - **Ⅰ** at `+2` — Shadow TearⅠ (杰克的南瓜+3)
    (Takes effect at the start of battle) At the start of battle, self gains 1 round of invisibility and will not lose invisibility for as long as there is another ally alive (can be seen by Eye of True Sight).
  - **Ⅱ** at `+10` — Shadow TearⅡ (杰克的南瓜+9)
    (Takes effect at the start of battle) At the start of battle, self gains 1 round of invisibility and will not lose invisibility for as long as there is another ally alive (can be seen by Eye of True Sight). Each time a skill is used, increases own E-ATK and S-ATK by 40%, stacking up to 4 times, lasting until the end of the battle.
  - **Ⅲ** at `+T1` — Shadow TearⅢ (杰克的南瓜+17)
    (Takes effect at the start of battle) At the start of battle, self gains 1 round of invisibility and will not lose invisibility for as long as there is another ally alive (can be seen by Eye of True Sight). Each time a skill is used, increases own E-ATK and S-ATK by 60%, stacking up to 4 times, lasting until the end of the battle. The duration of the curse effect is reduced to 1 round.
  - **Ⅳ** at `+T4` — Shadow TearIV (杰克的南瓜+20)
    (Takes effect at the start of battle) At the start of battle, self gains 1 round of invisibility and will not lose invisibility for as long as there is another ally alive (can be seen by Eye of True Sight). Each time a skill is used, increases own E-ATK and S-ATK by 80%, stacking up to 4 times, lasting until the end of the battle. The duration of the curse effect is reduced to 1 round. Enemies hit by skill attacks can only be revived once (including Rebirth). After reaching the revival limit, they cannot be revived by any resurrection or rebirth effects until the end of the battle.

**Slot 3 — Carnival Wishes** (id 1814, unlocks at `+5`)
  - **Ⅰ** at `+5` — Carnival WishesⅠ (杰克的南瓜+5)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): E-ATK: +40% S-ATK: +30% Penetration (absolute value): +20%
  - **Ⅱ** at `+11` — Carnival WishesⅡ (杰克的南瓜+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): E-ATK: +70% S-ATK: +60% Penetration (absolute value): +30%
  - **Ⅲ** at `+T` — Carnival WishesⅢ (杰克的南瓜+16)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): E-ATK: +100% S-ATK: +90% Penetration (absolute value): +40%
  - **Ⅳ** at `+T2` — Carnival WishesIV (杰克的南瓜+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): E-ATK: +150% S-ATK: +120% Penetration (absolute value): +50%

### Augment cost (per step)
- `+1` — 5× Destroyer Chip · 100,000 money
- `+2` — 10× Destroyer Chip · 200,000 money
- `+3` — 21× Destroyer Chip · 300,000 money
- `+4` — 28× Destroyer Chip · 500,000 money
- `+5` — 35× Destroyer Chip · 800,000 money
- `+6` — 42× Destroyer Chip · 10× Pandora Power Core
- `+7` — 49× Destroyer Chip · 50× Pandora Power Core
- `+8` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Jack's Pumpkin Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Jack's Pumpkin Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Jack's Pumpkin Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Jack's Pumpkin Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Jack's Pumpkin Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Jack's Pumpkin Ship Part · 100× Alien Essence · 100× Transcendence Core

---

## 582 · Adele 阿黛尔
**Role** Destroyer · **Attack** energy · **Generation** old
**Ratings** Damage 9/10 · Defence 6/10 · Assist 5/10

### Signature skill
- **Ⅰ** at `+0` — Holy Judgment (阿黛尔+0)
  Cross Attack, deals 200% S-ATK damage to targets. Lastly, you recover 100 Accumulator.
- **Ⅱ** at `Awaken` — — (莎莉)
  Vertical attack, deals 140% S-ATK damage, and increases both ATK and S-ATK of the entire fleet by 40% for 2 rounds.
- **Ⅲ** at `Second Awaken` — — (莎莉)
  _(no English description shipped)_
- **Ⅳ** at `Awaken +3` — — (莎莉)
  _(no English description shipped)_

### Augment cost (per step)
- `+1` — 5× Destroyer Chip · 100,000 money
- `+2` — 10× Destroyer Chip · 200,000 money
- `+3` — 21× Destroyer Chip · 300,000 money
- `+4` — 28× Destroyer Chip · 500,000 money
- `+5` — 35× Destroyer Chip · 800,000 money
- `+6` — 42× Destroyer Chip · 10× Pandora Power Core
- `+7` — 49× Destroyer Chip · 50× Pandora Power Core
- `+8` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Adele's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Adele's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Adele's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Adele's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Adele's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Adele's Ship Part · 100× Alien Essence · 100× Transcendence Core

---

## 589 · Nacali 娜卡莉
**Role** Destroyer · **Attack** energy · **Generation** latest
**Ratings** Damage 10/10 · Defence 6/10 · Assist 6/10

### Skill panels
**Slot 1 — Serpent Duet** (id 1844, unlocks at `+0`)
  - **Ⅰ** at `+0` — Serpent DuetⅠ (娜卡莉+0)
    Nacali alternates between [Poison Mist Devour] and [Serpent Entangle] each time a skill is cast, starting with [Poison Mist Devour] at the beginning of the battle. Lastly, recovers 100 Accumulator. [Poison Mist Devour]: Vertical attack; deals 280% S-ATK damage to the target. Targets hit by the skill will be poisoned for 2 rounds and they will receive 50% S-ATK damage each round. Lastly, recovers 100 Accumulator. [Serpent Entangle]: Horizontal attack; deals 280% S-ATK damage to the target. Each cast also increases Crit Rate by 10% and Crit ATK by 30% (can stack up to a maximum of 50% Crit Rate and 150% Crit ATK). Lastly, recovers 100 Accumulator.
  - **Ⅱ** at `+6` — Serpent DuetⅡ (娜卡莉+3（被动组合）)
    Nacali alternates between [Poison Mist Devour] and [Serpent Entangle] each time a skill is cast, starting with [Poison Mist Devour] at the beginning of the battle. Lastly, recovers 100 Accumulator. [Poison Mist Devour]: Vertical attack; deals 300% S-ATK damage to the target. Targets hit by the skill will be poisoned for 2 rounds and they will receive 100% S-ATK damage each round. Lastly, recovers 100 Accumulator. [Serpent Entangle]: Horizontal attack; deals 300% S-ATK damage to the target. Each cast also increases Crit Rate by 15% and Crit ATK by 40% (can stack up to a maximum of 75% Crit Rate and 200% Crit ATK). Lastly, recovers 100 Accumulator.
  - **Ⅲ** at `+10` — Serpent DuetⅢ (娜卡莉+6)
    Nacali alternates between [Poison Mist Devour] and [Serpent Entangle] each time a skill is cast, starting with [Poison Mist Devour] at the beginning of the battle. Lastly, recovers 100 Accumulator. [Poison Mist Devour]: Vertical attack; deals 320% S-ATK damage to the target. Targets hit by the skill will be poisoned for 3 rounds and they will receive 200% S-ATK damage each round. There's a 60% chance to Confuse targets for 2 rounds. Lastly, recovers 100 Accumulator. [Serpent Entangle]: Horizontal attack; deals 320% S-ATK damage to the target. There's a 60% chance to Entangle targets. Each cast also increases Crit Rate by 20% and Crit ATK by 50% (can stack up to a maximum of 100% Crit Rate and 250% Crit ATK). Lastly, recovers 100 Accumulator.
  - **Ⅳ** at `+15` — Serpent DuetIV (娜卡莉+10)
    Nacali alternates between [Poison Mist Devour] and [Serpent Entangle] each time a skill is cast, starting with [Poison Mist Devour] at the beginning of the battle. Lastly, recovers 100 Accumulator. [Poison Mist Devour]: Vertical attack; deals 360% S-ATK damage to the target. Targets hit by the skill will be poisoned for 5 rounds and they will receive 300% S-ATK damage each round. There's a 80% chance to Confuse targets for 2 rounds. Lastly, recovers 100 Accumulator. [Serpent Entangle]: Horizontal attack; deals 360% S-ATK damage to the target. There's a 80% chance to Entangle targets. Each cast also increases Crit Rate by 30% and Crit ATK by 60% (can stack up to a maximum of 150% Crit Rate and 300% Crit ATK). Lastly, recovers 100 Accumulator.

**Slot 2 — Revelation** (id 1840, unlocks at `+2`)
  - **Ⅰ** at `+2` — RevelationⅠ (娜卡莉+2)
    (Takes effect at the start of battle) At the start of battle, gains Eye of True Sight for 99 rounds.
  - **Ⅱ** at `+9` — RevelationⅡ (娜卡莉+9)
    (Takes effect at the start of battle) At the start of battle, gains Eye of True Sight for 99 rounds. When dealing skill damage, if the target's HP is above 40%, the damage dealt is increased by 40%.
  - **Ⅲ** at `+T` — RevelationⅢ (娜卡莉+16)
    (Takes effect at the start of battle) At the start of battle, gains Eye of True Sight for 99 rounds. When dealing skill damage, if the target's HP is above 40%, the damage dealt is increased by 60%. Entangle and Confuse applied by self are forced to take effect, ignoring any immunity and protection effects.
  - **Ⅳ** at `+T3` — RevelationIV (娜卡莉+19)
    (Takes effect at the start of battle) At the start of battle, gains Eye of True Sight for 99 rounds. When dealing skill damage, if the target's HP is above 40%, the damage dealt is increased by 80%. Entangle and Confuse effects applied by self are forced to take effect, ignoring any immunity and protection effects. When self is affected by Poison, Confuse, or Entangle, the corresponding debuff is removed, and immediately triggers [Serpent Entangle]. (Cannot be triggered if the ship is under other control effects).

**Slot 3 — Serpent's Aegis** (id 1841, unlocks at `+4`)
  - **Ⅰ** at `+4` — Serpent's AegisⅠ (娜卡莉+4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +60% E-ATK: +60% Penetration (Absolute Value): +30% Crit Rate (Absolute Value): +30%
  - **Ⅱ** at `+10` — Serpent's AegisⅡ (娜卡莉+10)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +90% E-ATK: +90% Penetration (Absolute Value): +50% Crit Rate (Absolute Value): +50%
  - **Ⅲ** at `+14` — Serpent's AegisⅢ (娜卡莉+14)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +120% E-ATK: +120% Penetration (Absolute Value): +70% Crit Rate (Absolute Value): +70%
  - **Ⅳ** at `+T2` — Serpent's AegisIV (娜卡莉+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +150% E-ATK: +150% Penetration (Absolute Value): +90% Crit Rate (Absolute Value): +90%

**Slot 4 — Serpent Curse** (id 1842, unlocks at `+3`)
  - **Ⅰ** at `+3` — Serpent CurseⅠ (娜卡莉+3)
    (Takes effect at the start of battle) Nacali's skills will be enhanced. [Poison Mist Devour]: When the affected target takes damage, the attacker ignores 30% of DEF, lasting 2 rounds. [Serpent Entangle]: Ignores Stasis and immunity to lethal attacks.
  - **Ⅱ** at `+13` — Serpent CurseⅡ (娜卡莉+13)
    (Takes effect at the start of battle) Nacali's skills will be enhanced. [Poison Mist Devour]: When the affected target takes damage, the attacker ignores 40% of DEF. The target cannot dodge when taking damage, lasts for 2 rounds. [Serpent Entangle]: Ignores Stasis and immunity to lethal attacks. Calculates the Poison and Scorch damage effects of all enemies based on their duration and damage, and immediately deal the corresponding damage to the target (maximum count of rounds: 5), and remove the Poison and Scorch from the target.
  - **Ⅲ** at `+T1` — Serpent CurseⅢ (娜卡莉+17)
    (Takes effect at the start of battle) Nacali's skills will be enhanced. [Poison Mist Devour]: When the affected target takes damage, the attacker ignores 50% of DEF. The target cannot dodge when taking damage. Additionally, when the target receives healing and recovery effects (excluding HP recovery from attacks, kills, and recovery from Lieutenants and Legendary Equipment), it instead takes damage equal to 80% of the recovered HP, lasting for 2 rounds. [Serpent Entangle]: Ignores Stasis and immunity to lethal attacks. Calculates the Poison and Scorch damage effects of all enemies based on their duration and damage, and immediately deal the corresponding damage to the target (maximum count of rounds: 10), and remove the Poison and Scorch from the target.
  - **Ⅳ** at `+T4` — Serpent CurseIV (娜卡莉+20)
    (Takes effect at the start of battle) Nacali's skills will be enhanced. [Poison Mist Devour]: When the affected target takes damage, the attacker ignores 60% of DEF. The target cannot dodge when taking damage. Additionally, when the target receives healing and recovery effects (excluding HP recovery from attacks, kills, and recovery from Lieutenants and Legendary Equipment), it instead takes damage equal to 100% of the recovered HP, lasting for 2 rounds. After casting this skill, [Serpent Entangle] will be immediately used. [Serpent Entangle]: Ignores Stasis and immunity to lethal attacks. Calculates the Poison and Scorch damage effects of all enemies based on their duration and damage, and immediately deal the corresponding damage to the target (maximum count of rounds: 10), without removing the poison and scorch effects from the target. If this skill kills an enemy, it deals True Damage to all enemies equal to 100% of the excess damage.

### Augment cost (per step)
- `+1` — 5× Destroyer Chip · 100,000 money
- `+2` — 10× Destroyer Chip · 200,000 money
- `+3` — 21× Destroyer Chip · 300,000 money
- `+4` — 28× Destroyer Chip · 500,000 money
- `+5` — 35× Destroyer Chip · 800,000 money
- `+6` — 42× Destroyer Chip · 10× Pandora Power Core
- `+7` — 49× Destroyer Chip · 50× Pandora Power Core
- `+8` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Nacali's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Nacali's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Nacali's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Nacali's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Nacali's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Nacali's Ship Part · 100× Alien Essence · 100× Transcendence Core

---

## 595 · Sylvina 西尔维娜
**Role** Destroyer · **Attack** energy · **Generation** latest
**Ratings** Damage 9/10 · Defence 9/10 · Assist 6/10

### Skill panels
**Slot 1 — Network Disruption** (id 1860, unlocks at `+0`)
  - **Ⅰ** at `+0` — Network DisruptionⅠ (西尔维娜+0)
    Cross Attack, deals 320% S-ATK damage to targets. Poisons targets, causing them to lose HP equal to 150% S-ATK damage per round for 5 rounds. Lastly, recovers 100 Accumulator.
  - **Ⅱ** at `+7` — Network DisruptionⅡ (西尔维娜+3(被动))
    Cross Attack, absorbs 30% of the target's S-ATK and Accumulator for 2 rounds, and deals 340% S-ATK damage to targets. Poisons targets, causing them to lose HP equal to 200% S-ATK per round for 5 rounds. Reduces the S-DEF of poisoned enemies by 60% for 2 rounds. Lastly, recovers 100 Accumulator.
  - **Ⅲ** at `+15` — Network DisruptionⅢ (西尔维娜+7)
    Cross Attack, absorbs 40% of the target's S-ATK and Accumulator for 2 rounds, and deals 360% S-ATK damage to targets. Poisons targets, causing them to lose HP equal to 250% S-ATK per round for 5 rounds. Reduces the S-DEF of poisoned units by 80% for 2 rounds. When S-ATK attacking enemies under poisoned, it always critical hit, and crit damage is increased by 240%. Lastly, recovers 100 Accumulator.
  - **Ⅳ** at `+T3` — Network DisruptionIV (西尔维娜+9(被动))
    Cross Attack, absorbs 50% of the target's S-ATK and Accumulator (ignores immunity) for 2 rounds, and deals 400% S-ATK damage to targets. Poisons targets, causing them to lose HP equal to 300% S-ATK per round for 5 rounds. Reduces the S-DEF of poisoned units by 80% for 2 rounds. When S-ATK attacking enemies under poisoned, it always critical hit, and crit damage is increased by 300%. Upon first use, prevents the target's(the enemy with the highest S-ATK) Active Skill from taking effect for 1 round. Lastly, recovers 100 Accumulator.

**Slot 2 — Network Intrusion** (id 1861, unlocks at `+3`)
  - **Ⅰ** at `+3` — Network IntrusionⅠ (西尔维娜+3)
    (Takes effect at the start of battle) When casting a skill, apply [Network Intrusion] to the enemy unit with the lowest HP (only one unit can be affected at a time), lasting until the end of the battle or his/her death. [Network Intrusion]: Reduces the target unit's damage by 75%.
  - **Ⅱ** at `+9` — Network IntrusionⅡ (西尔维娜+9)
    (Takes effect at the start of battle) When casting a skill, apply [Network Intrusion] to the enemy unit with the lowest HP (only one unit can be affected at a time), lasting until the end of the battle or his/her death. <Network Intrusion>: Reduces the target's damage dealt by 75%, and while this effect is active, the enemy cannot target Sylvina (including damage and skill effects. Except for subsequent damage).
  - **Ⅲ** at `+T1` — Network IntrusionⅢ (西尔维娜+17)
    (Takes effect at the start of battle) When casting a skill, apply <span style="color:#FF0000;">Network Intrusion</span> to the enemy unit with the lowest HP (only one unit can be affected at a time), lasting until the end of the battle or or his/her death. <span style="color:#FF0000;">Network Intrusion</span>: Reduces the target's damage dealt by 75%, and while this effect is active, the enemy cannot target Sylvina (including damage and skill effects. Except for subsequent damage). After the enemy takes action, if Sylvina is not in a state of inability to act, she will immediately launch a single-target skill attack against him/her (up to 2 times per turn).
  - **Ⅳ** at `+T4` — Network IntrusionIV (西尔维娜+20)
    (Takes effect at the start of battle) When casting a skill, apply [Network Intrusion] to the enemy unit with the lowest HP (only one unit can be affected at a time), lasting until the end of the battle or his/her death. [Network Intrusion]: Reduces the target's damage dealt by 75%, and while this effect is active, the enemy cannot target Sylvina (including damage and skill effects. Except for subsequent damage). After the enemy takes action, if Sylvina is not in a state of inability to act, she will immediately launch a single-target skill attack against him/her (up to 2 times per turn). If Sylvina is dead, there is a 50% chance to revive Sylvina when the unit casts a skill, restoring her to 100% Max HP and Accumulator (not affected by effects that prevent revival). When the enemy with [Network Intrusion] dies, Sylvina gains [Dark Conceal] for 1 round, making it immune to attacks and skill effects.

**Slot 3 — Data Analytics** (id 1862, unlocks at `+5`)
  - **Ⅰ** at `+5` — Data AnalyticsⅠ (西尔维娜+5)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): E-ATK: +40% S-ATK: +30% Crit ATK (Absolute Value): +20%
  - **Ⅱ** at `+11` — Data AnalyticsⅡ (西尔维娜+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): E-ATK: +70% S-ATK: +60% Crit ATK (Absolute Value): +30%
  - **Ⅲ** at `+T` — Data AnalyticsⅢ (西尔维娜+16)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): E-ATK: +100% S-ATK: +90% Crit ATK (Absolute Value): +40%
  - **Ⅳ** at `+T2` — Data AnalyticsIV (西尔维娜+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): E-ATK: +150% S-ATK: +120% Crit ATK (Absolute Value): +60%

### Augment cost (per step)
- `+1` — 5× Destroyer Chip · 100,000 money
- `+2` — 10× Destroyer Chip · 200,000 money
- `+3` — 21× Destroyer Chip · 300,000 money
- `+4` — 28× Destroyer Chip · 500,000 money
- `+5` — 35× Destroyer Chip · 800,000 money
- `+6` — 42× Destroyer Chip · 10× Pandora Power Core
- `+7` — 49× Destroyer Chip · 50× Pandora Power Core
- `+8` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Sylvina's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Sylvina's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Sylvina's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Sylvina's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Sylvina's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Sylvina's Ship Part · 100× Alien Essence · 100× Transcendence Core

---

## 602 · Grusen 格鲁瑟恩
**Role** Destroyer · **Attack** energy · **Generation** latest
**Ratings** Damage 10/10 · Defence 8/10 · Assist 7/10

### Skill panels
**Slot 1 — Despair Rend** (id 1882, unlocks at `+0`)
  - **Ⅰ** at `+0` — Despair RendⅠ (格鲁瑟恩+0)
    Cross Attack, plunders 20% Penetration and Accumulator from all enemies, then deals 360% S-ATK damage to targets. Gains Eye of True Sight for 2 rounds. Lastly, you recover 100 Accumulator.
  - **Ⅱ** at `+6` — Despair RendⅡ (格鲁瑟恩+2)
    Cross Attack, plunders 30% Penetration and Accumulator from all enemies, then deals 400% S-ATK damage to targets. Gains Eye of True Sight for 2 rounds. Each time a skill is cast, increases Crit Rate by 20% and Crit ATK by 50%, up to a maximum of 100% Crit Rate and 250% Crit ATK. Lastly, you recover 100 Accumulator.
  - **Ⅲ** at `+10` — Despair RendⅢ (格鲁瑟恩+6)
    Cross Attack, plunders 40% Penetration and Accumulator from all enemies, then deals 440% S-ATK damage to targets. Gains Eye of True Sight for 2 rounds. Has a 100% chance to inflict [Shadow Oppression] on the enemy with the highest S-ATK for 99 rounds. Each time a skill is cast, increases Crit Rate by 20% and Crit ATK by 50%, up to a maximum of 100% Crit Rate and 250% Crit ATK. Lastly, you recover 100 Accumulator. [Shadow Oppression]: The affected target's final damage is increased by 60%, when any enemy loses HP, the enemy takes 80% link damage(damage caused by link cannot be conducted again).
  - **Ⅳ** at `+15` — Despair RendIV (格鲁瑟恩+9)
    Cross Attack, plunders 50% Penetration and Accumulator from all enemies, then deals 480% S-ATK damage to targets. Gains Eye of True Sight for 2 rounds. Has a 100% chance to inflict [Shadow Oppression] on the enemy with the highest S-ATK for 99 rounds. Each time a skill is cast, increases Crit Rate by 30% and Crit ATK by 60%, up to a maximum of 150% Crit Rate and 300% Crit ATK. Deals True Damage equal to 200% of the initial S-ATK damage to all enemies with less than 50% HP. Lastly, you recover 100 Accumulator. [Shadow Oppression]: The affected target's final damage is increased by 80%, when any enemy loses HP, the enemy takes 100% link damage (damage caused by link cannot be conducted again). The affected target acts, it takes True Damage equal to 200% of Grusen's ATK.

**Slot 2 — Soul Slaughter** (id 1883, unlocks at `+2`)
  - **Ⅰ** at `+2` — Soul SlaughterⅠ (格鲁瑟恩+19)
    (Takes effect at the start of battle) For every 1% of the target's max HP lost, dealt an additional 1% S-ATK damage.
  - **Ⅱ** at `+9` — Soul SlaughterⅡ (格鲁瑟恩+19)
    (Takes effect at the start of battle) For every 1% of the target's max HP lost, dealt an additional 2% S-ATK damage. Enemies killed by Grusen's S-ATK will be locked for 1 round upon revival.
  - **Ⅲ** at `+T` — Soul SlaughterⅢ (格鲁瑟恩+19)
    (Takes effect at the start of battle) For every 1% of the target's max HP lost, dealt an additional 3% S-ATK damage. Enemies killed by Grusen's S-ATK will be locked for 1 round upon revival. At the start of battle, there is a 100% chance to inflict [Shadow Oppression] on a random enemy, lasting for 99 rounds. When casting a skill, there is a 100% chance to prohibit enemies with [Shadow Oppression] from using skills for 2 rounds.
  - **Ⅳ** at `+T3` — Soul SlaughterIV (格鲁瑟恩+19)
    (Takes effect at the start of battle) For every 1% of the target's max HP lost, dealt an additional 4% S-ATK damage, and your own S-ATK ignore immunity to lethal attack and stasis state effects. Enemies killed by Grusen's S-ATK will be locked for 1 round upon revival and gain [Shadow Oppression] for 2 rounds. At the start of battle, there is a 100% chance to inflict [Shadow Oppression] on a random enemy, lasting for 99 rounds. When casting a skill, there is a 100% chance to prohibit enemies with [Shadow Oppression] from using skills for 2 rounds. (Forced to take effect, ignoring immunity and protection effects.)

**Slot 3 — Dread Ruler** (id 1884, unlocks at `+4`)
  - **Ⅰ** at `+4` — Dread RulerⅠ (格鲁瑟恩+4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +60% E-ATK: +60% Penetration (Absolute Value): +30% Crit Rate (Absolute Value): +30%
  - **Ⅱ** at `+10` — Dread RulerⅡ (格鲁瑟恩+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +90% E-ATK: +90% Penetration (Absolute Value): +50% Crit Rate (Absolute Value): +50%
  - **Ⅲ** at `+14` — Dread RulerⅢ (格鲁瑟恩+14)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +120% E-ATK: +120% Penetration (Absolute Value): +70% Crit Rate (Absolute Value): +70%
  - **Ⅳ** at `+T2` — Dread RulerIV (格鲁瑟恩+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +150% E-ATK: +150% Penetration (Absolute Value): +90% Crit Rate (Absolute Value): +90%

**Slot 4 — Touch of Regeneration** (id 1885, unlocks at `+3`)
  - **Ⅰ** at `+3` — Touch of RegenerationⅠ (格鲁瑟恩+13)
    (Takes effect at the start of battle) Grusen's Regenerative Armor makes him immune to effects that reduce healing or prevent healing. (This effect cannot be disabled by skills that prevent other skill effects from taking effect.)
  - **Ⅱ** at `+13` — Touch of RegenerationⅡ (格鲁瑟恩+16)
    (Takes effect at the start of battle) Grusen's Regenerative Armor makes him immune to effects that reduce healing or prevent healing. (This effect cannot be disabled by skills that prevent other skill effects from taking effect.) At the start of battle, gain Rebirth. Reviving immediately upon death with 100% of initial HP and 150 Accumulator (unaffected by forbidding revival and rebirth effects).
  - **Ⅲ** at `+T1` — Touch of RegenerationⅢ (格鲁瑟恩+17)
    (Takes effect at the start of battle) Grusen's Regenerative Armor makes him immune to effects that reduce healing or prevent healing. (This effect cannot be disabled by skills that prevent other skill effects from taking effect.) At the start of battle, gain Rebirth. Reviving immediately upon death with 100% of initial HP and 150 Accumulator (unaffected by forbidding revival and rebirth effects). When taking lethal damage, you will not die immediately but instead trigger [Touch of Regeneration]. (Can trigger up to 3 times per battle.) [Touch of Regeneration]: Restores HP to 100%, recovers 300 Accumulator, and gains [Binding] status for 1 round, during which you are unable to act. While bound, you gain a shield equal to 1500% of your S-ATK. Each time this skill is triggered, your S-ATK increases by 80%, lasting until the end of the battle.
  - **Ⅳ** at `+T4` — Touch of RegenerationIV (格鲁瑟恩+20)
    (Takes effect at the start of battle) Grusen's Regenerative Armor makes him immune to effects that reduce healing or prevent healing. (This effect cannot be disabled by skills that prevent other skill effects from taking effect.) At the start of battle, gain Rebirth. Reviving immediately upon death with 100% of initial HP and 150 Accumulator (unaffected by forbidding revival and rebirth effects). If affected by certain control effects (Freeze, Lock, Confusion, Forbidding Skill Use, Petrify, Icebound, Entangle), they will be transferred to a random enemy unit. When taking lethal damage(Ignores immunity to lethal and instant destruction effects), you will not die immediately but instead trigger [Touch of Regeneration]. (Can trigger up to 3 times per battle.) [Touch of Regeneration]: Restores HP to 100%, recovers 500 Accumulator, you gain a shield equal to 2000% of your S-ATK for 1 round. Each time this skill is triggered, your S-ATK increases by 100%, lasting until the end of the battle.

### Augment cost (per step)
- `+1` — 5× Destroyer Chip · 100,000 money
- `+2` — 10× Destroyer Chip · 200,000 money
- `+3` — 21× Destroyer Chip · 300,000 money
- `+4` — 28× Destroyer Chip · 500,000 money
- `+5` — 35× Destroyer Chip · 800,000 money
- `+6` — 42× Destroyer Chip · 10× Pandora Power Core
- `+7` — 49× Destroyer Chip · 50× Pandora Power Core
- `+8` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Grusen's Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Grusen's Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Grusen's Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Grusen's Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Grusen's Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Grusen's Part · 100× Alien Essence · 100× Transcendence Core

---

## 607 · Liora 莉奥拉
**Role** Destroyer · **Attack** energy · **Generation** latest
**Ratings** Damage 10/10 · Defence 9/10 · Assist 8/10

### Skill panels
**Slot 1 — Starrail Pierce** (id 1898, unlocks at `+0`)
  - **Ⅰ** at `+0` — Starrail PierceⅠ (莉奥拉+0)
    Cross Attack, plunders 50% Accumulator and 50% S-ATK from the target, then attacks the hit targets 3 times consecutively, each dealing 120% S-ATK damage. Lastly, recovers 100 Accumulator.
  - **Ⅱ** at `+6` — Starrail PierceⅡ (莉奥拉+2)
    Cross Attack, plunders 50% Accumulator and 50% S-ATK from the target, then attacks the hit targets 3 times consecutively, each dealing 150% S-ATK damage. Gains Eye of True Sight for 99 rounds. S-ATK is guaranteed to Penetrate (ignores Block). Lastly, recovers 100 Accumulator.
  - **Ⅲ** at `+10` — Starrail PierceⅢ (莉奥拉+6)
    Cross Attack, plunders 50% Accumulator and 50% S-ATK from the target, then attacks the hit targets 3 times consecutively, each dealing 180% S-ATK damage. Gains Eye of True Sight for 99 rounds. S-ATK is guaranteed to Penetrate (ignores Block). After casting a skill, increases own S-ATK and Crit ATK by 80%, up to a maximum of 240% S-ATK and 240% Crit ATK. Lastly, recovers 100 Accumulator.
  - **Ⅳ** at `+15` — Starrail PierceIV (莉奥拉+9)
    Cross Attack, plunders 50% Accumulator and 50% S-ATK from the target, then attacks the hit targets 3 times consecutively, each dealing 200% S-ATK damage. Gains Eye of True Sight for 99 rounds. S-ATK is guaranteed to Penetrate (ignores Block). Deals True Damage equal to 300% of the first attack's S-ATK damage to the enemy with the least HP. After casting a skill, increases own S-ATK and Crit ATK by 80%, up to a maximum of 240% S-ATK and 240% Crit ATK, lasting 99 rounds. Shatters Rebirth from the hit target. Lastly, recovers 100 Accumulator.

**Slot 2 — Void Pulse** (id 1899, unlocks at `+2`)
  - **Ⅰ** at `+2` — Void PulseⅠ (莉奥拉+2)
    (Takes effect at the start of battle) S-ATK is guaranteed to crit and has a 25% chance to come with Hunter Focus (The attack always hits, ignores Dodge, Evasive and Time Ward.).
  - **Ⅱ** at `+9` — Void PulseⅡ (莉奥拉+9)
    (Takes effect at the start of battle) S-ATK is guaranteed to crit and has a 50% chance to come with Hunter Focus (The attack always hits, ignores Dodge, Evasive and Time Ward.). Killing an enemy with an S-ATK increases damage by 50%, stacks up to 200%, lasting 99 rounds.
  - **Ⅲ** at `+T` — Void PulseⅢ (莉奥拉+16)
    (Takes effect at the start of battle) S-ATK is guaranteed to crit and has a 75% chance to come with Hunter Focus (The attack always hits, ignores Dodge, Evasive and Time Ward.). Killing an enemy with an S-ATK increases damage by 50%, stacks up to 200%, lasting 99 rounds. After using a skill, she gains [Dark Conceal], making herself immune to attacks and skill effects for 1 round. This effect requires a 1-round cooldown before it can trigger again.
  - **Ⅳ** at `+T3` — Void PulseIV (莉奥拉+19)
    (Takes effect at the start of battle) S-ATK is guaranteed to crit and has a 75% chance to come with Hunter Focus (The attack always hits, ignores Dodge, Evasive and Time Ward.). Killing an enemy with an S-ATK increases damage by 50%, stacks up to 200%, lasting 99 rounds. And there is a 100% chance to confuse all enemies for 1 round. After using a skill, she gains [Dark Conceal], making herself immune to attacks and skill effects for 1 round. This effect requires a 1-round cooldown before it can trigger again. After the first S-ATK at the start of battle, you immediately perform another S-ATK. (If revived after death, the count resets. S-ATKs triggered by [Rift Parry Field] cannot trigger this effect.)

**Slot 3 — Dimensional Rush** (id 1900, unlocks at `+4`)
  - **Ⅰ** at `+4` — Dimensional RushⅠ (莉奥拉+4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +60% E-ATK: +60% Penetration (Absolute Value): +30% Crit Rate (Absolute Value): +30%
  - **Ⅱ** at `+10` — Dimensional RushⅡ (莉奥拉+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +90% E-ATK: +90% Penetration (Absolute Value): +50% Crit Rate (Absolute Value): +50%
  - **Ⅲ** at `+14` — Dimensional RushⅢ (莉奥拉+14)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +120% E-ATK: +120% Penetration (Absolute Value): +70% Crit Rate (Absolute Value): +70%
  - **Ⅳ** at `+T2` — Dimensional RushIV (莉奥拉+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +150% E-ATK: +150% Penetration (Absolute Value): +90% Crit Rate (Absolute Value): +90%

**Slot 4 — Rift Parry Field** (id 1901, unlocks at `+3`)
  - **Ⅰ** at `+3` — Rift Parry FieldⅠ (莉奥拉+3)
    (Takes effect at the start of battle) Liora is immune to damage and abnormal statuses caused by enemy Destroyers (excluding subsequent damage).
  - **Ⅱ** at `+13` — Rift Parry FieldⅡ (莉奥拉+13)
    (Takes effect at the start of battle) Liora is immune to damage and abnormal statuses caused by enemy Destroyers (excluding subsequent damage). At the start of battle and each time she revive or rebirth, if under a control effect, there is a 100% chance to cleanse the control effect, recover 100 Accumulator, and proceed with subsequent actions, lasting for 2 rounds.
  - **Ⅲ** at `+T1` — Rift Parry FieldⅢ (莉奥拉+17)
    (Takes effect at the start of battle) Liora is immune to damage and abnormal statuses caused by enemy Destroyers (excluding subsequent damage). At the start of battle and each time she revive or rebirth, if under a control effect, there is a 100% chance to cleanse the control effect, recover 100 Accumulator, and proceed with subsequent actions, lasting for 2 rounds. At the start of battle, gain [Rift Parry Field]: when taking lethal damage, this damage will be blocked, and immediately perform one S-ATK to the enemy who dealt the damage(if the enemy cannot be targeted, select other enemies in the cross-shaped area; this effect can trigger up to 2 times per battle).
  - **Ⅳ** at `+T4` — Rift Parry FieldIV (莉奥拉+20)
    (Takes effect at the start of battle) Liora is immune to damage and abnormal statuses caused by enemy Destroyers (excluding subsequent damage). At the start of battle and each time she revive or rebirth, if under a control effect, there is a 100% chance to cleanse the control effect, recover 100 Accumulator, and proceed with subsequent actions, lasting for 2 rounds. When casting a skill, first removes all enemies' Invisible and Dark Conceal states, then proceeds with the follow-up actions. At the start of battle, gain [Rift Parry Field]: when taking lethal damage (Ignores immunity to lethal damage and instant destruction), this damage will be blocked, and immediately perform one S-ATK to the enemy who dealt the damage(if the enemy cannot be targeted, select other enemies in the cross-shaped area; this effect can trigger up to 2 times per battle). If no S-ATK has been cast by herself during this battle, the skill triggered by this effect will also exile the target for 1 round. Targets in exile cannot attack or be attacked, but effects on the target before exile will continue to apply.

### Augment cost (per step)
- `+1` — 5× Destroyer Chip · 100,000 money
- `+2` — 10× Destroyer Chip · 200,000 money
- `+3` — 21× Destroyer Chip · 300,000 money
- `+4` — 28× Destroyer Chip · 500,000 money
- `+5` — 35× Destroyer Chip · 800,000 money
- `+6` — 42× Destroyer Chip · 10× Pandora Power Core
- `+7` — 49× Destroyer Chip · 50× Pandora Power Core
- `+8` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Liora Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Liora Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Liora Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Liora Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Liora Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Liora Ship Part · 100× Alien Essence · 100× Transcendence Core

---

## 609 · Ariya 艾瑞娅
**Role** Destroyer · **Attack** energy · **Generation** latest
**Ratings** Damage 10/10 · Defence 6/10 · Assist 6/10

### Skill panels
**Slot 1 — Resonance-Piercing Shell** (id 1906, unlocks at `+0`)
  - **Ⅰ** at `+0` — Resonance-Piercing ShellⅠ (艾瑞娅+0)
    Cross Attack, first clears all buffs from the target, then plunders 50% of the target's S-ATK and 75% of their Accumulator for 2 rounds, and deals 320% S-ATK damage to the targets. Lastly, recovers 200 Accumulator.
  - **Ⅱ** at `+7` — Resonance-Piercing ShellⅡ (艾瑞娅+3(被动))
    Cross Attack, first clears all buffs from the target, then plunders 50% of the target's S-ATK and 75% of their Accumulator for 2 rounds, and deals 340% S-ATK damage to the targets. After casting a skill, increases own Crit ATK by 100%, stacking up to 3 times, lasting until the end of the battle. Lastly, recovers 200 Accumulator.
  - **Ⅲ** at `+15` — Resonance-Piercing ShellⅢ (艾瑞娅+7)
    Cross Attack, first clears all buffs from the target, then plunders 50% of the target's S-ATK and 75% of their Accumulator for 2 rounds, and deals 360% S-ATK damage to the targets. After casting a skill, increases own Crit ATK by 100%, stacking up to 3 times, lasting until the end of the battle. When the skill is activated, if current Accumulator is above 200, the S-ATK cannot be blocked; if current Accumulator is above 300, the S-ATK deals damage 3 additional times. Lastly, recovers 200 Accumulator.
  - **Ⅳ** at `+T3` — Resonance-Piercing ShellIV (艾瑞娅+9(被动))
    Cross Attack, first clears all buffs from the target, then plunders 50% of the target's S-ATK and 100% of their Accumulator(ignores immunity) for 2 rounds, and deals 380% S-ATK damage to the targets. After casting a skill, increases own Crit ATK by 100%, stacking up to 3 times, lasting until the end of the battle. When the skill is activated, if current Accumulator is above 200, the S-ATK cannot be blocked; if current Accumulator is above 300, the S-ATK deals damage 3 additional times. Removes all enemies' Invisible and Dark Conceal states. Lastly, recovers 200 Accumulator.

**Slot 2 — Plasma Corrosion** (id 1907, unlocks at `+3`)
  - **Ⅰ** at `+3` — Plasma CorrosionⅠ (艾瑞娅+3)
    (Takes effect at the start of battle) Own S-ATK are guaranteed critical hits and deal 300% extra damage to shields' damage reduction.
  - **Ⅱ** at `+9` — Plasma CorrosionⅡ (艾瑞娅+9)
    (Takes effect at the start of battle) Own S-ATK are guaranteed critical hits and deal 300% extra damage to shields' damage reduction. When causing a kill, additionally recovers 300 Accumulator and increases own Crit ATK by 100% (stacks up to 3 times), lasting until the end of battle.
  - **Ⅲ** at `+T1` — Plasma CorrosionⅢ (艾瑞娅+17)
    (Takes effect at the start of battle) Own S-ATK are guaranteed critical hits and deal 300% extra damage to shields' damage reduction. When causing a kill, additionally recovers 300 Accumulator and increases own Crit ATK by 100% (stacks up to 3 times), lasting until the end of battle. If the target's HP is below 50% after using an S-ATK, an extra S-ATK will be triggered. (This effect can trigger once per S-ATK; if the target is killed directly by the S-ATK, the effect still activates.)
  - **Ⅳ** at `+T4` — Plasma CorrosionIV (艾瑞娅+20)
    (Takes effect at the start of battle) Own S-ATK are guaranteed critical hits and deal 300% extra damage to shields' damage reduction. When causing a kill, additionally recovers 300 Accumulator and increases own Crit ATK by 100% (stacks up to 3 times), lasting until the end of battle. If the target's HP is below 50% after using an S-ATK, an extra S-ATK will be triggered. (This effect can trigger once per S-ATK; if the target is killed directly by the S-ATK, the effect still activates.) At the start of battle and each time resurrect rebirthed, gain Dark Conceal for 2 rounds, making own immune to attacks and skill effects.

**Slot 3 — Desperate Breakthrough** (id 1908, unlocks at `+5`)
  - **Ⅰ** at `+5` — Desperate BreakthroughⅠ (艾瑞娅+5)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): E-ATK: +40% S-ATK: +30% Crit ATK (Absolute Value): +20%
  - **Ⅱ** at `+11` — Desperate BreakthroughⅡ (艾瑞娅+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): E-ATK: +70% S-ATK: +60% Crit ATK (Absolute Value): +30%
  - **Ⅲ** at `+T` — Desperate BreakthroughⅢ (艾瑞娅+16)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): E-ATK: +100% S-ATK: +90% Crit ATK (Absolute Value): +40%
  - **Ⅳ** at `+T2` — Desperate BreakthroughIV (艾瑞娅+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): E-ATK: +150% S-ATK: +120% Crit ATK (Absolute Value): +60%

### Augment cost (per step)
- `+1` — 5× Destroyer Chip · 100,000 money
- `+2` — 10× Destroyer Chip · 200,000 money
- `+3` — 21× Destroyer Chip · 300,000 money
- `+4` — 28× Destroyer Chip · 500,000 money
- `+5` — 35× Destroyer Chip · 800,000 money
- `+6` — 42× Destroyer Chip · 10× Pandora Power Core
- `+7` — 49× Destroyer Chip · 50× Pandora Power Core
- `+8` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Elenia Exclusive Chip · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Elenia Exclusive Chip · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Elenia Exclusive Chip · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Elenia Exclusive Chip · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Elenia Exclusive Chip · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Elenia Exclusive Chip · 100× Alien Essence · 100× Transcendence Core

---

## 614 · Karon 卡隆
**Role** Destroyer · **Attack** energy · **Generation** latest
**Ratings** Damage 10/10 · Defence 6/10 · Assist 6/10

### Skill panels
**Slot 1 — Radiant Verdict・Skyrend** (id 1925, unlocks at `+0`)
  - **Ⅰ** at `+0` — Radiant Verdict・SkyrendⅠ (卡隆+0)
    Cross Attack, attacks the target hit 3 times, each attack dealing 120% S-ATK damage. Gains Eye of True Sight for 99 rounds. Lastly, you recover 100 Accumulator.
  - **Ⅱ** at `+6` — Radiant Verdict・SkyrendⅡ (卡隆+2)
    Cross Attack, attacks the target hit 3 times, each attack dealing 140% S-ATK damage. S-ATK always guarantees Penetration and always crits. Gains Eye of True Sight for 99 rounds. Lastly, you recover 100 Accumulator.
  - **Ⅲ** at `+10` — Radiant Verdict・SkyrendⅢ (卡隆+6)
    Cross Attack, first plunders 50% Accumulator and 75% S-ATK from the target, then attacks the target hit 3 times, each attack dealing 160% S-ATK damage. S-ATK always guarantees Penetration and always crits. Gains Eye of True Sight for 99 rounds. Lastly, you recover 100 Accumulator.
  - **Ⅳ** at `+15` — Radiant Verdict・SkyrendIV (卡隆+9)
    Cross Attack, first removes the target's buffs, then plunders 50% Accumulator and 75% S-ATK from the target, and attacks the target hit 3 times, each attack dealing 180% S-ATK damage. S-ATK always guarantees Penetration and always crits. When dealing S-ATK damage, if the target's HP ratio is above 90%, this hit damage dealt is increased by 100%. Gains Eye of True Sight for 99 rounds. Lastly, you recover 100 Accumulator.

**Slot 2 — Return Across Styx** (id 1926, unlocks at `+2`)
  - **Ⅰ** at `+2` — Return Across StyxⅠ (卡隆+2)
    (Takes effect at the start of battle) After casting a skill, increases own S-ATK by 30% and Crit ATK by 50%, lasting until the end of battle. (Stacks up to 5 times)
  - **Ⅱ** at `+9` — Return Across StyxⅡ (卡隆+9)
    (Takes effect at the start of battle) After casting a skill, increases own S-ATK by 30% and Crit ATK by 50%, lasting until the end of battle. (Stacks up to 5 times) When using a skill, the first enemy in a vertical line is enter Overload. Casting a skill will consume an additional 300% Accumulator, lasting for 2 rounds.
  - **Ⅲ** at `+T` — Return Across StyxⅢ (卡隆+16)
    (Takes effect at the start of battle) After casting a skill, increases own S-ATK by 30% and Crit ATK by 50%, lasting until the end of battle. (Stacks up to 5 times) When using a skill, the first enemy in a vertical line is enter Overload. Casting a skill will consume an additional 300% Accumulator, lasting for 2 rounds. If an S-ATK results in a kill, dispel all enemies' Rebirth effects.
  - **Ⅳ** at `+T3` — Return Across StyxIV (卡隆+19)
    (Takes effect at the start of battle) After casting a skill, increases own S-ATK by 30% and Crit ATK by 50%, lasting until the end of battle. (Stacks up to 5 times) When using a skill, the first enemy in a vertical line is enter Overload. Casting a skill will consume an additional 300% Accumulator, lasting for 2 rounds. If an S-ATK results in a kill, dispel all enemies' Rebirth effects. When Karon takes lethal damage (including ignoring immunity to lethal attacks and instant destruction effects), the damage is blocked, and all allies turn invisible for 2 rounds. (Can only trigger once per battle)

**Slot 3 — Will of Divinity** (id 1927, unlocks at `+4`)
  - **Ⅰ** at `+4` — Will of DivinityⅠ (卡隆+4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +60% E-ATK: +60% Penetration (Absolute Value): +30% Crit Rate (Absolute Value): +30%
  - **Ⅱ** at `+10` — Will of DivinityⅡ (卡隆+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +90% E-ATK: +90% Penetration (Absolute Value): +50% Crit Rate (Absolute Value): +50%
  - **Ⅲ** at `+14` — Will of DivinityⅢ (卡隆+14)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +120% E-ATK: +120% Penetration (Absolute Value): +70% Crit Rate (Absolute Value): +70%
  - **Ⅳ** at `+T2` — Will of DivinityIV (卡隆+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +150% E-ATK: +150% Penetration (Absolute Value): +90% Crit Rate (Absolute Value): +90%

**Slot 4 — Supernova・Shadow Collapse** (id 1928, unlocks at `+0`)
  - **Ⅰ** at `+0` — Supernova・Shadow CollapseⅠ (卡隆+0)
    (Takes effect at the start of battle) Karon's Will of Divinity makes him immune to Lock effects, but he cannot gain effects provided by [Slaughter Feast] and [Fatal Pursuit]. (This includes ignoring all immunity and protection effects, and this effect cannot be disabled by skills that prohibit skill effects.)
  - **Ⅱ** at `+13` — Supernova・Shadow CollapseⅡ (卡隆+13)
    (Takes effect at the start of battle) Karon's Will of Divinity makes him immune to Lock effects. After casting a skill, he immediately performs an additional vertical S-ATK with [Radiant Verdict・Gleamedge], with the same effects as the original skill. However, he cannot gain effects provided by [Slaughter Feast] and [Fatal Pursuit]. (This includes ignoring all immunity and protection effects, and this effect cannot be disabled by skills that prohibit skill effects.)
  - **Ⅲ** at `+T1` — Supernova・Shadow CollapseⅢ (卡隆+17)
    (Takes effect at the start of battle) Karon's Will of Divinity makes him immune to Lock effects. After casting a skill, he immediately performs an additional vertical S-ATK with [Radiant Verdict・Gleamedge], with the same effects as the original skill. However, he cannot gain effects provided by [Slaughter Feast] and [Fatal Pursuit]. (This includes ignoring all immunity and protection effects, and this effect cannot be disabled by skills that prohibit skill effects.) His S-ATK is guaranteed to hit and can target units in Dark Conceal.
  - **Ⅳ** at `+T4` — Supernova・Shadow CollapseIV (卡隆+20)
    (Takes effect at the start of battle) Karon's Will of Divinity makes him immune to Lock effects. After casting a skill, he immediately performs an additional vertical S-ATK with [Radiant Verdict・Gleamedge], with the same effects as the original skill. However, he cannot gain effects provided by [Slaughter Feast] and [Fatal Pursuit]. (This includes ignoring all immunity and protection effects, and this effect cannot be disabled by skills that prohibit skill effects.) His S-ATK is guaranteed to hit and can target units in Dark Conceal. After using [Radiant Verdict・Gleamedge] S-ATK, if the target's HP is below 40%, an additional S-ATK is performed. (This effect can only trigger once per S-ATK; if the S-ATK directly kills the target, it is also considered to meet the condition.) If there are other members of the Supernova Blades Fleet (Aiolia, Ouros, Mu, Teda, Ulysses) in the team, when Karon casts a skill for the first time at the start of battle, Ouros, Teda, and Ulysses gain [Directional Shield] for 1 round, which will be removed at the start of their next ally action after being attacked during its duration. Aiolia and Mu gain [Dark Conceal], making them immune to attacks and skill effects for 1 round.

### Augment cost (per step)
- `+1` — 5× Destroyer Chip · 100,000 money
- `+2` — 10× Destroyer Chip · 200,000 money
- `+3` — 21× Destroyer Chip · 300,000 money
- `+4` — 28× Destroyer Chip · 500,000 money
- `+5` — 35× Destroyer Chip · 800,000 money
- `+6` — 42× Destroyer Chip · 10× Pandora Power Core
- `+7` — 49× Destroyer Chip · 50× Pandora Power Core
- `+8` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Elenia Exclusive Chip · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Elenia Exclusive Chip · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Elenia Exclusive Chip · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Elenia Exclusive Chip · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Elenia Exclusive Chip · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Elenia Exclusive Chip · 100× Alien Essence · 100× Transcendence Core

---

## 619 · Tagnias 塔格尼亚斯
**Role** Destroyer · **Attack** energy · **Generation** latest
**Ratings** Damage 10/10 · Defence 8/10 · Assist 6/10

### Skill panels
**Slot 1 — Supercore Gravitational Collapse** (id 1945, unlocks at `+0`)
  - **Ⅰ** at `+0` — Supercore Gravitational CollapseⅠ (塔格尼亚斯+0)
    Cross Attack, attacks the target hit 4 times, each attack dealing 100% S-ATK damage. Gains Eye of True Sight for 99 rounds. Lastly, recovers 100 Accumulator.
  - **Ⅱ** at `+6` — Supercore Gravitational CollapseⅡ (塔格尼亚斯+2)
    Cross Attack, first removes the target's buffs, then plunders 50% Accumulator and 70% S-ATK from the target, and attacks the target hit 4 times, each attack dealing 110% S-ATK damage. Gains Eye of True Sight for 99 rounds. Lastly, recovers 100 Accumulator.
  - **Ⅲ** at `+10` — Supercore Gravitational CollapseⅢ (塔格尼亚斯+3)
    Cross Attack, first removes the target's buffs, then plunders 50% Accumulator and 70% S-ATK from the target, and attacks the target hit 4 times, each attack dealing 120% S-ATK damage. Increases self Damage by 120% and Crit ATK by 300% for 2 rounds. Gains Eye of True Sight for 99 rounds. Lastly, recovers 100 Accumulator.
  - **Ⅳ** at `+15` — Supercore Gravitational CollapseIV (塔格尼亚斯+6)
    Cross Attack, first removes the target's buffs, then plunders 50% Accumulator and 70% S-ATK from the target, and attacks the target hit 4 times, each attack dealing 140% S-ATK damage. Increases self Damage by 120% and Crit ATK by 300% for 2 rounds. Gains Eye of True Sight for 99 rounds. If the S-ATK hits only one enemy, dispels the target's Rebirth effect. Lastly, recovers 100 Accumulator.

**Slot 2 — Supercore Stabilization Field** (id 1946, unlocks at `+2`)
  - **Ⅰ** at `+2` — Supercore Stabilization FieldⅠ (塔格尼亚斯+2)
    (Takes effect at the start of battle) Own S-ATK is guaranteed to crit hit.
  - **Ⅱ** at `+9` — Supercore Stabilization FieldⅡ (塔格尼亚斯+9)
    (Takes effect at the start of battle) Own S-ATK is guaranteed to crit hit. After casting a skill, increases own E-ATK by 40%, lasting until the end of battle. (Stacks up to 5 times)
  - **Ⅲ** at `+T` — Supercore Stabilization FieldⅢ (塔格尼亚斯+16)
    (Takes effect at the start of battle) Own S-ATK is guaranteed to crit hit. After casting a skill, increases own E-ATK by 40%, lasting until the end of battle. (Stacks up to 5 times) The enemies killed will be locked for 1 round after being revived.
  - **Ⅳ** at `+T3` — Supercore Stabilization FieldIV (塔格尼亚斯+19)
    (Takes effect at the start of battle) Own S-ATK is guaranteed to crit hit. After casting a skill, increases own E-ATK by 40%, lasting until the end of battle. (Stacks up to 5 times) The enemies killed will be locked for 1 round after being revived. If the S-ATK hits only one enemy, that enemy’s Active skill effects are disabled for 1 round.

**Slot 3 — Simulacrum** (id 1947, unlocks at `+4`)
  - **Ⅰ** at `+4` — SimulacrumⅠ (塔格尼亚斯+4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +60% E-ATK: +60% Penetration (Absolute Value): +30% Crit Rate (Absolute Value): +30%
  - **Ⅱ** at `+10` — SimulacrumⅡ (塔格尼亚斯+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +90% E-ATK: +90% Penetration (Absolute Value): +50% Crit Rate (Absolute Value): +50%
  - **Ⅲ** at `+14` — SimulacrumⅢ (塔格尼亚斯+14)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +120% E-ATK: +120% Penetration (Absolute Value): +70% Crit Rate (Absolute Value): +70%
  - **Ⅳ** at `+T2` — SimulacrumIV (塔格尼亚斯+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +150% E-ATK: +150% Penetration (Absolute Value): +90% Crit Rate (Absolute Value): +90%

**Slot 4 — Supercore Symbiosis** (id 1948, unlocks at `+3`)
  - **Ⅰ** at `+3` — Supercore SymbiosisⅠ (塔格尼亚斯+3)
    (Takes effect at the start of battle) At the start of battle and when casting a skill, randomly select one enemy to gain [Supercore Symbiosis] based on priority order, lasting until the end of battle or until the unit dies. The order is: Protector, Rover, Ranger. (If the highest priority Type is dead or absent, selects the next Type in order; If no eligible type exists, this effect does not trigger.) [Supercore Symbiosis]: After this enemy casts a skill, Tagnias restores 80% of max HP.
  - **Ⅱ** at `+13` — Supercore SymbiosisⅡ (塔格尼亚斯+13)
    (Takes effect at the start of battle) At the start of battle and when casting a skill, randomly select one enemy to gain [Supercore Symbiosis] based on priority order, lasting until the end of battle or until the unit dies. The order is: Protector, Rover, Ranger. (If the highest priority Type is dead or absent, selects the next Type in order; If no eligible type exists, this effect does not trigger.) [Supercore Symbiosis]: After this enemy casts a skill, Tagnias restores 80% of max HP, and Tagnias gains [Dark Conceal] for 1 round.
  - **Ⅲ** at `+T1` — Supercore SymbiosisⅢ (塔格尼亚斯+17)
    (Takes effect at the start of battle) At the start of battle and when casting a skill, randomly select one enemy to gain [Supercore Symbiosis] based on priority order, lasting until the end of battle or until the unit dies. The order is: Protector, Rover, Ranger. (If the highest priority Type is dead or absent, selects the next Type in order; If no eligible type exists, this effect does not trigger.) [Supercore Symbiosis]: After this enemy casts a skill, Tagnias restores 80% of max HP, and Tagnias gains [Dark Conceal] for 1 round. When taking lethal damage (ignores immunity to lethal attacks and instant destruction effects), the damage is blocked, then the enemy with [Supercore Symbiosis] has its HP reduced to 1. (Can only trigger once per battle)
  - **Ⅳ** at `+T4` — Supercore SymbiosisIV (塔格尼亚斯+20)
    (Takes effect at the start of battle) At the start of battle and when casting a skill, randomly select one enemy to gain [Supercore Symbiosis] based on priority order, lasting until the end of battle or until the unit dies. The order is: Protector, Rover, Ranger. (If the highest priority Type is dead or absent, selects the next Type in order; If no eligible type exists, this effect does not trigger.) [Supercore Symbiosis]: After this enemy casts a skill, Tagnias restores 80% of max HP, and Tagnias gains [Dark Conceal] for 1 round. When taking lethal damage (ignores immunity to lethal attacks and instant destruction effects), the damage is blocked, then the enemy with [Supercore Symbiosis] has its HP reduced to 1. (Can only trigger once per battle) While an enemy with [Supercore Symbiosis] is alive, an aura is emitted: It will disable the skill effect of "reviving allies when casting a skill" for all other allies except itself. When the ally with [Supercore Symbiosis] dies, this effect is removed.

### Augment cost (per step)
- `+1` — 5× Destroyer Chip · 100,000 money
- `+2` — 10× Destroyer Chip · 200,000 money
- `+3` — 21× Destroyer Chip · 300,000 money
- `+4` — 28× Destroyer Chip · 500,000 money
- `+5` — 35× Destroyer Chip · 800,000 money
- `+6` — 42× Destroyer Chip · 10× Pandora Power Core
- `+7` — 49× Destroyer Chip · 50× Pandora Power Core
- `+8` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Tagnias Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Tagnias Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Tagnias Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Tagnias Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Tagnias Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Tagnias Ship Part · 100× Alien Essence · 100× Transcendence Core

---

## 628 · Qin Yue 秦月
**Role** Destroyer · **Attack** energy · **Generation** latest
**Ratings** Damage 10/10 · Defence 6/10 · Assist 6/10

### Skill panels
**Slot 1 — Phantom Shadowblink** (id 1976, unlocks at `+0`)
  - **Ⅰ** at `+0` — Phantom ShadowblinkⅠ (秦月+0)
    Cross Attack, first plunders 75% Accumulator and 80% Hit Rate from the target, then attacks the hit targets 2 times consecutively, each dealing 200% S-ATK damage. Lastly, recovers 100 Accumulator.
  - **Ⅱ** at `+6` — Phantom ShadowblinkⅡ (秦月+2)
    Cross Attack, first plunders 75% Accumulator and 80% Hit Rate from the target, then attacks the hit targets 2 times consecutively, each dealing 220% S-ATK damage. Gains Eye of True Sight until the end of the battle. Lastly, recovers 100 Accumulator.
  - **Ⅲ** at `+10` — Phantom ShadowblinkⅢ (秦月+3)
    Cross Attack, first plunders 75% Accumulator and 80% Hit Rate from the target, then attacks the hit targets 2 times consecutively, each dealing 260% S-ATK damage. After each skill cast, increases own Crit ATK by 100%, stacking up to 3 times, lasting until the end of the BATTLE. Gains Eye of True Sight until the end of the battle. Lastly, recovers 100 Accumulator.
  - **Ⅳ** at `+15` — Phantom ShadowblinkIV (秦月+6)
    Cross Attack, first plunders 75% Accumulator and 80% Hit Rate from the target, then attacks the hit targets 2 times consecutively, each dealing 300% S-ATK damage. After each skill cast, increases own Crit ATK by 100%, stacking up to 3 times, lasting until the end of the BATTLE. Gains Eye of True Sight until the end of the battle. Deals True Damage equal to 150% of the first stage S-ATK damage to each enemy ship with less than 75% HP. Lastly, recovers 100 Accumulator.

**Slot 2 — Insight** (id 1977, unlocks at `+2`)
  - **Ⅰ** at `+2` — InsightⅠ (秦月+2)
    (Takes effect at the start of battle) At the start of battle, there is a 100% chance to gain Evasion, guaranteeing a dodge against enemy attacks for 2 rounds. Each time the skill [Phantom Shadowblink] is used, removes self's Evasion effect.
  - **Ⅱ** at `+9` — InsightⅡ (秦月+9)
    (Takes effect at the start of battle) At the start of battle, there is a 100% chance to gain Evasion, guaranteeing a dodge against enemy attacks for 2 rounds. Each time the skill [Phantom Shadowblink] is used, removes self's Evasion effect. At the start of battle and each time [Phantom Shadowblink] is used, gains [Insight] for 2 rounds or until triggered (repeated use will not increase the number of effects). [Insight]: The next time the unit receives an S-ATK, completely absorbs the incoming S-ATK damage. If the hero is not in a state of inability to act, immediately triggers [Counterattack], launching a vertical attack against the source of the attack, dealing HP equal to 100% of the absorbed damage to targets. Removed after triggering once. (If the target is already dead or cannot be selected, a vertical attack is launched directly.)
  - **Ⅲ** at `+T` — InsightⅢ (秦月+16)
    (Takes effect at the start of battle) At the start of battle, there is a 100% chance to gain Evasion, guaranteeing a dodge against enemy attacks for 2 rounds. Each time the skill [Phantom Shadowblink] is used, removes self's Evasion effect. At the start of battle and each time [Phantom Shadowblink] is used, gains [Insight] for 2 rounds or until triggered (repeated use will not increase the number of effects). [Insight]: The next time the unit receives an S-ATK, completely absorbs the incoming S-ATK damage. If the hero is not in a state of inability to act, immediately triggers [Counterattack], launching a vertical attack against the source of the attack, dealing HP equal to 150% of the absorbed damage to targets. Removed after triggering once. (If the target is already dead or cannot be selected, a vertical attack is launched directly.) After a counterattack is triggered by [Insight], gains Evasion, guaranteeing Dodge against enemy attacks for 2 rounds.
  - **Ⅳ** at `+T3` — InsightIV (秦月+19)
    (Takes effect at the start of battle) At the start of battle, there is a 100% chance to gain Evasion, guaranteeing a dodge against enemy attacks for 2 rounds. Each time the skill [Phantom Shadowblink] is used, removes self's Evasion effect. At the start of battle and each time [Phantom Shadowblink] is used, gains [Insight] for 2 rounds or until triggered (repeated use will not increase the number of effects). [Insight]: The next time the unit receives an S-ATK, completely absorbs the incoming S-ATK damage. If the hero is not in a state of inability to act, immediately triggers [Counterattack], launching a vertical attack against the source of the attack, dealing HP equal to 150% of the absorbed damage to targets. Removed after triggering once. (If the target is already dead or cannot be selected, a vertical attack is launched directly.) After a counterattack is triggered by [Insight], gains Evasion, guaranteeing Dodge against enemy attacks for 2 rounds, and has an additional 50% chance to gain [Dark Conceal] for 1 round, making self immune to attacks and skill effects.

**Slot 3 — Stormslash** (id 1978, unlocks at `+4`)
  - **Ⅰ** at `+4` — StormslashⅠ (秦月+4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): E-ATK: +40% S-ATK: +30% Crit ATK (Absolute Value): +20%
  - **Ⅱ** at `+10` — StormslashⅡ (秦月+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): E-ATK: +70% S-ATK: +60% Crit ATK (Absolute Value): +30%
  - **Ⅲ** at `+14` — StormslashⅢ (秦月+14)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): E-ATK: +100% S-ATK: +90% Crit ATK (Absolute Value): +40%
  - **Ⅳ** at `+T2` — StormslashIV (秦月+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): E-ATK: +150% S-ATK: +120% Crit ATK (Absolute Value): +60%

**Slot 4 — Unbroken Calm** (id 201978, unlocks at `+3`)
  - **Ⅰ** at `+3` — Unbroken CalmⅠ (秦月+4)
    (Takes effect at the start of battle) After self casts S-ATK, the target cannot Dodge when taking damage, lasting 2 rounds.
  - **Ⅱ** at `+13` — Unbroken CalmⅡ (秦月+11)
    (Takes effect at the start of battle) After self casts S-ATK, the target cannot Dodge when taking damage, lasting 2 rounds. Own S-ATK are guaranteed critical hits. Any Crit Rate above 200% is converted to Crit ATK at a 1:1 ratio, up to a maximum of 100%.
  - **Ⅲ** at `+T1` — Unbroken CalmⅢ (秦月+14)
    (Takes effect at the start of battle) After self casts S-ATK, the target cannot Dodge when taking damage, lasting 2 rounds. Own S-ATK are guaranteed critical hits. Any Crit Rate above 200% is converted to Crit ATK at a 1:1 ratio, up to a maximum of 100%. S-ATK comes with Hunter Focus: the attack guaranteed hits, ignores Dodge, Evasion and Time Ward.
  - **Ⅳ** at `+T4` — Unbroken CalmIV (秦月+18)
    (Takes effect at the start of battle) After self casts S-ATK, the target cannot Dodge when taking damage, lasting 2 rounds. Own S-ATK are guaranteed critical hits. Any Crit Rate above 200% is converted to Crit ATK at a 1:1 ratio, up to a maximum of 200%. S-ATK comes with Hunter Focus: the attack guaranteed hits, ignores Dodge, Evasion and Time Ward, and can hit units in Dark Conceal. If Accumulator is below 100, restore it to 200 before acting.

### Augment cost (per step)
- `+1` — 5× Destroyer Chip · 100,000 money
- `+2` — 10× Destroyer Chip · 200,000 money
- `+3` — 21× Destroyer Chip · 300,000 money
- `+4` — 28× Destroyer Chip · 500,000 money
- `+5` — 35× Destroyer Chip · 800,000 money
- `+6` — 42× Destroyer Chip · 10× Pandora Power Core
- `+7` — 49× Destroyer Chip · 50× Pandora Power Core
- `+8` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Qin Yue's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Qin Yue's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Qin Yue's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Qin Yue's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Qin Yue's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Qin Yue's Ship Part · 100× Alien Essence · 100× Transcendence Core

---

## 630 · Jiang Changxing 江长行
**Role** Destroyer · **Attack** energy · **Generation** old
**Ratings** Damage 9/10 · Defence 8/10 · Assist 10/10

### Signature skill
- **Ⅰ** at `+0` — Cloudrend (副官+0)
  Cross Attack, deals 200% S-ATK damage to targets. Lastly, you recover 100 Accumulator.

### Augment cost (per step)
- `+1` — 5× Destroyer Chip · 100,000 money
- `+2` — 10× Destroyer Chip · 200,000 money
- `+3` — 21× Destroyer Chip · 300,000 money
- `+4` — 28× Destroyer Chip · 500,000 money
- `+5` — 35× Destroyer Chip · 800,000 money
- `+6` — 42× Destroyer Chip · 10× Pandora Power Core
- `+7` — 49× Destroyer Chip · 50× Pandora Power Core
- `+8` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Jiang Changxing's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Jiang Changxing's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Jiang Changxing's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Jiang Changxing's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Jiang Changxing's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Jiang Changxing's Ship Part · 100× Alien Essence · 100× Transcendence Core

---

## 633 · Joe Lever 乔・雷弗
**Role** Destroyer · **Attack** energy · **Generation** latest
**Ratings** Damage 10/10 · Defence 6/10 · Assist 6/10

### Skill panels
**Slot 1 — Hunting Grounds** (id 1992, unlocks at `+0`)
  - **Ⅰ** at `+0` — Hunting GroundsⅠ (乔・雷弗+0)
    During battle preparation, if placed in the front row, the unit will enter [Encircling Hunt] state; if placed in the second or third row, the unit will enter [Standoff] state. Upon entering BATTLE, different skills will be triggered depending on the state. [Encircling Hunt]: Cross attack, first removes buffs from the target, then deals 300% S-ATK damage to the target. Finally, recovers 100 Accumulator. [Standoff]: Single attack, plunders 50% of the target's Accumulator and 75 S-ATK, then deals 280% S-ATK damage to the target. Finally, recovers 100 Accumulator.
  - **Ⅱ** at `+6` — Hunting GroundsⅡ (乔・雷弗+2)
    During battle preparation, if placed in the front row, the unit will enter [Encircling Hunt] state; if placed in the second or third row, the unit will enter [Standoff] state. Upon entering BATTLE, different skills will be triggered depending on the state. [Encircling Hunt]: Cross attack, first removes buffs from the target, then deals 350% S-ATK damage to the target. If the target's HP ratio is above 80%, this attack deals 100% additional damage. Finally, recovers 100 Accumulator. [Standoff]: Single attack, plunders 50% of the target's Accumulator and 75 S-ATK, then deals 300% S-ATK damage to the target. Finally, recovers 200 Accumulator.
  - **Ⅲ** at `+10` — Hunting GroundsⅢ (乔・雷弗+6)
    During battle preparation, if placed in the front row, the unit will enter [Encircling Hunt] state; if placed in the second or third row, the unit will enter [Standoff] state. Upon entering BATTLE, different skills will be triggered depending on the state. [Encircling Hunt]: Cross attack, first removes buffs from the target, then deals 400% S-ATK damage to the target. If the target's HP ratio is above 80%, this attack deals 100% additional damage. Deals an additional 180% damage to shields that offset damage. Finally, recovers 100 Accumulator. [Standoff]: Single attack, plunders 50% of the target's Accumulator and 75 S-ATK, then deals 320% S-ATK damage to the target. When dealing damage, for every 1% of max HP the target has lost, the damage dealt is increased by 3%. Finally, recovers 200 Accumulator.
  - **Ⅳ** at `+T` — Hunting GroundsIV (乔・雷弗+9)
    During battle preparation, if placed in the front row, the unit will enter [Encircling Hunt] state; if placed in the second or third row, the unit will enter [Standoff] state. Upon entering BATTLE, different skills will be triggered depending on the state. [Encircling Hunt]: Cross attack, first removes buffs from the target, then deals 450% S-ATK damage to the target. If the target's HP ratio is above 80%, this attack deals 100% additional damage. Deals an additional 180% damage to shields that offset damage. Gains Eye of True Sight for 99 rounds. Finally, recovers 100 Accumulator. [Standoff]: Single attack, plunders 50% of the target's Accumulator and 75 S-ATK, then deals 360% S-ATK damage to the target. When dealing damage, for every 1% of max HP the target has lost, the damage dealt is increased by 3%. Gains Eye of True Sight for 99 rounds, and the S-ATK can target units in Dark Conceal. Finally, recovers 200 Accumulator.

**Slot 2 — Final Showdown** (id 1993, unlocks at `+2`)
  - **Ⅰ** at `+2` — Final ShowdownⅠ (乔・雷弗+2)
    (Takes effect at the start of battle) S-ATK under the [Encircling Hunt] state deals 1 additional hit of 100% S-ATK damage; S-ATK under the [Standoff] state deals 2 additional hits of 200% S-ATK damage. For every 60 Accumulator consumed when casting an S-ATK, the number of additional hits increases by 1, up to a maximum of 3 times.
  - **Ⅱ** at `+9` — Final ShowdownⅡ (乔・雷弗+9)
    (Takes effect at the start of battle) S-ATK under the [Encircling Hunt] state deals 2 additional hit of 120% S-ATK damage; S-ATK under the [Standoff] state deals 3 additional hits of 220% S-ATK damage. For every 60 Accumulator consumed when casting an S-ATK, the number of additional hits increases by 1, up to a maximum of 4 times. Killing an enemy with an S-ATK, increases the hero's S-ATK by 30% and Crit ATK by 50%, lasting until the end of battle (stacks up to 5 times).
  - **Ⅲ** at `+15` — Final ShowdownⅢ (乔・雷弗+15)
    (Takes effect at the start of battle) S-ATK under the [Encircling Hunt] state deals 3 additional hit of 130% S-ATK damage; S-ATK under the [Standoff] state deals 4 additional hits of 240% S-ATK damage. For every 60 Accumulator consumed when casting an S-ATK, the number of additional hits increases by 1, up to a maximum of 5 times. Killing an enemy with an S-ATK, increases the hero's S-ATK by 30% and Crit ATK by 50%, lasting until the end of battle (stacks up to 5 times), and gains Rebirth, reviving immediately upon death with 100% of initial HP and 100 Accumulator (unaffected by forbidding revival and rebirth effects).
  - **Ⅳ** at `+T3` — Final ShowdownIV (乔・雷弗+19)
    (Takes effect at the start of battle) S-ATK under the [Encircling Hunt] state deals 3 additional hit of 150% S-ATK damage; S-ATK under the [Standoff] state deals 5 additional hits of 300% S-ATK damage. For every 60 Accumulator consumed when casting an S-ATK, the number of additional hits increases by 1, up to a maximum of 8 times. Killing an enemy with an S-ATK, increases the hero's S-ATK by 30% and Crit ATK by 50%, lasting until the end of battle (stacks up to 5 times), and gains Rebirth, reviving immediately upon death with 100% of initial HP and 100 Accumulator (unaffected by forbidding revival and rebirth effects). S-ATK in [Encircling Hunt] state ignores immunity to death and time-space stasis effects, and deals true damage equal to 200% of the first stage S-ATK total damage to the enemy ship with the lowest HP. S-ATK in [Standoff] state grants a shield that blocks 1 attack, and when casting a skill, for the portion of Accumulator consumed over 100, each additional point increases extra damage by 0.2%.

**Slot 3 — Bounty Hunter** (id 1994, unlocks at `+4`)
  - **Ⅰ** at `+4` — Bounty HunterⅠ (乔・雷弗+4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +60% E-ATK: +60% Penetration (Absolute Value): +30% Crit Rate (Absolute Value): +30%
  - **Ⅱ** at `+10` — Bounty HunterⅡ (乔・雷弗+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +90% E-ATK: +90% Penetration (Absolute Value): +50% Crit Rate (Absolute Value): +50%
  - **Ⅲ** at `+14` — Bounty HunterⅢ (乔・雷弗+14)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +120% E-ATK: +120% Penetration (Absolute Value): +70% Crit Rate (Absolute Value): +70%
  - **Ⅳ** at `+T2` — Bounty HunterIV (乔・雷弗+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +150% E-ATK: +150% Penetration (Absolute Value): +90% Crit Rate (Absolute Value): +90%

**Slot 4 — Sheath Break** (id 1995, unlocks at `+3`)
  - **Ⅰ** at `+3` — Sheath BreakⅠ (乔・雷弗+3)
    (Takes effect at the start of battle) At the start of battle, gain an additional 200 Accumulator.
  - **Ⅱ** at `+13` — Sheath BreakⅡ (乔・雷弗+13)
    (Takes effect at the start of battle) At the start of battle, gain an additional 200 Accumulator. At the start of battle and upon each revival or rebirth, there is a 100% chance to purifies the control effect before subsequent actions, lasting for 2 rounds.
  - **Ⅲ** at `+T1` — Sheath BreakⅢ (乔・雷弗+17)
    (Takes effect at the start of battle) At the start of battle, gain an additional 200 Accumulator. At the start of battle and upon each revival or rebirth, there is a 100% chance to purifies the control effect before subsequent actions, lasting for 2 rounds. When casting a skill, gain Accumulator equal to 50% of all allies' (excluding self) current total Accumulator, up to a maximum of 300.
  - **Ⅳ** at `+T4` — Sheath BreakIV (乔・雷弗+20)
    (Takes effect at the start of battle) At the start of battle, gain an additional 200 Accumulator. At the start of battle and upon each revival or rebirth, there is a 100% chance to purifies the control effect before subsequent actions, lasting for 2 rounds. When casting a skill, gain Accumulator equal to 50% of all allies' (excluding self) current total Accumulator, up to a maximum of 300. When entering battle or being revival/rebirth under [Encircling Hunt] status, gain [Dark Conceal] for 2 rounds, making self immune to attacks and skill effects. When entering battle under [Standoff] status, immediately take action once. (Reviving after death does not trigger the immediate action effect)

### Augment cost (per step)
- `+1` — 5× Destroyer Chip · 100,000 money
- `+2` — 10× Destroyer Chip · 200,000 money
- `+3` — 21× Destroyer Chip · 300,000 money
- `+4` — 28× Destroyer Chip · 500,000 money
- `+5` — 35× Destroyer Chip · 800,000 money
- `+6` — 42× Destroyer Chip · 10× Pandora Power Core
- `+7` — 49× Destroyer Chip · 50× Pandora Power Core
- `+8` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Destroyer Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Destroyer Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Joe Lever's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Joe Lever's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Joe Lever's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Joe Lever's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Joe Lever's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Joe Lever's Ship Part · 100× Alien Essence · 100× Transcendence Core

---
