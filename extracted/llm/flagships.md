# Galaxy Legends — SSS Flagships (24 heroes)

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
| 366 | Elijah | 以利亚 | 9 | 8 | 5 | old |
| 402 | Natasha | 娜塔莎 | 8 | 7 | 7 | old |
| 440 | Sorcerer Supreme | 至尊法师 | 8 | 7 | 7 | old |
| 451 | Valerian | 瓦利安 | 10 | 6 | 8 | old |
| 469 | Jayce Lot | 杰斯·洛特 | 10 | 10 | 8 | old |
| 477 | Erlang Shen | 杨戬 | 10 | 6 | 8 | old |
| 491 | Freya | 芙蕾雅 | 10 | 10 | 8 | old |
| 498 | Patton | 巴顿 | 10 | 10 | 8 | old |
| 503 | Chronos | 柯罗诺斯 | 10 | 6 | 8 | old |
| 514 | Galaxy Inquisitor No. 9 | 银河审判者9号 | 10 | 6 | 8 | old |
| 529 | Janus | 亚努斯 | 10 | 6 | 8 | old |
| 538 | Saint Kilian | 圣·凯尔 | 10 | 6 | 8 | latest |
| 546 | Gale | 疾风 | 10 | 10 | 8 | latest |
| 553 | Elenia | 伊莲尼亚 | 10 | 6 | 8 | latest |
| 565 | Baralson | 巴拉森 | 8 | 7 | 7 | latest |
| 579 | Shi Yu | 时宇 | 10 | 6 | 8 | latest |
| 586 | Altrius | 阿尔特瑞斯 | 10 | 10 | 8 | latest |
| 601 | Domina Hayley | 多米娜·海伊莉 | 10 | 10 | 8 | latest |
| 611 | Aiolia | 艾奥里亚 | 10 | 8 | 10 | latest |
| 629 | Elowyn | 爱洛温 | 9 | 8 | 10 | latest |
| 638 | E | E | 10 | 8 | 9 | latest |
| 641 | Jayce Lot - Silver Wolf | 杰斯·洛特-银狼 | 10 | 7 | 9 | latest |
| 643 | — | 柯罗诺斯SP | 7 | 9 | 10 | latest |
| 646 | Perthera | 珀瑟拉 | 9 | 8 | 10 | latest |

---

## 366 · Elijah 以利亚
**Role** Flagship · **Attack** physical · **Generation** old
**Ratings** Damage 9/10 · Defence 8/10 · Assist 5/10

### Signature skill
- **Ⅰ** at `+0` — Lava Purge (以利亚，熔岩净化)
  Vertical attack, deals 210% S-ATK damage and 6M True Damage (ignores defense), then clears targets' Accumulator. In addition, recover 100 Accumulator for self.

### Augment cost (per step)
- `+1` — 2× Flagship Chip · 1,000 money
- `+2` — 10× Flagship Chip · 20,000 money
- `+3` — 20× Flagship Chip · 300,000 money
- `+4` — 40× Flagship Chip · 500,000 money
- `+5` — 50× Flagship Chip · 800,000 money
- `+6` — 60× Flagship Chip · 20× Pandora Power Core
- `+7` — 70× Flagship Chip · 100× Pandora Power Core
- `+8` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Flagship Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Flagship Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Flagship Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 40× Galaxy Heart · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 80× Galaxy Heart · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 160× Galaxy Heart · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 320× Galaxy Heart · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 640× Galaxy Heart · 130× Inert Alloy · 100× Heated Alloy
- `Awaken` — 1280× Galaxy Heart · 1280× Inert Alloy · 1280× Heated Alloy

---

## 402 · Natasha 娜塔莎
**Role** Flagship · **Attack** physical · **Generation** old
**Ratings** Damage 8/10 · Defence 7/10 · Assist 7/10

### Signature skill
- **Ⅰ** at `+0` — Enchantment Kiss (娜塔莎)
  Single attack. After hitting a main target, the attack will create a chain of attacks so to deal damage to enemy targets in proximity of the main target. It will successively deal 350%, 370%, 400%, 430% S-ATK damage to each target. It has a 60% chance to cast a weakening effect on targets which get hit, decreasing all stats on those affected by 50% for 1 round; a 70% chance to increase S-ATK and S-DEF by 50% for the team for 2 rounds; a 60% chance to expose invisible enemies (the rate for each target will be settled independently). At last, increases 100 Accumulator for self.

### Augment cost (per step)
- `+1` — 2× Flagship Chip · 1,000 money
- `+2` — 10× Flagship Chip · 20,000 money
- `+3` — 20× Flagship Chip · 300,000 money
- `+4` — 40× Flagship Chip · 500,000 money
- `+5` — 50× Flagship Chip · 800,000 money
- `+6` — 60× Flagship Chip · 20× Pandora Power Core
- `+7` — 70× Flagship Chip · 100× Pandora Power Core
- `+8` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Flagship Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Flagship Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Flagship Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 40× Galaxy Heart · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 80× Galaxy Heart · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 160× Galaxy Heart · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 320× Galaxy Heart · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 640× Galaxy Heart · 130× Inert Alloy · 100× Heated Alloy
- `Awaken` — 1280× Galaxy Heart · 1280× Inert Alloy · 1280× Heated Alloy

---

## 440 · Sorcerer Supreme 至尊法师
**Role** Flagship · **Attack** physical · **Generation** old
**Ratings** Damage 8/10 · Defence 7/10 · Assist 7/10

### Signature skill
- **Ⅰ** at `+0` — Soul OutⅠ (至尊法师，灵魂出窍)
  Cross attack, deals 350% S-ATK damage to targets which get hit and then deals 50% of the previous total damage (True Damage) to enemies with 60% or above HP (ignores defense). Additionally, links all friendly ships, if a linked friendly ship is destroyed, increases Sorcerer Supreme's ATK damage and S-ATK damage to 300% (the damage bonus can't be stacked), lasting for 2 rounds. It also has a 75% chance to lock targets for 1 round. Each time it releases the skill, it can restore self maximum HP by 10% and becomes immune to Weaken and Accumulator Reduce effects for 1 round. At last, restores 100 Accumulator for self. S-ATK damage Sorcerer Supreme receives is reduced by 50%, check Attributes for details.
- **Ⅱ** at `Awaken` — Soul OutⅡ (至尊法师，灵魂出窍)
  Cross attack, deals 380% S-ATK damage to targets which get hit and then deals 100% of the previous total damage (True Damage) to all enemies (ignores defense). Additionally, links all friendly ships, if a linked friendly ship is destroyed, increases Sorcerer Supreme's ATK damage and S-ATK damage to 500% (the damage bonus can't be stacked), lasting for 2 rounds. It also has a 75% chance to lock targets for 1 round. Each time it releases the skill, it can restore self maximum HP by 40% and becomes immune to Weaken, Lock, Freeze, Confuse and all types of Accumulators plunder and forbidding skill use debuffs from the enemy, for 1 rounds. At last, restores 100 Accumulator for self. S-ATK damage Sorcerer Supreme receives is reduced by 60%, check Attributes for details.At the beginning of the battle, add a control enhancement effect lasting 3 rounds to the self, so that the lock can be forced to take effect regardless of immunity and protection effects.

### Augment cost (per step)
- `+1` — 2× Flagship Chip · 1,000 money
- `+2` — 10× Flagship Chip · 20,000 money
- `+3` — 20× Flagship Chip · 300,000 money
- `+4` — 40× Flagship Chip · 500,000 money
- `+5` — 50× Flagship Chip · 800,000 money
- `+6` — 60× Flagship Chip · 20× Pandora Power Core
- `+7` — 70× Flagship Chip · 100× Pandora Power Core
- `+8` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Flagship Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Flagship Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Flagship Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 40× Galaxy Heart · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 80× Galaxy Heart · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 160× Galaxy Heart · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 320× Galaxy Heart · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 640× Galaxy Heart · 130× Inert Alloy · 100× Heated Alloy
- `Awaken` — 1280× Galaxy Heart · 1280× Inert Alloy · 1280× Heated Alloy

---

## 451 · Valerian 瓦利安
**Role** Flagship · **Attack** physical · **Generation** old
**Ratings** Damage 10/10 · Defence 6/10 · Assist 8/10

### Signature skill
- **Ⅰ** at `+0` — Royal Supremacy (瓦利安，无上王权)
  Vertical attack. Deals 350% S-ATK damage, has a 80% chance of destroying the enemy Flagship directly, then deducts 30 Accumulator from hit target and recovers 25 Accumulator for all friendly units (except self); increases 1 million ATK and 1 million S-ATK (stackable, lasting until the end of the battle); also activates Eye of True Sight for all friendly units (including self), for 1 round; then recovers 100 Accumulator for self. If Valerian's vertical attack kills an enemy, then there's 100% chance he will initiate another round of skill attack, triggering all skill effects once more.
- **Ⅱ** at `Awaken` — Royal SupremacyⅡ (瓦利安，无上王权)
  Vertical attack. Deals 400% S-ATK damage, has a 80% chance of directly destroying the enemy ship of a certain class in the order of Flagship, Ranger, Striker, Destroyer, Rover, and Protector (If heroes of a certain class are dead or missing, next class will be chosen in the order of priority), then deducts 50 Accumulator from hit target and recovers 50 Accumulator for all friendly units (except self); increases 1.5 million ATK and 1.5 million S-ATK (stackable, lasting until the end of the battle); also activates Eye of True Sight for all friendly units (including self), for 1 round; then recovers 100 Accumulator for self. If Valerian's vertical attack kills an enemy, then there's 100% chance he will initiate another round of skill attack, triggering all skill effects once more.
- **Ⅲ** at `Second Awaken` — Royal SupremacyⅢ (瓦利安，无上王权)
  Vertical attack. Deals 420% S-ATK damage, has a 100% chance of directly destroying the enemy ship of a certain class in the order of Flagship, Ranger, Striker, Destroyer, Rover, and Protector (If heroes of a certain class are dead or missing, next class will be chosen in the order of priority), then deducts 100 Accumulator from hit target and recovers 100 Accumulator for all friendly units (except self); increases 3 million ATK and 3 million S-ATK (stackable, lasting until the end of the battle); also activates Eye of True Sight for all friendly units (including self), for 1 round; then recovers 100 Accumulator for self. If Valerian's vertical attack kills an enemy, then there's 100% chance he will initiate another round of skill attack, triggering all skill effects once more.

### Augment cost (per step)
- `+1` — 2× Flagship Chip · 1,000 money
- `+2` — 10× Flagship Chip · 20,000 money
- `+3` — 20× Flagship Chip · 300,000 money
- `+4` — 40× Flagship Chip · 500,000 money
- `+5` — 50× Flagship Chip · 800,000 money
- `+6` — 60× Flagship Chip · 20× Pandora Power Core
- `+7` — 70× Flagship Chip · 100× Pandora Power Core
- `+8` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Flagship Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Flagship Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Flagship Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 40× Galaxy Heart · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 80× Galaxy Heart · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 160× Galaxy Heart · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 320× Galaxy Heart · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 640× Galaxy Heart · 130× Inert Alloy · 100× Heated Alloy
- `Awaken` — 1280× Galaxy Heart · 1280× Inert Alloy · 1280× Heated Alloy

---

## 469 · Jayce Lot 杰斯·洛特
**Role** Flagship · **Attack** physical · **Generation** old
**Ratings** Damage 10/10 · Defence 10/10 · Assist 8/10

### Signature skill
- **Ⅰ** at `+0` — Precision StrikeⅠ (精准重击)
  Single attack; attacks 5 times consecutively, each attack deals 300% S-ATK damage and plunders 5% HP from all enemies. After the attacks are finished, there is a 70% chance (the rate for each target will be settled independently) to turn all friendly ships invisible for 1 round, and a 70% chance (the rate for each target will be settled independently) to dispel stat debuffs (including weakening) from all friendly ships. Also applies a Rebirth effect on itself (effective for 1 round; the lieutenant's revival effect will be used prior to the bound ship's) that allows it to revive immediately upon death. There is also a 50% chance to make 2 random ally heroes immune to damage and debuffs dealt by the enemy flagship (Not immune to subsequent damage), for 1 round. Finally, recovers 100 Accumulator for self.
- **Ⅱ** at `Awaken` — Precision StrikeⅡ (杰斯·洛特（1觉），精准重击)
  Single attack; attacks 5 times consecutively, each attack deals 400% S-ATK damage, 10M True Damage, and plunders 10% HP from all enemies. After the attacks are finished, there is a 75% chance (the rate for each target will be settled independently) to turn all friendly ships invisible for 1 round, and a 75% chance (the rate for each target will be settled independently) to dispel stat debuffs (including weakening) and some crowd controls (Freeze, Lock, Confuse, Forbidding Skill Use) from all friendly ships. Also applies a Rebirth effect on itself and 2 random allies (effective for 1 round; the lieutenant's revival effect will be used prior to the bound ship's) that allows it to revive immediately upon death to 100% of initial HP and 100 Accumulator. There is also a 60% chance to make 2 random ally heroes immune to damage and debuffs dealt by the enemy flagship (Not immune to subsequent damage), for 1 round. Finally, recovers 100 Accumulator for self. Self also gains a 2-round Rebirth at the start of battle, recovering immediately upon death with 100% of initial HP and 100 Accumulator.
- **Ⅲ** at `Second Awaken` — Precision StrikeⅢ (杰斯·洛特（2觉），精准重击)
  Single attack; attacks 5 times consecutively, each attack deals 500% S-ATK damage, 13M True Damage, and plunders 20% HP from all enemies. After the attacks are finished, there is an 80% chance (the rate for each target will be settled independently) to turn all friendly ships except for self invisible for 1 round, and a 100% chance for self to become invisible for 1 round and will not lose invisibility for as long as there is another allied unit alive (can be seen by Eye of True Sight). Also has an 80% chance (the rate for each target will be settled independently) to dispel stat debuffs (including weakening) and some crowd controls (Freeze, Lock, Confuse, Forbidding Skill Use, Petrify, Icebound, Entangle) from all friendly ships and dispel 3 random buffs from all enemies. Also applies a Rebirth effect on itself and 2 random allies (effective for 1 round; the lieutenant's revival effect will be used prior to the bound ship's) that allows it to revive immediately upon death to 100% of initial HP and 150 Accumulator. There is also a 70% chance to make 2 random ally heroes immune to damage and debuffs dealt by the enemy flagship (Not immune to subsequent damage), for 1 round. Finally, recovers 150 Accumulator for self. Self also gains a 2-round Rebirth at the start of battle, recovering immediately upon death with 100% of initial HP and 100 Accumulator.

### Augment cost (per step)
- `+1` — 5× Flagship Chip · 100,000 money
- `+2` — 10× Flagship Chip · 200,000 money
- `+3` — 21× Flagship Chip · 300,000 money
- `+4` — 28× Flagship Chip · 500,000 money
- `+5` — 35× Flagship Chip · 800,000 money
- `+6` — 42× Flagship Chip · 10× Pandora Power Core
- `+7` — 49× Flagship Chip · 50× Pandora Power Core
- `+8` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Flagship Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Flagship Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Flagship Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 40× Galaxy Heart · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 80× Galaxy Heart · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 160× Galaxy Heart · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 320× Galaxy Heart · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 640× Galaxy Heart · 130× Inert Alloy · 100× Heated Alloy
- `Awaken` — 1280× Galaxy Heart · 1280× Inert Alloy · 1280× Heated Alloy

---

## 477 · Erlang Shen 杨戬
**Role** Flagship · **Attack** physical · **Generation** old
**Ratings** Damage 10/10 · Defence 6/10 · Assist 8/10

### Signature skill
- **Ⅰ** at `+0` — The Hundred Changing Stars-Flagship (百变星君-旗舰)
  Using matter conversion technology, Erlang Shen can change the form of his ship at will during battles. The ship has the combat attributes of all classes and will convert to one of the following at random after casting a skill: Ranger, Striker, Protector, Destroyer, Rover. Each class corresponds to a different skill. Erlang Shen always enters battle as a flagship. Flagship Skill: Single attack; after hitting the main target, forms a chain of attacks on enemy units adjacent to the main target, dealing 180%, 240%, 300%, 360% S-ATK damage in turn. Increases own S-ATK by 800,000 (stackable, lasting until the end of the battle). It has a 50% chance to Weaken targets, reducing attributes by 50% for 1 round. At the same time, activates Eye of True Sight for all friendly ships until the end of the battle, and activates a shield with 30 million HP for itself for 3 rounds. Becomes immune to Forbidding Skill Use for 3 rounds, and immune to damage and debuffs dealt by the enemy Flagship (excluding Weaken and subsequent damages) for 1 round. Finally, recovers 100 Accumulator for self. Ranger Skill: Vertical attack; deals 400% S-ATK damage and deducts 40% of targets' current HP. Increases own S-ATK by 800,000 (stackable, lasting until the end of the battle). It has a 70% chance to Freeze targets for 2 rounds. Makes self immune to Lock and Accumulator Reduce effects for 3 rounds and becomes immune to damage and debuffs dealt by enemy Rangers (excluding Weaken and subsequent damages) for 1 round. Finally, recovers 100 Accumulator for self. Striker Skill: Cross attack; deals 350% S-ATK damage, then deals True Damage equal to 200% of the total previous S-ATK damage dealt to the enemy ship with the lowest HP. Increases own S-ATK by 800,000 (stackable, lasting until the end of the battle). Increases all friendly ships' ATK and S-ATK by 50% for 2 rounds. It also has a 70% chance to Lock targets for 2 rounds. It becomes immune to Freeze for 3 rounds, and immune to damage and debuffs dealt by enemy Strikers (excluding Weaken and subsequent damages) for 1 round. Finally, recovers 100 Accumulator for self. Protector Skill: All attack; deals 180% S-ATK damage to targets, and increases own S-ATK by 800,000 (stackable, lasting until the end of the battle). Releases a shield that can absorb 150 million damage for all friendly ships for 2 rounds (only the latest shield generated by the same skill can exist, and the effects cannot be stacked). Then, reduces targets' ATK and S-ATK by 50% for 2 rounds. It will trigger a Deflection Force Field for itself, the field resists 280% damage dealt by enemy vertical and cross attacks for self and the teammate behind it, lasts 3 rounds (the damage resisted is only related to the ATK, S-ATK, and Accumulator when Erlang Shen casts a skill). It becomes immune to damage and debuffs dealt by enemy Protectors (excluding Weaken and subsequent damages) for 1 round. Finally, recovers 100 Accumulator for self. Destroyer Skill: Single attack; attacks 4 times consecutively, plundering 30% Accumulator from all enemies, each attack dealing 200% S-ATK damage and an additional 2 million True Damage. Increases own S-ATK by 800,000 (stackable, lasting until the end of the battle). It also has a 40% chance to confuse all enemy units (probability for each unit calculated separately) for 2 rounds. Increases all friendly ships' Crit and Hit by 80% for 2 rounds, and has a 50% chance to make all friendly units Invisible for 1 round (probability calculated separately for each unit). It becomes immune to Weaken for 3 rounds, and immune to damage and debuffs dealt by enemy Destroyers (excluding Weaken and subsequent damages) for 1 round. Finally, recovers 100 Accumulator for self. Rover Skill: Vertical attack; deals 200% S-ATK damage and revives all defeated friendly ships, restoring 100% of their initial HP and 100% Accumulator. Increases own S-ATK by 800,000 (stackable, lasting until the end of the battle). It becomes immune to 1 lethal attacks for 3 rounds(including instant destruction). Restores 50% of max HP for all friendly units. It becomes immune to Weaken for 3 rounds, and immune to damage and debuffs dealt by enemy Rovers (excluding Weaken and subsequent damages) for 1 round. Finally, recovers 100 Accumulator for self.

### Augment cost (per step)
- `+1` — 5× Flagship Chip · 100,000 money
- `+2` — 10× Flagship Chip · 200,000 money
- `+3` — 21× Flagship Chip · 300,000 money
- `+4` — 28× Flagship Chip · 500,000 money
- `+5` — 35× Flagship Chip · 800,000 money
- `+6` — 42× Flagship Chip · 10× Pandora Power Core
- `+7` — 49× Flagship Chip · 50× Pandora Power Core
- `+8` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Flagship Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Flagship Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Flagship Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 40× Galaxy Heart · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 80× Galaxy Heart · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 160× Galaxy Heart · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 320× Galaxy Heart · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 640× Galaxy Heart · 130× Inert Alloy · 100× Heated Alloy
- `Awaken` — 1280× Galaxy Heart · 1280× Inert Alloy · 1280× Heated Alloy

---

## 491 · Freya 芙蕾雅
**Role** Flagship · **Attack** physical · **Generation** old
**Ratings** Damage 10/10 · Defence 10/10 · Assist 8/10

### Signature skill
- **Ⅰ** at `+0` — Seed of Life (芙蕾雅)
  When the battle begins, plant 5 Seeds of Life for each ally except for yourself. Units with a Seed of Life will lose 1 seed whenever they are targeted by a Normal Attack and 2 seeds whenever they are targeted by an S-ATK. Each Seed of Life grants 8% S-ATK damage reduction, 20% S-DEF and 20% DEF (stacks). Cross Attack, deals 300% S-ATK damage to the targets and reduces your damage received by 70% for 2 rounds. Consumes the Seeds of Life on allied units to grant one of the following buff - or an ability - based on the number of seeds consumed (one unit may only be granted one type of ability): 5 Seeds: Rebirth (Lieutenant rebirth effects are prioritized). Revive immediately upon death with 100% of initial HP and Accumulator. Lasts 1 round. 4 Seeds: 75% chance to gain immunity to debuffs: Lock, Confuse, Freeze, Curse, Petrify, Forbidding Skill Use (chance is calculated independently for each one) for 1 round. 3 Seeds: Grants Entangle (ability) for 1 round: attacks have a 50% chance to entangle targets, rendering them unable to act for 1 round. 2 Seeds: Grants 80% S-ATK, 80% ATK, 50% Critical (absolute value) and Eye of True Sight for 2 rounds. 1 Seed: Grants Bounce Damage (ability) for 1 round: attack the enemy ship with the least HP True Damage equal to 180% of your Normal Attack damage. After which you once again plant 5 Seeds of Life for each ally except for yourself. Finally, you recover 100 Accumulator.
- **Ⅱ** at `Awaken` — Seed of LifeⅡ (芙蕾雅，生命之种II)
  At the start of battle, plant 5 Seeds of Life onto all allied units. Units with a Seed of Life will lose 1 seed whenever they are targeted by an S-ATK. Each Seed of Life grants 12% S-ATK damage reduction, 25% S-DEF and 25% DEF (stacks). Cross Attack, deals 340% S-ATK damage to the targets and reduces your damage received by 70% for 2 rounds; has a 100% chance to make invisible enemies appear. When Freya casts skill, all allies deal 10% more damage for 1 round for every seed they lose. Consumes the Seeds of Life on allied units to grant one of the following buff - or an ability - based on the number of seeds consumed (one unit may only be granted one type of ability): 5 Seeds: Rebirth (Lieutenant rebirth effects are prioritized). Revive immediately upon death with 100% of initial HP and 150 Accumulator. Lasts 1 round. 4 Seeds: 100% chance to gain immunity to debuffs: Lock, Confuse, Freeze, Curse, Petrify, Weaken, Instant Destruction, Forbidding Skill Use (chance is calculated independently for each one) for 1 round. 3 Seeds: Grants Entangle (ability) for 1 round: attacks have a 75% chance to entangle targets, rendering them unable to act for 1 round. 2 Seeds: Grants 100% S-ATK, 80% ATK, 80% Critical (absolute value) and Eye of True Sight for 2 rounds. 1 Seed: Grants Bounce Damage (ability) for 1 round: attack the enemy ship with the least HP True Damage equal to 260% of your Normal Attack damage. After which you once again sow 5 Seeds of Life onto all allied units. Finally, you recover 100 Accumulator.
- **Ⅲ** at `Second Awaken` — Seed of LifeⅢ (芙蕾雅，生命之种III)
  At the start of battle, plant 5 Seeds of Life onto all allied units. Units with a Seed of Life will lose 1 seed whenever they are targeted by an S-ATK. Each Seed of Life grants 15% S-ATK damage reduction, 25% S-DEF and 25% DEF (stacks). Cross Attack, deals 380% S-ATK damage to the targets and reduces your damage received by 70% for 2 rounds; has a 100% chance to make invisible enemies appear. When Freya casts skill, all allies deal 10% more damage for 1 round for every seed they lose. Consumes the Seeds of Life on allied units to grant one of the following buff - or an ability - based on the number of seeds consumed (one unit may only be granted one type of ability): 5 Seeds: Rebirth (Lieutenant rebirth effects are prioritized). Revive immediately upon death with 100% of initial HP and 150 Accumulator. Lasts 1 round. 4 Seeds: 100% chance to gain immunity to debuffs: Lock, Confuse, Freeze, Curse, Petrify, Weaken, Instant Destruction, Forbidding Skill Use (chance is calculated independently for each one) for 1 round. 3 Seeds: Grants Entangle (ability) for 1 round: attacks have a 100% chance to entangle targets, rendering them unable to act for 1 round. 2 Seeds: Grants 140% S-ATK, 140% ATK, 120% Critical (absolute value) and Eye of True Sight for 2 rounds. 1 Seed: Grants Bounce Damage (ability) for 1 round: attack the enemy ship with the least HP True Damage equal to 300% of your Normal Attack damage. After which you once again sow 5 Seeds of Life onto all allied units. Finally, you recover 100 Accumulator. The applied entangle effect is empowered, ignoring all immunity and protection effects.

### Augment cost (per step)
- `+1` — 5× Flagship Chip · 100,000 money
- `+2` — 10× Flagship Chip · 200,000 money
- `+3` — 21× Flagship Chip · 300,000 money
- `+4` — 28× Flagship Chip · 500,000 money
- `+5` — 35× Flagship Chip · 800,000 money
- `+6` — 42× Flagship Chip · 10× Pandora Power Core
- `+7` — 49× Flagship Chip · 50× Pandora Power Core
- `+8` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Flagship Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Flagship Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Flagship Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 40× Galaxy Heart · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 80× Galaxy Heart · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 160× Galaxy Heart · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 320× Galaxy Heart · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 640× Galaxy Heart · 130× Inert Alloy · 100× Heated Alloy
- `Awaken` — 1280× Galaxy Heart · 1280× Inert Alloy · 1280× Heated Alloy

---

## 498 · Patton 巴顿
**Role** Flagship · **Attack** physical · **Generation** old
**Ratings** Damage 10/10 · Defence 10/10 · Assist 8/10

### Signature skill
- **Ⅰ** at `+0` — Energy Ward (源能护佑)
  Cross attack; deals 280% S-ATK damage. Whenever a unit dies within the next 2 rounds, all allies have their damage dealt increased by 60% (does not stack) for 1 round. For the next 2 rounds, whenever an ally is attacked, they recover 40% of max HP. There is a 70% chance to apply a Ward to 3 random allied units (probability for each target calculated separately) for 1 round. The enemy's skills will not affect units with Ward (except for skill damage and subsequent damage). A Ward disappears after being attacked 2 times (skills that cause multiple attacks will deduct 1 block chance per attack). Also reduces the damage all allies take by 75% for 2 rounds. Finally, recovers 100 Accumulator for self. Note: comes with a 40% skill damage reduction.
- **Ⅱ** at `Awaken` — Energy WardⅡ (巴顿觉醒1，庇护)
  Cross attack, deals 320% S-ATK damage. Whenever a ally dies within the next 2 rounds, all allies have their damage dealt increased by 80% (does not stack) for 1 round.Whenever all allies are attacked, they recover 40% of max HP, and the damage received in a single attack does not exceed 90% of their max HP, lasting for 2 rounds. There is a 100% chance to apply a Ward to 3 random allies for 1 round. The enemy's skills will not affect units with Ward (except for S-ATK damage and subsequent damage). A Ward disappears after being attacked 2 times (skills that cause multiple attacks will deduct 1 block chance per attack). Also reduces the damage all allies take by 80% for 2 rounds. Finally, recovers 100 Accumulator for self. Note: comes with a 40% skill damage reduction.
- **Ⅲ** at `Second Awaken` — Energy WardⅢ (巴顿觉醒2，庇护)
  Cross attack, deals 360% S-ATK damage. Whenever a ally dies within the next 2 rounds, all allies have their damage dealt increased by 120% (does not stack) for 1 round.Whenever all allies are attacked, they recover 40% of max HP, and the damage received in a single attack does not exceed 80% of their max HP, and there is a 50% chance to purifies abnormal status and clears the control effect, lasting for 2 rounds.There is a 100% chance to apply a Ward to all allies for 1 round. The enemy's skills will not affect units with Ward (except for S-ATK damage and subsequent damage). A Ward disappears after being attacked 2 times (skills that cause multiple attacks will deduct 1 block chance per attack). Also reduces the damage all allies take by 90% for 2 rounds. Finally, recovers 100 Accumulator for self. Note: comes with a 40% skill damage reduction.

### Augment cost (per step)
- `+1` — 5× Flagship Chip · 100,000 money
- `+2` — 10× Flagship Chip · 200,000 money
- `+3` — 21× Flagship Chip · 300,000 money
- `+4` — 28× Flagship Chip · 500,000 money
- `+5` — 35× Flagship Chip · 800,000 money
- `+6` — 42× Flagship Chip · 10× Pandora Power Core
- `+7` — 49× Flagship Chip · 50× Pandora Power Core
- `+8` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Flagship Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Flagship Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Flagship Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 40× Galaxy Heart · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 80× Galaxy Heart · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 160× Galaxy Heart · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 320× Galaxy Heart · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 640× Galaxy Heart · 130× Inert Alloy · 100× Heated Alloy
- `Awaken` — 1280× Galaxy Heart · 1280× Inert Alloy · 1280× Heated Alloy

---

## 503 · Chronos 柯罗诺斯
**Role** Flagship · **Attack** physical · **Generation** old
**Ratings** Damage 10/10 · Defence 6/10 · Assist 8/10

### Signature skill
- **Ⅰ** at `+0` — Time Warp (柯罗诺斯，时空穿梭)
  Cross Attack, deals 340% S-ATK damage to targets. Applies a Time Ward to all allies for 2 rounds. Time Ward has a 75% chance to prevent some enemy skill effects (Freeze, Lock, Confuse, and Forbidding Skill Use) from triggering (doesn't affect guaranteed skill effects) and has a 40% chance to dodge enemy S-ATK damage (unaffected by Hit Rate and attacks that are guaranteed to hit). The Time Ward breaks (having another Time Ward applies resets the damage counter) when a unit has taken damage equal to 40% of its max HP, whereupon it loses the ability to prevent enemy effects and dodge attacks, and then it Locks 1 random enemy for 1 round. Applies a Time Reversal lasting 2 rounds to all allied units, granting them a 100% chance to reverse time 1 time when taking lethal damage (including Instant Destruction), returning their HP and Accumulator to their status at the start of the battle (each unit has a 2-round cooldown for this effect to occur, during which they cannot gain or trigger Time Reversal) and clears all control effects and debuffs. Self gains 2 rounds of invisibility and will not lose invisibility for as long as there is another allied unit alive (can be seen by Eye of True Sight). Lastly, you recover 100 Accumulator.
- **Ⅱ** at `Awaken` — Time WarpⅡ (柯罗诺斯，时空穿梭)
  Cross Attack, deals 380% S-ATK damage to targets. Applies a Time Ward to all allies for 2 rounds. Time Ward has a 100% chance to prevent some enemy skill effects (Freeze, Lock, Confuse, and Forbidding Skill Use) from triggering (doesn't affect guaranteed skill effects) and has a 50% chance to dodge enemy S-ATK damage (unaffected by Hit Rate and attacks that are guaranteed to hit). The Time Ward breaks (having another Time Ward applies resets the damage counter) when a unit has taken damage equal to 60% of its max HP, whereupon it loses the ability to prevent enemy effects and dodge attacks, and then it Locks 1 random enemy for 1 round. Applies a Time Reversal lasting 2 rounds to all allied units, granting them a 100% chance to reverse time 1 time when taking lethal damage (including Instant Destruction), returning their HP and Accumulator to their status at the start of the battle (each unit has a 1-round cooldown for this effect to occur, during which they cannot gain or trigger Time Reversal) and clears all control effects and debuffs. Self gains 2 rounds of invisibility and will not lose invisibility for as long as there is another allied unit alive (can be seen by Eye of True Sight). Lastly, you recover 100 Accumulator. Apply Time Ward and Time Reversal for 1 round to all allies at the start of battle.
- **Ⅲ** at `Second Awaken` — Time WarpⅢ (柯罗诺斯觉醒+2，时空穿梭III)
  Cross Attack, deals 400% S-ATK damage to targets. Applies a Time Ward to all allies for 2 rounds. Time Ward has a 100% chance to prevent some enemy skill effects (Freeze, Lock, Confuse, Forbidding Skill Use, Petrify, Icebound, Entangle and Weaken) from triggering (doesn't affect guaranteed skill effects) and has a 60% chance to dodge enemy S-ATK damage (unaffected by Hit Rate and attacks that are guaranteed to hit). The Time Ward breaks (having another Time Ward applies resets the damage counter) when a unit has taken damage equal to 60% of its max HP, whereupon it loses the ability to prevent enemy effects and dodge attacks, and then it Locks 1 random enemy for 1 round (ignores immunity and protection effects). Applies a Time Reversal lasting 2 rounds to all allied units, granting them a 100% chance to reverse time 1 time when taking lethal damage (including Instant Destruction), returning their HP and Accumulator to their status at the start of the battle (each unit has a 1-round cooldown for this effect to occur, during which they cannot gain or trigger Time Reversal) and clears all control effects and debuffs. Triggering Time Reversal also Locks 1 random enemy for 1 round (ignores immunity and protection effects). Self gains 2 rounds of invisibility and will not lose invisibility for as long as there is another allied unit alive (can be seen by Eye of True Sight). The 1st and 4th times Chronos uses this skill (the skill counter resets when revived), he applies Rebirth (unaffected by forbidding revival and forbidden rebirth effects) lasting 4 rounds to all allies, enabling them to revive with 100% of their initial HP and 100 Accumulator when destroyed. Lastly, you recover 100 Accumulator. Apply Time Ward and Time Reversal for 1 round to all allies at the start of battle.

### Augment cost (per step)
- `+1` — 5× Flagship Chip · 100,000 money
- `+2` — 10× Flagship Chip · 200,000 money
- `+3` — 21× Flagship Chip · 300,000 money
- `+4` — 28× Flagship Chip · 500,000 money
- `+5` — 35× Flagship Chip · 800,000 money
- `+6` — 42× Flagship Chip · 10× Pandora Power Core
- `+7` — 49× Flagship Chip · 50× Pandora Power Core
- `+8` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Flagship Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Flagship Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Flagship Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 40× Galaxy Heart · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 80× Galaxy Heart · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 160× Galaxy Heart · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 320× Galaxy Heart · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 640× Galaxy Heart · 130× Inert Alloy · 100× Heated Alloy
- `Awaken` — 1280× Galaxy Heart · 1280× Inert Alloy · 1280× Heated Alloy

---

## 514 · Galaxy Inquisitor No. 9 银河审判者9号
**Role** Flagship · **Attack** physical · **Generation** old
**Ratings** Damage 10/10 · Defence 6/10 · Assist 8/10

### Signature skill
- **Ⅰ** at `+0` — Sword of JudgmentⅠ (银河审判者9号，审判之剑I)
  All attack; deals 320% S-ATK damage to targets, and has a 50% chance to apply Expose Weakness (probability for each target calculated separately). If the target already has Expose Weakness, add another stack. Stacks up to 3 times and lasts until the end of the battle. Each stack of Expose Weakness reduces DEF and S-DEF by 20% (Percentage), Anti Crit by 50% and Crit ATK RED by 30% (Absolute Value). 1 stack: Cannot block S-ATK. 2 stacks: Incoming S-ATKs always hit (unique effect: unaffected by Dodge and Evasive). 3 stacks: Galaxy Inquisitor No. 9's S-ATKs have a 50% chance to instantly destroy units with 3 stacks of Expose Weakness. All enemies require "Expose Weakness stacks x 10%" extra Accumulator to use skills. Allied heroes below 100 Accumulator recover to 100 Accumulator. Lastly, you recover 100 Accumulator.
- **Ⅱ** at `Awaken` — Sword of JudgmentⅡ (银河审判者9号，审判之剑II)
  All attack; deals 340% S-ATK damage to targets, and has a 60% chance to apply Expose Weakness (probability for each target calculated separately). If the target already has Expose Weakness, add another stack. Enemies with Expose Weakness gain another stack upon acting. Stacks up to 3 times and lasts until the end of the battle. Each stack of Expose Weakness reduces DEF and S-DEF by 25% (Percentage), Anti Crit by 60% and Crit ATK RED by 50% (Absolute Value). 1 stack: Cannot block S-ATK. 2 stacks: Incoming S-ATKs always hit (unique effect: unaffected by Dodge and Evasive). 3 stacks: Galaxy Inquisitor No. 9's S-ATKs have a 60% chance to instantly destroy units with 3 stacks of Expose Weakness. All enemies require "Expose Weakness stacks x 15%" extra Accumulator to use skills. Allied heroes below 100 Accumulator recover to 120 Accumulator. Self gains 2 rounds of invisibility. Lastly, you recover 100 Accumulator. Self gains 2 rounds of invisibility at the start of battle.
- **Ⅲ** at `Second Awaken` — Sword of JudgmentⅢ (银河审判者9号，审判之剑III)
  All attack; deals 380% S-ATK damage to targets, and has an 80% chance to apply Expose Weakness (probability for each target calculated separately). If the target already has Expose Weakness, add another stack. Enemies with Expose Weakness gain another stack upon acting. Enemies that revive gain 1 stack of Expose Weakness. Stacks up to 3 times and lasts until the end of the battle. Each stack of Expose Weakness reduces DEF and S-DEF by 30% (Percentage), Anti Crit by 80% and Crit ATK RED by 80% (Absolute Value). 1 stack: Cannot block S-ATK. 2 stacks: Incoming S-ATKs always hit (unique effect: unaffected by Dodge and Evasive). 3 stacks: Galaxy Inquisitor No. 9's S-ATKs have a 90% chance to instantly destroy units with 3 stacks of Expose Weakness (ignores shields that grant immunity to instant destruction and lethal damage). All enemies require "Expose Weakness stacks x 25%" extra Accumulator to use skills. Allied heroes below 100 Accumulator recover to 150 Accumulator. Self gains 2 rounds of invisibility and will not lose invisibility for as long as there is another allied unit alive (can be seen by Eye of True Sight). Lastly, you recover 100 Accumulator. Self gains 2 rounds of invisibility at the start of battle and will not lose invisibility for as long as there is another allied unit alive (can be seen by Eye of True Sight).

### Augment cost (per step)
- `+1` — 5× Flagship Chip · 100,000 money
- `+2` — 10× Flagship Chip · 200,000 money
- `+3` — 21× Flagship Chip · 300,000 money
- `+4` — 28× Flagship Chip · 500,000 money
- `+5` — 35× Flagship Chip · 800,000 money
- `+6` — 42× Flagship Chip · 10× Pandora Power Core
- `+7` — 49× Flagship Chip · 50× Pandora Power Core
- `+8` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Flagship Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Flagship Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Flagship Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 40× Galaxy Heart · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 80× Galaxy Heart · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 160× Galaxy Heart · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 320× Galaxy Heart · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 640× Galaxy Heart · 130× Inert Alloy · 100× Heated Alloy
- `Awaken` — 1280× Galaxy Heart · 1280× Inert Alloy · 1280× Heated Alloy

---

## 529 · Janus 亚努斯
**Role** Flagship · **Attack** physical · **Generation** old
**Ratings** Damage 10/10 · Defence 6/10 · Assist 8/10

### Signature skill
- **Ⅰ** at `+0` — Duality Soul-[Protective] (双生之魂，坚毅)
  Janus has two personalities and switches between his [Aggressive] and [Protective] personalities each time he acts, each having its own skill (You can in the Formation menu choose whether to start the battle in his [Aggressive] or [Protective] personality). [Aggressive]: Deals 320% S-ATK damage and follows up with 3 further attacks, each dealing 300% S-ATK damage and 3M True Damage to a random enemy unit. Attacks 1 extra time for each extra 60 Accumulator spent during the skill cast, up to 7. If Janus has more than 200 Accumulator when casting the skill, the attack cannot be blocked, and if more than 400 Accumulator, the attack is guaranteed to crit. Janus' skill attacks ignore 35% of the enemy's DEF and S-DEF. The skill's damage increases by 0.3% for each Accumulator above 100 spent during skill cast. Using the skill changes his personality to [Protective]. Lastly, he recovers 100 Accumulator. [Protective]: Recover 50% of max HP when switching to [Protective] personality and gain a shield equal to 180% of max HP (does not stack) lasting 1 round. He also gains 60% damage reduction, and allies gain 35%, for 1 round. He gains 100% DEF and S-DEF for 1 round. His block is increased by 100% (absolute value) for 1 round. Janus also gains Accumulator equal to 55% of the Accumulator cost of any skill not cast by himself for 1 round. He can gain up to 600 Accumulator per round this way. Janus is also cleared of all control effects on his next round before acting. [Protective] Active Skill: Does not attack but restores the max HP of all allies by 50% and has a 100% chance to reveal all invisible enemies. Janus himself gains Rebirth for 2 rounds, and is healed to 100% of his initial HP and Accumulator on rebirth. Then he gains invisibility for 1 round and a shield that withstands 1 instance of lethal damage (including instant death) for 1 round. He then switches to his [Aggressive] personality. Skills cast while in his [Protective] personality do not cost Accumulator (but he needs to have at least 100 Accumulator to cast). Janus gains an extra 300 Accumulator at the start of battle. If he starts the battle in [Aggressive] personality, he gains invisibility for 1 round and a shield that withstands 1 instance of lethal damage (including instant death) for 1 round. If he starts the battle in [Protective] personality, he gains a shield equal to 180% of his max HP (does not stack) lasting 1 round. He also gains 60% damage reduction, and allies gain 35%, for 1 round. He gains 100% DEF and S-DEF for 1 round. His block is increased by 100% (absolute value) for 1 round. Janus also gains Accumulator equal to 55% of the Accumulator cost of any skill not cast by himself for 1 round. He can gain up to 600 Accumulator per round this way. Janus is also cleared of all control effects on his next round before acting. Note: When Janus is revived or rebirths, he returns to battle in the personality chosen from the Formation menu.
- **Ⅱ** at `Awaken` — Duality Soul-[Protective]Ⅱ (双生之魂，觉醒+1，坚毅)
  Janus has two personalities and switches between his [Offensive] and [Protective] personalities each time he acts, each having its own skill (You can in the Formation menu choose whether to start the battle in his [Offensive] or [Protective] personality). [Offensive]: Deals 340% S-ATK damage and follows up with 3 further attacks, each dealing 320% S-ATK damage and 4M True Damage to a random enemy unit. Attacks 1 extra time for each extra 50 Accumulator spent during the skill cast, up to 9. If Janus has more than 200 Accumulator when casting the skill, the attack cannot be blocked, and if more than 400 Accumulator, the attack is guaranteed to crit. Janus' skill attacks ignore 40% of the enemy's DEF and S-DEF. The skill's damage increases by 0.5% for each Accumulator above 100 spent during the skill cast. Using the skill changes his personality to [Protective]. Lastly, he recovers 100 Accumulator. [Protective]: Recover 55% of max HP when switching to [Protective] personality and gain a shield equal to 200% of max HP (does not stack) lasting 1 round. He also gains 65% damage reduction, and allies gain 40%, for 1 round. He gains 100% DEF and S-DEF for 1 round. His block is increased by 100% (absolute value) for 1 round. Janus also gains Accumulator equal to 60% of the Accumulator cost of any skill not cast by himself for 1 round. He can gain up to 600 Accumulator per round this way. Janus is also cleared of all control effects on his next round before acting. [Protective] Active Skill: Does not attack but restores the max HP of all allies by 55% and has a 100% chance to reveal all invisible enemies. Janus himself gains Rebirth for 2 rounds, and is healed to 100% of his initial HP and Accumulator on rebirth, and has a 50% chance to revive dead allies (probability calculated individually for each unit), restoring them to 100% of their initial HP and Accumulator. Janus gains immunity to Accumulator Reduction for 2 rounds and invisibility for 1 round. Janus also gains [Dark Invisibility] (cannot be attacked or targeted by skills) for 1 round after casting a skill while at 600 or more Accumulator. Janus also gains a shield that withstands 1 instance of lethal damage (including instant death) for 1 round. He then switches to his [Offensive] personality. Skills cast while in his [Protective] personality do not cost Accumulator (but he needs to have at least 100 Accumulator to cast). Janus gains an extra 300 Accumulator at the start of battle. If he starts the battle in [Offensive] personality, he gains invisibility for 1 round and a shield that withstands 1 instance of lethal damage (including instant death) for 1 round. Janus follows up with 7 extra attacks the first time he casts the skill. If he starts the battle in [Protective] personality, he gains a shield equal to 200% of his max HP (does not stack) lasting 1 round. He also gains 65% damage reduction, and allies gain 40%, for 1 round. He gains 100% DEF and S-DEF for 1 round. His block is increased by 100% (absolute value) for 1 round. Janus also gains Accumulator equal to 60% of the Accumulator cost of any skill not cast by himself for 1 round. He can gain up to 600 Accumulator per round this way. Janus gains immunity to Accumulator Reduction for 2 rounds, and is also cleared of all control effects on his next round before acting. Note: When Janus is revived or rebirths, he returns to battle in the personality chosen from the Formation menu.
- **Ⅲ** at `Second Awaken` — Duality Soul-[Protective]Ⅲ (双生之魂，觉醒+2，坚毅)
  Janus has two personalities and switches between his [Offensive] and [Protective] personalities each time he acts, each having its own skill (You can in the Formation menu choose whether to start the battle in his [Offensive] or [Protective] personality). [Offensive]: Deals 360% S-ATK damage and follows up with 3 further attacks, each dealing 340% S-ATK damage and 6M True Damage to a random enemy unit. Attacks 1 extra time for each extra 40 Accumulator spent during the skill cast, up to 10. Each follow-up attack deals extra True Damage equal to 15% of the target's current HP. If Janus has more than 100 Accumulator when casting the skill, the attack cannot be blocked, and if more than 300 Accumulator, the attack is guaranteed to crit. Janus' skill attacks ignore 50% of the enemy's DEF and S-DEF. The skill's damage increases by 0.8% for each Accumulator above 100 spent during the skill cast. Using the skill changes his personality to [Protective]. Lastly, he recovers 100 Accumulator. [Protective]: Recover 60% of max HP when switching to [Protective] personality and gain a shield equal to 230% of max HP (does not stack) lasting 1 round. He also gains 70% damage reduction, and allies gain 50%, for 1 round. He gains 120% DEF and S-DEF for 1 round. His block is increased by 100% (absolute value) for 1 round. Janus also gains Accumulator equal to 70% of the Accumulator cost of any skill not cast by himself for 1 round. He can gain up to 600 Accumulator per round this way. Janus is also cleared of all control effects on his next round before acting. [Protective] Active Skill: Does not attack but restores the max HP of all allies by 60% and has a 100% chance to reveal all invisible enemies. Janus himself gains Rebirth for 2 rounds, and is healed to 100% of his initial HP and Accumulator on rebirth, and has a 55% chance to revive dead allies (probability calculated individually for each unit; unaffected by forbidding revival effects), restoring them to 100% of their initial HP and Accumulator. Janus gains immunity to Accumulator Reduction for 2 rounds and invisibility for 1 round. Janus also gains [Dark Invisibility] (cannot be attacked or targeted by skills) for 1 round after casting a skill while at 500 or more Accumulator. Janus also gains a shield that withstands 1 instance of lethal damage (including instant death) for 1 round. He then switches to his [Offensive] personality. Skills cast while in his [Protective] personality do not cost Accumulator (but he needs to have at least 100 Accumulator to cast). Janus gains an extra 300 Accumulator at the start of battle as well as Eye of True Sight for 99 rounds. If he starts the battle in [Offensive] personality, he gains invisibility for 1 round and a shield that withstands 1 instance of lethal damage (including instant death) for 1 round. Janus follows up with 7 extra attacks the first time he casts the skill. If he starts the battle in [Protective] personality, he gains a shield equal to 230% of his max HP (does not stack) lasting 1 round. He also gains 70% damage reduction, and allies gain 50%, for 1 round. He gains 120% DEF and S-DEF for 1 round. His block is increased by 100% (absolute value) for 1 round. Janus also gains Accumulator equal to 70% of the Accumulator cost of any skill not cast by himself for 1 round. He can gain up to 600 Accumulator per round this way. Janus gains immunity to Accumulator Reduction for 2 rounds. Janus deals 40% increased damage when fighting non-Player units. While in [Protector] personality, Janus is also cleared of all control effects on each round before acting. Note: When Janus is revived or rebirths, he returns to battle in the personality chosen from the Formation menu.
- **Ⅳ** at `Awaken +3` — — (双生之魂，觉醒+2(PVE)，坚毅)
  _(no English description shipped)_

### Transform form (530 · 亚努斯（防御）)
- **Ⅰ** at `+0` — Duality Soul-[Aggressive] (双生之魂，侵略)
  Janus has two personalities and switches between his [Aggressive] and [Protective] personalities each time he acts, each having its own skill (You can in the Formation menu choose whether to start the battle in his [Aggressive] or [Protective] personality). [Aggressive]: Deals 320% S-ATK damage and follows up with 3 further attacks, each dealing 300% S-ATK damage and 3M True Damage to a random enemy unit. Attacks 1 extra time for each extra 60 Accumulator spent during the skill cast, up to 7. If Janus has more than 200 Accumulator when casting the skill, the attack cannot be blocked, and if more than 400 Accumulator, the attack is guaranteed to crit. Janus' skill attacks ignore 35% of the enemy's DEF and S-DEF. The skill's damage increases by 0.3% for each Accumulator above 100 spent during skill cast. Using the skill changes his personality to [Protective]. Lastly, he recovers 100 Accumulator. [Protective]: Recover 50% of max HP when switching to [Protective] personality and gain a shield equal to 180% of max HP (does not stack) lasting 1 round. He also gains 60% damage reduction, and allies gain 35%, for 1 round. He gains 100% DEF and S-DEF for 1 round. His block is increased by 100% (absolute value) for 1 round. Janus also gains Accumulator equal to 55% of the Accumulator cost of any skill not cast by himself for 1 round. He can gain up to 600 Accumulator per round this way. Janus is also cleared of all control effects on his next round before acting. [Protective] Active Skill: Does not attack but restores the max HP of all allies by 50% and has a 100% chance to reveal all invisible enemies. Janus himself gains Rebirth for 2 rounds, and is healed to 100% of his initial HP and Accumulator on rebirth. Then he gains invisibility for 1 round and a shield that withstands 1 instance of lethal damage (including instant death) for 1 round. He then switches to his [Aggressive] personality. Skills cast while in his [Protective] personality do not cost Accumulator (but he needs to have at least 100 Accumulator to cast). Janus gains an extra 300 Accumulator at the start of battle. If he starts the battle in [Aggressive] personality, he gains invisibility for 1 round and a shield that withstands 1 instance of lethal damage (including instant death) for 1 round. If he starts the battle in [Protective] personality, he gains a shield equal to 180% of his max HP (does not stack) lasting 1 round. He also gains 60% damage reduction, and allies gain 35%, for 1 round. He gains 100% DEF and S-DEF for 1 round. His block is increased by 100% (absolute value) for 1 round. Janus also gains Accumulator equal to 55% of the Accumulator cost of any skill not cast by himself for 1 round. He can gain up to 600 Accumulator per round this way. Janus is also cleared of all control effects on his next round before acting. Note: When Janus is revived or rebirths, he returns to battle in the personality chosen from the Formation menu.
- **Ⅱ** at `Awaken` — Duality Soul-[Aggressive]Ⅱ (双生之魂，觉醒+1，侵略)
  Janus has two personalities and switches between his [Offensive] and [Protective] personalities each time he acts, each having its own skill (You can in the Formation menu choose whether to start the battle in his [Offensive] or [Protective] personality). [Offensive]: Deals 340% S-ATK damage and follows up with 3 further attacks, each dealing 320% S-ATK damage and 4M True Damage to a random enemy unit. Attacks 1 extra time for each extra 50 Accumulator spent during the skill cast, up to 9. If Janus has more than 200 Accumulator when casting the skill, the attack cannot be blocked, and if more than 400 Accumulator, the attack is guaranteed to crit. Janus' skill attacks ignore 40% of the enemy's DEF and S-DEF. The skill's damage increases by 0.5% for each Accumulator above 100 spent during the skill cast. Using the skill changes his personality to [Protective]. Lastly, he recovers 100 Accumulator. [Protective]: Recover 55% of max HP when switching to [Protective] personality and gain a shield equal to 200% of max HP (does not stack) lasting 1 round. He also gains 65% damage reduction, and allies gain 40%, for 1 round. He gains 100% DEF and S-DEF for 1 round. His block is increased by 100% (absolute value) for 1 round. Janus also gains Accumulator equal to 60% of the Accumulator cost of any skill not cast by himself for 1 round. He can gain up to 600 Accumulator per round this way. Janus is also cleared of all control effects on his next round before acting. [Protective] Active Skill: Does not attack but restores the max HP of all allies by 55% and has a 100% chance to reveal all invisible enemies. Janus himself gains Rebirth for 2 rounds, and is healed to 100% of his initial HP and Accumulator on rebirth, and has a 50% chance to revive dead allies (probability calculated individually for each unit), restoring them to 100% of their initial HP and Accumulator. Janus gains immunity to Accumulator Reduction for 2 rounds and invisibility for 1 round. Janus also gains [Dark Invisibility] (cannot be attacked or targeted by skills) for 1 round after casting a skill while at 600 or more Accumulator. Janus also gains a shield that withstands 1 instance of lethal damage (including instant death) for 1 round. He then switches to his [Offensive] personality. Skills cast while in his [Protective] personality do not cost Accumulator (but he needs to have at least 100 Accumulator to cast). Janus gains an extra 300 Accumulator at the start of battle. If he starts the battle in [Offensive] personality, he gains invisibility for 1 round and a shield that withstands 1 instance of lethal damage (including instant death) for 1 round. Janus follows up with 7 extra attacks the first time he casts the skill. If he starts the battle in [Protective] personality, he gains a shield equal to 200% of his max HP (does not stack) lasting 1 round. He also gains 65% damage reduction, and allies gain 40%, for 1 round. He gains 100% DEF and S-DEF for 1 round. His block is increased by 100% (absolute value) for 1 round. Janus also gains Accumulator equal to 60% of the Accumulator cost of any skill not cast by himself for 1 round. He can gain up to 600 Accumulator per round this way. Janus gains immunity to Accumulator Reduction for 2 rounds, and is also cleared of all control effects on his next round before acting. Note: When Janus is revived or rebirths, he returns to battle in the personality chosen from the Formation menu.
- **Ⅲ** at `Second Awaken` — Duality Soul-[Protective]Ⅲ (双生之魂，觉醒+2，侵略)
  Janus has two personalities and switches between his [Offensive] and [Protective] personalities each time he acts, each having its own skill (You can in the Formation menu choose whether to start the battle in his [Offensive] or [Protective] personality). [Offensive]: Deals 360% S-ATK damage and follows up with 3 further attacks, each dealing 340% S-ATK damage and 6M True Damage to a random enemy unit. Attacks 1 extra time for each extra 40 Accumulator spent during the skill cast, up to 10. Each follow-up attack deals extra True Damage equal to 15% of the target's current HP. If Janus has more than 100 Accumulator when casting the skill, the attack cannot be blocked, and if more than 300 Accumulator, the attack is guaranteed to crit. Janus' skill attacks ignore 50% of the enemy's DEF and S-DEF. The skill's damage increases by 0.8% for each Accumulator above 100 spent during the skill cast. Using the skill changes his personality to [Protective]. Lastly, he recovers 100 Accumulator. [Protective]: Recover 60% of max HP when switching to [Protective] personality and gain a shield equal to 230% of max HP (does not stack) lasting 1 round. He also gains 70% damage reduction, and allies gain 50%, for 1 round. He gains 120% DEF and S-DEF for 1 round. His block is increased by 100% (absolute value) for 1 round. Janus also gains Accumulator equal to 70% of the Accumulator cost of any skill not cast by himself for 1 round. He can gain up to 600 Accumulator per round this way. Janus is also cleared of all control effects on his next round before acting. [Protective] Active Skill: Does not attack but restores the max HP of all allies by 60% and has a 100% chance to reveal all invisible enemies. Janus himself gains Rebirth for 2 rounds, and is healed to 100% of his initial HP and Accumulator on rebirth, and has a 55% chance to revive dead allies (probability calculated individually for each unit; unaffected by forbidding revival effects), restoring them to 100% of their initial HP and Accumulator. Janus gains immunity to Accumulator Reduction for 2 rounds and invisibility for 1 round. Janus also gains [Dark Invisibility] (cannot be attacked or targeted by skills) for 1 round after casting a skill while at 500 or more Accumulator. Janus also gains a shield that withstands 1 instance of lethal damage (including instant death) for 1 round. He then switches to his [Offensive] personality. Skills cast while in his [Protective] personality do not cost Accumulator (but he needs to have at least 100 Accumulator to cast). Janus gains an extra 300 Accumulator at the start of battle as well as Eye of True Sight for 99 rounds. If he starts the battle in [Offensive] personality, he gains invisibility for 1 round and a shield that withstands 1 instance of lethal damage (including instant death) for 1 round. Janus follows up with 7 extra attacks the first time he casts the skill. If he starts the battle in [Protective] personality, he gains a shield equal to 230% of his max HP (does not stack) lasting 1 round. He also gains 70% damage reduction, and allies gain 50%, for 1 round. He gains 120% DEF and S-DEF for 1 round. His block is increased by 100% (absolute value) for 1 round. Janus also gains Accumulator equal to 70% of the Accumulator cost of any skill not cast by himself for 1 round. He can gain up to 600 Accumulator per round this way. Janus gains immunity to Accumulator Reduction for 2 rounds. Janus deals 40% increased damage when fighting non-Player units. While in [Protector] personality, Janus is also cleared of all control effects on each round before acting. Note: When Janus is revived or rebirths, he returns to battle in the personality chosen from the Formation menu.
- **Ⅳ** at `Awaken +3` — — (双生之魂，觉醒+2(PVE)，侵略)
  _(no English description shipped)_

### Augment cost (per step)
- `+1` — 5× Flagship Chip · 100,000 money
- `+2` — 10× Flagship Chip · 200,000 money
- `+3` — 21× Flagship Chip · 300,000 money
- `+4` — 28× Flagship Chip · 500,000 money
- `+5` — 35× Flagship Chip · 800,000 money
- `+6` — 42× Flagship Chip · 10× Pandora Power Core
- `+7` — 49× Flagship Chip · 50× Pandora Power Core
- `+8` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Flagship Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Flagship Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Flagship Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 40× Galaxy Heart · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 80× Galaxy Heart · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 160× Galaxy Heart · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 320× Galaxy Heart · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 640× Galaxy Heart · 130× Inert Alloy · 100× Heated Alloy
- `Awaken` — 1280× Galaxy Heart · 1280× Inert Alloy · 1280× Heated Alloy

---

## 538 · Saint Kilian 圣·凯尔
**Role** Flagship · **Attack** physical · **Generation** latest
**Ratings** Damage 10/10 · Defence 6/10 · Assist 8/10

### Skill panels
**Slot 1 — Divine Judgment** (id 1560, unlocks at `+0`)
  - **Ⅰ** at `+0` — Divine JudgmentⅠ (圣·凯尔+0，天神审判I)
    If not in a duel, selects the enemy unit with the highest S-ATK (absolute value) and duels them (units already in a duel cannot be selected), after which other actions follow. Single Attack, deals 300% S-ATK damage to targets and purges buffs. When taking attack damage in the next 2 rounds, you recover 30% of max HP. Lastly, you recover 100 Accumulator. Duel: Both duelists can only attack one another (except for subsequent damage; effect takes precedence over Unyielding). [Saint Kilian] takes 20% reduced damage from the other duelist and 20% reduced damage from other units. The duel lasts until either unit is destroyed.
  - **Ⅱ** at `+7` — Divine JudgmentⅡ (圣·凯尔+3，天神审判)
    If not in a duel, selects the enemy unit with the highest S-ATK (absolute value) and duels them (units already in a duel cannot be selected), after which other actions follow. Single Attack, deals 350% S-ATK damage to targets and purges buffs. S-ATK has Always Hit and Penetrate (cannot be blocked). When taking attack damage in the next 2 rounds, you recover 35% of max HP. Lastly, you recover 100 Accumulator. Duel: Both duelists can only attack one another (except for subsequent damage; effect takes precedence over Unyielding). [Saint Kilian] takes 40% reduced damage from the other duelist and 30% reduced damage from other units. The duel lasts until either unit is destroyed.
  - **Ⅲ** at `+T` — Divine JudgmentⅢ (圣·凯尔+7，天神审判II)
    If not in a duel, selects the enemy unit with the highest S-ATK (absolute value) and duels them (units already in a duel cannot be selected), after which other actions follow. Single Attack, deals 400% S-ATK damage to targets and purges buffs. S-ATK has Always Hit and Penetrate (cannot be blocked) and ignores 30% of the enemy's DEF and S-DEF. When taking attack damage in the next 2 rounds, you recover 40% of max HP. Lastly, you recover 100 Accumulator. Duel: Both duelists can only attack one another (except for subsequent damage; effect takes precedence over Unyielding). [Saint Kilian] takes 60% reduced damage from the other duelist and 40% reduced damage from other units. The duel lasts until either unit is destroyed.
  - **Ⅳ** at `+T4` — Divine JudgmentIV (圣·凯尔+13，天神审判II)
    If not in a duel, selects the enemy unit with the highest S-ATK (absolute value) and duels them (units already in a duel cannot be selected), after which other actions follow. Single Attack, deals 450% S-ATK damage to targets and purges buffs. S-ATK has Always Hit and Penetrate (cannot be blocked), ignores 45% of the enemy's DEF and S-DEF, and deals True Damage equal to 35% of the enemy's max HP. When taking attack damage in the next 2 rounds, you recover 45% of max HP. Lastly, you recover 100 Accumulator. Duel: Both duelists can only attack one another (except for subsequent damage; effect takes precedence over Unyielding). [Saint Kilian] takes 80% reduced damage from the other duelist and 50% reduced damage from other units. The duel lasts until either unit is destroyed.

**Slot 2 — Duel of Justice** (id 1561, unlocks at `+3`)
  - **Ⅰ** at `+3` — Duel of JusticeⅠ (圣·凯尔+0，决斗获胜触发技能)
    Takes effect at the start of battle: Activates Eye of True Sight for 99 rounds. Selects the enemy unit with the least HP (absolute value) and duels them (units already in a duel cannot be selected). If victorious, [Saint Kilian] recovers 40% of max HP and gains 40 Accumulator.
  - **Ⅱ** at `+13` — Duel of JusticeⅡ (圣·凯尔+3，决斗获胜触发技能)
    Takes effect at the start of battle: Obtain the Eye of Truth, lasting for 99 rounds. Selects the enemy unit with the least HP (absolute value) and duels them (units already in a duel cannot be selected). If victorious, [Saint Kilian] recovers 60% of max HP, gains 60 Accumulator and 20% S-ATK (stacks and lasts until the end of battle; disappears on death).
  - **Ⅲ** at `Awaken` — Duel of JusticeⅢ (圣·凯尔)
    Takes effect at the start of battle: Activates Eye of True Sight for 99 rounds. Selects the enemy unit with the least HP (absolute value) and duels them (units already in a duel cannot be selected). If victorious, [Saint Kilian] recovers 80% of max HP, gains 80 Accumulator and 30% S-ATK (stacks and lasts until the end of battle; disappears on death). [Saint Kilian] gains 15% of all allies' (except for himself) ATK, S-ATK, DEF and S-DEF at the start of each battle. He cannot gain more than 70% of his initial stat values.
  - **Ⅳ** at `Second Awaken` — Duel of JusticeIV (圣·凯尔+13，决斗获胜触发技能)
    Takes effect at the start of battle: Obtain the Eye of Truth, lasting for 99 rounds. Selects the enemy unit with the least HP (absolute value) and duels them (units already in a duel cannot be selected). If victorious, [Saint Kilian] recovers 100% of max HP, gains 100 Accumulator and 40% S-ATK (stacks and lasts until the end of battle; disappears on death). [Saint Kilian] gains 20% of all allies' (except for himself) ATK, S-ATK, DEF and S-DEF at the start of each battle. He cannot gain more than 100% of his initial stat values. The enemy [Saint Kilian] duels can only target [Saint Kilian] with their skills, and their allied units cannot target the duel target with skills.

**Slot 3 — Divine Physique** (id 1562, unlocks at `+6`)
  - **Ⅰ** at `+6` — Divine PhysiqueⅠ (圣·凯尔+0，受到伤害回血)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +60% S-ATK: +30% DMG Reduction (Absolute Value): +20%
  - **Ⅱ** at `+9` — Divine PhysiqueⅡ (圣·凯尔)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +80% S-ATK: +50% DMG Reduction (Absolute Value): +30%
  - **Ⅲ** at `+12` — Divine PhysiqueⅢ (圣·凯尔+7，受到伤害回血)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +100% S-ATK: +70% DMG Reduction (Absolute Value): +40%
  - **Ⅳ** at `+15` — Divine PhysiqueIV (圣·凯尔+16，受到伤害回血)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +120% S-ATK: +90% DMG Reduction (Absolute Value): +50%

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
- `+T` — 15× Saint Kilian Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Saint Kilian Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Saint Kilian Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Saint Kilian Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Saint Kilian Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 120× Saint Kilian Ship Part · 100× Alien Essence · 100× Transcendence Core

---

## 546 · Gale 疾风
**Role** Flagship · **Attack** physical · **Generation** latest
**Ratings** Damage 10/10 · Defence 10/10 · Assist 8/10

### Skill panels
**Slot 1 — Autocannon Blast** (id 1608, unlocks at `+0`)
  - **Ⅰ** at `+0` — Autocannon BlastⅠ (疾风技能描述，无实际意义)
    Cross attack, first clears all buffs from the target, then plunders 60% of their Penetration (absolute value) and 30% of their Accumulator and deals 340% S-ATK damage. Applies a Wind Barrier to all allies for 2 rounds. Wind Barrier: Grants immunity to Freeze, Lock and Confuse while active. Gains Eye of True Sight for 99 rounds. Lastly, you recover 100 Accumulator.
  - **Ⅱ** at `+5` — Autocannon BlastⅡ (疾风技能描述，无实际意义)
    Cross attack, first clears all buffs from the target, then plunders 70% of their Penetration (absolute value) and 35% of their Accumulator and deals 360% S-ATK damage. Applies a Wind Barrier to all allies for 2 rounds. Wind Barrier: Grants immunity to Freeze, Lock, Confuse, Petrify, Icebound and Entangle while active. Also gains 2 stacks of RX-78 Projection Energy Charge and Eye of True Sight for 99 rounds. Lastly, you recover 100 Accumulator.
  - **Ⅲ** at `+11` — Autocannon BlastⅢ (疾风技能描述，无实际意义)
    Cross attack, first clears all buffs from the target, then plunders 80% of their Penetration (absolute value) and 40% of their Accumulator and deals 380% S-ATK damage. Applies a Wind Barrier to all allies for 2 rounds. Wind Barrier: Grants immunity to Freeze, Lock, Confuse, Petrify, Icebound, Entangle, Forbidding Skill Use and Weaken while active. Also gains 2 stacks of RX-78 Projection Energy Charge and Eye of True Sight for 99 rounds. Lastly, you recover 100 Accumulator.
  - **Ⅳ** at `+T3` — Autocannon BlastIV (疾风技能描述，无实际意义)
    Cross attack, first clears all buffs from the target, then plunders 100% of their Penetration (absolute value) and 50% of their Accumulator and deals 420% S-ATK damage. Applies a Wind Barrier to all allies for 2 rounds. Wind Barrier: Grants immunity to Freeze, Lock, Confuse, Petrify, Icebound, Entangle, Forbidding Skill Use and Weaken while active, and a shield that blocks 1 attack. Also gains 2 stacks of RX-78 Projection Energy Charge and Eye of True Sight for 99 rounds. Lastly, you recover 100 Accumulator. Applies a Wind Barrier lasting 2 rounds to all allies at the start of battle. Wind Barrier grants immunity to Freeze, Lock, Confuse, Petrify, Icebound, Entangle, Forbidding Skill Use and Weaken while active, and a shield that blocks 1 attack.

**Slot 2 — RX-78 Projection** (id 1609, unlocks at `+2`)
  - **Ⅰ** at `+2` — RX-78 ProjectionⅠ (疾风技能描述，无实际意义)
    (Takes effect at the start of battle) Gale gains Energy Charge at the start of battle, starting at 3 stacks. Upon reaching the maximum 7 stacks, Gale summons an RX-78 Projection to join the battle. After Gale finishes using an attack skill (RX-78 Projections can use skills even while Gale doesn't have enough Accumulator, however, not if Gale is crowd-controlled), all Energy Charges are consumed and reset to 0. Gale gains 1 stack whenever allied or enemy unit uses a skill or whenever allied or enemy unit dies. RX-78 Projection: Immediately casts Heavy Obliteration upon reaching 7 Energy Charge stacks, hitting all enemies and dealing True Damage equal to 10% of each target's max HP. Then targets 1 random enemy and consumes all Energy Charge to launch a follow-up attack, dealing 260% S-ATK damage for each stack consumed this way.
  - **Ⅱ** at `+7` — RX-78 ProjectionⅡ (疾风技能描述，无实际意义)
    (Takes effect at the start of battle) Gale gains Energy Charge at the start of battle, starting at 3 stacks. Upon reaching the maximum 7 stacks, Gale summons an RX-78 Projection to join the battle. After Gale finishes using an attack skill (RX-78 Projections can use skills even while Gale doesn't have enough Accumulator, however, not if Gale is crowd-controlled), all Energy Charges are consumed and reset to 0. Gale gains 1 stack whenever any allied or enemy unit uses a skill or whenever any allied or enemy unit dies. RX-78 Projection: Immediately casts Heavy Obliteration upon reaching 7 Energy Charge stacks, hitting all enemies and dealing True Damage equal to 15% of each target's max HP. Then targets 1 random enemy and consumes all Energy Charge to launch a follow-up attack, dealing 280% S-ATK damage for each stack consumed this way. RX-78 Projections now also launch follow-up attacks, each dealing extra damage equal to 30% of targets' current HP.
  - **Ⅲ** at `+15` — RX-78 ProjectionⅢ (疾风技能描述，无实际意义)
    (Takes effect at the start of battle) Gale gains Energy Charge at the start of battle, starting at 3 stacks. Upon reaching the maximum 7 stacks, Gale summons an RX-78 Projection to join the battle. After Gale finishes using an attack skill (RX-78 Projections can use skills even while Gale doesn't have enough Accumulator, however, not if Gale is crowd-controlled), all Energy Charges are consumed and reset to 0. Gale gains 1 stack whenever any allied or enemy unit uses a skill or whenever any allied or enemy unit dies. RX-78 Projection: Immediately casts Heavy Obliteration upon reaching 7 Energy Charge stacks, hitting all enemies and dealing True Damage equal to 20% of each target's max HP. Then targets 1 random enemy and consumes all Energy Charge to launch a follow-up attack, dealing 300% S-ATK damage for each stack consumed this way. RX-78 Projections now also launch follow-up attacks, each dealing extra damage equal to 30% of targets' current HP. Gale's ship explodes when destroyed, dealing True Damage equal to 40% of Gale's max HP to all enemies.
  - **Ⅳ** at `Second Awaken` — RX-78 ProjectionIV (疾风技能描述，无实际意义)
    (Takes effect at the start of battle) Gale gains Energy Charge at the start of battle, starting at 3 stacks. Upon reaching the maximum 7 stacks, Gale summons an RX-78 Projection to join the battle. After Gale finishes using an attack skill (RX-78 Projections can use skills even while Gale doesn't have enough Accumulator, however, not if Gale is crowd-controlled), all Energy Charges are consumed and reset to 0. Gale gains 1 stack whenever any allied or enemy unit uses a skill or whenever any allied or enemy unit dies. RX-78 Projection: Immediately casts Heavy Obliteration upon reaching 7 Energy Charge stacks, hitting all enemies and dealing True Damage equal to 20% of each target's max HP. Then targets 1 random enemy and consumes all Energy Charge to launch a follow-up attack, dealing 300% S-ATK damage for each stack consumed this way. RX-78 Projections now also launch follow-up attacks, each dealing extra damage equal to 30% of targets' current HP. Gale's ship explodes when destroyed, dealing True Damage equal to 40% of Gale's max HP to all enemies. Gale and RX-78 Projections' skill attacks now deal True Damage (ignores defenses) and heal all allies for 50% of the total damage dealt. This effect lasts until the end of battle.

**Slot 3 — RX-78 Plating** (id 1610, unlocks at `+3`)
  - **Ⅰ** at `+3` — RX-78 PlatingⅠ (疾风技能描述，无实际意义)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +60% S-ATK: +60% DMG Bonus (Absolute Value): +15% Crit ATK (Absolute Value) +15%
  - **Ⅱ** at `+9` — RX-78 PlatingⅡ (疾风技能描述，无实际意义)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +90% S-ATK: +90% DMG Bonus (Absolute Value): +20% Crit ATK (Absolute Value) +20%
  - **Ⅲ** at `+T` — RX-78 PlatingⅢ (疾风技能描述，无实际意义)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +120% S-ATK: +120% DMG Bonus (Absolute Value): +25% Crit ATK (Absolute Value) +25%
  - **Ⅳ** at `+T4` — RX-78 PlatingIV (疾风技能描述，无实际意义)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +150% S-ATK: +150% DMG Bonus (Absolute Value): +30% Crit ATK (Absolute Value) +30%

**Slot 4 — RX-78 Booster** (id 1611, unlocks at `+13`)
  - **Ⅰ** at `+13` — RX-78 BoosterⅠ (疾风技能描述，无实际意义)
    (Takes effect at the start of battle) Gale and RX-78 Projections deal 20% increased damage for every 1 enemy unit in the battle.
  - **Ⅱ** at `+T1` — RX-78 BoosterⅡ (疾风技能描述，无实际意义)
    (Takes effect at the start of battle) Gale and RX-78 Projections deal 20% increased damage for every 1 enemy unit in the battle. The first time Gale drops below 90%, 60% and 30% HP (these triggers reset when revived), clears crowd-control effects (Freeze, Lock, Confuse, Petrify, Icebound, Entangle, Forbidding Skill Use and Weaken), sets Energy Charge to 7 stacks, and commands RX-78 Projections to immediately launch 1 skill attack (RX-78 Projections can use skills even while Gale doesn't have enough Accumulator, however, not if Gale is crowd-controlled).
  - **Ⅲ** at `+T2` — RX-78 BoosterⅢ (疾风技能描述，无实际意义)
    (Takes effect at the start of battle) Gale and RX-78 Projections deal 20% increased damage for every 1 enemy unit in the battle. The first time Gale drops below 90%, 60% and 30% HP (these triggers reset when revived), clears crowd-control effects (Freeze, Lock, Confuse, Petrify, Icebound, Entangle, Forbidding Skill Use and Weaken), sets Energy Charge to 7 stacks, and commands RX-78 Projections to immediately launch 1 skill attack (RX-78 Projections can use skills even while Gale doesn't have enough Accumulator, however, not if Gale is crowd-controlled). If Gale has at least 1 stack of Energy Charge when taking lethal damage, all Energy Charges are consumed to withstand that damage. This effect can trigger up to 3 times per battle (these 3 times do NOT reset when revived).
  - **Ⅳ** at `Awaken` — RX-78 BoosterIV (疾风技能描述，无实际意义)
    (Takes effect at the start of battle) Gale and RX-78 Projections deal 20% increased damage for every 1 enemy unit in the battle. The first time Gale drops below 90%, 60% and 30% HP (these triggers reset when revived), clears crowd-control effects (Freeze, Lock, Confuse, Petrify, Icebound, Entangle, Forbidding Skill Use and Weaken), sets Energy Charge to 7 stacks, and commands RX-78 Projections to immediately launch 1 skill attack (RX-78 Projections can use skills even while Gale doesn't have enough Accumulator, however, not if Gale is crowd-controlled). If Gale has at least 1 stack of Energy Charge when taking lethal damage, all Energy Charges are consumed to withstand that damage. This effect can trigger up to 3 times per battle (these 3 times do NOT reset when revived). Whenever Gale or RX-78 Projections destroy an enemy with a skill, they will use the wreckage to remodel destroyed allies, reviving all allies (unaffected by forbidding revival effects) with 100% of their initial HP and Accumulator.

### Augment cost (per step)
- `+1` — 5× Flagship Chip · 100,000 money
- `+2` — 10× Flagship Chip · 200,000 money
- `+3` — 21× Flagship Chip · 300,000 money
- `+4` — 28× Flagship Chip · 500,000 money
- `+5` — 35× Flagship Chip · 800,000 money
- `+6` — 42× Flagship Chip · 10× Pandora Power Core
- `+7` — 49× Flagship Chip · 50× Pandora Power Core
- `+8` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Flagship Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Flagship Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Flagship Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 40× Gale Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 80× Gale Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 160× Gale Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 320× Gale Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 640× Gale Ship Part · 130× Inert Alloy · 100× Heated Alloy
- `Awaken` — 1280× Gale Ship Part · 1280× Inert Alloy · 1280× Heated Alloy

---

## 553 · Elenia 伊莲尼亚
**Role** Flagship · **Attack** physical · **Generation** latest
**Ratings** Damage 10/10 · Defence 6/10 · Assist 8/10

### Skill panels
**Slot 1 — Rapid Pursuit** (id 1659, unlocks at `+0`)
  - **Ⅰ** at `+0` — Rapid PursuitⅠ (伊莲尼亚技能描述)
    Cross Attack, first clears all buffs from the target, then deals 280% S-ATK damage to the hit target, and finally performs a 【Pursuit】. Increases the Crit Rate of all friendly ships by 40% (absolute value) for 2 rounds. Increases the S-ATK of all friendly ships by 40% for 2 rounds. Lastly, you recover 100 Accumulator. Pursuit: Each pursuit deals 230% S-ATK damage to one random enemy on the Cross range, and deals an additional 4M True Damage. Starts with 3 pursuits. For every 80 Accumulator costed when casting a skill, one additional pursuit is performed, up to a maximum of 7 additional pursuits.
  - **Ⅱ** at `+7` — Rapid PursuitⅡ (伊莲尼亚技能描述)
    Cross attack, first clears all buffs from the target, reduces the target's S-DEF and DEF by 40% for 2 rounds, then deals 310% S-ATK damage to the hit target, and finally performs a 【Pursuit】.Increases all friendly ships' Crit Rate by 50% (absolute value) for 2 rounds. Increases all friendly ships' S-ATK by 60% for 2 rounds. Lastly, recovers 100 Accumulator. Pursuit: Each pursuit deals 260% S-ATK damage to one random enemy on the Cross range, and deals an additional 5M True Damage. Starts with 3 pursuits. For every 70 Accumulator costed when casting a skill, one additional pursuit is performed, up to a maximum of 7 additional pursuits.
  - **Ⅲ** at `+T` — Rapid PursuitⅢ (伊莲尼亚技能描述)
    Cross attack, first clears all buffs from the target, reduces the target's S-DEF and DEF by 70% for 2 rounds, then plunders 40% of the target's Accumulator, and deals 340% S-ATK damage to the hit target, and finally performs a 【Pursuit】.Increases all friendly ships' Crit Rate by 70% (absolute value) for 2 rounds. Increases all friendly ships' S-ATK by 70% for 2 rounds. Lastly, recovers 100 Accumulator. Pursuit: Each pursuit deals 290% S-ATK damage to one random enemy on the Cross range, and deals an additional 6M True Damage. Starts with 3 pursuits. For every 60 Accumulator costed when casting a skill, one additional pursuit is performed, up to a maximum of 10 additional pursuits.
  - **Ⅳ** at `+T4` — Rapid PursuitⅣ (伊莲尼亚技能描述)
    Cross attack, first clears all buffs from the target, reduces the target's S-DEF and DEF by 70% for 2 rounds, then plunders 60% of the target's Accumulator, and deals 370% S-ATK damage to the hit target, and finally performs a 【Pursuit】.Increases all friendly ships' Crit Rate by 100% (absolute value) for 2 rounds. Increases all friendly ships' S-ATK by 100% for 2 rounds. Adds 65 Accumulator to all allies. Lastly, recovers 100 Accumulator. Pursuit: Each pursuit deals 320% S-ATK damage to one random enemy on the Cross range, and deals an additional 8M True Damage. Starts with 3 pursuits. For every 50 Accumulator costed when casting a skill, one additional pursuit is performed, up to a maximum of 10 additional pursuits.

**Slot 2 — Energy Modification** (id 1660, unlocks at `+3`)
  - **Ⅰ** at `+3` — Energy ModificationⅠ (伊莲尼亚技能描述)
    (Takes effect at the start of battle) Increases all friendly ships' damage dealt by 15% (When fighting against non-Player enemies, increases all friendly ships' damage dealt by 30%)
  - **Ⅱ** at `+13` — Energy ModificationⅡ (伊莲尼亚技能描述)
    (Takes effect at the start of battle) Increases all friendly ships' damage dealt by 15% (When fighting against non-Player enemies, increases all friendly ships' damage dealt by 30%) After casting a skill, recovers an additional 150 Accumulator.
  - **Ⅲ** at `Awaken` — Energy ModificationⅢ (伊莲尼亚技能描述)
    (Takes effect at the start of battle) Increases all friendly ships' damage dealt by 15% (When fighting against non-Player enemies, increases all friendly ships' damage dealt by 30%) After casting a skill, recovers an additional 150 Accumulator. When dealing S-ATK damage, for every 1% of max HP the target has lost, the damage dealt to them increases by 2% (When fighting against non-Player enemies, the damage dealt increases by 4% for every 1% of HP lost).
  - **Ⅳ** at `Second Awaken` — Energy ModificationⅣ (伊莲尼亚技能描述)
    (Takes effect at the start of battle) Increases all friendly ships' damage dealt by 15% (When fighting against non-Player enemies, increases all friendly ships' damage dealt by 30%) After casting a skill, recovers an additional 150 Accumulator. When dealing S-ATK damage, for every 1% of max HP the target has lost, the damage dealt to them increases by 2% (When fighting against non-Player enemies, the damage dealt increases by 4% for every 1% of HP lost). When Elenia casts a skill, she first gains the Accumulator that equal to 50% of the total current Accumulator of all allies (excluding herself), up to a maximum of 300 (When fighting against non-Player enemies, the maximum is 500).

**Slot 3 — Fleet Enhancement** (id 1661, unlocks at `+5`)
  - **Ⅰ** at `+5` — Fleet EnhancementⅠ (伊莲尼亚技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +60% Penetration (absolute value): +60% Crit ATK (absolute value): +30%
  - **Ⅱ** at `+9` — Fleet EnhancementⅡ (伊莲尼亚技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +90% Penetration (absolute value): +70% Crit ATK (absolute value): +40%
  - **Ⅲ** at `+12` — Fleet EnhancementⅢ (伊莲尼亚技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +120% Penetration: +80% (absolute value) Crit ATK: +50% (absolute value)
  - **Ⅳ** at `+15` — Fleet EnhancementⅣ (伊莲尼亚技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +150% Penetration: +90% (absolute value) Crit ATK: +60% (absolute value)

### Augment cost (per step)
- `+1` — 2× Flagship Chip · 1,000 money
- `+2` — 10× Flagship Chip · 20,000 money
- `+3` — 20× Flagship Chip · 300,000 money
- `+4` — 40× Flagship Chip · 500,000 money
- `+5` — 50× Flagship Chip · 800,000 money
- `+6` — 60× Flagship Chip · 20× Pandora Power Core
- `+7` — 70× Flagship Chip · 100× Pandora Power Core
- `+8` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Flagship Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Flagship Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Flagship Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 40× Galaxy Heart · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 80× Galaxy Heart · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 160× Galaxy Heart · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 320× Galaxy Heart · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 640× Galaxy Heart · 130× Inert Alloy · 100× Heated Alloy
- `Awaken` — 1280× Galaxy Heart · 1280× Inert Alloy · 1280× Heated Alloy

---

## 565 · Baralson 巴拉森
**Role** Flagship · **Attack** physical · **Generation** latest
**Ratings** Damage 8/10 · Defence 7/10 · Assist 7/10

### Skill panels
**Slot 1 — Soul Guardian** (id 1725, unlocks at `+0`)
  - **Ⅰ** at `+0` — Soul GuardianⅠ (巴拉森技能描述)
    Cross Attack, deals 260% S-ATK damage to targets. Heals all allies for 30% of Max HP. Increases self DMG Reduction (Absolute Value) and S-ATK DMG Reduction (Absolute Value) by 30%, lasting for 2 rounds. Grants self "Soul Guardian" for 2 rounds. Lastly, recovers 100 Accumulator. Soul Guardian: During its duration, when an ally takes lethal damage, Baralson will take their place in death and enter a spectral state. He can replace multiple allies to suffer death at once, and for each ally he replaces, the duration of the spectral state increases by 2 rounds. Soul Guardian can only be triggered once per battle. This effect does not work while in spectral state. Spectral State: During this state, cannot move and cannot be targeted by any ships from either side. If there are still allies alive when Spectral State ends, Baralson will return to the state at the start of battle; if no allies are alive, then he will die.
  - **Ⅱ** at `+7` — Soul GuardianⅡ (巴拉森技能描述)
    Cross Attack, deals 280% S-ATK damage to targets. Heals all allies for 40% of Max HP. Increases self DMG Reduction (Absolute Value) and S-ATK DMG Reduction (Absolute Value) by 40%, lasting for 2 rounds. Grants self "Soul Guardian" for 2 rounds. Lastly, recovers 100 Accumulator. Soul Guardian: During its duration, when an ally takes lethal damage, Baralson will take their place in death and enter a spectral state. He can replace multiple allies to suffer death at once, and for each ally he replaces, the duration of the spectral state increases by 2 rounds. Soul Guardian can take effect up to 2 times per battle. Spectral State: During this state, cannot move and cannot be targeted by any ships from either side. If there are still allies alive when Spectral State ends, Baralson will return to the state at the start of battle; if no allies are alive, then he will die.
  - **Ⅲ** at `+T` — Soul GuardianⅢ (巴拉森技能描述)
    Cross Attack, deals 300% S-ATK damage to targets. Heals all allies for 50% of Max HP. Increases self DMG Reduction (Absolute Value) and S-ATK DMG Reduction (Absolute Value) by 50%, lasting for 2 rounds. All allies gain 50% Crit ATK RED (Absolute Value) for 2 rounds. Grants self "Soul Guardian" for 2 rounds. Finally, recovers 100 Accumulator. Soul Guardian: During its duration, when an ally takes lethal damage, Baralson will take their place in death and enter a spectral state. He can replace multiple allies to suffer death at once, and for each ally he replaces, the duration of the spectral state increases by 2 rounds. Soul Guardian can take effect up to 3 times per battle. Spectral State: During this state, cannot move and cannot be targeted by any ships from either side. If there are still allies alive when Spectral State ends, Baralson will return to the state at the start of battle; if no allies are alive, then he will die.
  - **Ⅳ** at `+T4` — Soul GuardianIV (巴拉森技能描述)
    Cross Attack, deals 330% S-ATK damage to targets. Heals all allies for 50% of Max HP. Increases self DMG Reduction (Absolute Value) and S-ATK DMG Reduction (Absolute Value) by 75%, lasting for 2 rounds. All allies gain 80% Crit ATK RED (Absolute Value) for 2 rounds. Grants self "Soul Guardian" for 2 rounds. Finally, recovers 100 Accumulator. Soul Guardian: During its duration, when an ally takes lethal damage, Baralson will take their place in death and enter a spectral state. He can replace multiple allies to suffer death at once, and for each ally he replaces, the duration of the spectral state increases by 2 rounds. Soul Guardian can take effect up to 4 times per battle. Spectral State: During this state, cannot move and cannot be targeted by any ships from either side. If there are still allies alive when Spectral State ends, Baralson will return to the state at the start of battle; if no allies are alive, then he will die.

**Slot 2 — Spectral State** (id 1726, unlocks at `+3`)
  - **Ⅰ** at `+3` — Spectral StateⅠ (巴拉森技能描述)
    (Takes effect at the start of battle) Die in place of each ally, the duration of the Spectral State is increase by 1 round (with a minimum duration of 2 rounds).
  - **Ⅱ** at `+13` — Spectral StateⅡ (巴拉森技能描述)
    (Takes effect at the start of battle) Die in place of each ally, the duration of the Spectral State is increase by 1 round (with a minimum duration of 2 rounds). Upon entering Spectral State, heals all allies for 50% of their HP and removes crowd-control effects (Freeze, Lock, Confuse, Petrify, Icebound, Entangle, and Forbidding Skill Use).
  - **Ⅲ** at `Awaken` — Spectral StateⅢ (巴拉森技能描述)
    (Takes effect at the start of battle) Die in place of each ally, the duration of the Spectral State is increase by 1 round (with a minimum duration of 2 rounds). Upon entering Spectral State, heals all allies for 50% of their HP and removes crowd-control effects (Freeze, Lock, Confuse, Petrify, Icebound, Entangle, and Forbidding Skill Use). At the start of battle and upon each revival or Rebirth, grants [Soul Guardian] to self for 2 rounds.
  - **Ⅳ** at `Second Awaken` — Spectral StateIV (巴拉森技能描述)
    (Takes effect at the start of battle) Die in place of each ally, the duration of the Spectral State is increase by 1 round (with a minimum duration of 2 rounds). Upon entering Spectral State, heals all allies for 50% of their HP and removes crowd-control effects (Freeze, Lock, Confuse, Petrify, Icebound, Entangle, and Forbidding Skill Use). At the start of battle and upon each revival or Rebirth, grants [Soul Guardian] to self for 2 rounds. Upon the end of the Spectral State, if there are no surviving allies, Baralson revives all other allies (unaffected by forbidding revival effects) with 100% of their HP and Accumulator from the start of the battle, then he will die.

**Slot 3 — Soul Blessing** (id 1727, unlocks at `+5`)
  - **Ⅰ** at `+5` — Soul BlessingⅠ (巴拉森技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +30% DEF: +30% S-DEF: +30% DMG Reduction (Absolute Value): +15%
  - **Ⅱ** at `+9` — Soul BlessingⅡ (巴拉森技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +60% DEF: +50% S-DEF: +50% DMG Reduction (Absolute Value): +20%
  - **Ⅲ** at `+12` — Soul BlessingⅢ (巴拉森技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +90% DEF: +70% S-DEF: +70% DMG Reduction (Absolute Value): +25%
  - **Ⅳ** at `+15` — Soul BlessingIV (巴拉森技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +120% DEF: +90% S-DEF: +90% DMG Reduction (Absolute Value): +30%

### Augment cost (per step)
- `+1` — 2× Flagship Chip · 1,000 money
- `+2` — 10× Flagship Chip · 20,000 money
- `+3` — 20× Flagship Chip · 300,000 money
- `+4` — 40× Flagship Chip · 500,000 money
- `+5` — 50× Flagship Chip · 800,000 money
- `+6` — 60× Flagship Chip · 20× Pandora Power Core
- `+7` — 70× Flagship Chip · 100× Pandora Power Core
- `+8` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Flagship Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Flagship Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Flagship Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Flagship Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 40× Galaxy Heart · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 80× Galaxy Heart · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 160× Galaxy Heart · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 320× Galaxy Heart · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 640× Galaxy Heart · 130× Inert Alloy · 100× Heated Alloy
- `Awaken` — 1280× Galaxy Heart · 1280× Inert Alloy · 1280× Heated Alloy

---

## 579 · Shi Yu 时宇
**Role** Flagship · **Attack** physical · **Generation** latest
**Ratings** Damage 10/10 · Defence 6/10 · Assist 8/10

### Skill panels
**Slot 1 — Sword Shadow Engraving** (id 1804, unlocks at `+0`)
  - **Ⅰ** at `+0` — Sword Shadow EngravingⅠ (时宇+0)
    All Attack, deals 260% S-ATK damage to all targets. First, clears [Sword Shadow Engraving] from all enemies, then applies [Sword Shadow Engraving] with an initial stack of 0 to all enemies. Finally, recovers 100 Accumulator. Sword Shadow Engraving: Starts with 0 stack, maximum of 3 stacks. Gains 1 stack when the affected target takes action. When the affected target uses a skill, it triggers the corresponding effect based on the current number of stacks (if already at the max stacks before action, the skill will be triggered at maximum stacks again). 1 stack: Clears itself buffs. 2 stacks: Dispels itself Rebirth effect. 3 stacks: After using a skill, reduces HP to 1.
  - **Ⅱ** at `+7` — Sword Shadow EngravingⅡ (时宇+7)
    All Attack, deals 280% S-ATK damage to all targets. First, clears [Sword Shadow Engraving] from all enemies, then applies [Sword Shadow Engraving] with an initial stack of 0 to all enemies. Finally, recovers 100 Accumulator. Sword Shadow Engraving: Starts with 0 stack, maximum of 3 stacks. Gains 1 stack when the affected target takes action. When the affected target uses a skill, it triggers the corresponding effect based on the current number of stacks (if already at the max stacks before action, the skill will be triggered at maximum stacks again). 1 stack: Clears itself buffs, and prevents critical hits for 2 rounds (takes priority over guaranteed critical hits). 2 stacks: Dispels itself Rebirth effect. 3 stacks: After using a skill, reduces HP to 1.
  - **Ⅴ** at `Awaken` — Sword Shadow EngravingⅢ (时宇+觉醒1)
    All Attack, deals 300% S-ATK damage to all targets. First, clears [Sword Shadow Engraving] from all enemies, then applies [Sword Shadow Engraving] with an initial stack of 0 to all enemies. Finally, recovers 100 Accumulator. Sword Shadow Engraving: Starts with 0 stack, maximum of 3 stacks. Gains 1 stack when the affected target takes action. When the affected target uses a skill, it triggers the corresponding effect based on the current number of stacks (if already at the max stacks before action, the skill will be triggered at maximum stacks again). 1 stack: Clears itself buffs, and prevents critical hits for 2 rounds (takes priority over guaranteed critical hits). 2 stacks: Dispels itself Rebirth effect, and the control effects can not be removed for 2 rounds. 3 stacks: After using a skill, reduces HP to 1.
  - **6** at `Second Awaken` — Sword Shadow EngravingIV (时宇+觉醒2)
    All Attack, deals 320% S-ATK damage to all targets. Upon first use, removes all enemy invisibility and Dark Conceal effects. First, clears [Sword Shadow Engraving] from all enemies, then applies [Sword Shadow Engraving] with an initial stack of 0 to all enemies. Finally, recovers 100 Accumulator. Sword Shadow Engraving: Starts with 0 stack, maximum of 3 stacks. Gains 1 stack when the affected target takes action. When the affected target uses a skill, it triggers the corresponding effect based on the current number of stacks (if already at the max stacks before action, the skill will be triggered at maximum stacks again). 1 stack: Clears itself buffs, and prevents critical hits for 2 rounds (takes priority over guaranteed critical hits). 2 stacks: Dispels itself Rebirth effect, and the control effects can not be removed for 2 rounds. 3 stacks: After using a skill, reduces HP to 1 point and disables itself's active skill effects for 2 rounds.

**Slot 2 — Shadow Trace Bloom** (id 1805, unlocks at `+0`)
  - **Ⅰ** at `+0` — Shadow Trace BloomⅠ (时宇+0)
    (Takes effect at the start of battle) Depending on the number of Sword Shadow Engraving stacks removed from enemies, additional effects are applied to targets with different stacks. 0 Stack: Clears the target's Accumulator.
  - **Ⅱ** at `+7` — Shadow Trace BloomⅡ (时宇+7)
    (Takes effect at the start of battle) Depending on the number of Sword Shadow Engraving stacks removed from enemies, additional effects are applied to targets with different stacks. 0 Stack: Clears the target's Accumulator. 1 Stack: Cannot recover HP for 2 rounds.
  - **Ⅲ** at `+T` — Shadow Trace BloomⅢ (时宇+16)
    (Takes effect at the start of battle) Depending on the number of Sword Shadow Engraving stacks removed from enemies, additional effects are applied to targets with different stacks. 0 Stack: Clears the target's Accumulator. 1 Stack: Cannot recover HP for 2 rounds. 2 stacks: Cannot trigger Lieutenant skills for 2 rounds.
  - **Ⅳ** at `+T1` — Shadow Trace BloomIV (时宇+17)
    (Takes effect at the start of battle) Depending on the number of Sword Shadow Engraving stacks removed from enemies, additional effects are applied to targets with different stacks. 0 Stack: Clears the target's Accumulator. 1 Stack: Cannot recover HP for 2 rounds. 2 stacks: Cannot trigger Lieutenant skills for 2 rounds. 3 Stacks: Cannot be revived after death (including Rebirth).

**Slot 3 — Radiant Covenant** (id 1806, unlocks at `+5`)
  - **Ⅰ** at `+5` — Radiant CovenantⅠ (时宇+0)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +60% S-ATK: +60% DMG Bonus (Absolute Value): +15% Crit ATK (Absolute Value) +15%
  - **Ⅱ** at `+11` — Radiant CovenantⅡ (时宇+7)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +90% S-ATK: +90% DMG Bonus (Absolute Value): +20% Crit ATK (Absolute Value) +20%
  - **Ⅲ** at `+15` — Radiant CovenantⅢ (时宇+16)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +120% S-ATK: +120% DMG Bonus (Absolute Value): +25% Crit ATK (Absolute Value) +25%
  - **Ⅳ** at `+T2` — Radiant CovenantIV (时宇+17)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +150% S-ATK: +150% DMG Bonus (Absolute Value): +30% Crit ATK (Absolute Value) +30%

**Slot 4 — Bold Edge** (id 1807, unlocks at `+0`)
  - **Ⅰ** at `+0` — Bold EdgeⅠ (时宇+0)
    (Takes effect at the start of battle) Upon death, clears all stacks of [Sword Shadow Engraving] from all enemies (this clearing will not trigger the additional effects of the skill Shadow Trace Bloom). At the start of battle, gains Eye of True Sight for 99 rounds.
  - **Ⅱ** at `+7` — Bold EdgeⅡ (时宇+7)
    (Takes effect at the start of battle) Upon death, clears all stacks of [Sword Shadow Engraving] from all enemies (this clearing will not trigger the additional effects of the skill [Shadow Trace Bloom]). At the start of battle, gains Eye of True Sight for 99 rounds. All allies' damage is increased by 20%, and the damage dealt ignores 40% of the enemy's defense.
  - **Ⅲ** at `+T1` — Bold EdgeⅢ (时宇+16)
    (Takes effect at the start of battle) Upon death, clears all stacks of [Sword Shadow Engraving] from all enemies (this clearing will not trigger the additional effects of the skill [Shadow Trace Bloom]). At the start of battle, gains Eye of True Sight for 99 rounds. At the start of battle, applies an initial 0 stack of [Sword Shadow Engraving] to all enemies. All allies' damage is increased by 30%, and the damage dealt ignores 50% of the enemy's defense.
  - **Ⅳ** at `+T4` — Bold EdgeIV (时宇+17)
    (Takes effect at the start of battle) Upon death, it does not remove all stacks of [Sword Shadow Engraving] from all enemies. At the start of battle, gains Eye of True Sight for 99 rounds. At the start of battle, applies an initial 0 stack of [Sword Shadow Engraving] to all enemies. All allies' damage is increased by 40%, and the damage dealt ignores 60% of the enemy's defense.

### Augment cost (per step)
- `+1` — 5× Galaxy Heart · 100,000 money
- `+2` — 10× Galaxy Heart · 200,000 money
- `+3` — 21× Galaxy Heart · 300,000 money
- `+4` — 28× Galaxy Heart · 500,000 money
- `+5` — 35× Galaxy Heart · 800,000 money
- `+6` — 42× Galaxy Heart · 10× Pandora Power Core
- `+7` — 49× Galaxy Heart · 50× Pandora Power Core
- `+8` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Galaxy Heart · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Galaxy Heart · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Galaxy Heart · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 40× Galaxy Heart · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 80× Galaxy Heart · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 160× Galaxy Heart · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 320× Galaxy Heart · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Galaxy Heart · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Galaxy Heart · 100× Alien Essence · 100× Transcendence Core

---

## 586 · Altrius 阿尔特瑞斯
**Role** Flagship · **Attack** physical · **Generation** latest
**Ratings** Damage 10/10 · Defence 10/10 · Assist 8/10

### Skill panels
**Slot 1 — Supernova Blast** (id 1829, unlocks at `+0`)
  - **Ⅰ** at `+0` — Supernova BlastⅠ (阿尔特瑞斯+0)
    All attack, deals 300% S-ATK damage to all enemies, applies [Vulnerable Mark] to all enemies for 2 rounds, then performs [Pursuit]. Lastly, you recover 100 Accumulator. [Vulnerable Mark]: When attacked, takes additional damage equal to 5% of current HP. [Pursuit]: Each pursuit deals 260% S-ATK damage to 1 random enemy. Starts with 3 pursuits. Each 40 Accumulator spent during skill use grants 1 additional pursuit, up to a maximum of 5 additional pursuits.
  - **Ⅱ** at `+6` — Supernova BlastⅡ (阿尔特瑞斯+6)
    All attack, absorbs 30% of all enemies' S-DEF and DEF for 2 rounds, deals 320% S-ATK damage to all enemies, applies [Vulnerable Mark] to all enemies for 2 rounds, then performs [Pursuit]. Lastly, you recover 100 Accumulator. [Vulnerable Mark]: When attacked, takes additional damage equal to 10% of current HP. [Pursuit]: Each pursuit deals 280% S-ATK damage to 1 random enemy. Starts with 3 pursuits. Each 40 Accumulator spent during skill use grants 1 additional pursuit, up to a maximum of 6 additional pursuits.
  - **Ⅲ** at `+10` — Supernova BlastⅢ (阿尔特瑞斯+10)
    All attack, absorbs 30% of all enemies' S-DEF and DEF for 2 rounds, absorbs 50% of all enemies' Accumulator, deals 340% S-ATK damage to all enemies, and applies [Vulnerable Mark] to all enemies for 2 rounds, then performs [Pursuit]. Lastly, you recover 150 Accumulator. [Vulnerable Mark]: When attacked, takes additional damage equal to 15% of current HP. [Pursuit]: Each pursuit deals 320% S-ATK damage to 1 random enemy. Starts with 3 pursuits. Each 40 Accumulator spent during skill use grants 1 additional pursuit, up to a maximum of 8 additional pursuits.
  - **Ⅳ** at `+T3` — Supernova BlastIV (阿尔特瑞斯+19)
    All attack, first removes buffs from all targets, absorbs 30% of all enemies' S-DEF and DEF for 2 rounds, absorbs 50% of all enemies' Accumulator, deals 360% S-ATK damage to all enemies, and applies [Vulnerable Mark] to all enemies for 2 rounds, then performs [Pursuit]. Lastly, you recover 200 Accumulator. [Vulnerable Mark]: When attacked, takes additional damage equal to 20% of current HP. [Pursuit]: Each pursuit deals 360% S-ATK damage to 1 random enemy. Starts with 3 pursuits. Each 40 Accumulator spent during skill use grants 1 additional pursuit, up to a maximum of 10 additional pursuits.

**Slot 2 — Battle Frenzy** (id 1830, unlocks at `+2`)
  - **Ⅰ** at `+2` — Battle FrenzyⅠ (阿尔特瑞斯+2)
    (Takes effect at the start of battle) Altrius is immune to damage and abnormal statuses caused by enemy flagship (Not immune to subsequent damage) and Accumulator Reduction effects. Additionally, at the start of battle, gains an extra 100 Accumulator.
  - **Ⅱ** at `+9` — Battle FrenzyⅡ (阿尔特瑞斯+9)
    (Takes effect at the start of battle) Altrius is immune to damage and abnormal statuses caused by enemy flagship (Not immune to subsequent damage) and Accumulator Reduction effects. Additionally, at the start of battle, gains an extra 100 Accumulator. The skill's damage increases by 0.3% for each Accumulator above 100 spent during skill cast (up to a maximum of 120%)
  - **Ⅲ** at `+T` — Battle FrenzyⅢ (阿尔特瑞斯+16)
    (Takes effect at the start of battle) Altrius is immune to damage and abnormal statuses caused by enemy flagship (Not immune to subsequent damage) and Accumulator Reduction effects. Additionally, at the start of battle, gains an extra 200 Accumulator. The skill's damage increases by 0.5% for each Accumulator above 100 spent during skill cast (up to a maximum of 200%) During the battle, whenever any ships other than itself uses a skill, Altrius gains 20% of the consumed Accumulator, up to a maximum of 200 Accumulator per round.
  - **Ⅳ** at `Awaken` — Battle FrenzyIV (阿尔特瑞斯 觉醒+1)
    (Takes effect at the start of battle) Altrius is immune to damage and abnormal statuses caused by enemy flagship (Not immune to subsequent damage) and Accumulator Reduction effects. Additionally, at the start of battle, gains an extra 300 Accumulator. The skill's damage increases by 0.7% for each Accumulator above 100 spent during skill cast. During the battle, whenever any ships other than itself uses a skill, Altrius gains 40% of the consumed Accumulator, up to a maximum of 300 Accumulator per round. At the start of battle and when casting a skill, all allies gain [Battle Frenzy]. [Battle Frenzy]: When the skill is cast, it will be considered to result in a kill, triggering the corresponding effect, which is removed after being triggered once. (Effects that trigger after a kill will activate unconditionally. If the skill effect depends on the number of kills, it is considered to have killed one enemy. This effect does not apply to "follow-up attack to the unkilled target")

**Slot 3 — Empire Glory** (id 1831, unlocks at `+4`)
  - **Ⅰ** at `+4` — Empire GloryⅠ (阿尔特瑞斯+4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +60% S-ATK: +60% DMG Bonus (Absolute Value): +15% Crit ATK (Absolute Value) +15%
  - **Ⅱ** at `+10` — Empire GloryⅡ (阿尔特瑞斯+10)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +90% S-ATK: +90% DMG Bonus (Absolute Value): +20% Crit ATK (Absolute Value) +20%
  - **Ⅲ** at `+14` — Empire GloryⅢ (阿尔特瑞斯+14)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +120% S-ATK: +120% DMG Bonus (Absolute Value): +25% Crit ATK (Absolute Value) +25%
  - **Ⅳ** at `+T2` — Empire GloryIV (阿尔特瑞斯+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +150% S-ATK: +150% DMG Bonus (Absolute Value): +30% Crit ATK (Absolute Value) +30%

**Slot 4 — Interstellar Destruction** (id 1832, unlocks at `+3`)
  - **Ⅰ** at `+3` — Interstellar DestructionⅠ (阿尔特瑞斯+3)
    (Takes effect at the start of battle) When using a skill, gains Eye of True Sight for 99 rounds.
  - **Ⅱ** at `+13` — Interstellar DestructionⅡ (阿尔特瑞斯+13)
    (Takes effect at the start of battle) When using a skill, gains Eye of True Sight for 99 rounds. When using a skill, causes all enemies to enter Overload. Casting a skill in Overload consumes 20% more Accumulato for 2 rounds.
  - **Ⅲ** at `+T4` — Interstellar DestructionⅢ (阿尔特瑞斯+20)
    (Takes effect at the start of battle) When using a skill, gains Eye of True Sight for 99 rounds. When using a skill, causes all enemies to enter Overload. Casting a skill in Overload consumes 50% more Accumulato for 2 rounds. Altrius gains additional effects based on the number of skill uses in battle (if revived after death, the count resets): First skill cast: Skill attacks always critical hit and ignore 60% of the enemy's DEF and S-DEF. Second skill cast: Skill attacks comes with Hunter Focus. Third skill cast: Ignores effects that grant immunity to lethal damage and block lethal damage, except for Starcore Essence.
  - **Ⅳ** at `Second Awaken` — Interstellar DestructionIV (阿尔特瑞斯 觉醒+2)
    (Takes effect at the start of battle) When using a skill, gains Eye of True Sight for 99 rounds. When using a skill, causes all enemies to enter Overload. Casting a skill in Overload consumes 80% more Accumulato for 2 rounds. When using a skill, converts damage reduction and Crit ATK RED exceeding 200% into damage increase and Crit ATK at a 100% ratio, up to a maximum of 100%, lasting for 2 rounds. When using a skill, has a 20% chance that the skill will not consume Accumulator. Altrius gains additional effects based on the number of skill uses in battle (if revived after death, the count is retained): First skill cast: Skills always critical hit and ignore 60% of the enemy's DEF and S-DEF. Second skill cast: Skill attacks comes with Hunter Focus. Third skill cast: Ignores effects that grant immunity to lethal damage and block lethal damage, except for Starcore Essence. Fourth skill cast: Prevents all enemies from reviving or being reborn after death (including revivals and rebirths unaffected by revival prohibition) until the battle ends.

### Augment cost (per step)
- `+1` — 5× Galaxy Heart · 100,000 money
- `+2` — 10× Galaxy Heart · 200,000 money
- `+3` — 21× Galaxy Heart · 300,000 money
- `+4` — 28× Galaxy Heart · 500,000 money
- `+5` — 35× Galaxy Heart · 800,000 money
- `+6` — 42× Galaxy Heart · 10× Pandora Power Core
- `+7` — 49× Galaxy Heart · 50× Pandora Power Core
- `+8` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Galaxy Heart · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Galaxy Heart · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Galaxy Heart · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 40× Galaxy Heart · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 80× Galaxy Heart · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 160× Galaxy Heart · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 320× Galaxy Heart · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Galaxy Heart · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Galaxy Heart · 100× Alien Essence · 100× Transcendence Core

---

## 601 · Domina Hayley 多米娜·海伊莉
**Role** Flagship · **Attack** physical · **Generation** latest
**Ratings** Damage 10/10 · Defence 10/10 · Assist 8/10

### Skill panels
**Slot 1 — Laser Strike** (id 1878, unlocks at `+0`)
  - **Ⅰ** at `+0` — Laser StrikeⅠ (多米娜·海伊莉+0)
    Cross Attack, then deals 360% S-ATK damage to targets, increasing self Crit Rate and Penetration by 50% (absolute value). Grants all allies <Tactical Deployment> for 2 rounds. Lastly, recovers 100 Accumulator. <Tactical Deployment>: Before allies under this effect act, recovers 100 Accumulator, then proceeds with the follow-up actions.
  - **Ⅱ** at `+6` — Laser StrikeⅡ (多米娜·海伊莉+3)
    Cross Attack, then deals 380% S-ATK damage to targets, increasing self Crit Rate and Penetration by 100% (absolute value). Grants all allies <Tactical Deployment> for 2 rounds. Lastly, recovers 100 Accumulator. <Tactical Deployment>: Before allies under this effect act, recovers 100 Accumulator, then proceeds with the follow-up actions.
  - **Ⅲ** at `+10` — Laser StrikeⅢ (多米娜·海伊莉+6)
    Cross Attack, plunders 50% of the target's DEF and S-DEF by 50% for 2 rounds, then deals 400% S-ATK damage to targets, increasing self Crit Rate and Penetration by 100% (absolute value). Grants all allies <Tactical Deployment> for 2 rounds. Lastly, recovers 100 Accumulator. <Tactical Deployment>: Before allies under this effect act, recovers 100 Accumulator, then proceeds with the follow-up actions.
  - **Ⅳ** at `+15` — Laser StrikeIV (多米娜·海伊莉+10)
    Cross Attack, first removes the target's buffs, plunders 50% of the target's DEF and S-DEF by 50% for 2 rounds, then deals 420% S-ATK damage to targets, all allies gain a shield that blocks 1 attack, lasting 2 rounds.Increasing self Crit Rate and Penetration by 150% (absolute value). Grants all allies <Tactical Deployment> for 2 rounds. Lastly, recovers 100 Accumulator. <Tactical Deployment>: Before allies under this effect act, recovers 100 Accumulator, then proceeds with the follow-up actions.

**Slot 2 — Tactical Deployment** (id 1879, unlocks at `+3`)
  - **Ⅰ** at `+3` — Tactical DeploymentⅠ (多米娜·海伊莉+3)
    (Takes effect at the start of battle) At the start of battle, applies [Tactical Deployment] to all allies, lasting 2 rounds.
  - **Ⅱ** at `+T` — Tactical DeploymentⅡ (多米娜·海伊莉+16)
    (Takes effect at the start of battle) At the start of battle, applies [Tactical Deployment] to all allies for 2 rounds. Allies with [Tactical Deployment] will gain additional effects when using skills based on the types of buffs or debuffs the ship has. If self is in any state of Shield, Invisible, or Dark Conceal, when using skills, gains Eye of True Sight for 99 rounds. If self is in any state of attack power change (increase or decrease), defense power change, or damage dealt change, when using skills, increases own S-ATK and S-DEF by 100%, and damage dealt by 60%.
  - **Ⅲ** at `+T3` — Tactical DeploymentⅢ (多米娜·海伊莉+19)
    (Takes effect at the start of battle) At the start of battle, applies [Tactical Deployment] to all allies for 2 rounds. Self gains 2 round of invisibility and will not lose invisibility for as long as there is another ally alive (can be seen by Eye of True Sight). Allies with [Tactical Deployment] will gain additional effects when using skills based on the types of buffs or debuffs the ship has. If self is in any state of Shield, Invisible, or Dark Conceal, when using skills, gains Eye of True Sight for 99 rounds. If self is in any state of attack power change (increase or decrease), defense power change, or damage dealt change, when using skills, increases own S-ATK and S-DEF by 100%, and damage dealt by 60%. Self's skill attacks have a 75% chance to gains Hunter Focus.
  - **Ⅳ** at `Second Awaken` — Tactical DeploymentIV (多米娜·海伊莉+觉醒2)
    (Takes effect at the start of battle) At the start of battle, applies [Tactical Deployment] to all allies for 2 rounds. Self gains 2 round of invisibility and will not lose invisibility for as long as there is another ally alive (can be seen by Eye of True Sight). Allies with [Tactical Deployment] will gain additional effects when using skills based on the types of buffs or debuffs the ship has. If self is in any state of Shield, Invisible, or Dark Conceal, when using skills, gains Eye of True Sight for 99 rounds. Before casting a skill, first removes all enemies' Invisible and Dark Conceal states, then proceeds with the follow-up actions. If self is in any state of attack power change (increase or decrease), defense power change, or damage dealt change, when using skills, clean own abnormal statuses and increases own S-ATK and S-DEF by 120%, and damage dealt by 80%. Self's skill attacks have a 75% chance to gains Hunter Focus, and after [Laser Strike] completes its action, there is a 50% chance to trigger another round of [Laser Strike] S-ATK. (S-ATKs triggered by this effect cannot trigger this effect again)

**Slot 3 — Rapid Deployment** (id 1880, unlocks at `+4`)
  - **Ⅰ** at `+4` — Rapid DeploymentⅠ (多米娜·海伊莉+4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +60% S-ATK: +60% DMG Bonus (Absolute Value): +15% Crit ATK (Absolute Value) +15%
  - **Ⅱ** at `+11` — Rapid DeploymentⅡ (多米娜·海伊莉+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +90% S-ATK: +90% DMG Bonus (Absolute Value): +20% Crit ATK (Absolute Value) +20%
  - **Ⅲ** at `+14` — Rapid DeploymentⅢ (多米娜·海伊莉+14)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +120% S-ATK: +120% DMG Bonus (Absolute Value): +25% Crit ATK (Absolute Value) +25%
  - **Ⅳ** at `+T2` — Rapid DeploymentIV (多米娜·海伊莉+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +150% S-ATK: +150% DMG Bonus (Absolute Value): +30% Crit ATK (Absolute Value) +30%

**Slot 4 — P50 Electromagnetic Blast** (id 1881, unlocks at `+3`)
  - **Ⅰ** at `+3` — P50 Electromagnetic BlastⅠ (多米娜·海伊莉+3)
    (Takes effect at the start of battle) During the battle, Domina activates her signature weapon - the P50 Electromagnetic Cannon. During the brief charging process, she focuses on the enemy formation and dynamics to ensure the optimal firing moment. The cannon starts at 0 stacks and can have a maximum of 4 stacks. Each time the skill is cast, it gains 1 stack. Upon reaching 4 stacks, if she is not in a state of inability to act, she immediately releases the [P50 Electromagnetic Blast], which will reset the stacks and needs recharging again. [P50 Electromagnetic Blast]: Vertical Attack, attacks the target hit 3 times, each attack dealing 200% S-ATK damage, and depleted targets' Accumulator.
  - **Ⅱ** at `+T1` — P50 Electromagnetic BlastⅡ (多米娜·海伊莉+17)
    (Takes effect at the start of battle) During the battle, Domina activates her signature weapon - the P50 Electromagnetic Cannon. During the brief charging process, she focuses on the enemy formation and dynamics to ensure the optimal firing moment. The cannon starts at 0 stacks and can have a maximum of 4 stacks. Each time the skill is cast, it gains 1 stack. Upon reaching 4 stacks, if she is not in a state of inability to act, she immediately releases the [P50 Electromagnetic Blast], which will reset the stacks and needs recharging again. [P50 Electromagnetic Blast]: Vertical Attack, attacks the target hit 3 times, each attack dealing 200% S-ATK damage, and depleted targets' Accumulator. After casting this skill, her damage dealt is increased by 100%, stacking up to 300%.
  - **Ⅲ** at `+T4` — P50 Electromagnetic BlastⅢ (多米娜·海伊莉+20)
    (Takes effect at the start of battle) During the battle, Domina activates her signature weapon - the P50 Electromagnetic Cannon. During the brief charging process, she focuses on the enemy formation and dynamics to ensure the optimal firing moment. The cannon starts at 0 stacks and can have a maximum of 4 stacks. Each time the skill is cast, it gains 1 stack. Upon reaching 4 stacks, if she is not in a state of inability to act, she immediately releases the [P50 Electromagnetic Blast], which will reset the stacks and needs recharging again. [P50 Electromagnetic Blast]: Vertical Attack, attacks the target hit 3 times, each attack dealing 200% S-ATK damage, and depleted targets' Accumulator. After casting this skill, her damage dealt is increased by 100%, stacking up to 300%. When she takes lethal damage, all stacks are cleared to block the lethal damage, this effect can trigger up to 3 times per battle.
  - **Ⅳ** at `Awaken` — P50 Electromagnetic BlastIV (多米娜·海伊莉+觉醒1)
    (Takes effect at the start of battle) During the battle, Domina activates her signature weapon - the P50 Electromagnetic Cannon. During the brief charging process, she focuses on the enemy formation and dynamics to ensure the optimal firing moment. The cannon starts at 0 stacks and can have a maximum of 4 stacks. Each time the skill is cast, it gains 1 stack. Upon reaching 4 stacks, if she is not in a state of inability to act, she immediately releases the [P50 Electromagnetic Blast], which will reset the stacks and needs recharging again. [P50 Electromagnetic Blast]: Vertical Attack, attacks the target hit 3 times, each attack dealing 250% S-ATK damage, and depleted targets' Accumulator. After casting this skill, her damage dealt is increased by 100%, stacking up to 300%. If the target's HP is below 50% after using this skill, she will immediately perform a [Laser Strike] skill attack. She gains 1 stack of charge each time an ally dies. When she takes lethal damage (including ignores immunity to lethal attacks and instant destruction), all stacks are cleared to block the lethal damage, this effect can trigger up to 3 times per battle.

### Augment cost (per step)
- `+1` — 5× Galaxy Heart · 100,000 money
- `+2` — 10× Galaxy Heart · 200,000 money
- `+3` — 21× Galaxy Heart · 300,000 money
- `+4` — 28× Galaxy Heart · 500,000 money
- `+5` — 35× Galaxy Heart · 800,000 money
- `+6` — 42× Galaxy Heart · 10× Pandora Power Core
- `+7` — 49× Galaxy Heart · 50× Pandora Power Core
- `+8` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Galaxy Heart · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Galaxy Heart · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Galaxy Heart · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 40× Galaxy Heart · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 80× Galaxy Heart · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 160× Galaxy Heart · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 320× Galaxy Heart · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Galaxy Heart · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Galaxy Heart · 100× Alien Essence · 100× Transcendence Core

---

## 611 · Aiolia 艾奥里亚
**Role** Flagship · **Attack** physical · **Generation** latest
**Ratings** Damage 10/10 · Defence 8/10 · Assist 10/10

### Skill panels
**Slot 1 — Starblade Judgement** (id 1913, unlocks at `+0`)
  - **Ⅰ** at `+0` — Starblade JudgementⅠ (艾奥里亚+0)
    All Attack, deals 260% S-ATK damage to all targets. Grants self [Will of Starblade], if already under the effect of [Will of Starblade], increases its stack by 1. Finally, recovers 100 Accumulator. [Will of Starblade]: Starts with 0 stack, maximum of 3 stacks. After gaining stacks of [Will of Starblade], triggers the corresponding effect based on the current number of stacks. When reaching the maximum stacks, all stacks are cleared after action, returning to 0. (Effects from each stack can be accumulated) 1 stack: Clears the target's Accumulator. 2 stacks: S-ATK attacks comes with Hunter Focus for 2 rounds. 3 stacks: S-ATK ignores Stasis and immunity to lethal attacks.
  - **Ⅱ** at `+6` — Starblade JudgementⅡ (艾奥里亚+2)
    All Attack, deals 280% S-ATK damage to all targets. Increases self Crit Rate by 150% and Crit ATK by 300% until the end of the battle. Grants self [Will of Starblade], if already under the effect of [Will of Starblade], increases its stack by 1. Finally, recovers 100 Accumulator. [Will of Starblade]: Starts with 0 stack, maximum of 3 stacks. After gaining stacks of [Will of Starblade], triggers the corresponding effect based on the current number of stacks. When reaching the maximum stacks, all stacks are cleared after action, returning to 0. (Effects from each stack can be accumulated) 1 stack: Clears the target's Accumulator. 2 stacks: S-ATK attacks comes with Hunter Focus for 2 rounds. 3 stacks: S-ATK ignores Stasis and immunity to lethal attacks.
  - **Ⅲ** at `+10` — Starblade JudgementⅢ (艾奥里亚+3)
    All Attack, first plunders 20% of all enemies' S-ATK and 50% Hit Rate for 2 rounds, then deals 300% S-ATK damage to all targets. Increases self Crit Rate by 150% and Crit ATK by 300% until the end of the battle. Grants self [Will of Starblade], if already under the effect of [Will of Starblade], increases its stack by 1. Finally, recovers 100 Accumulator. [Will of Starblade]: Starts with 0 stack, maximum of 3 stacks. After gaining stacks of [Will of Starblade], triggers the corresponding effect based on the current number of stacks. When reaching the maximum stacks, all stacks are cleared after action, returning to 0. (Effects from each stack can be accumulated) 1 stack: Clears the target's Accumulator. 2 stacks: S-ATK attacks comes with Hunter Focus for 2 rounds. 3 stacks: S-ATK ignores Stasis and immunity to lethal attacks.
  - **Ⅳ** at `+T3` — Starblade JudgementIV (艾奥里亚+6)
    All Attack, first removes the target's buffs, and plunders 20% of all enemies' S-ATK and 50% Hit Rate for 2 rounds, then deals 340% S-ATK damage to all targets. Increases self Crit Rate by 150% and Crit ATK by 300% until the end of the battle. Grants self [Will of Starblade], if already under the effect of [Will of Starblade], increases its stack by 1. Finally, recovers 100 Accumulator. [Will of Starblade]: Starts with 0 stack, maximum of 3 stacks. After gaining stacks of [Will of Starblade], triggers the corresponding effect based on the current number of stacks. When reaching the maximum stacks, all stacks are cleared after action, returning to 0. (Effects from each stack can be accumulated) 1 stack: Clears the target's Accumulator. 2 stacks: S-ATK attacks comes with Hunter Focus for 2 rounds. 3 stacks: S-ATK ignores Stasis and immunity to lethal attacks, and instantly kill a random enemy.

**Slot 2 — Will of Starblade** (id 1914, unlocks at `+2`)
  - **Ⅰ** at `+2` — Will of StarbladeⅠ (艾奥里亚+2)
    (Takes effect at the start of battle) When using a skill, gains Eye of True Sight for 2 rounds.
  - **Ⅱ** at `+9` — Will of StarbladeⅡ (艾奥里亚+9)
    (Takes effect at the start of battle) When using a skill, gains Eye of True Sight for 2 rounds. At the start of battle, immediately gains [Will of Starblade] with 0 initial stack.
  - **Ⅲ** at `+T` — Will of StarbladeⅢ (艾奥里亚+16)
    (Takes effect at the start of battle) When using a skill, gains Eye of True Sight for 2 rounds. At the start of battle, immediately gains [Will of Starblade] with 1 initial stack. S-ATK will apply additional effects based on the position of the target ship: [All Enemies]: Randomly attacks one enemy 3 additional times, each dealing 300% S-ATK damage and an additional 10,000,000 True Damage. [Front Row]: 100% chance to lock the enemies for 2 rounds. [Second Row]: After dealing damage, reduces the targets' HP to 1. [Third Row]: Removes Invisible and Dark Conceal states from the ships in this position.
  - **Ⅳ** at `Awaken` — Will of StarbladeIV (艾奥里亚觉醒+1)
    (Takes effect at the start of battle) When using a skill, gains Eye of True Sight for 2 rounds. At the start of battle, immediately gains [Will of Starblade] with 2 initial stacks. S-ATK will apply additional effects based on the position of the target ship: [All Enemies]: Randomly attacks one enemy 5 additional times, each dealing 340% S-ATK damage and an additional 20,000,000 True Damage. [Front Row]: 100% chance to lock the enemies for 2 rounds, ignoring targets' immunity and protection effects. [Second Row]: After dealing damage, reduces the targets' HP to 1, and enemies in the second row can only revive once after death. (including revivals and rebirths unaffected by revival prohibition) [Third Row]: Removes Invisible and Dark Conceal states from the ships in this position, and they cannot enter Dark Conceal by any means for 2 rounds.

**Slot 3 — Dawn of Empire** (id 1915, unlocks at `+4`)
  - **Ⅰ** at `+4` — Dawn of EmpireⅠ (艾奥里亚+4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +60% S-ATK: +60% DMG Bonus (Absolute Value): +15% Crit ATK (Absolute Value) +15%
  - **Ⅱ** at `+10` — Dawn of EmpireⅡ (艾奥里亚+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +90% S-ATK: +90% DMG Bonus (Absolute Value): +20% Crit ATK (Absolute Value) +20%
  - **Ⅲ** at `+14` — Dawn of EmpireⅢ (艾奥里亚+15)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +120% S-ATK: +120% DMG Bonus (Absolute Value): +25% Crit ATK (Absolute Value) +25%
  - **Ⅳ** at `+T2` — Dawn of EmpireIV (艾奥里亚+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +150% S-ATK: +150% DMG Bonus (Absolute Value): +30% Crit ATK (Absolute Value) +30%

**Slot 4 — Supernova・Blade Ignition** (id 1916, unlocks at `+3`)
  - **Ⅰ** at `+3` — Supernova・Blade IgnitionⅠ (艾奥里亚+3)
    (Takes effect at the start of battle) Own S-ATK ignores 75% of the enemy's DEF and S-DEF.
  - **Ⅱ** at `+13` — Supernova・Blade IgnitionⅡ (艾奥里亚+13)
    (Takes effect at the start of battle) Own S-ATK ignores 75% of the enemy's DEF and S-DEF. After [Will of Starblade] stacks are cleared, the initial stack count increases to 1.
  - **Ⅲ** at `+T4` — Supernova・Blade IgnitionⅢ (艾奥里亚+20)
    (Takes effect at the start of battle) Own S-ATK ignores 75% of the enemy's DEF and S-DEF. After [Will of Starblade] stacks are cleared, the initial stack count increases to 1, and at 3 stacks of [Will of Starblade], gain an additional effect: instant destruction effects ignore the target's immunity to instant destruction. At the start of battle, all allies gain [Blade Ignition] for 2 rounds. [Blade Ignition]: When the skill is cast, if the owner skill includes [Slaughter Feast] and [Fatal Pursuit], an additional effect will be applied. (Effects provided by allied units or Potential Chips can still trigger this skill) [Slaughter Feast]: Grants self the Rebirth effect; upon death, reviving immediately upon death with 100% HP and Accumulator as at the start of the battle. (which isn't affected by forbidding revival effects.) [Fatal Pursuit]: Removes self's forbidding revival effects and revive limit effects.
  - **Ⅳ** at `Second Awaken` — Supernova・Blade IgnitionIV (艾奥里亚觉醒+2)
    (Takes effect at the start of battle) Own S-ATK ignores 75% of the enemy's DEF and S-DEF. After [Will of Starblade] stacks are cleared, the initial stack count increases to 1, and at 3 stacks of [Will of Starblade], gain an additional effect: instant destruction effects ignore the target's immunity to instant destruction, and self immediately takes an action. At the start of battle, all allies gain [Blade Ignition] for 2 rounds. [Blade Ignition]: When the skill is cast, if the owner skill includes [Slaughter Feast] and [Fatal Pursuit], an additional effect will be applied. (Effects provided by allied units or Potential Chips can still trigger this skill) [Slaughter Feast]: Gains [Dark Conceal], immune to attacks and skill effects for 1 round. Grants self the Rebirth effect; upon death, reviving immediately upon death with 100% HP and Accumulator as at the start of the battle. (which isn't affected by forbidding revival effects.) [Fatal Pursuit]: Removes self's forbidding revival effects and revive limit effects. If there are other members of the Supernova Blades Fleet (Ouros, Mu, Karon) in the team, they will unconditionally trigger the buff effect provided by [Slaughter Feast] under [Blade Ignition] at the start of battle. If Teda or Ulysses is present, they will unconditionally trigger the buff effect provided by [Fatal Pursuit] under [Blade Ignition] at the start of battle, lasting 2 rounds.

### Augment cost (per step)
- `+1` — 5× Galaxy Heart · 100,000 money
- `+2` — 10× Galaxy Heart · 200,000 money
- `+3` — 21× Galaxy Heart · 300,000 money
- `+4` — 28× Galaxy Heart · 500,000 money
- `+5` — 35× Galaxy Heart · 800,000 money
- `+6` — 42× Galaxy Heart · 10× Pandora Power Core
- `+7` — 49× Galaxy Heart · 50× Pandora Power Core
- `+8` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Galaxy Heart · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Galaxy Heart · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Galaxy Heart · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 40× Galaxy Heart · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 80× Galaxy Heart · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 160× Galaxy Heart · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 320× Galaxy Heart · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Galaxy Heart · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Galaxy Heart · 100× Alien Essence · 100× Transcendence Core

---

## 629 · Elowyn 爱洛温
**Role** Flagship · **Attack** physical · **Generation** latest
**Ratings** Damage 9/10 · Defence 8/10 · Assist 10/10

### Skill panels
**Slot 1 — Stellar Cannon Array** (id 1980, unlocks at `+0`)
  - **Ⅰ** at `+0` — Stellar Cannon ArrayⅠ (爱洛温+0)
    Cross Attack, first plunders 75% Accumulator and 50% S-ATK from targets, each attack dealing 280% S-ATK damage. Gains Eye of True Sight until the end of the BATTLE. Lastly, recovers 100 Accumulator.
  - **Ⅱ** at `+6` — Stellar Cannon ArrayⅡ (爱洛温+2)
    Cross Attack, first plunders 75% Accumulator and 50% S-ATK from targets, each attack dealing 300% S-ATK damage. After each skill cast, increases own Crit ATK by 100%, stacking up to 5 times and lasting until the end of the battle. Gains Eye of True Sight until the end of the BATTLE. Lastly, recovers 100 Accumulator.
  - **Ⅲ** at `+15` — Stellar Cannon ArrayⅢ (爱洛温+3)
    Cross Attack, first plunders 75% Accumulator and 50% S-ATK from targets, each attack dealing 320% S-ATK damage. After each skill cast, increases own Crit ATK by 100%, stacking up to 5 times and lasting until the end of the battle. If the target's HP is above 50%, this damage dealt is increased by 80%. Gains Eye of True Sight until the end of the BATTLE. Lastly, recovers 100 Accumulator.
  - **Ⅳ** at `+T3` — Stellar Cannon ArrayIV (爱洛温+6)
    Cross Attack, first plunders 75% Accumulator and 50% S-ATK from targets, each attack dealing 360% S-ATK damage. After each skill cast, increases own Crit ATK by 100%, stacking up to 5 times and lasting until the end of the battle. If the target's HP is above 50%, this damage dealt is increased by 80%. Gains Eye of True Sight until the end of the BATTLE, and own S-ATK can attack enemies in Dark Conceal. Lastly, recovers 100 Accumulator.

**Slot 2 — Quantum Phase** (id 1981, unlocks at `+2`)
  - **Ⅰ** at `+2` — Quantum PhaseⅠ (爱洛温+2)
    (Takes effect at the start of battle) S-ATK randomly attacks one enemy 5 additional times, each dealing 280% S-ATK damage.
  - **Ⅱ** at `+9` — Quantum PhaseⅡ (爱洛温+9)
    (Takes effect at the start of BATTLE) S-ATK randomly attacks one enemy 5 additional times, each dealing 300% S-ATK damage. After casting a skill, all allies recover an extra 50 Accumulator.
  - **Ⅲ** at `+T1` — Quantum PhaseⅢ (爱洛温+17)
    (Takes effect at the start of BATTLE) S-ATK randomly attacks one enemy 5 additional times, each dealing 320% S-ATK damage. After casting a skill, all allies recover an extra 50 Accumulator. The skill's damage increases by 0.5% for per Accumulator above 100 spent during skill cast (up to a maximum of 200%).
  - **Ⅳ** at `+T4` — Quantum PhaseIV (爱洛温+20)
    (Takes effect at the start of battle) S-ATK randomly attacks one enemy 10 additional times, each dealing 360% S-ATK damage and inflicting an extra 10,000,000 true damage. After casting a skill, all allies recover an extra 100 Accumulator. The skill's damage increases by 0.5% for per Accumulator above 100 spent during skill cast (up to a maximum of 200%). All allies' S-ATK ignores 80% of the target's S-DEF, and all allies' S-ATK ignores immunity to lethal attacks and effects that block lethal damage.

**Slot 3 — White Star Aura** (id 1982, unlocks at `+4`)
  - **Ⅰ** at `+4` — White Star AuraⅠ (爱洛温+4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +60% S-ATK: +60% DMG Bonus (Absolute Value): +15% Crit ATK (Absolute Value) +15%
  - **Ⅱ** at `+10` — White Star AuraⅡ (爱洛温+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +90% S-ATK: +90% DMG Bonus (Absolute Value): +20% Crit ATK (Absolute Value) +20%
  - **Ⅲ** at `+14` — White Star AuraⅢ (爱洛温+14)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +120% S-ATK: +120% DMG Bonus (Absolute Value): +25% Crit ATK (Absolute Value) +25%
  - **Ⅳ** at `+T2` — White Star AuraIV (爱洛温+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +150% S-ATK: +150% DMG Bonus (Absolute Value): +30% Crit ATK (Absolute Value) +30%

**Slot 4 — Supernova: Stellar Blessing** (id 1983, unlocks at `+3`)
  - **Ⅰ** at `+3` — Supernova: Stellar BlessingⅠ (爱洛温+3)
    (Takes effect at the start of BATTLE) When casting a skill, all allies damage dealt is increased by 60%, lasting until the end of BATTLE.
  - **Ⅱ** at `+T1` — Supernova: Stellar BlessingⅡ (爱洛温+16)
    (Takes effect at the start of BATTLE) When casting a skill, all allies damage dealt is increased by 60%, lasting until the end of BATTLE. When casting a skill, increases all allies' Crit ATK by 50%, lasting until the end of BATTLE, and her S-ATK is guaranteed to critically hit.
  - **Ⅲ** at `Awaken` — Supernova: Stellar BlessingⅢ (爱洛温+觉醒1)
    (Takes effect at the start of BATTLE) When casting a skill, all allies damage dealt is increased by 60%, lasting until the end of BATTLE. When casting a skill, increases all allies' Crit ATK by 50%, lasting until the end of BATTLE, and her S-ATK is guaranteed to critically hit. During battle preparation, if Elowyn is placed in the 1st row, she gains the [Shock] state; if placed in the 2nd or 3rd row, she gains the [Harmonic Field] state. Different states activate different skill effects. (Takes effect at the start of BATTLE and each time she triggers Rebirth or Revival) [Shock]: Before using S-ATK, removes the target's Rebirth effect. [Harmonic Field]: When an ally is affected by certain control effects (Freeze, Lock, Confuse, Petrify, Icebound, Entangle and Forbidding Skill Use), the effect is redirected to herself.
  - **Ⅳ** at `Second Awaken` — Supernova: Stellar BlessingIV (爱洛温+觉醒2)
    (Takes effect at the start of BATTLE) When casting a skill, all allies damage dealt is increased by 60%, lasting until the end of BATTLE. When casting a skill, increases all allies' Crit ATK by 50%, lasting until the end of BATTLE, and her S-ATK is guaranteed to critically hit. During battle preparation, if Elowyn is placed in the 1st row, she gains the [Shock] state; if placed in the 2nd or 3rd row, she gains the [Harmonic Field] state. Different states activate different skill effects. (Takes effect at the start of BATTLE and each time she triggers Rebirth or Revival) [Shock]: Before using S-ATK, removes the target's Rebirth effect. At the start of battle, acts immediately once. (Immediate action does not trigger upon revival) [Harmonic Field]: When an ally is affected by certain control effects (Freeze, Lock, Confuse, Petrify, Icebound, Entangle and Forbidding Skill Use), the effect is redirected to herself. Gains a Directional Shield for 2 rounds; during this period, after being attacked, the shield is removed when the next ally acts. If there are other members of the Supernova Blades Fleet (Ouros, Mu, Karon, Teda, Ulysses) in the team, each time they cast a skill, enemies Invisible and Dark Conceal states are removed for 2 rounds. (If she is defeated, this effect disappears; takes effect at the start of battle and each time revived or reborn.)

### Augment cost (per step)
- `+1` — 5× Galaxy Heart · 100,000 money
- `+2` — 10× Galaxy Heart · 200,000 money
- `+3` — 21× Galaxy Heart · 300,000 money
- `+4` — 28× Galaxy Heart · 500,000 money
- `+5` — 35× Galaxy Heart · 800,000 money
- `+6` — 42× Galaxy Heart · 10× Pandora Power Core
- `+7` — 49× Galaxy Heart · 50× Pandora Power Core
- `+8` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Galaxy Heart · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Galaxy Heart · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Galaxy Heart · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 40× Galaxy Heart · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 80× Galaxy Heart · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 160× Galaxy Heart · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 320× Galaxy Heart · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Galaxy Heart · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Galaxy Heart · 100× Alien Essence · 100× Transcendence Core

---

## 638 · E E
**Role** Flagship · **Attack** physical · **Generation** latest
**Ratings** Damage 10/10 · Defence 8/10 · Assist 9/10

### Skill panels
**Slot 1 — Silent Verdict** (id 2009, unlocks at `+0`)
  - **Ⅰ** at `+0` — Silent VerdictⅠ (E+0)
    All Attack, plunders 30% S-DEF and DEF from all Enemies for 2 rounds, plunders 50% Accumulator from all Enemies, deals 280% S-ATK to all Enemies, and finally recovers 100 Accumulator. [Pursuit]: Each pursuit deals 280% S-ATK to a random Enemy among all Enemies. Starts with 3 pursuits. For every 40 Accumulator consumed when casting the skill, gains 1 additional pursuit, up to a maximum of 5 additional pursuits.
  - **Ⅱ** at `+6` — Silent VerdictⅡ (E+6)
    All attack, first clears all buffs from the target, plunders 30% S-DEF and DEF from all Enemies for 2 rounds, plunders 50% Accumulator from all Enemies, deals 300% S-ATK to all Enemies, and finally recovers 100 Accumulator. [Pursuit]: Each pursuit deals 300% S-ATK to a random Enemy among all Enemies. Starts with 3 pursuits. For every 40 Accumulator consumed when casting the skill, gains 1 additional pursuit, up to a maximum of 6 additional pursuits.
  - **Ⅲ** at `+10` — Silent VerdictⅢ (E+10)
    All attack, first clears all buffs from the target, plunders 30% S-DEF and DEF from all Enemies for 2 rounds, plunders 50% Accumulator from all Enemies, deals 320% S-ATK to all Enemies, and gains Eye of True Sight for 99 rounds.Finally recovers 100 Accumulator. [Pursuit]: Each pursuit deals 320% S-ATK to a random Enemy among all Enemies. Starts with 3 pursuits. For every 40 Accumulator consumed when casting the skill, gains 1 additional pursuit, up to a maximum of 8 additional pursuits.
  - **Ⅳ** at `+T2` — Silent VerdictIV (E+15)
    All attack, first clears all buffs from the target, plunders 30% S-DEF and DEF from all Enemies for 2 rounds, plunders 50% Accumulator from all Enemies, deals 360% S-ATK to all Enemies, and gains Eye of True Sight for 99 rounds. After each skill cast, increases own damage dealt and S-ATK damage by 30%, stacking up to 5 times, lasting until the end of the battle. S-ATK always critical hit. Finally recovers 200 Accumulator. [Pursuit]: Each pursuit deals 360% S-ATK to a random Enemy among all Enemies. Starts with 3 pursuits. For every 40 Accumulator consumed when casting the skill, gains 1 additional pursuit, up to a maximum of 10 additional pursuits.

**Slot 2 — Awakened Mission** (id 2010, unlocks at `+2`)
  - **Ⅰ** at `+2` — Awakened MissionⅠ (E+2)
    (Takes effect at the start of battle) E is immune to damage and abnormal statuses caused by enemy flagship (except for subsequent damage) and Accumulator Reduction effects. Additionally, at the start of battle, gains an extra 100 Accumulator.
  - **Ⅱ** at `+15` — Awakened MissionⅡ (E+15)
    (Takes effect at the start of battle) E is immune to damage and abnormal statuses caused by enemy flagship (except for subsequent damage) and Accumulator Reduction effects. Additionally, at the start of battle, gains an extra 100 Accumulator. When casting a skill, E first gains Accumulator equal to 50% of the total current Accumulator of all allies (excluding itself), up to a maximum of 200 Accumulator gained through this effect.
  - **Ⅲ** at `+T3` — Awakened MissionⅢ (E+19)
    (Takes effect at the start of battle) E is immune to damage and abnormal statuses caused by enemy flagship (except for subsequent damage) and Accumulator Reduction effects. Additionally, at the start of battle, gains an extra 200 Accumulator. When casting a skill, E first gains Accumulator equal to 50% of the total current Accumulator of all allies (excluding itself), up to a maximum of 300 Accumulator gained through this effect. When casting a skill, if current Accumulator is greater than 300, the S-ATK comes with Hunter Focus and ignores 75% of the enemy's DEF and S-DEF. If greater than 400, the S-ATK ignores effects that grant immunity to lethal damage and block lethal damage. If greater than 500, there is a 50% chance to refund 10% of the Accumulator spent for this skill.
  - **Ⅳ** at `Second Awaken` — Awakened MissionIV (E+觉醒+2)
    (Takes effect at the start of battle) E is immune to damage and abnormal statuses caused by enemy flagship (except for subsequent damage) and Accumulator Reduction effects. Additionally, at the start of battle, gains an extra 300 Accumulator. When casting a skill, E first gains Accumulator equal to 50% of the total current Accumulator of all allies (excluding itself), up to a maximum of 500 Accumulator gained through this effect. When casting a skill, if current Accumulator is greater than 300, the S-ATK comes with Hunter Focus and ignores 75% of the enemy's DEF and S-DEF. If greater than 400, the S-ATK ignores effects that grant immunity to lethal damage and block lethal damage. If greater than 500, there is a 50% chance to refund 30% of the Accumulator spent for this skill. At the start of battle and when casting a skill, all allies gain [Awakened Mission], which is removed after being triggered once. [Awakened Mission]: When the holder casts a skill to attack an enemy target, and this S-ATK is treated as "lethal damage that ignores immunity to lethal and instant destruction effects", forcibly triggering the target's "block effects that ignore immunity to lethal and instant destruction." (Applicable cases: blocking "block effects that ignore immunity to lethal and instant-kill." This lethal damage only forcibly triggers the block effect and does not actually deal damage.)

**Slot 3 — The Enforcer** (id 2011, unlocks at `+4`)
  - **Ⅰ** at `+4` — The EnforcerⅠ (E+4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +60% S-ATK: +60% DMG Bonus (Absolute Value): +15% Crit ATK (Absolute Value) +15%
  - **Ⅱ** at `+11` — The EnforcerⅡ (E+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +90% S-ATK: +90% DMG Bonus (Absolute Value): +20% Crit ATK (Absolute Value) +20%
  - **Ⅲ** at `+T` — The EnforcerⅢ (E+16)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +120% S-ATK: +120% DMG Bonus (Absolute Value): +25% Crit ATK (Absolute Value) +25%
  - **Ⅳ** at `+T2` — The EnforcerIV (E+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +150% S-ATK: +150% DMG Bonus (Absolute Value): +30% Crit ATK (Absolute Value) +30%

**Slot 4 — Shadow Strategy** (id 2012, unlocks at `+3`)
  - **Ⅰ** at `+3` — Shadow StrategyⅠ (E+3)
    (Takes effect at the start of battle) If your own formation's speed is higher than the enemy's speed in this battle, E will gain [Shadow Strategy]. (Speed is determined at the start of battle and is not affected by in-battle buffs or debuffs) [Shadow Strategy]: At the start of battle, self is not affected by enemy skills that take effect immediately at the start of battle.
  - **Ⅱ** at `+13` — Shadow StrategyⅡ (E+13)
    (Takes effect at the start of battle) The skill's damage increases by 0.4% for each Accumulator spent above 100 during skill cast. If your own formation's speed is higher than the enemy's speed in this battle, E will gain [Shadow Strategy]. (Speed is determined at the start of battle and is not affected by in-battle buffs or debuffs) [Shadow Strategy]: At the start of battle, self is not affected by enemy skills that take effect immediately at the start of battle.
  - **Ⅲ** at `+T4` — Shadow StrategyⅢ (E+20)
    (Takes effect at the start of battle) The skill's damage increases by 0.6% for each Accumulator spent above 100 during skill cast. When casting a skill, all Enemies can only revive once (including Rebirth) after being destroyed. Once the revival limit is reached, they cannot revive or Rebirth by any means until the end of the battle. If your own formation's speed is higher than the enemy's speed in this battle, E will gain [Shadow Strategy]. (Speed is determined at the start of battle and is not affected by in-battle buffs or debuffs) [Shadow Strategy]: At the start of battle, self is not affected by enemy skills that take effect immediately at the start of battle.
  - **Ⅳ** at `Awaken` — Shadow StrategyIV (E+觉醒+1)
    (Takes effect at the start of battle) The skill's damage increases by 0.8% for each Accumulator spent above 100 during skill cast. When casting a skill, all Enemies can only revive once (including Rebirth) after being destroyed. Once the revival limit is reached, they cannot revive or Rebirth by any means until the end of the battle. If your own formation's speed is higher than the enemy's speed in this battle, E will gain [Shadow Strategy]. (Speed is determined at the start of battle and is not affected by in-battle buffs or debuffs) [Shadow Strategy]: At the start of battle, self is not affected by enemy skills that take effect immediately at the start of battle. While E is alive, all Enemies' [Immediate Action], [Slaughter Feast] and [Fatal Pursuit] are disabled. (If E dies, this effect is removed)

### Augment cost (per step)
- `+1` — 5× Galaxy Heart · 100,000 money
- `+2` — 10× Galaxy Heart · 200,000 money
- `+3` — 21× Galaxy Heart · 300,000 money
- `+4` — 28× Galaxy Heart · 500,000 money
- `+5` — 35× Galaxy Heart · 800,000 money
- `+6` — 42× Galaxy Heart · 10× Pandora Power Core
- `+7` — 49× Galaxy Heart · 50× Pandora Power Core
- `+8` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Galaxy Heart · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Galaxy Heart · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Galaxy Heart · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 40× Galaxy Heart · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 80× Galaxy Heart · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 160× Galaxy Heart · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 320× Galaxy Heart · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Galaxy Heart · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Galaxy Heart · 100× Alien Essence · 100× Transcendence Core

---

## 641 · Jayce Lot - Silver Wolf 杰斯·洛特-银狼
**Role** Flagship · **Attack** physical · **Generation** latest
**Ratings** Damage 10/10 · Defence 7/10 · Assist 9/10

### Skill panels
**Slot 1 — Precision Strike** (id 2024, unlocks at `+0`)
  - **Ⅰ** at `+0` — Precision StrikeⅠ (杰斯·洛特SP+0)
    Single attack, attacks the target hit 3 times, plunders 20% of all enemy current HP, and each attack deals 400% skill damage to hit targets. Lastly, recovers 100 Accumulator.
  - **Ⅱ** at `+6` — Precision StrikeⅡ (杰斯·洛特SP+2)
    Single attack, attacks the target hit 4 times, additionally inflicts 10,000,000 true damage, first plunders 100% Accumulator from the target, plunders 50% of all enemy current HP, and each attack deals 480% S-ATK damage to hit targets. Lastly, recovers 100 Accumulator.
  - **Ⅲ** at `+10` — Precision StrikeⅢ (杰斯·洛特SP+6)
    Single attack, attacks the target hit 5 times, additionally inflicts 15,000,000 true damage, first plunders 100% Accumulator from the target, plunders 50% of all enemy current HP, and each attack deals 550% S-ATK damage to hit targets. Gains Eye of True Sight lasting until the end of the battle. Lastly, recovers 100 Accumulator.
  - **Ⅳ** at `+T2` — Precision StrikeIV (杰斯·洛特SP+10)
    Single attack, attacks the target hit 5 times, additionally inflicts 20,000,000 true damage, first plunders 100% Accumulator from the target, plunders 50% of all enemy current HP, and each attack deals 600% S-ATK damage to hit targets. Gains Eye of True Sight lasting until the end of the battle. Removes all buffs from all enemies, dispels all Attribute debuffs and partial control effects from all allies: Freeze, Lock, Confusion, Prohibiting the use of skills, Petrify, Icebound, Entangle, Brittle. Lastly, recovers 100 Accumulator.

**Slot 2 — Trace Erasure** (id 2025, unlocks at `+2`)
  - **Ⅰ** at `+2` — Trace ErasureⅠ (杰斯·洛特SP+2)
    (Takes effect at the start of battle) When casting a skill, allies' damage dealt is increased by 120% for 2 rounds, stacking up to 2 times.
  - **Ⅱ** at `+15` — Trace ErasureⅡ (杰斯·洛特SP+15)
    (Takes effect at the start of battle) When casting a skill, allies' damage dealt is increased by 120% for 2 rounds, stacking up to 2 times. At the start of battle, gains Rebirth. When casting a skill, grants Rebirth to own and 2 random allies. Upon death, immediately revive with 100% HP and Accumulator as at the start of battle (unaffected by forbidding revival effects).
  - **Ⅲ** at `+T3` — Trace ErasureⅢ (杰斯·洛特SP+19)
    (Takes effect at the start of battle) When casting a skill, allies' damage dealt is increased by 120% for 2 rounds, stacking up to 2 times. At the start of battle, gains Rebirth. When casting a skill, grants Rebirth to own and 2 random allies. Upon death, immediately revive with 100% HP and Accumulator as at the start of battle (unaffected by forbidding revival effects). If the S-ATK does not kill an Enemy, an additional S-ATK is immediately cast. (Similar effects cannot stack.)
  - **Ⅳ** at `Awaken` — Trace ErasureIV (杰斯·洛特SP+觉醒+1)
    (Takes effect at the start of battle) When casting a skill, allies' damage dealt is increased by 120% for 2 rounds, stacking up to 2 times. At the start of battle, gains Rebirth. When casting a skill, grants Rebirth to own and 2 random allies. Upon death, immediately revive with 100% HP and Accumulator as at the start of battle (unaffected by forbidding revival effects). If the S-ATK does not kill an Enemy, an additional S-ATK is immediately cast. (Similar effects cannot stack.) When casting a skill, there is a 100% chance to turn invisible for 2 rounds. On the first S-ATK at the start of battle, all allies gain Dark Conceal for 1 round.

**Slot 3 — Lone Wolf** (id 2026, unlocks at `+4`)
  - **Ⅰ** at `+4` — Lone WolfⅠ (杰斯·洛特SP+4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +60% S-ATK: +60% DMG Bonus (Absolute Value): +15% Crit ATK (Absolute Value) +15%
  - **Ⅱ** at `+11` — Lone WolfⅡ (杰斯·洛特SP+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +90% S-ATK: +90% DMG Bonus (Absolute Value): +20% Crit ATK (Absolute Value) +20%
  - **Ⅲ** at `+T` — Lone WolfⅢ (杰斯·洛特SP+16)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +120% S-ATK: +120% DMG Bonus (Absolute Value): +25% Crit ATK (Absolute Value) +25%
  - **Ⅳ** at `+T2` — Lone WolfIV (杰斯·洛特SP+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +150% S-ATK: +150% DMG Bonus (Absolute Value): +30% Crit ATK (Absolute Value) +30%

**Slot 4 — Light and Shadow** (id 2027, unlocks at `+3`)
  - **Ⅰ** at `+3` — Light and ShadowⅠ (杰斯·洛特SP+3)
    (Takes effect at the start of battle) All allies are immune to damage and abnormal statuses caused by Enemy Flagship. (except for subsequent damage.)
  - **Ⅱ** at `+13` — Light and ShadowⅡ (杰斯·洛特SP+13)
    (Takes effect at the start of battle) All allies are immune to damage and abnormal statuses caused by Enemy Flagship. (except for subsequent damage.) When all allies with Rebirth deal S-ATK damage, their Crit ATK is increased by 120%.
  - **Ⅲ** at `+T4` — Light and ShadowⅢ (杰斯·洛特SP+20)
    (Takes effect at the start of battle) All allies are immune to damage and abnormal statuses caused by Enemy Flagship. (except for subsequent damage.) When all allies with Rebirth deal S-ATK damage, their Crit ATK is increased by 120%. All allies’ S-ATK ignores 75% of the target’s S-DEF, and their S-ATK is converted to true damage. (True damage completely ignores the target’s defense)
  - **Ⅳ** at `Second Awaken` — Light and ShadowIV (杰斯·洛特SP+觉醒+2)
    (Takes effect at the start of battle) All allies are immune to damage and abnormal statuses caused by Enemy Flagship. (except for subsequent damage.) When all allies with Rebirth deal S-ATK damage, their Crit ATK is increased by 120%. All allies’ S-ATK ignores 75% of the target’s S-DEF, and their S-ATK is converted to true damage. (True damage completely ignores the target’s defense) Jayce Lot - Silver Wolf excels at capturing the dynamic changes of Light and Shadow, providing different effects based on the speed gap between own team and the enemy team. If own team's speed is greater than the enemy squad's, Jayce Lot - Silver Wolf gains [Light]; otherwise, gains [Shadow]. (Speed is determined at the start of battle and is unaffected by buffs/debuffs during battle) [Light]: At the start of battle and each time a unit is resurrect rebirthed, self immediately acts once. [Shadow]: At the start of battle and each time a unit is resurrect rebirthed, all allies gain [Dark Conceal] for 1 round, and receive a Shield that can block any type of damage once. The Shield is removed after taking damage once.

### Augment cost (per step)
- `+1` — 5× Galaxy Heart · 100,000 money
- `+2` — 10× Galaxy Heart · 200,000 money
- `+3` — 21× Galaxy Heart · 300,000 money
- `+4` — 28× Galaxy Heart · 500,000 money
- `+5` — 35× Galaxy Heart · 800,000 money
- `+6` — 42× Galaxy Heart · 10× Pandora Power Core
- `+7` — 49× Galaxy Heart · 50× Pandora Power Core
- `+8` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Galaxy Heart · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Galaxy Heart · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Galaxy Heart · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 40× Galaxy Heart · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 80× Galaxy Heart · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 160× Galaxy Heart · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 320× Galaxy Heart · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Galaxy Heart · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Galaxy Heart · 100× Alien Essence · 100× Transcendence Core

---

## 643 · (no English name) 柯罗诺斯SP
**Role** Flagship · **Attack** physical · **Generation** latest
**Ratings** Damage 7/10 · Defence 9/10 · Assist 10/10

### Skill panels
**Slot 1 — —** (id 2032, unlocks at `+0`)
  - **Ⅰ** at `+0` — — (柯罗诺斯SP+0)
    _(no English description shipped)_
  - **Ⅱ** at `+6` — — (柯罗诺斯SP+2)
    _(no English description shipped)_
  - **Ⅲ** at `+10` — — (柯罗诺斯SP+3)
    _(no English description shipped)_
  - **Ⅳ** at `+T2` — — (柯罗诺斯SP+6)
    _(no English description shipped)_

**Slot 2 — —** (id 2033, unlocks at `+2`)
  - **Ⅰ** at `+2` — — (柯罗诺斯-起源+2)
    _(no English description shipped)_
  - **Ⅱ** at `+15` — — (柯罗诺斯-起源+15)
    _(no English description shipped)_
  - **Ⅲ** at `+T3` — — (柯罗诺斯-起源+19)
    _(no English description shipped)_
  - **Ⅳ** at `Awaken` — — (柯罗诺斯-起源+觉醒+1)
    _(no English description shipped)_

**Slot 3 — —** (id 2034, unlocks at `+4`)
  - **Ⅰ** at `+4` — — (柯罗诺斯-起源+4)
    _(no English description shipped)_
  - **Ⅱ** at `+11` — — (柯罗诺斯-起源+11)
    _(no English description shipped)_
  - **Ⅲ** at `+T` — — (柯罗诺斯-起源+16)
    _(no English description shipped)_
  - **Ⅳ** at `+T2` — — (柯罗诺斯-起源+18)
    _(no English description shipped)_

**Slot 4 — —** (id 2035, unlocks at `+3`)
  - **Ⅰ** at `+3` — — (柯罗诺斯-起源+3)
    _(no English description shipped)_
  - **Ⅱ** at `+13` — — (柯罗诺斯-起源+13)
    _(no English description shipped)_
  - **Ⅲ** at `+T4` — — (柯罗诺斯-起源+20)
    _(no English description shipped)_
  - **Ⅳ** at `Second Awaken` — — (柯罗诺斯-起源+觉醒+2)
    _(no English description shipped)_

### Augment cost (per step)
- `+1` — 5× Galaxy Heart · 100,000 money
- `+2` — 10× Galaxy Heart · 200,000 money
- `+3` — 21× Galaxy Heart · 300,000 money
- `+4` — 28× Galaxy Heart · 500,000 money
- `+5` — 35× Galaxy Heart · 800,000 money
- `+6` — 42× Galaxy Heart · 10× Pandora Power Core
- `+7` — 49× Galaxy Heart · 50× Pandora Power Core
- `+8` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Galaxy Heart · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Galaxy Heart · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Galaxy Heart · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 40× Galaxy Heart · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 80× Galaxy Heart · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 160× Galaxy Heart · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 320× Galaxy Heart · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Galaxy Heart · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Galaxy Heart · 100× Alien Essence · 100× Transcendence Core

---

## 646 · Perthera 珀瑟拉
**Role** Flagship · **Attack** physical · **Generation** latest
**Ratings** Damage 9/10 · Defence 8/10 · Assist 10/10

### Skill panels
**Slot 1 — —** (id 2044, unlocks at `+0`)
  - **Ⅰ** at `+0` — — (珀瑟拉+0)
    _(no English description shipped)_
  - **Ⅱ** at `+6` — — (珀瑟拉+2)
    _(no English description shipped)_
  - **Ⅲ** at `+10` — — (珀瑟拉+6)
    _(no English description shipped)_
  - **Ⅳ** at `+T1` — — (珀瑟拉+10)
    _(no English description shipped)_

**Slot 2 — —** (id 2045, unlocks at `+2`)
  - **Ⅰ** at `+2` — — (珀瑟拉+2)
    _(no English description shipped)_
  - **Ⅱ** at `+15` — — (珀瑟拉+15)
    _(no English description shipped)_
  - **Ⅲ** at `+T3` — — (珀瑟拉+19)
    _(no English description shipped)_
  - **Ⅳ** at `Awaken` — — (珀瑟拉+觉醒+1)
    _(no English description shipped)_

**Slot 3 — —** (id 2046, unlocks at `+4`)
  - **Ⅰ** at `+4` — — (珀瑟拉+4)
    _(no English description shipped)_
  - **Ⅱ** at `+8` — — (珀瑟拉+11)
    _(no English description shipped)_
  - **Ⅲ** at `+12` — — (珀瑟拉+16)
    _(no English description shipped)_
  - **Ⅳ** at `+T` — — (珀瑟拉+18)
    _(no English description shipped)_

**Slot 4 — —** (id 2047, unlocks at `+3`)
  - **Ⅰ** at `+3` — — (珀瑟拉+3)
    _(no English description shipped)_
  - **Ⅱ** at `+13` — — (珀瑟拉+13)
    _(no English description shipped)_
  - **Ⅲ** at `+T4` — — (珀瑟拉+20)
    _(no English description shipped)_
  - **Ⅳ** at `Second Awaken` — — (珀瑟拉+觉醒+2)
    _(no English description shipped)_

### Augment cost (per step)
- `+1` — 5× Galaxy Heart · 100,000 money
- `+2` — 10× Galaxy Heart · 200,000 money
- `+3` — 21× Galaxy Heart · 300,000 money
- `+4` — 28× Galaxy Heart · 500,000 money
- `+5` — 35× Galaxy Heart · 800,000 money
- `+6` — 42× Galaxy Heart · 10× Pandora Power Core
- `+7` — 49× Galaxy Heart · 50× Pandora Power Core
- `+8` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Galaxy Heart · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Galaxy Heart · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Galaxy Heart · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Galaxy Heart · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 40× Galaxy Heart · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 80× Galaxy Heart · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 160× Galaxy Heart · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 320× Galaxy Heart · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Galaxy Heart · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Galaxy Heart · 100× Alien Essence · 100× Transcendence Core

---
