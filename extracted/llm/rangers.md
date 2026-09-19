# Galaxy Legends — SSS Rangers (42 heroes)

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
| 339 | Scar | 斯卡尔 | 9 | 9 | 7 | old |
| 341 | Ambrose | 安布罗斯 | 7 | 7 | 7 | old |
| 361 | Snake | 斯内克 | 7 | 9 | 3 | old |
| 385 | Rango | 兰格 | 8 | 8 | 6 | old |
| 398 | Bombbeats | 布姆毕斯 | 8 | 8 | 6 | old |
| 418 | Rambic | 拉比克 | 9 | 7 | 5 | old |
| 441 | Panda | 庞达 | 8 | 7 | 7 | old |
| 448 | Space Ninja | 太空忍者 | 8 | 7 | 7 | old |
| 460 | Horus | 荷鲁斯 | 9 | 7 | 7 | old |
| 470 | Wukong | 悟空 | 10 | 10 | 7 | old |
| 471 | 悟空分身 | 悟空分身 | 10 | 10 | 7 | old |
| 473 | Shun | 瞬 | 9 | 7 | 7 | old |
| 480 | No.1113 | No.1113 | 9 | 7 | 7 | old |
| 483 | Hermes | 赫尔墨斯 | 9 | 7 | 7 | old |
| 487 | Nezha | 哪吒 | 9 | 7 | 7 | old |
| 493 | Aquilis | 阿奎利斯 | 9 | 7 | 7 | old |
| 508 | Alize | 艾丽捷 | 9 | 7 | 7 | old |
| 511 | Teneb | 塔内巴 | 10 | 10 | 8 | old |
| 512 | Losa | 洛萨 | 9 | 7 | 7 | old |
| 522 | Lenish | 莱纳希 | 9 | 7 | 7 | old |
| 527 | Wenet | 乌涅特 | 9 | 7 | 7 | old |
| 539 | Parvati | 帕瓦娜 | 9 | 7 | 7 | latest |
| 548 | Hassan | 哈桑 | 9 | 7 | 7 | old |
| 549 | Colin | 柯林 | 9 | 7 | 7 | latest |
| 552 | Eluma | 艾露玛 | 9 | 7 | 7 | latest |
| 563 | Coliver | 柯利弗 | 9 | 5 | 6 | latest |
| 564 | Kelly | 凯莉 | 6 | 8 | 9 | old |
| 566 | Syllabear | 塞拉比尔 | 8 | 7 | 7 | latest |
| 569 | Antandra | 安丹德拉 | 9 | 7 | 7 | latest |
| 580 | Leonidas | 列奥尼达斯 | 9 | 7 | 7 | latest |
| 587 | Ice Fury | 冰怒 | 8 | 8 | 6 | latest |
| 588 | Vera | 薇拉 | 9 | 7 | 5 | old |
| 592 | Elf | 爱尔芙 | 9 | 7 | 10 | latest |
| 600 | Starborn | 星辰 | 9 | 7 | 10 | latest |
| 604 | Roselle | 洛瑟儿 | 9 | 7 | 10 | old |
| 605 | Clarissa | 克拉丽莎 | 9 | 10 | 7 | latest |
| 612 | Ouros | 欧罗斯 | 9 | 7 | 10 | latest |
| 618 | Karen Thorne | 凯伦·索恩 | 9 | 7 | 10 | latest |
| 622 | Zeno | 泽诺 | 9 | 7 | 10 | latest |
| 632 | Kariel | 卡里尔 | 9 | 7 | 10 | latest |
| 635 | Kalastor | 卡拉斯托 | 8 | 7 | 10 | latest |
| 640 | Linore | 莉诺尔 | 7 | 10 | 9 | latest |

---

## 339 · Scar 斯卡尔
**Role** Ranger · **Attack** physical · **Generation** old
**Ratings** Damage 9/10 · Defence 9/10 · Assist 7/10

### Signature skill
- **Ⅰ** at `+0` — Overwhelming Army (5月WD)
  Vertical attack, plunders 50% of all enemies' DEF and S-DEF and then deals 210% S-ATK damage, lasting for 1 round. Plundered attributes can be stacked, equal to enemies' attribute values lost. The ship itself will inherit the plundered values.
- **Ⅱ** at `+T4` — Overwhelming ArmyⅡ (斯卡尔)
  Vertical attack, plunders 80% of all enemies' DEF and S-DEF and then deals 240% S-ATK damage, lasting for 1 round. Plundered attributes can be stacked, equal to enemies' attribute values lost. The ship itself will inherit the plundered values.

### Augment cost (per step)
- `+1` — 5× Ranger Chip · 100,000 money
- `+2` — 10× Ranger Chip · 200,000 money
- `+3` — 21× Ranger Chip · 300,000 money
- `+4` — 28× Ranger Chip · 500,000 money
- `+5` — 35× Ranger Chip · 800,000 money
- `+6` — 42× Ranger Chip · 10× Pandora Power Core
- `+7` — 49× Ranger Chip · 50× Pandora Power Core
- `+8` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Scar Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Scar Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Scar Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Scar Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Scar Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Scar Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 341 · Ambrose 安布罗斯
**Role** Ranger · **Attack** physical · **Generation** old
**Ratings** Damage 7/10 · Defence 7/10 · Assist 7/10

### Signature skill
- **Ⅰ** at `+0` — Lightning Guard (安布罗斯)
  Single attack, after hitting the main target it will also attack enemy targets in proximity to the main target. It will successively deal 200%, 200%, 200% S-ATK damage to each target respectively, additionally deals 3M True Damage (ignore defense) to each target, and it also has a 70% chance to lock targets for 1 round. At the same time, activates a BUFF for self and the friendly ship with lowest HP to reduce receiving damage by 60%, lasting for 2 round. In addition, recovers 100 Accumulator for self.
- **II** at `+T4` — Lightning GuardII (安布罗斯)
  Single attack, after hitting the main target it will also attack enemy targets in proximity to the main target. It will successively deal 250%, 250%, 250% S-ATK damage to each target respectively, additionally deals 6M True Damage (ignore defense) to each target, and it also has a 80% chance to lock targets for 1 round. At the same time, activates a BUFF for self and the friendly ship with lowest HP to reduce receiving damage by 80%, lasting for 2 round. In addition, recovers 100 Accumulator for self.

### Augment cost (per step)
- `+1` — 5× Ranger Chip · 100,000 money
- `+2` — 10× Ranger Chip · 200,000 money
- `+3` — 21× Ranger Chip · 300,000 money
- `+4` — 28× Ranger Chip · 500,000 money
- `+5` — 35× Ranger Chip · 800,000 money
- `+6` — 42× Ranger Chip · 10× Pandora Power Core
- `+7` — 49× Ranger Chip · 50× Pandora Power Core
- `+8` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Ambrose Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Ambrose Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Ambrose Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Ambrose Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Ambrose Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Ambrose Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 361 · Snake 斯内克
**Role** Ranger · **Attack** physical · **Generation** old
**Ratings** Damage 7/10 · Defence 9/10 · Assist 3/10

### Signature skill
- **Ⅰ** at `+0` — Ballistic Deterrent (10月wd)
  Cross attack, plunders 30% (absolute value) Block from all enemies for 2 rounds and then deals 300% S-ATK damage. It has a 90% chance to lock targets for 1 round. At last it can increase 50 Accumulator for the ship itself.
- **II** at `+T4` — Ballistic Deterrent II (斯内克)
  Cross attack, initially plunders 50% [Absolute Value] Interception and 50% [Absolute Value] Penetration from all enemies for 2 rounds, then deals 350% S-ATK damage, and has a 100% chance to lock the target for 1 round. Finally, it adds 100 Accumulator for self.

### Augment cost (per step)
- `+1` — 5× Ranger Chip · 100,000 money
- `+2` — 10× Ranger Chip · 200,000 money
- `+3` — 21× Ranger Chip · 300,000 money
- `+4` — 28× Ranger Chip · 500,000 money
- `+5` — 35× Ranger Chip · 800,000 money
- `+6` — 42× Ranger Chip · 10× Pandora Power Core
- `+7` — 49× Ranger Chip · 50× Pandora Power Core
- `+8` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Snake Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Snake Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Snake Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Snake Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Snake Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Snake Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 385 · Rango 兰格
**Role** Ranger · **Attack** physical · **Generation** old
**Ratings** Damage 8/10 · Defence 8/10 · Assist 6/10

### Signature skill
- **Ⅰ** at `+0` — Venom Bomb (2月wd)
  Cross attack, deals 320% S-ATK damage. And then deals 130% of the previous total damage (True Damage) to the enemy ship with the lowest HP. It can also activate a shield for the ship itself which can withstand the damage of two attacks for one round and increases 100 Accumulator for the ship itself.
- **Ⅱ** at `+T2` — Venom Bomb Ⅱ (兰格+T2)
  Cross attack, deals 350% S-ATK damage. And then deals 180% of the previous total damage (True Damage) to the enemy ship with the lowest HP. It can also activate a shield for the ship itself which can withstand the damage of two attacks for one round and increases 100 Accumulator for the ship itself.
- **III** at `+T4` — Venom Bomb III (兰格，剧毒炸弹)
  Cross attack, deals 380% S-ATK damage. And then deals 210% of the previous total damage (True Damage) to the enemy ship with the lowest HP. It can also activate a shield for the ship itself which can withstand the damage of two attacks for one round and increases 100 Accumulator for the ship itself.

### Augment cost (per step)
- `+1` — 5× Ranger Chip · 100,000 money
- `+2` — 10× Ranger Chip · 200,000 money
- `+3` — 21× Ranger Chip · 300,000 money
- `+4` — 28× Ranger Chip · 500,000 money
- `+5` — 35× Ranger Chip · 800,000 money
- `+6` — 42× Ranger Chip · 10× Pandora Power Core
- `+7` — 49× Ranger Chip · 50× Pandora Power Core
- `+8` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Rango’s Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Rango’s Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Rango’s Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Rango’s Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Rango’s Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Rango’s Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 398 · Bombbeats 布姆毕斯
**Role** Ranger · **Attack** physical · **Generation** old
**Ratings** Damage 8/10 · Defence 8/10 · Assist 6/10

### Signature skill
- **I** at `+0` — Fatal Beats I (布姆毕斯，致命节奏)
  Vertical attack, deal 300% S-ATK damage. Each Hero in the team has a 60% chance (the rate for each one will be settled independently) to increase 50% S-ATK for 2 rounds. Also it can increase 90% Dodge for self and the teammate with the lowest HP percentage except self for 1 round. Then, it can activate a shield for self which can block the damage of two attacks for 1 round. In addition, recover 100 Accumulator for self,
- **II** at `+T2` — Fatal Beats II (布姆毕斯+T2)
  Vertical attack, deal 350% S-ATK damage. Each Hero in the team has a 70% chance (the rate for each one will be settled independently) to increase 70% S-ATK for 2 rounds. Also it can increase 90% Dodge for self and the teammate with the lowest HP percentage except self for 1 round. Then, it can activate a shield for self which can block the damage of two attacks for 1 round. In addition, recover 100 Accumulator for self,
- **III** at `+T4` — Fatal Beats III (布姆毕斯，致命节奏)
  Vertical attack, deal 380% S-ATK damage. Each Hero in the team has a 100% chance (the rate for each one will be settled independently) to increase 100% S-ATK for 2 rounds. Also it can increase 100% Dodge for self and the teammate with the lowest HP percentage except self for 1 round. Then, it can activate a shield for self which can block the damage of two attacks for 1 round. In addition, recover 100 Accumulator for self,

### Augment cost (per step)
- `+1` — 5× Ranger Chip · 100,000 money
- `+2` — 10× Ranger Chip · 200,000 money
- `+3` — 21× Ranger Chip · 300,000 money
- `+4` — 28× Ranger Chip · 500,000 money
- `+5` — 35× Ranger Chip · 800,000 money
- `+6` — 42× Ranger Chip · 10× Pandora Power Core
- `+7` — 49× Ranger Chip · 50× Pandora Power Core
- `+8` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Bombbeats's Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Bombbeats's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Bombbeats's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Bombbeats's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Bombbeats's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Bombbeats's Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 418 · Rambic 拉比克
**Role** Ranger · **Attack** physical · **Generation** old
**Ratings** Damage 9/10 · Defence 7/10 · Assist 5/10

### Signature skill
- **I** at `+0` — Multiple Tricks I (拉比克（洛基），多重诡计)
  Vertical attack, crazily attack targets three times, each time it can deal 150% S-ATK damage (deal 450% S-ATK damage in total to each target which get hit), and plunder 50 Accumulator from targets; it can also poison targets which get hit so they will suffer 150% S-ATK damage each round for 2 rounds. There is also a 60% chance to weaken targets and reduce all their stats by 40% for 1 round. After that, the Hero has a 60% chance to become invisible for 1 round, In addition, recover 100 Accumulator for self.
- **II** at `+T2` — Multiple Tricks II (拉比克+T2)
  Vertical attack, crazily attack targets three times, each time it can deal 160% S-ATK damage (deal 480% S-ATK damage in total to each target which get hit), and plunder 50 Accumulator from targets; it can also poison targets which get hit so they will suffer 180% S-ATK damage each round for 2 rounds. There is also a 70% chance to weaken targets and reduce all their stats by 40% for 1 round. After that, the Hero has a 70% chance to become invisible for 1 round, In addition, recover 100 Accumulator for self.
- **III** at `+T4` — Multiple Tricks III (拉比克，多重诡计)
  Vertical attack, crazily attack targets three times, each time it can deal 180% S-ATK damage (deal 540% S-ATK damage in total to each target which get hit), and plunder 70 Accumulator from targets; it can also poison targets which get hit so they will suffer 200% S-ATK damage each round for 2 rounds. There is also a 80% chance to weaken targets and reduce all their stats by 50% for 1 round. After that, the Hero has a 100% chance to become invisible for 1 round, In addition, recover 100 Accumulator for self.

### Augment cost (per step)
- `+1` — 5× Ranger Chip · 100,000 money
- `+2` — 10× Ranger Chip · 200,000 money
- `+3` — 21× Ranger Chip · 300,000 money
- `+4` — 28× Ranger Chip · 500,000 money
- `+5` — 35× Ranger Chip · 800,000 money
- `+6` — 42× Ranger Chip · 10× Pandora Power Core
- `+7` — 49× Ranger Chip · 50× Pandora Power Core
- `+8` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Rambic's Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Rambic's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Rambic's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Rambic's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Rambic's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Rambic's Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 441 · Panda 庞达
**Role** Ranger · **Attack** physical · **Generation** old
**Ratings** Damage 8/10 · Defence 7/10 · Assist 7/10

### Signature skill
- **Ⅰ** at `+0` — Ultimate PowerⅠ (庞达，力量之王Ⅰ)
  Vertical attack, plunders 20% (absolute value) Crit from each main target for 1 round. Then it deals 400% S-ATK Damage and clears target’s accumulator. Additionally, makes teammates with the lowest HP percentage invisible for 1 round. It also increases 80% S-DEF & DEF for self and two teammates with the lowest HP percentage, lasting for 1 round. It has a 80% chance to lock and confuse the target for 1 round。 Also it become immune to Weaken and Freeze for 1 round. At last, restores 100 Accumulator for self.
- **Ⅱ** at `+T2` — Ultimate Power Ⅱ (庞达，力量之王Ⅱ)
  Vertical attack, plunders 25% (absolute value) Crit from each main target for 1 round. Then it deals 450% S-ATK Damage and clears target’s accumulator. Additionally, makes teammates with the lowest HP percentage invisible for 1 round. It also increases 90% S-DEF & DEF for self and two teammates with the lowest HP percentage, lasting for 1 round. It has a 90% chance to lock and confuse the target for 1 round。 Also it become immune to Weaken and Freeze for 1 round. At last, restores 100 Accumulator for self.
- **III** at `+T4` — Ultimate Power III (庞达T4，力量之王III)
  Vertical attack, plunders 60% (absolute value) Crit from each main target for 1 round. Then it deals 480% S-ATK Damage and clears target’s accumulator. Additionally, makes teammates with the lowest HP percentage invisible for 1 round. It also increases 120% S-DEF & DEF for self and two teammates with the lowest HP percentage, lasting for 1 round. It has a 100% chance to lock and confuse the target for 2 rounds. Also it become immune to Weaken, Freeze, Lock and Confuse for 1 round. At last, restores 100 Accumulator for self.

### Augment cost (per step)
- `+1` — 5× Ranger Chip · 100,000 money
- `+2` — 10× Ranger Chip · 200,000 money
- `+3` — 21× Ranger Chip · 300,000 money
- `+4` — 28× Ranger Chip · 500,000 money
- `+5` — 35× Ranger Chip · 800,000 money
- `+6` — 42× Ranger Chip · 10× Pandora Power Core
- `+7` — 49× Ranger Chip · 50× Pandora Power Core
- `+8` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Panda's Ship Parts · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Panda's Ship Parts · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Panda's Ship Parts · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Panda's Ship Parts · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Panda's Ship Parts · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Panda's Ship Parts · 140× Alien Essence · 140× Transcendence Core

---

## 448 · Space Ninja 太空忍者
**Role** Ranger · **Attack** physical · **Generation** old
**Ratings** Damage 8/10 · Defence 7/10 · Assist 7/10

### Signature skill
- **Ⅰ** at `+0` — Star NinjutsuⅠ (太空忍者，星际忍术)
  Cross attack, deals 300% S-ATK damage to targets and poison all enemy ships for 2 rounds, making them take 250% S-ATK damage each round. Reduces all targets' Hit Rate by 50% for 1 round. Makes two friendly ships with the lowest HP percentage become invisible for 1 round (except for self). Inflicts Death Code on hit targets for 2 rounds. If a target ship is destroyed with the Death Code effect, the destroyed ship will cause a cross explosion that deals 500% S-ATK damage to the enemy ships on the cross. At last, recovers 100 Accumulator for self.
- **Ⅱ** at `+T` — Star NinjutsuⅡ (太空忍者，星际忍术)
  Cross attack, deals 330% S-ATK damage to targets and poisons all enemy ships for 2 rounds, making them take 300% S-ATK damage each round. Reduces all targets' Hit Rate by 60% for 1 round. Makes two friendly ships with the lowest HP percentage become invisible for 1 round (except for self). Inflicts Death Code on hit targets for 2 rounds. If a target ship is destroyed with the Death Code effect, the destroyed ship will cause a cross explosion that deals 600% S-ATK damage to the enemy ships on the cross. At last, recovers 100 Accumulator for self.
- **Ⅲ** at `+T3` — Star NinjutsuⅢ (太空忍者，星际忍术)
  Cross attack, deals 350% S-ATK damage to targets and poisons all enemy ships for 2 rounds, making them take 300% S-ATK damage each round. Reduces all targets' Hit Rate by 60% for 1 round. There's a 100% chance to make all friendly ships invisible for 1 round.Clears 100% Accumulator from targets. Inflicts Death Code on hit targets for 2 rounds. If a target ship is destroyed with the Death Code effect, the destroyed ship will cause a cross explosion that deals 600% S-ATK damage to the enemy ships on the cross. At last, recovers 100 Accumulator for self.
- **Ⅳ** at `+T4` — Star NinjutsuⅣ (太空忍者，星际忍术)
  Cross attack, deals 380% S-ATK damage to targets and poisons all enemy ships for 2 rounds, making them take 350% S-ATK damage each round. Reduces all targets' Hit Rate by 75% for 1 round. There's a 100% chance to make all friendly ships invisible for 1 round. Makes self immune to Weaken and to 1 lethal attack for 1 round. Clears 100% Accumulator from targets. Inflicts Death Code on hit targets for 2 rounds. If a target ship is destroyed with the Death Code effect, the destroyed ship will cause a cross explosion that deals 1000% S-ATK damage to the enemy ships on the cross. At last, recovers 100 Accumulator for self.

### Augment cost (per step)
- `+1` — 5× Ranger Chip · 100,000 money
- `+2` — 10× Ranger Chip · 200,000 money
- `+3` — 21× Ranger Chip · 300,000 money
- `+4` — 28× Ranger Chip · 500,000 money
- `+5` — 35× Ranger Chip · 800,000 money
- `+6` — 42× Ranger Chip · 10× Pandora Power Core
- `+7` — 49× Ranger Chip · 50× Pandora Power Core
- `+8` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Space Ninja Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Space Ninja Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Space Ninja Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Space Ninja Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Space Ninja Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Space Ninja Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 460 · Horus 荷鲁斯
**Role** Ranger · **Attack** physical · **Generation** old
**Ratings** Damage 9/10 · Defence 7/10 · Assist 7/10

### Signature skill
- **Ⅰ** at `+0` — Dead Silence Ⅰ (死亡沉寂 Ⅰ)
  Vertical attack; before attacking targets, activates Eye of True Sight until the end of battle. First plunders 100% Hit Rate and 100% Penetration from targets, for 1 round, then deals 400% S-ATK damage and 10M True Damage. Then, deals 200% of the previous total damage (True Damage) to the enemy with the lowest HP. In order of priority, forbids enemy heroes of a certain class to use their skills, for 99 rounds, the order being Striker, Destroyer, Rover, Protector, Flagship, then Ranger (if the highest priority class is missing or destroyed, then the next class in line will be selected). Then, there's a 100% chance of becoming invisible for 2 rounds, immune to forbidding skill use for 2 rounds, and immune to Accumulator Reduce effects for 1 round. Finally, recovers 100 Accumulator for self.
- **Ⅱ** at `+T` — Dead Silence Ⅱ (荷鲁斯+T，死亡沉寂Ⅱ)
  Vertical attack; before attacking targets, activates Eye of True Sight until the end of battle. First plunders 100% Hit Rate and 100% Penetration from targets, for 1 round, then deals 410% S-ATK damage and 10M True Damage. Then, deals 210% of the previous total damage (True Damage) to the enemy with the lowest HP. Also, reduces target's current HP by 50%. In order of priority, forbids enemy heroes of a certain class to use their skills, for 99 rounds, the order being Striker, Destroyer, Rover, Protector, Flagship, then Ranger (if the highest priority class is missing or destroyed, then the next class in line will be selected). Then, there's a 100% chance of becoming invisible for 2 rounds, immune to forbidding skill use for 2 rounds, and immune to Accumulator Reduce and Lock effects for 1 round. Finally, recovers 100 Accumulator for self.
- **Ⅲ** at `+T3` — Dead Silence Ⅲ (荷鲁斯+T3，死亡沉寂Ⅲ)
  Vertical attack; before attacking targets, activates Eye of True Sight until the end of battle. First plunders 100% Hit Rate and 100% Penetration from targets, for 1 round, then deals 450% S-ATK damage and 10M True Damage. Then, deals 250% of the previous total damage (True Damage) to the enemy with the lowest HP. Also, reduces target's current HP by 90%. In order of priority, forbids enemy heroes of a certain class to use their skills, for 99 rounds, the order being Striker, Destroyer, Rover, Protector, Flagship, then Ranger (if the highest priority class is missing or destroyed, then the next class in line will be selected). Then, there's a 100% chance of becoming invisible for 2 rounds, immune to forbidding skill use for 2 rounds, and immune to Accumulator Reduce and Lock effects for 1 round. Finally, recovers 100 Accumulator for self.
- **Ⅳ** at `+T4` — Dead Silence Ⅳ (荷鲁斯+T4，死亡沉寂IV)
  Vertical attack; before attacking targets, activates Eye of True Sight until the end of battle. First plunders 130% Hit Rate and 130% Penetration from targets, for 1 round, then deals 480% S-ATK damage and 15M True Damage. Then, deals 300% of the previous total damage (True Damage) to the enemy with the lowest HP. Also, reduces target's current HP by 90%. In order of priority, forbids enemy heroes of a certain class to use their skills with an extra 65% chance to forbid 1 random enemy from using skills, for 99 rounds, the order being Striker, Destroyer, Rover, Protector, Flagship, then Ranger (if the highest priority class is missing or destroyed, then the next class in line will be selected). Horus's Forbidding Skill Use effects ignore all immunity and protection skills. Then, there's a 100% chance of becoming invisible for 2 rounds, immune to forbidding skill use for 2 rounds, and immune to Accumulator Reduce and Lock effects for 1 round. Finally, recovers 100 Accumulator for self.

### Augment cost (per step)
- `+1` — 5× Ranger Chip · 100,000 money
- `+2` — 10× Ranger Chip · 200,000 money
- `+3` — 21× Ranger Chip · 300,000 money
- `+4` — 28× Ranger Chip · 500,000 money
- `+5` — 35× Ranger Chip · 800,000 money
- `+6` — 42× Ranger Chip · 10× Pandora Power Core
- `+7` — 49× Ranger Chip · 50× Pandora Power Core
- `+8` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Horus Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Horus Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Horus Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Horus Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Horus Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Horus Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 470 · Wukong 悟空
**Role** Ranger · **Attack** physical · **Generation** old
**Ratings** Damage 10/10 · Defence 10/10 · Assist 7/10

### Signature skill
- **Ⅰ** at `+0` — Doppelgangers StrikeⅠ (悟空分身，分身一击)
  分身技能描述
- **Ⅱ** at `+13` — Doppelgangers StrikeⅡ (悟空分身，分身一击+13)
  待补充
- **Ⅲ** at `+T` — Doppelgangers StrikeⅢ (悟空分身，分身一击)
  _(no English description shipped)_
- **IV** at `+T3` — Doppelgangers StrikeIV (悟空分身，分身一击+13)
  _(no English description shipped)_

### Augment cost (per step)
- `+1` — 5× Ranger Chip · 100,000 money
- `+2` — 10× Ranger Chip · 200,000 money
- `+3` — 21× Ranger Chip · 300,000 money
- `+4` — 28× Ranger Chip · 500,000 money
- `+5` — 35× Ranger Chip · 800,000 money
- `+6` — 42× Ranger Chip · 10× Pandora Power Core
- `+7` — 49× Ranger Chip · 50× Pandora Power Core
- `+8` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Wukong Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Wukong Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Wukong Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Wukong Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 60× Wukong Ship Part · 130× Inert Alloy · 100× Heated Alloy

---

## 471 · 悟空分身 悟空分身
**Role** Ranger · **Attack** physical · **Generation** old
**Ratings** Damage 10/10 · Defence 10/10 · Assist 7/10

### Signature skill
- **Ⅰ** at `+0` — Doppelgangers StrikeⅠ (悟空分身，分身一击)
  分身技能描述
- **Ⅱ** at `+13` — Doppelgangers StrikeⅡ (悟空分身，分身一击+13)
  待补充
- **Ⅲ** at `Awaken` — Doppelgangers StrikeⅢ (悟空分身，分身一击)
  _(no English description shipped)_
- **IV** at `Second Awaken` — Doppelgangers StrikeIV (悟空分身，分身一击+13)
  _(no English description shipped)_

### Augment cost (per step)
- `+1` — 5× Ranger Chip · 100,000 money
- `+2` — 10× Ranger Chip · 200,000 money
- `+3` — 21× Ranger Chip · 300,000 money
- `+4` — 28× Ranger Chip · 500,000 money
- `+5` — 35× Ranger Chip · 800,000 money
- `+6` — 42× Ranger Chip · 10× Pandora Power Core
- `+7` — 49× Ranger Chip · 50× Pandora Power Core
- `+8` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Wukong Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Wukong Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Wukong Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Wukong Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 60× Wukong Ship Part · 130× Inert Alloy · 100× Heated Alloy

---

## 473 · Shun 瞬
**Role** Ranger · **Attack** physical · **Generation** old
**Ratings** Damage 9/10 · Defence 7/10 · Assist 7/10

### Signature skill
- **Ⅰ** at `+0` — Cross Twilight SlashⅠ (瞬，十字幕光斩Ⅰ)
  Cross attack; deals 300% S-ATK damage to targets and reduces their Accumulator by 50%. At the same time, applies Forbid Accumulator Recovery effects to targets (can only recover Accumulator through normal attack), for 2 rounds. Applies the Enraged buff to all friendly ships so that they recover an additional 50 Accumulator each time damage is taken, for 3 rounds. Activates a shield for friendly ships that reduces damage taken by 50% for 3 rounds, and activates Eye of True Sight for all friendly ships for 99 rounds. Finally, recovers 100 Accumulator for self.
- **Ⅱ** at `+T` — Cross Twilight SlashⅡ (瞬，十字幕光斩Ⅱ)
  Cross attack; deals 350% S-ATK damage to targets and reduces their Accumulator by 75%. At the same time, applies Forbid Accumulator Recovery effects to targets (can only recover Accumulator through normal attack), for 2 rounds. Applies the Enraged buff to all friendly ships so that they recover an additional 50 Accumulator each time damage is taken, for 3 rounds. Activates a shield for friendly ships that reduces damage taken by 60% for 3 rounds, and activates Eye of True Sight for all friendly ships for 99 rounds. Finally, recovers 100 Accumulator for self.
- **Ⅲ** at `+T3` — Cross Twilight SlashⅢ (瞬，十字幕光斩Ⅲ)
  Cross attack; deals 400% S-ATK damage to targets and reduces their Accumulator by 100%. At the same time, applies Forbid Accumulator Recovery effects to targets (can only recover Accumulator through normal attack), for 2 rounds. Applies the Enraged buff to all friendly ships so that they recover an additional 50 Accumulator each time damage is taken, for 3 rounds. Activates a shield for friendly ships that reduces damage taken by 70% for 3 rounds, and activates Eye of True Sight for all friendly ships for 99 rounds. Finally, recovers 100 Accumulator for self.
- **IV** at `+T4` — Cross Twilight SlashIV (瞬，十字幕光斩IV)
  Cross attack; plunders 100% Accumulator (ignores Accumulator Reduction immunity and Forbidding Accumulator Plunder effects) from targets, before dealing 430% S-ATK damage and 12M True Damage. At the same time, applies Forbid Accumulator Recovery effects to targets (can only recover Accumulator through normal attack), for 2 rounds. Applies the Enraged buff to all friendly ships so that they recover an additional 80 Accumulator each time damage is taken, for 3 rounds. Activates a shield for friendly ships that reduces damage taken by 80% for 3 rounds, and activates Eye of True Sight for all friendly ships for 99 rounds. Finally, recovers 100 Accumulator for self. Applies the Enraged buff to all allies at the start of battle, making them recover an additional 80 Accumulator each time they take damage for 3 rounds. Also has a 100% chance to apply Forbid Accumulator Recovery (can only recover Accumulator through normal attack) to 2 random enemies for 2 rounds.

### Augment cost (per step)
- `+1` — 5× Ranger Chip · 100,000 money
- `+2` — 10× Ranger Chip · 200,000 money
- `+3` — 21× Ranger Chip · 300,000 money
- `+4` — 28× Ranger Chip · 500,000 money
- `+5` — 35× Ranger Chip · 800,000 money
- `+6` — 42× Ranger Chip · 10× Pandora Power Core
- `+7` — 49× Ranger Chip · 50× Pandora Power Core
- `+8` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Shun Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Shun Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Shun Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Shun Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Shun Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Shun Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 480 · No.1113 No.1113
**Role** Ranger · **Attack** physical · **Generation** old
**Ratings** Damage 9/10 · Defence 7/10 · Assist 7/10

### Signature skill
- **I** at `+0` — Phantom Halo I (No.1113-幽魂光罩)
  Cross attack; deals 300% S-ATK damage and 10M True Damage. Then, deducts 50% HP from all female enemies, with a 100% chance of clearing invisibility effects from all enemies. Activates Phantom Halo for itself for 2 rounds. During this time, if any of the following debuffs (Freeze, Confuse, Petrify, Lock) are present in its turn, then it will instantly destroy a random enemy hero before taking an action. Activates Accumulator Suppression Force Field for itself for 2 rounds (This field will not work together with the shield that can reflect damage) . If it is attacked by any enemy while the force field is active, then it will reduce the enemy's Accumulator by 50% at the end of their attack(implements before immunity to Accumulator Reduce effects); it will also reflect 50% of HP damage onto the attacker. Finally, recovers 100 Accumulator for self. Note: While Phantom Halo is in effect, confused heroes will not conduct Normal Attacks after executing instant destruction. Note2: The ship's receiving S-ATK damage will be reduced by 50%.
- **II** at `+T` — Phantom Halo II (No.1113-幽魂光罩)
  Cross attack; deals 330% S-ATK damage and 12M True Damage. Then, deducts 50% HP from all female enemies, with a 100% chance of clearing invisibility effects from all enemies. Activates Phantom Halo for itself for 2 rounds. During this time, if any of the following debuffs (Freeze, Confuse, Petrify, Lock) are present in its turn, then it will instantly destroy a random enemy hero before taking an action. Activates Accumulator Suppression Force Field for itself for 2 rounds (This field will not work together with the shield that can reflect damage) . If it is attacked by any enemy while the force field is active, then it will reduce the enemy's Accumulator by 60% at the end of their attack(implements before immunity to Accumulator Reduce effects); it will also reflect 60% of HP damage onto the attacker. Finally, recovers 100 Accumulator for self. Note: While Phantom Halo is in effect, confused heroes will not conduct Normal Attacks after executing instant destruction. Note2: The ship's receiving S-ATK damage will be reduced by 55%.
- **III** at `+T3` — Phantom Halo III (No.1113-幽魂光罩)
  Cross attack; deals 330% S-ATK damage and 12M True Damage. Then, deducts 50% HP from all female enemies, with a 100% chance of clearing invisibility effects from all enemies. Activates Phantom Halo for itself for 2 rounds. During this time, if any of the following debuffs (Freeze, Confuse, Petrify, Lock) are present in its turn, then it will instantly destroy two random enemy hero before taking an action. Activates Accumulator Suppression Force Field for itself for 2 rounds (This field will not work together with the shield that can reflect damage) . If it is attacked by any enemy while the force field is active, then it will reduce the enemy's Accumulator by 60% at the end of their attack(implements before immunity to Accumulator Reduce effects); it will also reflect 60% of HP damage onto the attacker. Immunity-type effects lose effectiveness while Phantom Halo is active. The user also gains 120% S-DEF and DEF. Finally, recovers 100 Accumulator for self. Note: While Phantom Halo is in effect, confused heroes will not conduct Normal Attacks after executing instant destruction. Note2: The ship's receiving S-ATK damage will be reduced by 55%.
- **IV** at `+T4` — Phantom Halo IV (No.1113（T4）-幽魂光罩)
  Cross attack; deals 360% S-ATK damage and 15M True Damage. Then, deducts 70% HP from all female enemies, with a 100% chance of clearing invisibility effects from all enemies. Activates Phantom Halo for itself for 2 rounds. During this time, if any of the following debuffs (Freeze, Confuse, Petrify, Lock, Icebound, Entangle, Forbidding Skill Use and Weaken) are present in its turn, then it will instantly destroy (ignores immunity to lethal attacks and instant destruction) two random enemy heroes before taking an action. Activates Accumulator Suppression Force Field for itself for 2 rounds (This field will not work together with the shield that can reflect damage). If it is attacked by any enemy while the force field is active, then it will reduce the enemy's Accumulator by 100% at the end of their attack (implements before immunity to Accumulator Reduce effects); it will also reflect 80% of HP damage onto the attacker. Immunity-type effects lose effectiveness while Phantom Halo is active. The user also gains 120% S-DEF and DEF. Crowd-control effects (Freeze, Confuse, Petrify, Lock, Icebound, Entangle, Forbidding Skill Use and Weaken) applied to itself cannot be cleansed. Finally, recovers 100 Accumulator for self. Note: While Phantom Halo is in effect, confused heroes will not conduct Normal Attacks after executing instant destruction. Note 2: The ship's receiving S-ATK damage will be reduced by 55%. Applies Accumulator Suppression Force Field and Phantom Halo to itself lasting 2 rounds at the start of battle.

### Augment cost (per step)
- `+1` — 5× Ranger Chip · 100,000 money
- `+2` — 10× Ranger Chip · 200,000 money
- `+3` — 21× Ranger Chip · 300,000 money
- `+4` — 28× Ranger Chip · 500,000 money
- `+5` — 35× Ranger Chip · 800,000 money
- `+6` — 42× Ranger Chip · 10× Pandora Power Core
- `+7` — 49× Ranger Chip · 50× Pandora Power Core
- `+8` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× No.1113 ship part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× No.1113 ship part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× No.1113 ship part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× No.1113 ship part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× No.1113 ship part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× No.1113 ship part · 140× Alien Essence · 140× Transcendence Core

---

## 483 · Hermes 赫尔墨斯
**Role** Ranger · **Attack** physical · **Generation** old
**Ratings** Damage 9/10 · Defence 7/10 · Assist 7/10

### Signature skill
- **I** at `+0` — Arcane Arts I (诡术秘技)
  Has a 25% chance to copy the skill of a random enemy hero (cannot copy invisible targets; if the skill copied also has copy effects, then the copying is considered a failure) and cast it. The copied skill will have the following additional effects: first, plunders 25% Accumulator from a random enemy hero, then provides itself with a 25% chance to be immune to Accumulator Reduction for 99 rounds. It will then forbid the copied enemy hero from using the skill for 1 round. If copying fails, then launches a cross attack, dealing 350% damage to targets. Finally, recovers 100 Accumulator. (Obtain Hermes to unlock the <Hermes Token Shop>. Purchase packs to get [Hermes Tokens], which can be used to exchange for items in the shop)
- **II** at `+T` — Arcane Arts II (诡术秘技)
  Has a 50% chance to copy the skill of a random enemy hero (cannot copy invisible targets; if the skill copied also has copy effects, then the copying is considered a failure) and cast it. The copied skill will have the following additional effects: first, plunders 50% Accumulator from a random enemy hero, then provides itself with a 50% chance to be immune to Accumulator Reduction and Forbidding Skill Use (probability for each effect calculated separately) for 99 rounds. It will then forbid the copied enemy hero from using the skill for 1 round. If copying fails, then launches a cross attack, dealing 350% damage to targets. Finally, recovers 100 Accumulator. (Obtain Hermes to unlock the <Hermes Token Shop>. Purchase packs to get [Hermes Tokens], which can be used to exchange for items in the shop)
- **III** at `+T3` — Arcane Arts III (诡术秘技)
  Has a 75% chance to copy the skill of a random enemy hero (cannot copy invisible targets; if the skill copied also has copy effects, then the copying is considered a failure) and cast it. The copied skill will have the following additional effects: first, plunders 75% Accumulator from a random enemy hero, then provides itself with a 75% chance to be immune to Accumulator Reduction and Forbidding Skill Use (probability for each effect calculated separately) for 99 rounds, and a 75% chance to be immune to Instant Destruction once for 1 round (including instant destruction). It will then forbid the copied enemy hero from using the skill for 1 round. If copying fails, then launches a cross attack, dealing 350% damage to targets. Finally, recovers 100 Accumulator. (Obtain Hermes to unlock the <Hermes Token Shop>. Purchase packs to get [Hermes Tokens], which can be used to exchange for items in the shop)
- **IV** at `+T4` — Arcane Arts IV (诡术秘技)
  Has a 100% chance to copy the skill of a random enemy hero (cannot copy invisible targets; if the skill copied also has copy effects, then the copying is considered a failure) and cast it. The copied skill will have the following additional effects: first, plunders 100% Accumulator from a random enemy hero, then provides itself with a 100% chance to be immune to Accumulator Reduction and Forbidding Skill Use (probability for each effect calculated separately) for 99 rounds, and a 100% chance to be immune to Instant Destruction once for 1 round (including instant destruction).; also deals 15M True Damage to targets. It will then forbid the copied enemy hero from using the skill for 1 round. If copying fails, then launches a cross attack, dealing 350% damage to targets. Finally, recovers 100 Accumulator. (Obtain Hermes to unlock the <Hermes Token Shop>. Purchase packs to get [Hermes Tokens], which can be used to exchange for items in the shop)

### Augment cost (per step)
- `+1` — 5× Ranger Chip · 100,000 money
- `+2` — 10× Ranger Chip · 200,000 money
- `+3` — 21× Ranger Chip · 300,000 money
- `+4` — 28× Ranger Chip · 500,000 money
- `+5` — 35× Ranger Chip · 800,000 money
- `+6` — 42× Ranger Chip · 10× Pandora Power Core
- `+7` — 49× Ranger Chip · 50× Pandora Power Core
- `+8` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Hermes Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Hermes Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Hermes Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Hermes Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Hermes Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Hermes Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 487 · Nezha 哪吒
**Role** Ranger · **Attack** physical · **Generation** old
**Ratings** Damage 9/10 · Defence 7/10 · Assist 7/10

### Signature skill
- **Ⅰ** at `+0` — Six-Armed HydraⅠ (哪吒，三头六臂Ⅰ)
  Nezha's heads and arms have transmorphic powers, he cycles between different forms in the order of Ranger, Protector, and Rover, possessing the corresponding skill of each form. A reconstructed Nezha possesses strong rebirth abilities. After casting a skill, he increases both his S-ATK and S-DEF by 300K. Nezha always enters battle as a Ranger. Ranger: Cross attack; deals 300% S-ATK damage to targets. Targets also take additional S-ATK damage based on their current Accumulator (2% more damage per 10 Accumulator). There's a 40% chance to Lock targets for 1 round. Finally, recovers 100 Accumulator. Protector: Horizontal attack; deals 220% S-ATK damage to targets and reduces their S-ATK damage by 20% for 1 round. There's also a 30% chance to apply Rebirth on himself, which allows Nezha to revive immediately upon death and recover to his initial stats, for 2 rounds. Finally, recovers 100 Accumulator. Rover: Vertical attack; deals 240% S-ATK damage and removes all stat debuffs (including Weaken) from all friendly ships. There's also a 30% chance to revive 2 random friendly ships and restore 70% of their initial HP and 100 Accumulator. Finally, recovers 100 Accumulator for self.
- **Ⅱ** at `+T` — Six-Armed HydraⅡ (哪吒，三头六臂Ⅱ)
  Nezha's heads and arms have transmorphic powers, he cycles between different forms in the order of Ranger, Protector, and Rover, possessing the corresponding skill of each form. A reconstructed Nezha possesses strong rebirth abilities. After casting a skill, he increases both his S-ATK and S-DEF by 500K. Nezha always enters battle as a Ranger. Ranger: Cross attack; deals 320% S-ATK damage to targets. Targets also take additional S-ATK damage based on their current Accumulator (3% more damage per 10 Accumulator). There's a 60% chance to Lock targets for 1 round. Reduces the Accumulator they gain from skills by 30% for 1 round. Finally, recovers 100 Accumulator. Protector: Horizontal attack; deals 240% S-ATK damage to targets and reduces their S-ATK damage by 30% for 1 round. Triggers a Deflection Force Field for self, the field resists 180% damage dealt by enemy vertical and cross attacks to self and the teammate behind it, lasting 2 rounds (the damage resisted is related to Nezha's ATK, S-ATK, and Accumulator when he casts the skill). There's also a 50% chance to apply Rebirth on himself, which allows Nezha to revive immediately upon death and recover to his initial stats, for 2 rounds. Finally, recovers 100 Accumulator. Rover: Vertical attack; deals 260% S-ATK damage and removes all stat debuffs (including Weaken) and Forbidding Skill Use restriction from all friendly ships. There's also a 50% chance to revive 2 random friendly ships and restore 100% of their initial HP and 100 Accumulator. Finally, recovers 100 Accumulator for self.
- **Ⅲ** at `+T3` — Six-Armed HydraⅢ (哪吒，三头六臂Ⅲ)
  Nezha's heads and arms have transmorphic powers, he cycles between different forms in the order of Ranger, Protector, and Rover, possessing the corresponding skill of each form. A reconstructed Nezha possesses strong rebirth abilities. After casting a skill, he increases both his S-ATK and S-DEF by 500K. Nezha always enters battle as a Ranger. Ranger: Cross attack; deals 340% S-ATK damage to targets. Targets also take additional S-ATK damage based on their current Accumulator (4% more damage per 10 Accumulator). There's a 75% chance to Lock targets for 1 round. Reduces the Accumulator they gain from skills by 50% for 1 round. Finally, recovers 100 Accumulator. Protector: Horizontal attack; deals 260% S-ATK damage to targets and reduces their S-ATK damage by 40% for 1 round. Triggers a Deflection Force Field for self, the field resists 200% damage dealt by enemy vertical and cross attacks to self and the teammate behind it, lasting 2 rounds (the damage resisted is related to Nezha's ATK, S-ATK, and Accumulator when he casts the skill). There's also a 100% chance to apply Rebirth on himself, which allows Nezha to revive immediately upon death and recover to his initial stats, for 2 rounds. Finally, recovers 100 Accumulator. Rover: Vertical attack; deals 280% S-ATK damage and removes all stat debuffs (including Weaken) and Forbidding Skill Use restriction from all friendly ships. There's also an 80% chance to revive 2 random friendly ships and restore 100% of their initial HP and 100 Accumulator. Finally, recovers 100 Accumulator for self.
- **IV** at `+T4` — Six-Armed HydraIV (哪吒，三头六臂IV)
  Nezha's heads and arms have transmorphic powers, he cycles between different forms in the order of Ranger, Protector, and Rover, possessing the corresponding skill of each form. A reconstructed Nezha possesses strong rebirth abilities. After casting a skill, he increases both his S-ATK and S-DEF by 500K. Nezha always enters battle as a Ranger. Ranger: Cross attack; deals 360% S-ATK damage to targets. Targets also take additional S-ATK damage based on their current Accumulator (5% more damage per 10 Accumulator). There's a 100% chance to Lock targets for 1 round. Reduces the Accumulator they gain from skills by 100% for 1 round. Finally, recovers 100 Accumulator. Protector: Horizontal attack; deals 260% S-ATK damage to targets and reduces their S-ATK damage by 50% for 1 round. Triggers a Deflection Force Field for self, the field resists 220% damage dealt by enemy vertical and cross attacks to self and the teammate behind it, lasting 2 rounds (the damage resisted is related to Nezha's ATK, S-ATK, and Accumulator when he casts the skill). There's also a 100% chance to apply Rebirth on himself, which allows Nezha to revive immediately upon death and recover to his initial stats, for 2 rounds. Finally, recovers 100 Accumulator. Rover: Vertical attack; deals 280% S-ATK damage and removes all stat debuffs (including Weaken), Forbidding Skill Use, and control debuffs (Freeze, Lock, Confuse, Petrify) from all friendly ships. There's also an 100% chance to revive 2 random friendly ships and restore 100% of their initial HP and 150 Accumulator. Finally, recovers 100 Accumulator for self.

### Augment cost (per step)
- `+1` — 5× Ranger Chip · 100,000 money
- `+2` — 10× Ranger Chip · 200,000 money
- `+3` — 21× Ranger Chip · 300,000 money
- `+4` — 28× Ranger Chip · 500,000 money
- `+5` — 35× Ranger Chip · 800,000 money
- `+6` — 42× Ranger Chip · 10× Pandora Power Core
- `+7` — 49× Ranger Chip · 50× Pandora Power Core
- `+8` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Nezha Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Nezha Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Nezha Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Nezha Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Nezha Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Nezha Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 493 · Aquilis 阿奎利斯
**Role** Ranger · **Attack** physical · **Generation** old
**Ratings** Damage 9/10 · Defence 7/10 · Assist 7/10

### Signature skill
- **Ⅰ** at `+0` — Energy Transfer Ⅰ (阿奎利斯)
  Trigger Energy Transfer at the start of battle to link yourself and two allies with enemies in the following order: yourself and enemy with the most HP (absolute value) are linked; the ally with the most S-ATK and enemy with the most S-ATK are linked; the ally with the least HP (absolute value) and enemy with the least HP (absolute value) are linked. A single target may only have one Energy Transfer effect at a time (targets with an active link are removed from the calculation of new links). Energy Transfer has the following effects while active:When inflicted with control effects (Freeze, Lock, Confuse, Petrify, Entangle), the linked ally transfers them to the linked enemy instead (the linked ally is not affected by these control effects). Disregards any immunities.50% of enemy's attack damage taken by the linked ally (except lethal damage) is transferred to the linked enemy. This damage cannot be reduced or spread across different enemies, and ignores shields.Energy Transfer lasts for 2 rounds, and no more than 3 Energy Transfers may be active at any one time. Active Energy Transfers are cleared each time Energy Transfer triggers, and three new links are established.Vertical Attacks deal 340% S-ATK damage, and grant the ally with the least HP a shield able to negate one instance of fatal damage for 1 round. There is a 50% chance that enemies linked with allies are unable to deal damage or inflict status effects to allied units they are linked to for 1 round. Allies also leech 40% of linked enemies' stats (apart from Speed, HP, and Accumulator) for 1 round, as well as 20M HP (directly; this damage cannot be reduced or spread across different enemies, and ignores shields) from all linked enemies and transfer an amount equal to this to all linked allies before recovering 100 Accumulator.
- **Ⅱ** at `+T` — Energy TransferⅡ (阿奎利斯)
  Trigger Energy Transfer at the start of battle to link three allies with enemies in the following order: the ally and enemy with the most HP (absolute value) are linked; the ally and enemy with the most S-ATK are linked; the ally and enemy with the least HP (absolute value) are linked. A single target may only have one Energy Transfer effect at a time (targets with an active link are removed from the calculation of new links). Energy Transfer has the following effects while active: When inflicted with control effects (Freeze, Lock, Confuse, Petrify, Entangle), the linked ally transfers them to the linked enemy instead (the linked ally is not affected by these control effects). Disregards any immunities. 60% of enemy's attack damage taken by the linked ally (except lethal damage) is transferred to the linked enemy. This damage cannot be reduced or spread across different enemies, and ignores shields. Energy Transfer lasts for 2 rounds, and no more than 3 Energy Transfers may be active at any one time. Active Energy Transfers are cleared each time Energy Transfer triggers, and three new links are established. Vertical Attacks deal 380% S-ATK damage, and grant the ally with the least HP a shield able to negate one instance of fatal damage for 1 round. There is a 50% chance that enemies linked with allies are unable to deal damage or inflict status effects to allied units they are linked to for 1 round. Allies also leech 50% of linked enemies' stats (apart from Speed, HP, and Accumulator) for 1 round, as well as 20M HP (directly; this damage cannot be reduced or spread across different enemies, and ignores shields) from all linked enemies and transfer an amount equal to this to all linked allies before recovering 100 Accumulator.
- **Ⅲ** at `+T3` — Energy TransferⅢ (阿奎利斯)
  Trigger Energy Transfer at the start of battle to link three allies with enemies in the following order: the ally and enemy with the most HP (absolute value) are linked; the ally and enemy with the most S-ATK are linked; the ally and enemy with the least HP (absolute value) are linked. A single target may only have one Energy Transfer effect at a time (targets with an active link are removed from the calculation of new links). Energy Transfer has the following effects while active: When inflicted with control effects (Freeze, Lock, Confuse, Petrify, Entangle, Forbidding Skill Use, Icebound, Forbid Revive on all enemy Lieutenants with reviving skills, and Accumulator Reduction (removing and stealing Accumulator)), the linked ally transfers them to the linked enemy instead (the linked ally is not affected by these control effects). Disregards any immunities. 60% of enemy's attack damage taken by the linked ally (except lethal damage) is transferred to the linked enemy. This damage cannot be reduced or spread across different enemies, and ignores shields. Allies with Energy Transfer have a 50% chance to instantly kill an enemy linked to them when attacking with skills. Energy Transfer lasts for 2 rounds, and no more than 3 Energy Transfers may be active at any one time. Active Energy Transfers are cleared each time Energy Transfer triggers, and three new links are established. Vertical Attacks deal 380% S-ATK damage, and grant the ally with the least HP a shield able to negate one instance of fatal damage for 1 round. There is a 50% chance that enemies linked with allies are unable to deal damage or inflict status effects to allied units they are linked to for 1 round. Allies also leech 50% of linked enemies' stats (apart from Speed, HP, and Accumulator) for 1 round, as well as 20M HP (directly; this damage cannot be reduced or spread across different enemies, and ignores shields) from all linked enemies and transfer an amount equal to this to all linked allies before recovering 100 Accumulator.
- **IV** at `+T4` — Energy Transfer IV (阿奎利斯T4，能量转移)
  Trigger Energy Transfer at the start of battle to link three allies with enemies in the following order: the ally and enemy with the most HP (absolute value) are linked; the ally and enemy with the most S-ATK are linked; the ally and enemy with the least HP (absolute value) are linked. A single target may only have one Energy Transfer effect at a time (targets with an active link are removed from the calculation of new links). Energy Transfer has the following effects while active: When inflicted with control effects (Freeze, Lock, Confuse, Petrify, Entangle, Forbidding Skill Use, Icebound, Forbid Revive on all enemy Lieutenants with reviving skills, and Accumulator Reduction (removing and stealing Accumulator)), the linked ally transfers them to the linked enemy instead (the linked ally is not affected by these control effects). Disregards any immunities. 70% of enemy's attack damage taken by the linked ally (except lethal damage) is transferred to the linked enemy. This damage cannot be reduced or spread across different enemies, and ignores shields. Allies with Energy Transfer have a 70% chance to instantly kill an enemy linked to them when attacking with skills (not affected by Immunity to Instant Destruction and Lethal Damage). When allies with Energy Transfer attacks with skills, they leech 100% Accumulator of the enemy they're linked with (ignoring Immunity) and deal S-ATK, plus 18M True Damage. When the linked enemy ship dies, increases ATK, S-ATK, DEF, S-DEF of the ally linked with it by 120% and damage dealt by 20% until the battle ends (does not stack). Energy Transfer lasts for 2 rounds, and no more than 3 Energy Transfers may be active at any one time. Active Energy Transfers are cleared each time Energy Transfer triggers, and three new links are established. Vertical Attacks deal 400% S-ATK damage, and grant the ally with the least HP a shield able to negate one instance of fatal damage for 1 round. There is a 75% chance that enemies linked with allies are unable to deal damage or inflict status effects to allied units they are linked to for 1 round. Allies also leech 60% of linked enemies' stats (apart from Speed, HP, and Accumulator) for 1 round, as well as 24M HP (directly; this damage cannot be reduced or spread across different enemies, and ignores shields) from all linked enemies and transfer an amount equal to this to all linked allies. Allies with Energy Transfer gains Eye of True Sight for 1 round before attack. Lastly, recovers 100 Accumulator.
- **Ⅴ** at `Awaken` — — (被连接目标死亡触发)
  _(no English description shipped)_

### Augment cost (per step)
- `+1` — 5× Ranger Chip · 100,000 money
- `+2` — 10× Ranger Chip · 200,000 money
- `+3` — 21× Ranger Chip · 300,000 money
- `+4` — 28× Ranger Chip · 500,000 money
- `+5` — 35× Ranger Chip · 800,000 money
- `+6` — 42× Ranger Chip · 10× Pandora Power Core
- `+7` — 49× Ranger Chip · 50× Pandora Power Core
- `+8` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Aquilis Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Aquilis Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Aquilis Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Aquilis Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Aquilis Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Aquilis Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 508 · Alize 艾丽捷
**Role** Ranger · **Attack** physical · **Generation** old
**Ratings** Damage 9/10 · Defence 7/10 · Assist 7/10

### Signature skill
- **Ⅰ** at `+0` — Nebula EMP Bomb Ⅰ (艾丽捷，云流磁暴弹)
  Cross attack, deals 260% S-ATK damage to targets. Has a 40% chance (probability for each target calculated separately) to add 1 stack of [Nebula EMP] to all enemies and 2 extra stacks to enemies with [Nebula EMP]. Enemies with [Nebula EMP] get 2 more stacks upon movement, and when they die, all their current stacks will be transferred to a random enemy. [Nebula EMP]: Each stack increases Miss by 5%, with a chance to make attacks miss (cannot make guaranteed hits miss), and reduces S-DEF and DEF by 5%; When all enemies have total of 15 stacks of [Nebula EMP], attacks each enemy with [Nebula EMP] the number of times equal to their stacks of [Nebula EMP], each time dealing 160% S-ATK damage and 1M True Damage and removing all the stacks; Plunders 30% Penetration from targets for 1 round. Also recovers 100 Accumulator.
- **Ⅱ** at `+T` — Nebula EMP BombⅡ (艾丽捷T，云流磁暴弹)
  Cross attack, deals 280% S-ATK damage to targets. Has a 50% chance (probability for each target calculated separately) to add 1 stack of [Nebula EMP] to all enemies and 2 extra stacks to enemies with [Nebula EMP]. Enemies with [Nebula EMP] get 2 more stacks upon movement, and when they die, all their current stacks will be transferred to a random enemy. [Nebula EMP]: Each stack increases Miss by 6%, with a chance to make attacks miss (cannot make guaranteed hits miss), and reduces S-DEF and DEF by 8% (up to 90%); When all enemies have total of 15 stacks of [Nebula EMP], attacks each enemy with [Nebula EMP] the number of times equal to their stacks of [Nebula EMP], each time dealing 180% S-ATK damage and 1.2M True Damage and removing all the stacks; Plunders 50% Penetration from targets for 1 round; Activates Eye of True Sight for 1 round. Also recovers 100 Accumulator.
- **Ⅲ** at `+T3` — Nebula EMP BombⅢ (艾丽捷T3，云流磁暴弹)
  Cross attack, deals 300% S-ATK damage to targets. Has a 80% chance (probability for each target calculated separately) to add 2 stack of [Nebula EMP] to all enemies and 2 extra stacks to enemies with [Nebula EMP]. Enemies with [Nebula EMP] get 2 more stacks upon movement, and when they die, all their current stacks will be transferred to a random enemy. [Nebula EMP]: Each stack increases Miss by 8%, with a chance to make attacks miss (cannot make guaranteed hits miss), and reduces S-DEF and DEF by 10% (up to 90%) and the chance of skill effects by 5% (reduces the chances of skill effects and buffs triggered with skills, up to 30%); When all enemies have total of 15 stacks of [Nebula EMP], attacks each enemy with [Nebula EMP] the number of times equal to their stacks of [Nebula EMP], each time dealing 220% S-ATK damage and 1.5M True Damage and removing all the stacks; Plunders 60% Penetration from targets for 1 round; Activates Eye of True Sight for 1 round. Also recovers 100 Accumulator.
- **IV** at `+T4` — Nebula EMP Bomb IV (艾丽捷T4，云流磁暴弹)
  Cross attack, deals 320% S-ATK damage to targets. Has a 80% chance (probability for each target calculated separately) to add 3 stack of [Nebula EMP] to all enemies and 3 extra stacks to enemies with [Nebula EMP]. Enemies with [Nebula EMP] get 3 more stacks upon movement, and when they die, all their current stacks will be transferred to a random enemy. [Nebula EMP]: Each stack increases Miss by 10%, with a chance to make attacks miss (cannot make guaranteed hits miss), and reduces S-DEF and DEF by 12% (up to 90%) and the chance of skill effects by 8% (reduces the chances of skill effects and buffs triggered with skills, up to 50%); When all enemies have total of 15 stacks of [Nebula EMP], attacks each enemy with [Nebula EMP] the number of times equal to their stacks of [Nebula EMP], each time dealing 300% S-ATK damage and 3M True Damage and removing all the stacks, with a 80% chance (probability for each target calculated separately) to readd 3 stacks of [Nebula EMP] to all enemies; Plunders 60% Penetration from targets for 1 round; Activates Eye of True Sight for 1 round. Also recovers 100 Accumulator.

### Augment cost (per step)
- `+1` — 5× Ranger Chip · 100,000 money
- `+2` — 10× Ranger Chip · 200,000 money
- `+3` — 21× Ranger Chip · 300,000 money
- `+4` — 28× Ranger Chip · 500,000 money
- `+5` — 35× Ranger Chip · 800,000 money
- `+6` — 42× Ranger Chip · 10× Pandora Power Core
- `+7` — 49× Ranger Chip · 50× Pandora Power Core
- `+8` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Alize Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Alize Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Alize Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Alize Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Alize Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Alize Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 511 · Teneb 塔内巴
**Role** Ranger · **Attack** physical · **Generation** old
**Ratings** Damage 10/10 · Defence 10/10 · Assist 8/10

### Signature skill
- **Ⅰ** at `+0` — Mecha WargodⅠ (机械战神)
  Cross attack, deals 360% S-ATK damage and blocks Freeze, Lock, Confuse, Entangle, Icebound, Petrify, Forbidding Skill Use or Instant Destruction effects for 1 round. If an effect is blocked, retaliate against the enemy with a single-target attack (can only trigger 1 time) and steal 80% of that enemy's Accumulator and deal 500% S-ATK damage. If this attack kills the enemy, apply Lock for 1 turn on them if they revive. Teneb' skill attacks (including triggered ones) cannot be Blocked and ignore 30% of the enemy's S-DEF and DEF. The damage dealt is increased by 1% for each 1% of HP the enemy is missing. There's a 50% chance that Teneb will Lock all enemy units upon death (calculated individually for each unit) for 1 round and a 50% chance to gain a Rebirth effect for 1 round, reviving immediately upon death with 100% of its initial HP and Accumulator. Lastly, you recover 100 Accumulator. Gains 1 skill effect block at the start of battle and retaliates with a skill attack against the caster.
- **Ⅱ** at `+T` — Mecha WargodⅡ (机械战神)
  Cross attack, deals 400% S-ATK damage and blocks Freeze, Lock, Confuse, Entangle, Icebound, Petrify, Forbidding Skill Use or Instant Destruction effects for 1 round. If an effect is blocked, retaliate against the enemy with a single-target attack (can only trigger 1 time) and steal 100% of that enemy's Accumulator (not affected by immunity) and deal 600% S-ATK damage. If this attack kills the enemy, apply Lock for 1 turn on them if they revive. Teneb' skill attacks (including triggered ones) cannot be Blocked and ignore 50% of the enemy's S-DEF and DEF. The damage dealt is increased by 2% for each 1% of HP the enemy is missing. There's a 50% chance that Teneb will Lock all enemy units upon death (calculated individually for each unit) for 1 round and a 50% chance to gain a Rebirth effect for 1 round, reviving immediately upon death with 100% of its initial HP and Accumulator. Lastly, you recover 100 Accumulator. Gains 1 skill effect block at the start of battle and retaliates with a skill attack against the caster.
- **Ⅲ** at `+T3` — Mecha WargodⅢ (机械战神)
  Cross attack, deals 420% S-ATK damage and blocks Freeze, Lock, Confuse, Entangle, Icebound, Petrify, Forbidding Skill Use or Instant Destruction effects for 1 round. If an effect is blocked, retaliate against the enemy with a single-target attack (can only trigger 2 times) and steal 100% of that enemy's Accumulator (not affected by immunity) and deal 700% S-ATK damage. If this attack kills the enemy, apply Lock for 1 turn on them if they revive. Teneb' skill attacks (including triggered ones) cannot be Blocked and ignore 60% of the enemy's S-DEF and DEF. The damage dealt is increased by 2% for each 1% of HP the enemy is missing. There's a 75% chance that Teneb will Lock all enemy units upon death (calculated individually for each unit and isn't affected by immunity or protection effects) for 1 round and a 60% chance to gain a Rebirth effect for 1 round, reviving immediately upon death with 100% of its initial HP and Accumulator. Lastly, you recover 100 Accumulator. Gains 1 skill effect block at the start of battle and retaliates with a skill attack against the caster.
- **IV** at `+T4` — Mecha WargodIV (机械战神)
  Cross attack, deals 450% S-ATK damage and blocks Freeze, Lock, Confuse, Entangle, Icebound, Petrify, Forbidding Skill Use or Instant Destruction effects for 1 round. If an effect is blocked, retaliate against the enemy with a single-target attack (can only trigger 2 times) and steal 100% of that enemy's Accumulator (not affected by immunity) and deal 900% S-ATK damage. If this attack kills the enemy, apply Lock for 1 turn on them if they revive. Teneb' skill attacks (including triggered ones) cannot be Blocked and ignore 80% of the enemy's S-DEF and DEF. The damage dealt is increased by 3% for each 1% of HP the enemy is missing. There's a 75% chance that Teneb will Lock all enemy units upon death (calculated individually for each unit and isn't affected by immunity or protection effects) for 1 round and a 70% chance to gain a Rebirth effect for 1 round, reviving immediately upon death with 100% of its initial HP and Accumulator. Lastly, you recover 100 Accumulator. Gains 2 skill effect block at the start of battle and retaliates with a skill attack against the caster.

### Augment cost (per step)
- `+1` — 5× Ranger Chip · 100,000 money
- `+2` — 10× Ranger Chip · 200,000 money
- `+3` — 21× Ranger Chip · 300,000 money
- `+4` — 28× Ranger Chip · 500,000 money
- `+5` — 35× Ranger Chip · 800,000 money
- `+6` — 42× Ranger Chip · 10× Pandora Power Core
- `+7` — 49× Ranger Chip · 50× Pandora Power Core
- `+8` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Teneb Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Teneb Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Teneb Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Teneb Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Teneb Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Teneb Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 512 · Losa 洛萨
**Role** Ranger · **Attack** physical · **Generation** old
**Ratings** Damage 9/10 · Defence 7/10 · Assist 7/10

### Signature skill
- **Ⅰ** at `+0` — Alien Energy BlastⅠ (洛萨，异能轰击)
  Cross Attack; before attacking targets, activates Eye of True Sight for 1 Round and deals 280% S-ATK damage to the target. Dispels stat debuffs (including Weaken) from all friendly ships and clears debuffs from all friendly ships (Freeze, Lock, Confuse, Forbidding Skill Use, Poison, and Curse); applies Deflection Force Field to itself for 2 Rounds, which resists 240% incoming horizontal and vertical damage from enemies' S-ATK for itself and allied units behind it and in its horizontal range (effective when enemies attack units with Deflection Force Field). The damage it can resist is related to Losa's ATK, S-ATK, and Accumulator when casting the skill; all allies have their damage dealt increased by 20% for 2 Rounds, and deals True Damage of 50% of the previous total damage to all controlled enemy units for 2 Rounds; Losa's S-ATK deals extra damage to controlled enemy units of 15% of their Max HP. Lastly, you recover 100 Accumulator.
- **Ⅱ** at `+T` — Alien Energy BlastⅡ (洛萨，异能轰击)
  Cross Attack; before attacking targets, activates Eye of True Sight for 1 Round and deals 320% S-ATK damage to the target. Dispels stat debuffs (including Weaken) from all friendly ships and clears debuffs from all friendly ships (Freeze, Lock, Confuse, Forbidding Skill Use, Poison, and Curse); applies Deflection Force Field to itself for 2 Rounds, which resists 260% incoming horizontal and vertical damage from enemies' S-ATK for itself and allied units behind it and in its horizontal range (effective when enemies attack units with Deflection Force Field). The damage it can resist is related to Losa's ATK, S-ATK, and Accumulator when casting the skill; all allies have their damage dealt increased by 30% for 2 Rounds, and deals True Damage of 60% of the previous total damage to all controlled enemy units for 2 Rounds; Losa's S-ATK deals extra damage to controlled enemy units of 20% of their Max HP. Lastly, you recover 100 Accumulator. (At the start of battle, Losa has a 50% chance of dispelling or clearing itself before acting if it's controlled (Freeze, Lock, Confuse, Petrify, Icebound, Entangle).)
- **Ⅲ** at `+T3` — Alien Energy BlastⅢ (洛萨，异能轰击)
  Cross Attack; before attacking targets, activates Eye of True Sight for 1 Round and deals 340% S-ATK damage to the target. Dispels stat debuffs (including Weaken) from all friendly ships and clears debuffs from all friendly ships (Freeze, Lock, Confuse, Forbidding Skill Use, Poison, Curse, Petrify, Entangle, Icebound); applies Deflection Force Field to itself for 2 Rounds, which resists 300% incoming horizontal and vertical damage from enemies' S-ATK for itself and allied units behind it and in its horizontal range (effective when enemies attack units with Deflection Force Field). The damage it can resist is related to Losa's ATK, S-ATK, and Accumulator when casting the skill; all allies have their damage dealt increased by 40% for 2 Rounds, and deals True Damage of 80% of the previous total damage to all controlled enemy units for 2 Rounds; Losa's S-ATK deals extra damage to controlled enemy units of 30% of their Max HP. Lastly, you recover 100 Accumulator. (At the start of battle, Losa has an 80% chance of dispelling or clearing itself before acting if it's controlled (Freeze, Lock, Confuse, Petrify, Icebound, Entangle); at the start of battle, Losa applies Deflection Force Field to itself for 1 Round.)
- **IV** at `+T4` — Alien Energy BlastIV (洛萨，异能轰击)
  Cross Attack; before attacking targets, activates Eye of True Sight for 1 Round and deals 360% S-ATK damage to the target. Dispels stat debuffs (including Weaken) from all friendly ships and clears debuffs from all friendly ships (Freeze, Lock, Confuse, Forbidding Skill Use, Poison, Curse, Petrify, Entangle, Icebound); applies Deflection Force Field to itself for 2 Rounds, which resists 320% incoming horizontal and vertical damage from enemies' S-ATK for itself and allied units behind it and in its horizontal range (effective when enemies attack units with Deflection Force Field). The damage it can resist is related to Losa's ATK, S-ATK, and Accumulator when casting the skill; all allies have their damage dealt increased by 50% for 2 Rounds, and deals True Damage of 100% of the previous total damage to all controlled enemy units for 2 Rounds; Losa's S-ATK deals extra damage to controlled enemy units of 40% of their Max HP. Has a 100% chance to make allied heroes of a certain class ignore enemy immunity or protection against their skills with control effects (Freeze, Lock, Confuse, Forbidding Skill Use, Entangle, Petrify, Icebound) or debuffs (Poison, Weaken) for 1 round (Priority of Hero Class: Striker, Ranger, Destroyer, Rover, Protector, Flagship. If heroes of a certain class are dead or missing, next class will be chosen in the order of priority) Lastly, you recover 100 Accumulator. (At the start of battle, Losa has an 100% chance of dispelling or clearing itself before acting if it's controlled (Freeze, Lock, Confuse, Petrify, Icebound, Entangle); at the start of battle, Losa applies Deflection Force Field to itself for 1 Round.)

### Augment cost (per step)
- `+1` — 5× Ranger Chip · 100,000 money
- `+2` — 10× Ranger Chip · 200,000 money
- `+3` — 21× Ranger Chip · 300,000 money
- `+4` — 28× Ranger Chip · 500,000 money
- `+5` — 35× Ranger Chip · 800,000 money
- `+6` — 42× Ranger Chip · 10× Pandora Power Core
- `+7` — 49× Ranger Chip · 50× Pandora Power Core
- `+8` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Losa Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Losa Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Losa Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Losa Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Losa Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Losa Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 522 · Lenish 莱纳希
**Role** Ranger · **Attack** physical · **Generation** old
**Ratings** Damage 9/10 · Defence 7/10 · Assist 7/10

### Signature skill
- **Ⅰ** at `+0` — All-StarⅠ (莱纳希，全能明星I)
  Being the most acclaimed football player in the Galaxy Empire, Lenish excels at any position. When placed in the front row of a defensive lineup, he becomes a forward and his skill is replaced by [World Wave!]' when placed in the second row of a defensive lineup, he becomes a midfielder and his skill is replaced by [Pinpoint Pass]; when placed in the third row, he becomes a defender and his skill is replaced by [Tackle!]. World Wave!: Cross attack, first clears all buffs from the target, then plunders 30% of their Penetration and Accumulator and deals 350% S-ATK damage. The first attack also deals 80% S-ATK True Damage to all enemies. You gain 20% increased damage each time the skill is used for 3 rounds, stacking up to 60%. Lastly, you recover 100 Accumulator. Pinpoint Pass: Cross attack, deals 220% S-ATK damage. Targets the ally with the highest attack (the highest of ATK or S-ATK) except for self to clear their crowd-control effects and debuffs and enable them to act 1 extra time this round (does not stack with similar effects), while also increasing their Penetration by 80% and damage dealt by 30% for 2 rounds. Lastly, you recover 100 Accumulator. Tackle!: Cross attack, deals 200% S-ATK damage and plunders 50% of the target's S-DEF and DEF for 2 rounds. Applies a Shield absorbing 150M damage to all allies (shield effects do not stack and the latest one overrides previous shields) for 2 rounds. All allies also gain Eye of True Sight for 2 rounds. Lastly, you recover 100 Accumulator.
- **Ⅱ** at `+T` — All-StarⅡ (莱纳希，全能明星II)
  Being the most acclaimed football player in the Galaxy Empire, Lenish excels at any position. When placed in the front row of a defensive lineup, he becomes a forward and his skill is replaced by [World Wave!]' when placed in the second row of a defensive lineup, he becomes a midfielder and his skill is replaced by [Pinpoint Pass]; when placed in the third row, he becomes a defender and his skill is replaced by [Tackle!]. World Wave!: Cross attack, first clears all buffs from the target, then plunders 40% of their Penetration and Accumulator and deals 370% S-ATK damage. The first attack also deals 90% S-ATK True Damage to all enemies. You gain 25% increased damage each time the skill is used for 3 rounds, stacking up to 75%. Lastly, you recover 100 Accumulator. Pinpoint Pass: Cross attack, deals 240% S-ATK damage. Targets the ally with the highest attack (the highest of ATK or S-ATK) except for self to clear their crowd-control effects and debuffs and enable them to act 1 extra time this round (does not stack with similar effects), while also increasing their Penetration by 100% and damage dealt by 40% for 2 rounds. Lastly, you recover 100 Accumulator. Tackle!: Cross attack, deals 220% S-ATK damage and plunders 65% of the target's S-DEF and DEF for 2 rounds. Applies a Shield absorbing 200M damage to all allies (shield effects do not stack and the latest one overrides previous shields) for 2 rounds. All allies also gain Eye of True Sight for 2 rounds. Lastly, you recover 100 Accumulator.
- **Ⅲ** at `+T3` — All-StarⅢ (莱纳希，全能明星III)
  Being the most acclaimed football player in the Galaxy Empire, Lenish excels at any position. When placed in the front row of a defensive lineup, he becomes a forward and his skill is replaced by [World Wave!]' when placed in the second row of a defensive lineup, he becomes a midfielder and his skill is replaced by [Pinpoint Pass]; when placed in the third row, he becomes a defender and his skill is replaced by [Tackle!]. World Wave!: Cross attack, first clears all buffs from the target, then plunders 50% of their Penetration and Accumulator and deals 390% S-ATK damage. The first attack also deals 100% S-ATK True Damage to all enemies. You gain 30% increased damage each time the skill is used for 3 rounds, stacking up to 90%. Self gains 2 rounds of invisibility and will not lose invisibility for as long as there is another allied unit alive (can be seen by Eye of True Sight). Lastly, you recover 100 Accumulator. Pinpoint Pass: Cross attack, deals 260% S-ATK damage. Targets the ally with the highest attack (the highest of ATK or S-ATK) except for self to clear their crowd-control effects and debuffs and enable them to act 1 extra time this round (does not stack with similar effects), while also increasing their Penetration by 120%, damage dealt by 50% and granting them a new skill effect lasting 1 round: deals 200% S-ATK True Damage the enemy with the least HP. Lastly, you recover 100 Accumulator. Tackle!: Cross attack, deals 240% S-ATK damage and plunders 70% of the target's S-DEF and DEF for 2 rounds. Applies a Shield absorbing 300M damage to all allies (shield effects do not stack and the latest one overrides previous shields) for 2 rounds. If Lenish's shield is active when the enemy attacks, the ally is protected and is immune to debuffs and some crowd-control effects: Freeze, Lock, Confuse and Forbidding Skill Use). All allies also gain Eye of True Sight for 2 rounds. Lastly, you recover 100 Accumulator.
- **IV** at `+T4` — All-StarIV (莱纳希，全能明星IV)
  Being the most acclaimed football player in the Galaxy Empire, Lenish excels at any position. When placed in the front row of a defensive lineup, he becomes a forward and his skill is replaced by [World Wave!]' when placed in the second row of a defensive lineup, he becomes a midfielder and his skill is replaced by [Pinpoint Pass]; when placed in the third row, he becomes a defender and his skill is replaced by [Tackle!]. World Wave!: Cross attack, first clears all buffs from the target, then plunders 65% of their Penetration and Accumulator and deals 420% S-ATK damage. The first attack also deals 120% S-ATK True Damage to all enemies. You gain 40% increased damage and 100% increased Crit ATK each time the skill is used for 3 rounds, stacking up to 120% damage and 300% Crit ATK. Self gains 2 rounds of invisibility and will not lose invisibility for as long as there is another allied unit alive (can be seen by Eye of True Sight). Lenish's skill attacks have a 60% chance to crit (guaranteed to crit when triggered). Lastly, you recover 150 Accumulator. Pinpoint Pass: Cross attack, deals 300% S-ATK damage. Targets the ally with the highest attack (the highest of ATK or S-ATK) except for self to clear their crowd-control effects and debuffs and enable them to act 1 extra time this round (does not stack with similar effects), while also increasing their Penetration by 150%, damage dealt by 80% and granting them a new skill effect lasting 1 round: deals 230% S-ATK True Damage the enemy with the least HP. Makes the crowd-control effects and debuffs of the next acting unit (does not count extra actions gained from skills) go through immunity and protection effects for 1 round. Lastly, you recover 100 Accumulator. Tackle!: Cross attack, deals 260% S-ATK damage and plunders 80% of the target's S-DEF and DEF for 2 rounds. Applies a Shield absorbing 400M damage to all allies (shield effects do not stack and the latest one overrides previous shields) for 2 rounds. (If Lenish's shield is active when the enemy attacks, the ally is protected and is immune to debuffs and some crowd-control effects: Freeze, Lock, Confuse and Forbidding Skill Use). All allies also gain Eye of True Sight for 2 rounds. Has a 50% chance to revive all allies with HP and Accumulator equal to 100% of their initial state (probability calculated individually for each unit; isn't affected by forbidding revival effects). Lastly, you recover 100 Accumulator.

### Augment cost (per step)
- `+1` — 5× Ranger Chip · 100,000 money
- `+2` — 10× Ranger Chip · 200,000 money
- `+3` — 21× Ranger Chip · 300,000 money
- `+4` — 28× Ranger Chip · 500,000 money
- `+5` — 35× Ranger Chip · 800,000 money
- `+6` — 42× Ranger Chip · 10× Pandora Power Core
- `+7` — 49× Ranger Chip · 50× Pandora Power Core
- `+8` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Lenish Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Lenish Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Lenish Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Lenish Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Lenish Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Lenish Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 527 · Wenet 乌涅特
**Role** Ranger · **Attack** physical · **Generation** old
**Ratings** Damage 9/10 · Defence 7/10 · Assist 7/10

### Signature skill
- **Ⅰ** at `+0` — Divine BlessingⅠ (乌涅特，神力恩赐Ⅰ)
  Cross attack, deals 320% S-ATK damage. Increases the damage of all allies by 1% and S-ATK damage reduction by 0.5% (capped at 80%) for each 1% of their missing HP (the buff's effect are twice as potent for Wenet) for 2 rounds. Whenever Wenet deals damage with a skill, all allies are healed for 30% of the damage dealt. Whenever Wenet kills an enemy with a skill she has a 50% chance to revive 1 ally. If an ally takes damage and is brought below 50% within the next 2 rounds, they have a 50% chance to gain a shield for 2 rounds that blocks 1 attack (this effect can trigger multiple times). Lastly, you recover 100 Accumulator
- **Ⅱ** at `+T` — Divine BlessingⅡ (乌涅特，神力恩赐Ⅱ)
  Cross attack, deals 340% S-ATK damage. Increases the damage of all allies by 1.2% and S-ATK damage reduction by 0.8% (capped at 80%) for each 1% of their missing HP (the buff's effect are twice as potent for Wenet) for 2 rounds. Whenever Wenet deals damage with a skill, all allies are healed for 40% of the damage dealt. Whenever Wenet kills an enemy with a skill she has a 60% chance to revive 1 ally (unaffected by forbidding revival effects). If an ally takes damage and is brought below 60% within the next 2 rounds, they have a 50% chance to gain a shield for 2 rounds that blocks 1 attack (this effect can trigger multiple times). Lastly, you recover 100 Accumulator.
- **Ⅲ** at `+T3` — Divine BlessingⅢ (乌涅特，神力恩赐Ⅲ)
  Cross attack, starts by stealing 40% of the target's Accumulator before dealing 360% S-ATK damage. Increases the damage of all allies by 1.5% and S-ATK damage reduction by 1% (capped at 80%) for each 1% of their missing HP (the buff's effect are twice as potent for Wenet) for 2 rounds. Whenever Wenet deals damage with a skill, all allies are healed for 50% of the damage dealt. Whenever Wenet kills an enemy with a skill she has a 80% chance to revive 1 ally (unaffected by forbidding revival effects). If an ally takes damage and is brought below 70% within the next 2 rounds, they have a 60% chance to gain a shield for 2 rounds that blocks 1 attack (this effect can trigger multiple times). If an ally takes damage and is brought below 40% within the next 2 rounds, they'll be made invisible. Lastly, you recover 100 Accumulator. At the start of battle, for every 1% of the maximum HP of all allies, the attack damage will be increased by 1.5%, and the S-ATK damage reduction (up to 80%) will be increased by 1% (Wenet gets double damage increase and S-ATK damage reduction effect)
- **Ⅳ** at `+T4` — Divine BlessingⅣ (乌涅特，神力恩赐IV)
  Cross attack, starts by stealing 50% of the target's Accumulator before dealing 400% S-ATK damage. Wenet' S-ATK has a 60% chance of not being Blocked. Increases the damage of all allies by 2% and S-ATK damage reduction by 1.2% (capped at 80%) for each 1% of their missing HP (the buff's effect are twice as potent for Wenet) for 2 rounds. Whenever Wenet deals damage with a skill, all allies are healed for 60% of the damage dealt. Whenever Wenet kills an enemy with a skill she has a 100% chance to revive 1 ally (unaffected by forbidding revival effects). If an ally takes damage and is brought below 75% within the next 2 rounds, they have a 70% chance to gain a shield for 2 rounds that blocks 1 attack (this effect can trigger multiple times). If an ally is brought below 65% within the next 2 rounds, clear all their control effects and debuffs and gain immunity for 2 rounds: Freeze, Lock, Confuse, Forbidding Skill Use. If an ally is brought below 55% within the next 2 rounds, they'll be made invisible and increase the Penetration by 80%(absolute value) for 2 rounds. Lastly, you recover 100 Accumulator. At the start of battle, for every 1% of the maximum HP of all allies, the attack damage will be increased by 2%, and the S-ATK damage reduction (up to 80%) will be increased by 1.2% (the buff's effect are twice as potent for Wenet). At the start of battle, all allies have the ability to trigger the skill effect after receiving damage (the HP limit and actual skill effect of the trigger skill effect are the same as the active skill);

### Augment cost (per step)
- `+1` — 5× Ranger Chip · 100,000 money
- `+2` — 10× Ranger Chip · 200,000 money
- `+3` — 21× Ranger Chip · 300,000 money
- `+4` — 28× Ranger Chip · 500,000 money
- `+5` — 35× Ranger Chip · 800,000 money
- `+6` — 42× Ranger Chip · 10× Pandora Power Core
- `+7` — 49× Ranger Chip · 50× Pandora Power Core
- `+8` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Wenet Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Wenet Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Wenet Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Wenet Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Wenet Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Wenet Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 539 · Parvati 帕瓦娜
**Role** Ranger · **Attack** physical · **Generation** latest
**Ratings** Damage 9/10 · Defence 7/10 · Assist 7/10

### Skill panels
**Slot 1 — Eye of the Storm** (id 1568, unlocks at `+0`)
  - **Ⅰ** at `+0` — Eye of the StormⅠ (薇薇安+0，怒海潮生)
    Cross Attack, deals 360% S-ATK damage to targets. Accrues the power within the eye of the storm to create 12 Windfury Blades (12 at most). When anyone uses an attack skill, trigger 1 Windfury Blade against to 3 random targets, dealing 100% S-ATK damage (1 Windfury Blade will be expended at each trigger; cannot trigger while at 0 Windfury Blades). Windfury Blades have a 100% chance to apply 1 stack of Gale Corrosion (lasts for 2 rounds; applying it again to the same target refreshes the duration). Lastly, you recover 100 Accumulator. Gale Corrosion: Reduces the target's DEF and S-DEF by 10% per stack.
  - **Ⅱ** at `+5` — Eye of the StormⅡ (薇薇安+7，怒海潮生)
    Cross Attack, deals 380% S-ATK damage to targets. Accrues the power within the eye of the storm to create 12 Windfury Blades (12 at most). When anyone all uses an attack skill, trigger 1 Windfury Blade against to 3 random targets, dealing 120% S-ATK damage (1 Windfury Blade will be expended at each trigger; cannot trigger while at 0 Windfury Blades). Windfury Blades have an 100% chance to apply 1 stack of Gale Corrosion (lasts for 2 rounds; applying it again to the same target refreshes the duration). Lastly, you recover 100 Accumulator. Gale Corrosion: Reduces the target's DEF and S-DEF by 15% per stack and Accumulator gained from skill effects by 10% per stack.
  - **Ⅲ** at `+11` — Eye of the StormⅢ (薇薇安+13，怒海潮生)
    Cross Attack, deals 400% S-ATK damage to targets. Accrues the power within the eye of the storm to create 12 Windfury Blades (12 at most). When anyone uses an attack skill, trigger 1 Windfury Blade against to 3 random targets, dealing 140% S-ATK damage (1 Windfury Blade will be expended at each trigger; cannot trigger while at 0 Windfury Blades) and True Damage equal to 15% of the target's max HP. Windfury Blades have a 100% chance to apply 1 stack of Gale Corrosion (lasts for 2 rounds; applying it again to the same target refreshes the duration). Lastly, you recover 100 Accumulator. Gale Corrosion: Reduces the target's DEF and S-DEF by 20% per stack and Accumulator gained from skill effects by 20% per stack.
  - **Ⅳ** at `+15` — Eye of the StormIV (薇薇安+15，怒海潮生)
    Cross Attack, deals 430% S-ATK damage to targets. Accrues the power within the eye of the storm to create 12 Windfury Blades (12 at most). When anyone uses an attack skill, trigger 1 Windfury Blade against to 3 random targets, dealing 180% S-ATK damage (1 Windfury Blade will be expended at each trigger; cannot trigger while at 0 Windfury Blades) and True Damage equal to 30% of the target's max HP. Windfury Blades have a 100% chance to apply 1 stack of Gale Corrosion (lasts for 2 rounds; applying it again to the same target refreshes the duration). Lastly, you recover 100 Accumulator. Gale Corrosion: Reduces the target's DEF and S-DEF by 25% per stack and Accumulator gained from skill effects by 30% per stack.

**Slot 2 — Windfury Blades** (id 1565, unlocks at `+0`)
  - **Ⅰ** at `+0` — Windfury BladesⅠ (帕瓦娜技能2)
    (Takes effect at the start of battle) Creates 12 Windfury Blades (12 at most).
  - **Ⅱ** at `+7` — Windfury BladesⅡ (帕瓦娜技能2)
    (Takes effect at the start of battle) Creates 12 Windfury Blades (12 at most). Creates 5 Windfury Blades whenever an enemy unit is destroyed.
  - **Ⅲ** at `+T2` — Windfury BladesⅢ (帕瓦娜技能2)
    (Takes effect at the start of battle) Creates 12 Windfury Blades (12 at most). Creates 5 Windfury Blades whenever an enemy unit is destroyed. Launches 2 Windfury Blades against the attacker whenever hit by a skill attack.
  - **Ⅳ** at `+T3` — Windfury BladesIV (帕瓦娜技能2)
    (Takes effect at the start of battle) Creates 12 Windfury Blades (12 at most). Creates 5 Windfury Blades whenever an enemy unit is destroyed. Launches 3 Windfury Blades against the attacker whenever hit by a skill attack. Windfury Blades instantly destroy (ignores immunity to instant destruction and shields that grant immunity to lethal damage) enemies below 35% HP.

**Slot 3 — Avatar of Wind** (id 1566, unlocks at `+4`)
  - **Ⅰ** at `+4` — Avatar of WindⅠ (帕瓦娜技能3)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +60% ATK: +60% DMG Reduction (Absolute Value): +15% Block (Absolute Value): +15%
  - **Ⅱ** at `+9` — Avatar of WindⅡ (帕瓦娜技能3)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +90% ATK: +90% DMG Reduction (Absolute Value): +20% Block (Absolute Value): +20%
  - **Ⅲ** at `+13` — Avatar of WindⅢ (帕瓦娜技能3)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +120% ATK: +120% DMG Reduction (Absolute Value): +25% Block (Absolute Value): +25%
  - **Ⅳ** at `+T` — Avatar of WindIV (帕瓦娜技能3)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +150% ATK: +150% DMG Reduction (Absolute Value): +30% Block (Absolute Value): +30%

**Slot 4 — Gale Corrosion** (id 1567, unlocks at `+12`)
  - **Ⅰ** at `+12` — Gale CorrosionⅠ (帕瓦娜技能4)
    (Takes effect at the start of battle) The special sandstorms of [Zovras] further increase the effect of each stack of Gale Corrosion: 1 Stack: When an enemy acts to trigger damage or Accumulator reduction, the damage is increased by 50% and the Accumulator reduction is increased by 30% (applicable to Poison, Curse, Night Curse, Plague and Scorch).
  - **Ⅱ** at `+14` — Gale CorrosionⅡ (帕瓦娜技能4)
    (Takes effect at the start of battle) The special sandstorms of [Zovras] further increase the effect of each stack of Gale Corrosion: 1 Stack: When an enemy acts to trigger damage or Accumulator reduction, the damage is increased by 80% and the Accumulator reduction is increased by 50% (applicable to Poison, Curse, Night Curse, Plague and Scorch). 2 Stacks: Destroys the enemy's immunity effects and disables the enemy's CC immunity effects (Freeze, Lock and Confuse).
  - **Ⅲ** at `+T1` — Gale CorrosionⅢ (帕瓦娜技能4)
    (Takes effect at the start of battle) The special sandstorms of [Zovras] further increase the effect of each stack of Gale Corrosion: 1 Stack: When an enemy acts to trigger damage or Accumulator reduction, the damage is increased by 100% and the Accumulator reduction is increased by 70% (applicable to Poison, Curse, Night Curse, Plague and Scorch). 2 Stacks: Destroys the enemy's immunity effects and disables the enemy's CC immunity effects (Freeze, Lock and Confuse and Forbidding Skill Use).Receives 40% less Accum from Lieutenant boosts.
  - **Ⅳ** at `+T4` — Gale CorrosionIV (帕瓦娜技能4)
    (Takes effect at the start of battle) The special sandstorms of [Zovras] further increase the effect of each stack of Gale Corrosion: 1 Stack: When an enemy acts to trigger damage or Accumulator reduction, the damage is increased by 150% and the Accumulator reduction is increased by 100% (applicable to Poison, Curse, Night Curse, Plague and Scorch). 2 Stacks: Destroys the enemy's immunity effects and disables the enemy's CC immunity effects (Freeze, Lock, Confuse, Petrify, Icebound, Entangle and Forbidding Skill Use).Receives 70% less Accum from Lieutenant boosts. 3 Stacks: Cannot be revived upon death (including Rebirth).Accum boosted by Legendary Equipment are reduced by 70%

### Augment cost (per step)
- `+1` — 5× Ranger Chip · 100,000 money
- `+2` — 10× Ranger Chip · 200,000 money
- `+3` — 21× Ranger Chip · 300,000 money
- `+4` — 28× Ranger Chip · 500,000 money
- `+5` — 35× Ranger Chip · 800,000 money
- `+6` — 42× Ranger Chip · 10× Pandora Power Core
- `+7` — 49× Ranger Chip · 50× Pandora Power Core
- `+8` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Parvati Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Parvati Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Parvati Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Parvati Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Parvati Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Parvati Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 548 · Hassan 哈桑
**Role** Ranger · **Attack** physical · **Generation** old
**Ratings** Damage 9/10 · Defence 7/10 · Assist 7/10

### Signature skill
- **Ⅰ** at `+0` — Deadly Sniper (狙击)
  Cross attack, deals 350% S-ATK damage to targets. Lastly, you recover 100 Accumulator.

### Augment cost (per step)
- `+1` — 5× Ranger Chip · 100,000 money
- `+2` — 10× Ranger Chip · 200,000 money
- `+3` — 21× Ranger Chip · 300,000 money
- `+4` — 28× Ranger Chip · 500,000 money
- `+5` — 35× Ranger Chip · 800,000 money
- `+6` — 42× Ranger Chip · 10× Pandora Power Core
- `+7` — 49× Ranger Chip · 50× Pandora Power Core
- `+8` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Hassan's Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Hassan's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Hassan's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Hassan's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Hassan's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Hassan's Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 549 · Colin 柯林
**Role** Ranger · **Attack** physical · **Generation** latest
**Ratings** Damage 9/10 · Defence 7/10 · Assist 7/10

### Skill panels
**Slot 1 — Fearless Assault** (id 1631, unlocks at `+0`)
  - **Ⅰ** at `+0` — Fearless AssaultⅠ (柯林技能描述)
    During battle preparation, if placed in the first row, its skill becomes "Defensive Counterattack". If placed in the second or third row, the skill becomes "Cooperative Assault". Defensive Counterattack: When casting a skill, no attack will be launched, and Colin will enter a "Defensive Counterattack" state, lasting for 2 rounds. The next time an enemy unit casts a skill attack, Colin will be the target of the attack (Colin's teammates can be immune to attack damage), and Colin will completely absorb the upcoming skill attack damage. If Colin is not in a state of inaction, he will immediately launch a "Counterattack" (When the number of times damage can be absorbed and a counterattack triggered is 0, Colin will exit the "Defensive Counterattack" state). Lastly, recover 100 Accumulator points."Counterattack": Launches a vertical attack on the source of the attack, deducting 40% of the absorbed damage value from the target's health. (If there is no attack target, the target is dead, or in an unselectable state, Colin will launch a vertical attack on the enemy). Cooperative Assault: Vertical attack, deals 320% S-ATK damage to targets, and marks the 2 allies with the highest ATK (excluding self) for 2 rounds (the marked units will be reselected each time a skill is cast). After they cast their next skill, if Colin is not in a state of inaction, there is a 50% chance to trigger a "Cooperative Assault". Lastly, recover 100 Accumulator points."Cooperative Assault": Launches a vertical attack on the attack target of the marked units, dealing 320% S-ATK damage (If there is no attack target or the target is dead, Colin will launch a vertical attack). (If there is no attack target, the target is dead, or in an unselectable state, Colin will launch a vertical attack on the enemy).
  - **Ⅱ** at `+7` — Fearless AssaultⅡ (柯林技能描述)
    During battle preparation, if placed in the first row, its skill becomes "Defensive Counterattack". If placed in the second or third row, the skill becomes "Cooperative Assault". Defensive Counterattack: When casting a skill, no attack will be launched, and Colin will enter a "Defensive Counterattack" state, lasting for 2 rounds. The next time an enemy unit casts a skill attack, Colin will be the target of the attack (Colin's teammates can be immune to attack damage), and Colin will completely absorb the upcoming skill attack damage. If Colin is not in a state of inaction, he will immediately launch a "Counterattack" (When the number of times damage can be absorbed and a counterattack triggered is 0, Colin will exit the "Defensive Counterattack" state).Recovers 40% of max HP for all allies. Lastly, you recover 100 Accumulator."Counterattack": Launches a vertical attack on the source of the attack, deducting 60% of the absorbed damage value from the target's health. (If there is no attack target, the target is dead, or in an unselectable state, Colin will launch a vertical attack on the enemy). Cooperative Assault: Vertical attack, deals 340% S-ATK damage to targets, and marks the 2 allies with the highest ATK (excluding self) for 2 rounds (the marked units will be reselected each time a skill is cast). After they cast their next skill, if Colin is not in a state of inaction, there is a 50% chance to trigger a "Cooperative Assault".Grants self and marked units Guaranteed Hit for 2 rounds. Lastly, recover 100 Accumulator."Cooperative Assault": Launches a vertical attack on the attack target of the marked units, dealing 340% S-ATK damage (If there is no attack target, the target is dead, or in an unselectable state, Colin will launch a vertical attack on the enemy).
  - **Ⅲ** at `+13` — Fearless AssaultⅢ (柯林技能描述)
    During battle preparation, if placed in the first row, its skill becomes "Defensive Counterattack". If placed in the second or third row, the skill becomes "Cooperative Assault". Defensive Counterattack: When casting a skill, no attack will be launched, and Colin will enter a "Defensive Counterattack" state, lasting for 2 rounds. The next time an enemy unit casts a skill attack, Colin will be the target of the attack (Colin's teammates can be immune to attack damage), and Colin will completely absorb the upcoming skill attack damage. If Colin is not in a state of inaction, he will immediately launch a "Counterattack" (When the number of times damage can be absorbed and a counterattack triggered is 0, Colin will exit the "Defensive Counterattack" state).Restores 40% of Max HP for all allies. Lastly, you recover 100 Accumulator."Counterattack": Launches a vertical attack on the source of the attack, deducting 80% of the absorbed damage value from the target's health. (If there is no attack target, the target is dead, or in an unselectable state, Colin will launch a vertical attack on the enemy). Cooperative Assault: Vertical attack, deals 360% S-ATK damage to targets, and marks the 2 allies with the highest ATK (excluding self) for 2 rounds (the marked units will be reselected each time a skill is cast). After they cast their next skill, if Colin is not in a state of inaction, there is a 75% chance to trigger a "Cooperative Assault".Grants itself and the marked unit a guaranteed hit and a guaranteed defense break, lasting 2 rounds. Finally restore 100 points of energy.[Cooperation]: Launch a vertical attack on the target of the marked unit, causing 360% skill damage (if there is no attack target, the target is dead or cannot be selected, Colin will launch a vertical attack on the enemy).
  - **Ⅳ** at `+15` — Fearless AssaultIV (柯林技能描述)
    When preparing for battle, if it is placed in the 1st row, its skill becomes [Defense Counterattack]. If it is placed in the 2nd and 3rd rows, its skill becomes [Assault Assault]. Defensive Counterattack: When casting a skill, it will not launch an attack, putting itself into a [Defensive Counterattack] state, which lasts for 2 rounds. The next time the enemy unit casts a skill attack, it will target Colin (Colin's teammates can Immune to attack damage), and Colin will completely absorb the upcoming skill attack damage. If Colin is not in an incapacitated state, he will immediately launch [Counterattack] (when the number of times that can absorb damage and trigger counterattacks is 0, he will Exit the [Defense and Counterattack] state).Restores 40% of the maximum HP of all allies. Makes all allies immune to freezing, confusion, locking, petrification, freezing, entangling, prohibiting the use of skills, and weakening for 2 rounds. Finally restore 100 points of energy.[Counterattack]: Launch a vertical attack at the source of the attack, deducting the hit target's HP equal to 100% of the damage absorbed this time. (If there is no target to attack, the target is dead or cannot be selected, Colin will launch a vertical attack on the enemy). Coordinated Assault: Vertical attack, first absorb 50% of the attack target's energy, then cause 400% skill damage to the hit target, and mark the 2 units with the highest attack power except yourself (the marked units will be re-selected each time you cast a skill) Lasts for 2 rounds. After the next skill is cast, if Colin is not unable to move, there is a 100% probability of launching [Cooperation].Grants itself and the marked unit a guaranteed hit and a guaranteed defense break, and increases the damage caused by 30% for 2 rounds. Finally restore 100 points of energy.[Cooperation]: Launch a vertical attack on the target of the marked unit, first absorbing 50% of the attack target's energy, and then causing 400% of skill damage (if there is no attack target, the target is dead or cannot be selected, Colin will Launch a vertical attack against the enemy).

**Slot 2 — Balanced Offense and Defense** (id 1632, unlocks at `+3`)
  - **Ⅰ** at `+3` — Balanced Offense and DefenseⅠ (柯林技能描述)
    (Takes effect at the start of battle) Each time you enter the [Assisted Raid] state, the damage caused by all allies will be increased by 50%, lasting for 2 rounds;Each time you enter the [Defense Counterattack] state, the damage reduction of all allies is increased by 50%, lasting for 2 rounds.
  - **Ⅱ** at `+9` — Balanced Offense and DefenseⅡ (柯林技能描述)
    (Takes effect at the start of battle) Each time you enter the [Assisted Raid] state, the damage caused by all allies will be increased by 50%, lasting for 2 rounds;Each time you enter the [Defense Counterattack] state, the damage reduction of all allies is increased by 50%, lasting for 2 rounds. [Assisted Raid] is changed to mark the 3 units with the highest attack power of one's side, and the number of times [Defensive Counterattack] absorbs damage and triggers counterattacks is changed to 2 times.
  - **Ⅲ** at `+T1` — Balanced Offense and DefenseⅢ (柯林技能描述)
    (Takes effect at the start of battle) Each time you enter the [Assisted Raid] state, the damage caused by all allies will be increased by 50%, lasting for 2 rounds;Each time you enter the [Defense Counterattack] state, the damage reduction of all allies is increased by 50%, lasting for 2 rounds. [Assisted Raid] is changed to mark the 3 units with the highest attack power of one's side, and the number of times [Defensive Counterattack] absorbs damage and triggers counterattacks is changed to 2 times. When launching a cooperative battle and the marked unit launches a skill attack, the attack damage will be increased by 2% for every 1% of the target's maximum HP lost;The skill attack launched by counterattack is increased to deduct the hit target's HP equal to 150% of the absorbed damage value.
  - **Ⅳ** at `+T4` — Balanced Offense and DefenseIV (柯林技能描述)
    (Takes effect at the start of battle) Each time you enter the [Assisted Raid] state, the damage caused by all allies will be increased by 50%, lasting for 2 rounds;Each time you enter the [Defense Counterattack] state, the damage reduction of all allies is increased by 50%, lasting for 2 rounds. [Assisted Raid] is changed to mark the 3 units with the highest attack power of one's side, and the number of times [Defensive Counterattack] absorbs damage and triggers counterattacks is changed to 2 times. When launching a cooperative battle and the marked unit launches a skill attack, the attack damage will be increased by 2% for every 1% of the target's maximum HP lost;The skill attack launched by counterattack is increased to deduct the hit target's HP equal to 150% of the absorbed damage value. Each time you cast [Assisted Raid], you and the marked unit will be cleared of their own control effects (freezing, locking, chaos, petrification, freezing, entangling, prohibiting the casting of skills, and weakening) before the next action, and then take subsequent actions. ;Each time [Defense Counterattack] is cast, 3 random units of your own will be resurrected and their HP and energy storage will be restored to 100% of the initial state.

**Slot 3 — Body of Steel** (id 1633, unlocks at `+5`)
  - **Ⅰ** at `+5` — Body of SteelⅠ (柯林技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP +60% Damage increase (absolute value) +15% Damage reduction (absolute value) +15%
  - **Ⅱ** at `+11` — Body of SteelⅡ (柯林技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP +90% Damage increase (absolute value) +20% Damage reduction (absolute value) +20%
  - **Ⅲ** at `+T2` — Body of SteelⅢ (柯林技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP +120% Damage increase (absolute value) +25% Damage reduction (absolute value) +25%
  - **Ⅳ** at `+T3` — Body of SteelIV (柯林技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP +150% Damage increase (absolute value) +30% Damage reduction (absolute value) +30%

### Augment cost (per step)
- `+1` — 5× Ranger Chip · 100,000 money
- `+2` — 10× Ranger Chip · 200,000 money
- `+3` — 21× Ranger Chip · 300,000 money
- `+4` — 28× Ranger Chip · 500,000 money
- `+5` — 35× Ranger Chip · 800,000 money
- `+6` — 42× Ranger Chip · 10× Pandora Power Core
- `+7` — 49× Ranger Chip · 50× Pandora Power Core
- `+8` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Colin Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Colin Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Colin Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Colin Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Colin Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Colin Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 552 · Eluma 艾露玛
**Role** Ranger · **Attack** physical · **Generation** latest
**Ratings** Damage 9/10 · Defence 7/10 · Assist 7/10

### Skill panels
**Slot 1 — Stealth Shadow Strike** (id 1651, unlocks at `+0`)
  - **Ⅰ** at `+0` — Stealth Shadow StrikeⅠ (艾露玛技能描述)
    Cross Attack, deals 320% S-ATK damage to targets. Has a 50% chance to apply [Assassination Mark] to a random enemy, lasting for 3 rounds, with a maximum of 1 Mark at the same time. Lastly, you recover 100 Accumulator. Assassination Mark: Prevents the targeted unit from healing and recovering HP through healing and recovery effects (Excluding HP recovery from attacks and kills), and when affected by control effects (Freeze, Lock, Confuse), their immunity and protection effects will not trigger.
  - **Ⅱ** at `+6` — Stealth Shadow StrikeⅡ (艾露玛技能描述)
    Cross Attack, deals 340% S-ATK damage to targets. Has a 75% chance to apply [Assassination Mark] to a random enemy for 3 rounds, with a maximum of 1 Mark at the same time. Self becomes invisible, and will not lose invisibility for as long as there is another allied alive (can be seen by Eye of True Sight) for 2 rounds. Lastly, you recover 100 Accumulator. Assassination Mark: Prevents the marked target from restoring HP through healing and recovery effects (Excluding HP recovery from attacks and kills), and when the target is under crowd-control effects (Freeze, Lock, Confuse, Petrify, Icebound, Entangle), their immunity and protective effects will not activate.
  - **Ⅲ** at `+10` — Stealth Shadow StrikeⅢ (艾露玛技能描述)
    Cross Attack, deals 360% S-ATK damage to targets. Has a 100% chance to apply [Assassination Mark] to a random enemy for 5 rounds, with a maximum of 1 Mark at the same time.Self becomes invisible, and will not lose invisibility for as long as there is another allied alive (can be seen by Eye of True Sight) for 2 rounds. Self gains Eye of True Sight for 99 rounds. Lastly, recovers 100 Accumulator. Assassination Mark: Prevents the marked target unit from restoring HP through healing and recovery effects, and when the target is under crowd-control effects (Freeze, Lock, Confuse, Petrify, Icebound, Entangle, Forbidding Skill Use and Weaken), their immunity and protection effects will not be triggered.
  - **Ⅳ** at `+15` — Stealth Shadow StrikeⅣ (艾露玛技能描述)
    Cross Attack, deals 400% S-ATK damage to targets. There's a 100% chance to apply [Assassination Mark] to a random enemy for 5 rounds, with a maximum of 1 Mark at the same time.Self becomes invisible, and will not lose invisibility for as long as there is another allied alive (can be seen by Eye of True Sight). Eluma gains [Shadow Strike], lasting for 2 rounds. [Estrange] affects all enemies, preventing them from triggering Lieutenant skills for 2 rounds. Lastly, recovers 100 Accumulator. Assassination Mark: Prevents the marked target from restoring HP through healing and recovery effects, and when the target is under crowd-control effects (Freeze, Lock, Confuse, Petrify, Icebound, Entangle, Forbidding Skill Use and Weaken), their immunity and protective effects will not activate. Shadow Strike: Gain 1 raid attempt: When a friendly unit other than oneself takes S-ATK damage from an enemy, a raid is triggered, first plundering 30% Accumulator from all enemies, then dealing 500% S-ATK damage to a random unit with [Assassination Mark].

**Slot 2 — Assassination Mark** (id 1652, unlocks at `+2`)
  - **Ⅰ** at `+2` — Assassination MarkⅠ (艾露玛技能描述)
    (Takes effect at the start of battle) During the duration of [Assassination Mark], the marked target takes 30% increased damage.
  - **Ⅱ** at `+9` — Assassination MarkⅡ (艾露玛技能描述)
    (Takes effect at the start of battle) During the duration of [Assassination Mark], the marked target takes 30% increased damage. [Assassination Mark] is now applied to 2 random enemies, with a maximum of 2 Marks at the same time.
  - **Ⅲ** at `+12` — Assassination MarkⅢ (艾露玛技能描述)
    (Takes effect at the start of battle) During the duration of [Assassination Mark], the marked target takes 30% increased damage. [Assassination Mark] is now applied to 2 random enemies, with a maximum of 2 Marks at the same time. Applies the [Assassination Mark] on targets, causing any healing and recovery effects (excluding attack recovery and kill recovery,Lieutenant, and Legendary equipment effects) to instead deal damage equal to 80% of the HP that would have been recovered.
  - **Ⅳ** at `+T3` — Assassination MarkⅣ (艾露玛技能描述)
    (Takes effect at the start of battle) During the duration of [Assassination Mark], the marked target takes 30% increased damage. [Assassination Mark] is now applied to 2 random enemies, with a maximum of 2 Marks at the same time. Applies the [Assassination Mark] on targets, causing any healing and recovery effects (excluding attack recovery and kill recovery,Lieutenant, and Legendary equipment effects) to instead deal damage equal to 80% of the HP that would have been recovered. During the duration of [Assassination Mark], the crowd-control effects (Freeze, Lock, Confuse, Petrify, Icebound, Entangle, Forbidding Skill Use and Weaken) on the marked target cannot be cleansed.

**Slot 3 — Physical Exercise** (id 1653, unlocks at `+4`)
  - **Ⅰ** at `+4` — Physical ExerciseⅠ (艾露玛技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +60% S-ATK: +60% DMG Bonus (Absolute Value): +15% Dodge (Absolute Value): +30%
  - **Ⅱ** at `+8` — Physical ExerciseⅡ (艾露玛技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +90% S-ATK: +90% DMG Bonus (Absolute Value): +20% Dodge (Absolute Value): +40%
  - **Ⅲ** at `+13` — Physical ExerciseⅢ (艾露玛技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +120% S-ATK: +120% DMG Bonus (Absolute Value): +25% Dodge (Absolute Value): +50%
  - **Ⅳ** at `+T` — Physical ExerciseⅣ (艾露玛技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +150% S-ATK: +150% DMG Bonus (Absolute Value): +30% Dodge (Absolute Value): +60%

**Slot 4 — Shadow Strike** (id 1654, unlocks at `+T`)
  - **Ⅰ** at `+T` — Shadow StrikeⅠ (艾露玛技能描述)
    (Takes effect at the start of battle) Each time you activate [Shadow Strike], the number of times you can launch a raid attempt becomes 3.
  - **Ⅱ** at `+T1` — Shadow StrikeⅡ (艾露玛技能描述)
    (Takes effect at the start of battle) Each time you activate [Shadow Strike], the number of times you can launch a raid attempt becomes 3. [Shadow Strike] Units killed by a raid attack cannot revive or rebirth.
  - **Ⅲ** at `+T2` — Shadow StrikeⅢ (艾露玛技能描述)
    (Takes effect at the start of battle) Each time you activate [Shadow Strike], the number of times you can launch a raid attempt becomes 3. [Shadow Strike] Units killed by a raid attack cannot revive or rebirth. Raid attacks always result in critical hits and Penetration definitely.
  - **Ⅳ** at `+T4` — Shadow StrikeⅣ (艾露玛技能描述)
    (Takes effect at the start of battle) Each time you activate [Shadow Strike], the number of times you can launch a raid attempt becomes 3. [Shadow Strike] Units killed by a raid attack cannot revive or rebirth. Raid attacks always result in critical hits and Penetration definitely. Upon activating [Shadow Strike], when an enemy next uses a skill, Eluma can block the skill's attack damage and launch a raid on a random enemy with [Assassination Mark], dealing 500% S-ATK damage plus an extra 150% of the blocked damage.

### Augment cost (per step)
- `+1` — 5× Ranger Chip · 100,000 money
- `+2` — 10× Ranger Chip · 200,000 money
- `+3` — 21× Ranger Chip · 300,000 money
- `+4` — 28× Ranger Chip · 500,000 money
- `+5` — 35× Ranger Chip · 800,000 money
- `+6` — 42× Ranger Chip · 10× Pandora Power Core
- `+7` — 49× Ranger Chip · 50× Pandora Power Core
- `+8` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Horus Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Horus Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Horus Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Horus Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Horus Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Horus Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 563 · Coliver 柯利弗
**Role** Ranger · **Attack** physical · **Generation** latest
**Ratings** Damage 9/10 · Defence 5/10 · Assist 6/10

### Skill panels
**Slot 1 — Fission Orbital Cannon** (id 1716, unlocks at `+0`)
  - **Ⅰ** at `+0` — Fission Orbital CannonⅠ (柯利弗技能描述)
    Cross Attack, deals 280% S-ATK damage to hit targets. Absorbs 35% of the target's DEF and S-DEF for 2 rounds. Applies "Lethal Link" to 2 random enemies; if there are already 2 linked enemies, no additional links are applied, lasting for 2 rounds. Lastly, recovers 100 Accumulator. Lethal Link: When a linked enemy is affected by control effects (Freeze, Lock, Confuse), the same effects are applied to other connected enemies (ignoring immunity effects).
  - **Ⅱ** at `+7` — Fission Orbital CannonⅡ (柯利弗技能描述)
    Cross Attack, deals 300% S-ATK damage to hit targets. Absorbs 45% of the target's DEF and S-DEF for 2 rounds. Reduces the target's Accumulator by 30%. Applies "Lethal Link" to 2 random enemies; if there are already 2 linked enemies, no additional links are applied, lasting for 2 rounds. Lastly, recovers 100 Accumulator. Lethal Link: When a linked enemy is affected by control effects (Freeze, Lock, Confuse, Forbidding Skill Use), the same effects are applied to other connected enemies (ignoring immunity effects).
  - **Ⅲ** at `+13` — Fission Orbital CannonⅢ (柯利弗技能描述)
    Cross Attack, deals 320% S-ATK damage to hit targets. Absorbs 55% of the target's DEF and S-DEF for 2 rounds. Reduces the target's Accumulator by 40%. Applies "Lethal Link" to 2 random enemies; if there are already 2 linked enemies, no additional links are applied, lasting for 2 rounds. Lastly, recovers 100 Accumulator. Lethal Link: When a linked enemy is affected by control effects (Freeze, Lock, Confuse, Forbidding Skill Use, Petrify, Icebound, Entangle), the same effects are applied to other connected enemies (ignoring immunity effects).
  - **Ⅳ** at `+15` — Fission Orbital CannonIV (柯利弗技能描述)
    Cross Attack, deals 350% S-ATK damage to hit targets. Absorbs 75% of the targets' DEF and S-DEF for 2 rounds. Reduces the targets' Accumulator by 50% (ignores immunity). Applies "Lethal Link" to 2 random enemies; if there are already 2 linked enemies, no additional links are applied, lasting for 2 rounds. Lastly, recovers 100 Accumulator. Lethal Link: When a linked enemy is affected by control effects (Freeze, Lock, Confuse, Forbidding Skill Use, Petrify, Icebound, Entangle), the same effects are applied to other connected enemies (ignoring immunity effects). When a linked ship takes S-ATK damage, it inflicts True Damage equal to 50% of the damage received to other linked enemies.

**Slot 2 — Lethal Link** (id 1717, unlocks at `+3`)
  - **Ⅰ** at `+3` — Lethal LinkⅠ (柯利弗技能描述)
    (Takes effect at the start of battle) When casting a skill that applies [Lethal Link], an additional enemy is selected, with priority given to the enemy with the highest S-ATK.
  - **Ⅱ** at `+9` — Lethal LinkⅡ (柯利弗技能描述)
    (Takes effect at the start of battle) When casting a skill that applies [Lethal Link], an additional enemy is selected, with priority given to the enemy with the highest S-ATK. At the start of battle, applies "Lethal Link" to 2 random enemies for 2 rounds.
  - **Ⅲ** at `+T3` — Lethal LinkⅢ (柯利弗技能描述)
    (Takes effect at the start of battle) When casting a skill that applies [Lethal Link], an additional enemy is selected, with priority given to the enemy with the highest S-ATK. At the start of battle, applies "Lethal Link" to 2 random enemies for 2 rounds. When Coliver is affected by control effects (Freeze, Lock, Confuse, Forbidding Skill Use, Petrify, Icebound, Entangle), he will apply the same effects to the enemies with the Lethal Link (ignoring immunity effects).
  - **Ⅳ** at `+T4` — Lethal LinkIV (柯利弗技能描述)
    (Takes effect at the start of battle) When casting a skill that applies [Lethal Link], an additional enemy is selected, with priority given to the enemy with the highest S-ATK. At the start of battle, applies "Lethal Link" to 2 random enemies for 2 rounds. When Coliver is affected by control effects (Freeze, Lock, Confuse, Forbidding Skill Use, Petrify, Icebound, Entangle), he will apply the same effects to the enemies with the Lethal Link (ignoring immunity effects). When using a skill, if there are already 3 enemies with [Lethal Link] (or if there are fewer than 3 enemies remaining and all have [Lethal Link]), there is a 70% chance to instantly kill all enemies with [Lethal Link] (probability calculated individually for each ship, ignoring immunity to instant destruction) , then [Lethal Link] is applied to enemies (applied in the same manner as when using a skill).

**Slot 3 — Fission Armament** (id 1718, unlocks at `+5`)
  - **Ⅰ** at `+5` — Fission ArmamentⅠ (柯利弗技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP +60% Damage increase (absolute value) +15% Damage reduction (absolute value) +15%
  - **Ⅱ** at `+11` — Fission ArmamentⅡ (柯利弗技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP +90% Damage increase (absolute value) +20% Damage reduction (absolute value) +20%
  - **Ⅲ** at `+T1` — Fission ArmamentⅢ (柯利弗技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP +120% Damage increase (absolute value) +25% Damage reduction (absolute value) +25%
  - **Ⅳ** at `+T2` — Fission ArmamentIV (柯利弗技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP +150% Damage increase (absolute value) +30% Damage reduction (absolute value) +30%

### Augment cost (per step)
- `+1` — 5× Ranger Chip · 100,000 money
- `+2` — 10× Ranger Chip · 200,000 money
- `+3` — 21× Ranger Chip · 300,000 money
- `+4` — 28× Ranger Chip · 500,000 money
- `+5` — 35× Ranger Chip · 800,000 money
- `+6` — 42× Ranger Chip · 10× Pandora Power Core
- `+7` — 49× Ranger Chip · 50× Pandora Power Core
- `+8` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Coliver's Parts · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Coliver's Parts · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Coliver's Parts · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Coliver's Parts · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Coliver's Parts · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Coliver's Parts · 140× Alien Essence · 140× Transcendence Core

---

## 564 · Kelly 凯莉
**Role** Ranger · **Attack** physical · **Generation** old
**Ratings** Damage 6/10 · Defence 8/10 · Assist 9/10

### Signature skill
- **Ⅰ** at `+0` — Flame Assault (烈焰冲击)
  Cross Attack, deals 200% S-ATK damage to targets. Lastly, you recover 100 Accumulator.

### Augment cost (per step)
- `+1` — 5× Rover Chip · 100,000 money
- `+2` — 10× Rover Chip · 200,000 money
- `+3` — 21× Rover Chip · 300,000 money
- `+4` — 28× Rover Chip · 500,000 money
- `+5` — 35× Rover Chip · 800,000 money
- `+6` — 42× Rover Chip · 10× Pandora Power Core
- `+7` — 49× Rover Chip · 50× Pandora Power Core
- `+8` — 49× Rover Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Rover Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Rover Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Rover Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Rover Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Rover Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Rover Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Rover Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Kelly's Parts · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Kelly's Parts · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Kelly's Parts · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Kelly's Parts · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Kelly's Parts · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Kelly's Parts · 140× Alien Essence · 140× Transcendence Core

---

## 566 · Syllabear 塞拉比尔
**Role** Ranger · **Attack** physical · **Generation** latest
**Ratings** Damage 8/10 · Defence 7/10 · Assist 7/10

### Skill panels
**Slot 1 — Enraged Roar** (id 1732, unlocks at `+0`)
  - **Ⅰ** at `+0` — Enraged RoarⅠ (塞拉贝尔技能描述)
    Without using S-ATK, applies [Fury Mark] to 1 random enemy. Only 1 enemy can have [Fury Mark] at a time, lasting for 99 rounds. Lastly, recovers 100 Accumulator. Fury Mark: The affected target will attack Syllabear prioritize (effect takes precedence over Unyielding), and his damage dealt will reduce by 20%.
  - **Ⅱ** at `+5` — Enraged RoarⅡ (塞拉贝尔技能描述)
    Without using S-ATK, applies [Fury Mark] to 1 random enemy, with a maximum of 1 enemy affected, lasting for 99 rounds. Lastly, recovers 100 Accumulator. Fury Mark: The affected target will attack Syllabear prioritize (effect takes precedence over Unyielding), and his damage dealt will reduce by 30%. After the marked target acts, Syllabear will use Counterattack. Counterattack: Absorbs 40% of the target's S-ATK for 2 rounds, then deals 350% S-ATK damage to the enemy with Fury Mark. Lastly, recovers 100 Accumulator.
  - **Ⅲ** at `+9` — Enraged RoarⅢ (塞拉贝尔技能描述)
    Without using S-ATK, applies [Fury Mark] to 1 random enemy, with a maximum of 1 enemy affected, lasting for 99 rounds. Increases damage dealt by all allies by 30% for 2 rounds. Lastly, recovers 100 Accumulator. Fury Mark: The affected target will attack Syllabear prioritize (effect takes precedence over Unyielding), and his damage dealt will reduce by 40%. After the marked target acts, Syllabear will counter with a skill. Counterattack: Absorbs 40% of the target's S-ATK for 2 rounds, then deals 400% S-ATK damage to the enemy with Fury Mark. Lastly, recovers 100 Accumulator.
  - **Ⅳ** at `+15` — Enraged RoarIV (塞拉贝尔技能描述)
    Without using S-ATK, applies [Fury Mark] to 1 random enemy, with a maximum of 1 enemy affected, lasting for 99 rounds. Increases damage dealt by all allies by 40% for 2 rounds. Lastly, recovers 100 Accumulator. Fury Mark: The affected target will attack Syllabear prioritize (effect takes precedence over Unyielding), and his damage dealt will reduce by 50%. After the marked target acts, Syllabear will counter with a skill. Counterattack: Absorb 50% of the target's S-ATK (lasting 2 rounds) and 50% Accumulator (ignores immunity effects), then deal 450% S-ATK damage to the enemy with the Fury Mark. Lastly, recovers 100 Accumulator.

**Slot 2 — Fury Mark** (id 1733, unlocks at `+2`)
  - **Ⅰ** at `+2` — Fury MarkⅠ (塞拉贝尔技能描述)
    (Takes effect at the start of battle) Targets with the "Fury Mark" take 30% more damage.
  - **Ⅱ** at `+7` — Fury MarkⅡ (塞拉贝尔技能描述)
    (Takes effect at the start of battle) Targets with the "Fury Mark" take 30% more damage. At the start of battle, applies [Fury Mark] to 1 random enemy for 99 rounds.
  - **Ⅲ** at `+11` — Fury MarkⅢ (塞拉贝尔技能描述)
    (Takes effect at the start of battle) Targets with the "Fury Mark" take 30% more damage. At the start of battle, applies [Fury Mark] to 1 random enemy for 99 rounds. When Syllabear applies [Fury Mark] and uses a skill, he will remove the Rebirth effect from the target.
  - **Ⅳ** at `+T3` — Fury MarkIV (塞拉贝尔技能描述)
    (Takes effect at the start of battle) Targets with the "Fury Mark" take 30% more damage. At the start of battle, applies [Fury Mark] to 1 random enemy for 99 rounds. When Syllabear applies [Fury Mark] and uses a skill, he will remove the Rebirth effect from the target. Ships with [Fury Mark] take damage equal to 80% of the healing and recovery effects they receive (excluding recovery from attacks, kills, Lieutenant, and legendary equipment).

**Slot 3 — Physical Exercise** (id 1734, unlocks at `+3`)
  - **Ⅰ** at `+3` — Physical ExerciseⅠ (塞拉贝尔技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +60% S-ATK: +60% DMG Bonus (Absolute Value): +15% Dodge (Absolute Value): +30%
  - **Ⅱ** at `+8` — Physical ExerciseⅡ (塞拉贝尔技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +90% S-ATK: +90% DMG Bonus (Absolute Value): +20% Dodge (Absolute Value): +40%
  - **Ⅲ** at `+13` — Physical ExerciseⅢ (塞拉贝尔技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +120% S-ATK: +120% DMG Bonus (Absolute Value): +25% Dodge (Absolute Value): +50%
  - **Ⅳ** at `+T` — Physical ExerciseIV (塞拉贝尔技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +150% S-ATK: +150% DMG Bonus (Absolute Value): +30% Dodge (Absolute Value): +60%

**Slot 4 — Fury Strike** (id 1735, unlocks at `+10`)
  - **Ⅰ** at `+10` — Fury StrikeⅠ (塞拉贝尔技能描述)
    (Takes effect at the start of battle) Counterattack triggered by [Fury Mark] becomes True Damage, ignoring the target's DEF and S-DEF.
  - **Ⅱ** at `+T1` — Fury StrikeⅡ (塞拉贝尔技能描述)
    (Takes effect at the start of battle) Counterattack triggered by [Fury Mark] becomes True Damage, ignoring the target's DEF and S-DEF. When a ship with [Fury Mark] dies, Syllabear immediately casts a skill, applying [Fury Mark] to a random enemy.
  - **Ⅲ** at `+T2` — Fury StrikeⅢ (塞拉贝尔技能描述)
    (Takes effect at the start of battle) Counterattack triggered by [Fury Mark] becomes True Damage, ignoring the target's DEF and S-DEF. When a ship with [Fury Mark] dies, Syllabear immediately casts a skill, applying [Fury Mark] to a random enemy. When a ship with [Fury Mark] attacks, Syllabear can absorb damage equal to 300% of S-ATK at the start of battle, and when counterattacking, he deals additional S-ATK damage equal to 100% of the absorbed damage.
  - **Ⅳ** at `+T4` — Fury StrikeIV (塞拉贝尔技能描述)
    (Takes effect at the start of battle) Counterattack triggered by [Fury Mark] becomes True Damage, ignoring the target's DEF and S-DEF. When a ship with [Fury Mark] dies, Syllabear immediately casts a skill, applying [Fury Mark] to a random enemy. When a ship with [Fury Mark] attacks, Syllabear can absorb damage equal to 300% of S-ATK at the start of battle, and when counterattacking, he deals additional S-ATK damage equal to 100% of the absorbed damage. At most 2 enemies can be afflicted with [Fury Mark] at the same time, and when applying or triggering counterattack skills, ships in invisible and Dark Conceal can be targeted.

### Augment cost (per step)
- `+1` — 5× Ranger Chip · 100,000 money
- `+2` — 10× Ranger Chip · 200,000 money
- `+3` — 21× Ranger Chip · 300,000 money
- `+4` — 28× Ranger Chip · 500,000 money
- `+5` — 35× Ranger Chip · 800,000 money
- `+6` — 42× Ranger Chip · 10× Pandora Power Core
- `+7` — 49× Ranger Chip · 50× Pandora Power Core
- `+8` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Syllabear's Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Syllabear's Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Syllabear's Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Syllabear's Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Syllabear's Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Syllabear's Part · 140× Alien Essence · 140× Transcendence Core

---

## 569 · Antandra 安丹德拉
**Role** Ranger · **Attack** physical · **Generation** latest
**Ratings** Damage 9/10 · Defence 7/10 · Assist 7/10

### Skill panels
**Slot 1 — Energy Reversal** (id 1746, unlocks at `+0`)
  - **Ⅰ** at `+0` — Energy ReversalⅠ (安丹德拉技能描述)
    Cross Attack, first plunders 30% Accumulator from the target, then deals 320% S-ATK damage to the target. Gains Eye of True Sight and [Reversal Shield] for 2 rounds. The hero is immune to instant destruction for 2 rounds. Lastly, recovers 100 Accumulator. [Reversal Shield]: While active, if damage taken exceeds 50% of Max HP, the excess damage is negated (maximum damage taken is 50% of Max. HP). It can trigger up to 2 times with each application, and the number of triggers is Reset when applied again.
  - **Ⅱ** at `+5` — Energy ReversalⅡ (安丹德拉技能描述)
    Cross Attack, first plunders 40% Accumulator from the target, then deals 340% S-ATK damage to the target. Increases your own Penetration by 100% (absolute value) for 2 rounds. Gains Eye of True Sight and [Reversal Shield] for 2 rounds. The hero is immune to instant destruction for 2 rounds. Lastly, recovers 100 Accumulator. [Reversal Shield]: While active, if damage taken exceeds 40% of Max HP, the excess damage is negated (maximum damage taken is 40% of Max. HP). It can trigger up to 2 times with each application, and the number of triggers is Reset when applied again.
  - **Ⅲ** at `+9` — Energy ReversalⅢ (安丹德拉技能描述)
    Cross Attack, first plunders 50% Accumulator from the target, then deals 360% S-ATK damage to the hit target. Each of our ships recovers HP equal to 50% of the total damage dealt.Increases own Penetration by 120% (absolute value) for 2 rounds. Gains Eye of True Sight and [Reversal Shield] for 2 rounds. The hero is immune to instant destruction for 2 rounds. Lastly, recovers 100 Accumulator. [Reversal Shield]: While active, if damage taken exceeds 30% of Max HP, the excess damage is negated (maximum damage taken is 30% of Max. HP). It can trigger up to 2 times with each application, and the number of triggers is Reset when applied again.
  - **Ⅳ** at `+15` — Energy ReversalIV (安丹德拉技能描述)
    Cross Attack, first plunders 50% Accumulator from the target, then deals 400% S-ATK damage to the hit target. Each of our ships recovers HP equal to 50% of the total damage dealt.Increases own Penetration by 130% (absolute value) for 2 rounds. Gains Eye of True Sight and [Reversal Shield] for 2 rounds. The hero is immune to instant destruction for 2 rounds. Lastly, recovers 100 Accumulator. At the start of battle, gains [Energy Nexus], lasting until the end of combat. [Reversal Shield]: While active, if damage taken exceeds 30% of Max HP, the excess damage is negated (maximum damage taken is 30% of Max. HP). It can trigger up to 2 times with each application, and the number of triggers is Reset when applied again. [Energy Nexus]: Each time the hero or an enemy uses a skill, it gains 1 charge. Upon reaching 4 charges, the next time skill will become [Crystal Core Burst], after which all charges are reset. [Crystal Core Burst]: Cross attack, first plunders 50% Accumulator from the target (not affected by immunity), then deals 450% S-ATK damage to the hit target, with an additional True Damage equal to 100% of the total S-ATK damage dealt by Antandra during CHARGE (the extra damage gained during CHARGE and from Reversal Shield cannot exceed 800% of Antandra's S-ATK at the start of battle).S-ATK has Hunter Focus (The attack always hits, ignores Dodge, Evasive and Time Ward) and guaranteed Penetration (cannot be Blocked) effects. Lastly, recovers 100 Accumulator.

**Slot 2 — Reversal Shield** (id 1747, unlocks at `+2`)
  - **Ⅰ** at `+2` — Reversal ShieldⅠ (安丹德拉技能描述)
    (Takes effect at the start of battle) [Reversal Shield] During its effect, transfers control effects (Freeze, Lock, Confuse) targeting self to a random enemy.
  - **Ⅱ** at `+7` — Reversal ShieldⅡ (安丹德拉技能描述)
    (Takes effect at the start of battle) [Reversal Shield] During its effect, transfers control effects (Freeze, Lock, Confuse, Forbidding Skill Use) targeting self to a random enemy. [Reversal Shield] The excess damage blocked is logged, and when Antandra uses [Crystal Core Burst], it will additionally deals true damage equal to 100% of the logged damage.
  - **Ⅲ** at `+12` — Reversal ShieldⅢ (安丹德拉技能描述)
    (Takes effect at the start of battle) [Reversal Shield] During its active period, transfers control effects (Freeze, Lock, Confuse, Forbidding Skill Use, Petrify, Icebound, Entangle) targeting self to a random enemy. [Reversal Shield] The excess damage blocked is logged, and when Antandra uses [Crystal Core Burst], it will additionally deals true damage equal to 100% of the logged damage. At the start of battle, gains [Reversal Shield] for 2 rounds.
  - **Ⅳ** at `+T3` — Reversal ShieldIV (安丹德拉技能描述)
    (Takes effect at the start of battle) [Reversal Shield] During its active period, transfers control effects (Freeze, Lock, Confuse, Forbidding Skill Use, Petrify, Icebound, Entangle) targeting self to a random enemy. [Reversal Shield] The excess damage blocked is logged, and when Antandra uses [Crystal Core Burst], it will additionally deals true damage equal to 100% of the logged damage. At the start of battle, gains [Reversal Shield] for 2 rounds. [Reversal Shield] When the shield's damage block count is not zero, enemies will prioritize Antandra as their attack target (takes precedence over Unyielding and Taunt).

**Slot 3 — Crystal Core** (id 1748, unlocks at `+3`)
  - **Ⅰ** at `+3` — Crystal CoreⅠ (安丹德拉技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +60% ATK: +60% Crit ATK (Absolute Value): +30% DMG Bonus (Absolute Value): +15%
  - **Ⅱ** at `+8` — Crystal CoreⅡ (安丹德拉技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +90% ATK: +90% Crit ATK (Absolute Value): +40% DMG Bonus (Absolute Value): +20%
  - **Ⅲ** at `+10` — Crystal CoreⅢ (安丹德拉技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +120% ATK: +120% Crit ATK (Absolute Value): +50% DMG Bonus (Absolute Value): +25%
  - **Ⅳ** at `+14` — Crystal CoreIV (安丹德拉技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +150% ATK: +150% Crit ATK (Absolute Value): +60% DMG Bonus (Absolute Value): +30%

**Slot 4 — Energy Nexus** (id 1749, unlocks at `+T`)
  - **Ⅰ** at `+T` — Energy NexusⅠ (安丹德拉技能描述)
    (Takes effect at the start of battle) [Crystal Core Burst]'s S-ATK is guaranteed to critical hit.
  - **Ⅱ** at `+T1` — Energy NexusⅡ (安丹德拉技能描述)
    (Takes effect at the start of battle) [Crystal Core Burst]'s S-ATK is guaranteed to critical hit. [Crystal Core Burst]'s S-ATK ignores 75% of the target's DEF and S-DEF.
  - **Ⅲ** at `+T2` — Energy NexusⅢ (安丹德拉技能描述)
    (Takes effect at the start of battle) [Crystal Core Burst]'s S-ATK is guaranteed to critical hit. [Crystal Core Burst]'s S-ATK ignores 75% of the target's DEF and S-DEF. [Energy Nexus] Upon completing 4 charges, if Antandra is not under control and has sufficient Accumulator, she will immediately use [Crystal Core Burst].
  - **Ⅳ** at `+T4` — Energy NexusIV (安丹德拉技能描述)
    (Takes effect at the start of battle) [Crystal Core Burst]'s S-ATK is guaranteed to critical hit. [Crystal Core Burst]'s S-ATK ignores 75% of the target's DEF and S-DEF. [Energy Nexus] Upon completing 4 charges, if Antandra is not under control and has sufficient Accumulator, she will immediately use [Crystal Core Burst]. Disables the enemy's [Slaughter Feast] and [Fatal Pursuit], and if Antandra is not under control and has sufficient Accumulator, she will also Freeze them for 1 round (ignoring immunity effects), and finally increases the charge of Energy Nexus by 1.(if Antandra dies, the effect disappears) [Slaughter Feast]: After the skill attack results in a kill, the effect of the skill is cast once more. [Fatal Pursuit]: If the skill attack does not cause a kill, the effect of the skill will be cast again.

### Augment cost (per step)
- `+1` — 5× Ranger Chip · 100,000 money
- `+2` — 10× Ranger Chip · 200,000 money
- `+3` — 21× Ranger Chip · 300,000 money
- `+4` — 28× Ranger Chip · 500,000 money
- `+5` — 35× Ranger Chip · 800,000 money
- `+6` — 42× Ranger Chip · 10× Pandora Power Core
- `+7` — 49× Ranger Chip · 50× Pandora Power Core
- `+8` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Antandra Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Antandra Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Antandra Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Antandra Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Antandra Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Antandra Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 580 · Leonidas 列奥尼达斯
**Role** Ranger · **Attack** physical · **Generation** latest
**Ratings** Damage 9/10 · Defence 7/10 · Assist 7/10

### Skill panels
**Slot 1 — Tempest Pierce** (id 1808, unlocks at `+0`)
  - **Ⅰ** at `+0` — Tempest PierceⅠ (列奥尼达斯+0)
    Vertical Attack, deals 320% S-ATK damage to targets, reduces the target's current HP by 30%, and increases your S-ATK damage by 30% each time the skill is cast (stacking up to 150%), lasting 99 rounds. Lastly, you recover 100 Accumulator.
  - **Ⅱ** at `+6` — Tempest PierceⅡ (列奥尼达斯+6)
    Vertical Attack, absorbs 50% of the target's S-ATK, then deals 360% S-ATK damage to the target. Reduces the target's current HP by 40%, and increases your S-ATK damage by 40% each time the skill is cast (stacking up to 200%), lasting 99 rounds. Lastly, you recover 100 Accumulator.
  - **Ⅲ** at `+10` — Tempest PierceⅢ (列奥尼达斯+10)
    Vertical Attack, absorbs 70% of the target's S-ATK, reduces the target's S-DEF by 50%, and deals 380% S-ATK damage to the target. Reduces the target's current HP by 50%, and increases your S-ATK by 50% each time the skill is cast (stacking up to 250%), lasting 99 rounds. Lastly, you recover 100 Accumulator.
  - **Ⅳ** at `+15` — Tempest PierceIV (列奥尼达斯+15)
    Vertical Attack, first clears the target's buffs, absorbs 70% of the target's S-ATK, then reduces the target's S-DEF by 60%, deals 400% S-ATK damage to the target, reduces the target's current HP by 60%, and increases your S-ATK by 60% each time the skill is cast (stacking up to 300%), lasting 99 rounds. Lastly, you recover 100 Accumulator.

**Slot 2 — Spirit Shield** (id 1809, unlocks at `+2`)
  - **Ⅰ** at `+2` — Spirit ShieldⅠ (列奥尼达斯+2)
    (Takes effect at the start of battle) At the start of battle and each time you revive or rebirth, the damage taken from a single hit will not exceed 30% of your max HP, lasting 2 rounds.
  - **Ⅱ** at `+9` — Spirit ShieldⅡ (列奥尼达斯+9)
    (Takes effect at the start of battle) At the start of battle and each time you revive or rebirth, the damage you take from a single hit will not exceed 20% of your Max HP, lasting for 2 rounds. S-ATK is guaranteed to crit and has a 50% chance to come with Hunter Focus (The attack always hits, ignores Dodge, Evasive and Time Ward.).
  - **Ⅲ** at `+13` — Spirit ShieldⅢ (列奥尼达斯+13)
    (Takes effect at the start of battle) At the start of battle and each time you revive or rebirth, the damage you take from a single hit will not exceed 15% of your Max HP, lasting for 2 rounds. S-ATK is guaranteed to crit and has a 50% chance to come with Hunter Focus (The attack always hits, ignores Dodge, Evasive and Time Ward.). At the start of battle and upon each revival or rebirth, if under a control effect, there is a 50% chance to cleanse the control effect before subsequent actions, lasting for 2 rounds.
  - **Ⅳ** at `+T3` — Spirit ShieldIV (列奥尼达斯+19)
    (Takes effect at the start of battle) At the start of battle and each time you revive or rebirth, the damage you take from a single hit will not exceed 10% of your Max HP, lasting for 2 rounds. S-ATK is guaranteed to crit and has a 75% chance to come with Hunter Focus (The attack always hits, ignores Dodge, Evasive and Time Ward.). At the start of battle and upon each revival or rebirth, if under a control effect, there is a 100% chance to cleanse the control effect and proceed with subsequent actions, lasting for 2 rounds.

**Slot 3 — Combat Instinct** (id 1810, unlocks at `+4`)
  - **Ⅰ** at `+4` — Combat InstinctⅠ (列奥尼达斯+4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +60% ATK: +60% Crit ATK (Absolute Value): +30% DMG Bonus (Absolute Value): +15%
  - **Ⅱ** at `+12` — Combat InstinctⅡ (列奥尼达斯+10)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +90% ATK: +90% Crit ATK (Absolute Value): +40% DMG Bonus (Absolute Value): +20%
  - **Ⅲ** at `+15` — Combat InstinctⅢ (列奥尼达斯+15)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +120% ATK: +120% Crit ATK (Absolute Value): +50% DMG Bonus (Absolute Value): +25%
  - **Ⅳ** at `+T2` — Combat InstinctIV (列奥尼达斯+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +150% ATK: +150% Crit ATK (Absolute Value): +60% DMG Bonus (Absolute Value): +30%

**Slot 4 — Bloodline Fury** (id 1811, unlocks at `+3`)
  - **Ⅰ** at `+3` — Bloodline FuryⅠ (列奥尼达斯+3)
    (Takes effect at the start of battle) At the start of battle, gains Eye of True Sight for 99 rounds. Revives immediately upon death with 100% of initial HP and 150 Accumulator (unaffected by forbidding revival effects).
  - **Ⅱ** at `+9` — Bloodline FuryⅡ (列奥尼达斯+9)
    (Takes effect at the start of battle) At the start of battle, gains Eye of True Sight for 99 rounds. Revives immediately upon death with 100% of initial HP and 150 Accumulator (unaffected by forbidding revival effects). If Accumulator is below 100, it is restored to 100 before taking action.
  - **Ⅲ** at `+T` — Bloodline FuryⅢ (列奥尼达斯+16)
    (Takes effect at the start of battle) At the start of battle, gains Eye of True Sight for 99 rounds. Revives immediately upon death with 100% of initial HP and 150 Accumulator (unaffected by forbidding revival effects). If Accumulator is below 100, it is restored to 100 before taking action. Skill damage becomes True Damage (ignores target's defense).
  - **Ⅳ** at `+T4` — Bloodline FuryIV (列奥尼达斯+20)
    (Takes effect at the start of battle) At the start of battle, gains Eye of True Sight for 99 rounds. Revives immediately upon death with 100% of initial HP and 150 Accumulator (unaffected by forbidding revival effects), and takes an immediate action. If Accumulator is below 100, it will be restored to 150 before taking action. Skill damage becomes True Damage (ignores target's defense). If an S-ATK does not kill an enemy target, a follow-up attack will be triggered, immediately releasing an additional S-ATK.

### Augment cost (per step)
- `+1` — 5× Ranger Chip · 100,000 money
- `+2` — 10× Ranger Chip · 200,000 money
- `+3` — 21× Ranger Chip · 300,000 money
- `+4` — 28× Ranger Chip · 500,000 money
- `+5` — 35× Ranger Chip · 800,000 money
- `+6` — 42× Ranger Chip · 10× Pandora Power Core
- `+7` — 49× Ranger Chip · 50× Pandora Power Core
- `+8` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Leonidas' Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Leonidas' Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Leonidas' Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Leonidas' Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Leonidas' Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Leonidas' Ship Part · 100× Alien Essence · 100× Transcendence Core

---

## 587 · Ice Fury 冰怒
**Role** Ranger · **Attack** physical · **Generation** latest
**Ratings** Damage 8/10 · Defence 8/10 · Assist 6/10

### Skill panels
**Slot 1 — Frost Roar** (id 1834, unlocks at `+0`)
  - **Ⅰ** at `+0` — Frost RoarⅠ (冰怒+0)
    Cross Attack, deals 280% S-ATK damage to targets. Activates [Accumulator Suppression Force Field] for itself for 2 rounds (This field will not work together with the shield that can reflect damage). Applies [Adaptive Protection] to all allies for 1 round (this effect can be triggered again after 2 rounds). Lastly, recovers 100 Accumulator. [Accumulator Suppression Force Field]: If it is attacked by any enemy, it will reduce the enemy's Accumulator by 40% at the end of their attack; it will also reflect 60% of HP damage onto the attacker. [Adaptive Protection]: The ally with the effect is immune to damage and abnormal statuses caused by enemies of the same class (except for subsequent damage).
  - **Ⅱ** at `+7` — Frost RoarⅡ (冰怒+7)
    Cross Attack, deals 300% S-ATK damage to targets. Has an 80% chance to freeze a random enemy for 2 rounds. Activates [Accumulator Suppression Force Field] for itself for 2 rounds (This field will not work together with the shield that can reflect damage). Applies [Adaptive Protection] to all allies for 1 round (this effect can be triggered again after 2 rounds). Lastly, recovers 100 Accumulator. [Accumulator Suppression Force Field]: If it is attacked by any enemy, it will reduce the enemy's Accumulator by 60% at the end of their attack; it will also reflect 80% of HP damage onto the attacker. [Adaptive Protection]: The ally with the effect is immune to damage and abnormal statuses caused by enemies of the same class (except for subsequent damage).
  - **Ⅲ** at `+15` — Frost RoarⅢ (冰怒+15)
    Cross Attack, deals 320% S-ATK damage to targets. Has a 100% chance to Freeze a random enemy, increasing damage taken by controlled enemies by 60% for 2 rounds. Activates [Accumulator Suppression Force Field] for itself for 2 rounds (This field will not work together with the shield that can reflect damage). Applies [Adaptive Protection] to all allies for 1 round (this effect can be triggered again after 2 rounds). Lastly, recovers 100 Accumulator. [Accumulator Suppression Force Field]: If it is attacked by any enemy, it will reduce the enemy's Accumulator by 80% at the end of their attack; it will also reflect 100% of HP damage onto the attacker. [Adaptive Protection]: The ally with the effect is immune to damage and abnormal statuses caused by enemies of the same class (except for subsequent damage).
  - **Ⅳ** at `+T3` — Frost RoarIV (冰怒+19)
    Cross Attack, deals 350% S-ATK damage to targets. Has a 100% chance to Freeze 2 random enemies. Increases damage taken by controlled enemies by 80% and deals additional damage equal to 50% of their max HP for 2 rounds. Activates [Accumulator Suppression Force Field] for itself for 2 rounds (This field will not work together with the shield that can reflect damage). Applies [Adaptive Protection] to all allies for 1 round (this effect can be triggered again after 2 rounds). Lastly, recovers 100 Accumulator. [Accumulator Suppression Force Field]: If it is attacked by any enemy, it will reduce the enemy's Accumulator by 100% at the end of their attack; it will also reflect 120% of HP damage onto the attacker. [Adaptive Protection]: The ally with the effect is immune to damage and abnormal statuses caused by enemies of the same class (except for subsequent damage).

**Slot 2 — Snowfield Blessing** (id 1835, unlocks at `+3`)
  - **Ⅰ** at `+3` — Snowfield BlessingⅠ (冰怒+3)
    (Takes effect at the start of battle) When casting a skill, grants [Snowfield Amplification] to our Rangers (including self), Strikers, and Destroyers, and grants [Snowfield Protection] to our Rovers, Protectors, and Flagship for 2 rounds. [Snowfield Amplification]: 50% chance to freeze the target when attacking. [Snowfield Protection]: 50% chance to freeze a random enemy when attacked.
  - **Ⅱ** at `+9` — Snowfield BlessingⅡ (冰怒+9)
    (Takes effect at the start of battle) When casting a skill, grants [Snowfield Amplification] to our Rangers (including self), Strikers, and Destroyers, and grants [Snowfield Protection] to our Rovers, Protectors, and Flagship for 2 rounds. [Snowfield Amplification]: S-ATK always crits, 50% chance to freeze the target when attacking. [Snowfield Protection]: Reduces damage taken by 40%, and 50% chance to freeze a random enemy when attacked.
  - **Ⅲ** at `+T1` — Snowfield BlessingⅢ (冰怒+17)
    (Takes effect at the start of battle) When casting a skill, grants [Snowfield Amplification] to our Rangers (including self), Strikers, and Destroyers, and grants [Snowfield Protection] to our Rovers, Protectors, and Flagship for 2 rounds. [Snowfield Amplification]: S-ATK always crits, and crit damage is increased by 80%. 50% chance to freeze the target when attacking. [Snowfield Protection]: Reduces damage taken by 60% and grants a shield that can block one attack. When attacked, there is a 50% chance to freeze a random enemy. At the start of battle, gains [Accumulator Suppression Force Field] for 2 rounds.
  - **Ⅳ** at `+T4` — Snowfield BlessingIV (冰怒+20)
    (Takes effect at the start of battle) When casting a skill, grants [Snowfield Amplification] to our Rangers (including self), Strikers, and Destroyers, and grants [Snowfield Protection] to our Rovers, Protectors, and Flagship for 2 rounds. [Snowfield Amplification]: S-ATK always crits, and crit damage is increased by 120%. 50% chance to freeze the target when attacking. Before acting, there is a 100% chance to recover 50% HP and 100 Accumulator, then proceed with subsequent actions. [Snowfield Protection]: Reduces damage taken by 80% and grants a shield that can block 2 attacks. When attacked, there is a 50% chance to freeze a random enemy. There is a 50% chance to gain Rebirth, reviving upon death with 100% of initial HP and 100 Accumulator. (unaffected by forbidding revival effects) At the start of battle, gains [Accumulator Suppression Force Field] for 2 rounds. Rangers, Strikers, and Destroyers gain [Snowfield Amplification], and Rovers, Protectors, and Flagship gain [Snowfield Protection] for 2 rounds.

**Slot 3 — Will of Ice and Snow** (id 1836, unlocks at `+5`)
  - **Ⅰ** at `+5` — Will of Ice and SnowⅠ (冰怒+5)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP +60% Damage increase (absolute value) +15% Damage reduction (absolute value) +15%
  - **Ⅱ** at `+11` — Will of Ice and SnowⅡ (冰怒+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP +90% Damage increase (absolute value) +20% Damage reduction (absolute value) +20%
  - **Ⅲ** at `+T` — Will of Ice and SnowⅢ (冰怒+16)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP +120% Damage increase (absolute value) +25% Damage reduction (absolute value) +25%
  - **Ⅳ** at `+T2` — Will of Ice and SnowIV (冰怒+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP +150% Damage increase (absolute value) +30% Damage reduction (absolute value) +30%

### Augment cost (per step)
- `+1` — 5× Ranger Chip · 100,000 money
- `+2` — 10× Ranger Chip · 200,000 money
- `+3` — 21× Ranger Chip · 300,000 money
- `+4` — 28× Ranger Chip · 500,000 money
- `+5` — 35× Ranger Chip · 800,000 money
- `+6` — 42× Ranger Chip · 10× Pandora Power Core
- `+7` — 49× Ranger Chip · 50× Pandora Power Core
- `+8` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Ice Fury's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Ice Fury's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Ice Fury's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Ice Fury's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Ice Fury's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Ice Fury's Ship Part · 100× Alien Essence · 100× Transcendence Core

---

## 588 · Vera 薇拉
**Role** Ranger · **Attack** physical · **Generation** old
**Ratings** Damage 9/10 · Defence 7/10 · Assist 5/10

### Signature skill
- **Ⅰ** at `+0` — Frost Dance (薇拉)
  Cross Attack, deals 200% S-ATK damage to targets. Lastly, you recover 100 Accumulator.

### Augment cost (per step)
- `+1` — 5× Ranger Chip · 100,000 money
- `+2` — 10× Ranger Chip · 200,000 money
- `+3` — 21× Ranger Chip · 300,000 money
- `+4` — 28× Ranger Chip · 500,000 money
- `+5` — 35× Ranger Chip · 800,000 money
- `+6` — 42× Ranger Chip · 10× Pandora Power Core
- `+7` — 49× Ranger Chip · 50× Pandora Power Core
- `+8` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Vera's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Vera's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Vera's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Vera's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Vera's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Vera's Ship Part · 100× Alien Essence · 100× Transcendence Core

---

## 592 · Elf 爱尔芙
**Role** Ranger · **Attack** physical · **Generation** latest
**Ratings** Damage 9/10 · Defence 7/10 · Assist 10/10

### Skill panels
**Slot 1 — Crystallized Illusion** (id 1852, unlocks at `+0`)
  - **Ⅰ** at `+0` — Crystallized IllusionⅠ (爱尔芙+0)
    Vertical Attack, deals 280% S-ATK damage to the target and applies [Crystal Erosion]. If the target already has [Crystal Erosion], increases its stack by 1, lasting 99 rounds. Lastly, recovers 100 Accumulator. [Crystal Erosion]: Starts with 1 stack, maximum of 2 stacks. It triggers corresponding effects based on the current number of stacks (if the maximum stack is reached, the effect of the maximum stack is repeatedly triggered). 1 stack: Gains 50% Miss, with a chance to make attacks miss (cannot make guaranteed hits miss), lasting 2 rounds. 2 stacks: Clears the target's Accumulator.
  - **Ⅱ** at `+6` — Crystallized IllusionⅡ (爱尔芙+2（被动组合）)
    Vertical Attack, deals 300% S-ATK damage to the target and applies [Crystal Erosion]. If the target already has [Crystal Erosion], increases its stack by 1, lasting 99 rounds. Lastly, recovers 100 Accumulator. [Crystal Erosion]: Starts with 1 stack, maximum of 3 stacks. It triggers corresponding effects based on the current number of stacks (if the maximum stack is reached, the effect of the maximum stack is repeatedly triggered). 1 stack: Gains 50% Miss, with a chance to make attacks miss (cannot make guaranteed hits miss), lasting 2 rounds. 2 stacks: Clears the target's Accumulator. 3 stacks: The target gains [Crystallization], rendering it unable to act for 2 rounds. (This effect cannot be cleansed, isn't affected by immunity)
  - **Ⅲ** at `+10` — Crystallized IllusionⅢ (爱尔芙+6)
    Vertical Attack, deals 320% S-ATK damage to the target and applies [Crystal Erosion]. If the target already has [Crystal Erosion], increases its stack by 1, lasting 99 rounds. Gains a shield equal to 40% of Max HP (cannot stack, resets upon repeated skill use). Lastly, recovers 100 Accumulator. [Crystal Erosion]: Starts with 1 stack, maximum of 3 stacks. It triggers corresponding effects based on the current number of stacks (if the maximum stack is reached, the effect of the maximum stack is repeatedly triggered). 1 stack: Gains 50% Miss, with a chance to make attacks miss (cannot make guaranteed hits miss), lasting 2 rounds. 2 stacks: Clears the target's Accumulator. 3 stacks: The target gains [Crystallization], rendering it unable to act for 2 rounds. (This effect cannot be cleansed, isn't affected by immunity)
  - **Ⅳ** at `+15` — Crystallized IllusionIV (爱尔芙+9)
    Vertical Attack, deals 360% S-ATK damage to the target and applies [Crystal Erosion]. If the target already has [Crystal Erosion], increases its stack by 1, lasting 99 rounds. Gains a shield equal to 60% of Max HP (cannot stack, resets upon repeated skill use). Lastly, recovers 100 Accumulator. [Crystal Erosion]: Starts with 1 stack, maximum of 4 stacks. It triggers corresponding effects based on the current number of stacks (if the maximum stack is reached, the effect of the maximum stack is repeatedly triggered). 1 stack: Gains 50% Miss, with a chance to make attacks miss (cannot make guaranteed hits miss), lasting 2 rounds. 2 stacks: Clears the target's Accumulator. 3 stacks: The target gains [Crystallization], rendering it unable to act for 2 rounds. (This effect cannot be cleansed, isn't affected by immunity) 4 stacks: Prevents the target's Active Skill from taking effect, lasting 2 rounds.

**Slot 2 — Crystal Dream** (id 1848, unlocks at `+2`)
  - **Ⅰ** at `+2` — Crystal DreamⅠ (爱尔芙+2)
    (Takes effect at the start of battle) When casting a skill, through the crystalline power of the planet, Elf can create a crystallized form of a random ally as a [Starlight Phantom] (maximum of 1). [Starlight Phantom]: Possesses the same skills as the original hero but takes 50% more damage and deals 50% reduced damage. Gains 50% of the original hero's attributes. And it cannot be revived or rebirthed. (Cannot replicate itself, Solaris, Wukong, or units created by skill replication.) (Starlight Phantoms cannot appear on locations where ships, not summonings, started the battle or on locations where there is a ship. If a Phantom uses a skill that another of your ships has, the last effect will overwrite the previous one.)
  - **Ⅱ** at `+9` — Crystal DreamⅡ (爱尔芙+9)
    (Takes effect at the start of battle) When casting a skill, through the crystalline power of the planet, Elf can create a crystallized form of a random ally as a [Starlight Phantom] (maximum of 1). [Starlight Phantom]: Possesses the same skills as the original hero but takes 40% more damage and deals 40% reduced damage. Gains 60% of the original hero's attributes. And it cannot be revived or rebirthed. If a Starlight Phantom dies, Elf recovers 40% of her max HP. (Cannot replicate itself, Solaris, Wukong, or units created by skill replication.) (Starlight Phantoms cannot appear on locations where ships, not summonings, started the battle or on locations where there is a ship. If a Phantom uses a skill that another of your ships has, the last effect will overwrite the previous one.)
  - **Ⅲ** at `+T` — Crystal DreamⅢ (爱尔芙+16（1）)
    (Takes effect at the start of battle) When casting a skill, through the crystalline power of the planet, Elf can create a crystallized form of a random ally as a [Starlight Phantom] (maximum of 1). [Starlight Phantom]: Possesses the same skills as the original hero but takes 30% more damage and deals 30% reduced damage. Gains 70% of the original hero's attributes. And it cannot be revived or rebirthed. If the Starlight Phantom dies, Elf recovers 60% of max HP and is cleansed of abnormal statuses and crowd-control effects. (Cannot replicate itself, Solaris, Wukong, or units created by skill replication.) (Starlight Phantoms cannot appear on locations where ships, not summonings, started the battle or on locations where there is a ship. If a Phantom uses a skill that another of your ships has, the last effect will overwrite the previous one.)
  - **Ⅳ** at `+T2` — Crystal DreamIV (爱尔芙+18（1）)
    (Takes effect at the start of battle) When casting a skill, through the crystalline power of the planet, Elf can create a crystallized form of a random ally as a [Starlight Phantom] (maximum of 1). [Starlight Phantom]: Possesses the same skills as the original hero but takes 30% more damage and deals 20% reduced damage. Gains 80% of the original hero's attributes. And it cannot be revived or rebirthed. If the Starlight Phantom dies, Elf recovers 80% of max HP and is cleansed of abnormal statuses and crowd-control effects. The Starlight Phantom will Taunt, forcing all enemies to attack it. (Unyielding effect still takes precedence) (Cannot replicate itself, Solaris, Wukong, or units created by skill replication.) (Starlight Phantoms cannot appear on locations where ships, not summonings, started the battle or on locations where there is a ship. If a Phantom uses a skill that another of your ships has, the last effect will overwrite the previous one.)

**Slot 3 — Dream Condensation** (id 1849, unlocks at `+4`)
  - **Ⅰ** at `+4` — Dream CondensationⅠ (爱尔芙+4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +60% S-ATK: +60% DMG Bonus (Absolute Value): +15% Crit ATK (Absolute Value) +15%
  - **Ⅱ** at `+10` — Dream CondensationⅡ (爱尔芙+10)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +90% S-ATK: +90% DMG Bonus (Absolute Value): +20% Crit ATK (Absolute Value) +20%
  - **Ⅲ** at `+14` — Dream CondensationⅢ (爱尔芙+14)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +120% S-ATK: +120% DMG Bonus (Absolute Value): +25% Crit ATK (Absolute Value) +25%
  - **Ⅳ** at `+T1` — Dream CondensationIV (爱尔芙+17)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +150% S-ATK: +150% DMG Bonus (Absolute Value): +30% Crit ATK (Absolute Value) +30%

**Slot 4 — Soul Crystal** (id 1850, unlocks at `+T`)
  - **Ⅰ** at `+T` — Soul CrystalⅠ (爱尔芙+16)
    (Takes effect at the start of battle) When Elf takes lethal damage or is affected by an Instant Destruction effect, the damage is negated, and she enters the [Soul Crystal] state, while clearing all skill effects except for Rebirth (this effect may trigger up to 1 time per battle). [Soul Crystal]: HP and other attributes are 150% of the initial battle values. Elf returns to the battle with 100% of initial HP and 150 Accumulator if her [Soul Crystal] is not destroyed before her next action.
  - **Ⅱ** at `+T2` — Soul CrystalⅡ (爱尔芙+18)
    (Takes effect at the start of battle) At the start of battle, applies [Crystal Erosion] to the enemy with the highest S-ATK. When Elf takes lethal damage or is affected by an Instant Destruction effect, the damage is negated, and she enters the [Soul Crystal] state, while clearing all skill effects except for Rebirth (this effect may trigger up to 1 time per battle). [Soul Crystal]: HP and other attributes are 150% of the initial battle values. Elf returns to the battle with 100% of initial HP and 150 Accumulator if her [Soul Crystal] is not destroyed before her next action.
  - **Ⅲ** at `+T3` — Soul CrystalⅢ (爱尔芙+19)
    (Takes effect at the start of battle) At the start of battle, applies [Crystal Erosion] to the enemy with the highest S-ATK. When Starlight Phantom casts a skill, increases the stack of [Crystal Erosion] on the affected enemy by 1. When Elf takes lethal damage or is affected by an Instant Destruction effect, the damage is negated, and she enters the [Soul Crystal] state, while clearing all skill effects except for Rebirth (this effect may trigger up to 1 time per battle). [Soul Crystal]: HP and other attributes are 150% of the initial battle values. Elf returns to the battle with 100% of initial HP and 150 Accumulator if her [Soul Crystal] is not destroyed before her next action.
  - **Ⅳ** at `+T4` — Soul CrystalIV (爱尔芙+20)
    (Takes effect at the start of battle) At the start of battle, applies [Crystal Erosion] to the enemy with the highest S-ATK. When Starlight Phantom casts a skill, increases the stack of [Crystal Erosion] on the affected enemy by 1. The mysterious power of the crystal infiltrates and erodes the target, the target with [Crystal Erosion] takes 40% more damage, and [Slaughter Feast] and [Fatal Pursuit] cannot take effect. When Elf takes lethal damage or is affected by an Instant Destruction effect, the damage is negated, and she enters the [Soul Crystal] state, while clearing all skill effects except for Rebirth (this effect may trigger up to 1 time per battle). [Soul Crystal]: HP and other attributes are 150% of the initial battle values. Elf returns to the battle with 100% of initial HP and 150 Accumulator if her [Soul Crystal] is not destroyed before her next action.

### Augment cost (per step)
- `+1` — 5× Ranger Chip · 100,000 money
- `+2` — 10× Ranger Chip · 200,000 money
- `+3` — 21× Ranger Chip · 300,000 money
- `+4` — 28× Ranger Chip · 500,000 money
- `+5` — 35× Ranger Chip · 800,000 money
- `+6` — 42× Ranger Chip · 10× Pandora Power Core
- `+7` — 49× Ranger Chip · 50× Pandora Power Core
- `+8` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Elf's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Elf's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Elf's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Elf's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Elf's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Elf's Ship Part · 100× Alien Essence · 100× Transcendence Core

---

## 600 · Starborn 星辰
**Role** Ranger · **Attack** physical · **Generation** latest
**Ratings** Damage 9/10 · Defence 7/10 · Assist 10/10

### Skill panels
**Slot 1 — Celestial Stratagem** (id 1875, unlocks at `+0`)
  - **Ⅰ** at `+0` — Celestial StratagemⅠ (星辰+0)
    Cross Attack, first plunders 40% Accumulator from targets, then deals 280% S-ATK damage to targets. Grants all allies Eye of True Sight until the end of the battle. Increases all allies' Penetration by 100% for 2 rounds. Lastly, you recover 100 Accumulator.
  - **Ⅱ** at `+7` — Celestial StratagemⅡ (星辰+7)
    Cross Attack, first plunders 60% Accumulator from targets, then deals 300% S-ATK damage to targets. Grants all allies Eye of True Sight until the end of the battle. Increases all allies' Penetration by 100% for 2 rounds. Increases the damage dealt of all allies by 80% for 2 rounds. Lastly, you recover 100 Accumulator.
  - **Ⅲ** at `+15` — Celestial StratagemⅢ (星辰+9(被动))
    Cross Attack, first plunders 80% Accumulator from targets, then deals 320% S-ATK damage to targets. Grants all allies Eye of True Sight until the end of the battle. Increases all allies' Penetration by 150% for 2 rounds. Increases the damage dealt of all allies by 80% for 2 rounds. Grants self the Celestial Stratagem effect for 2 rounds. Lastly, you recover 100 Accumulator. <em>Celestial Stratagem:</em> When next enemy uses a skill, Starborn could block this skill attack damage (except for subsequent damage), and Starborn will release Stratagem's Reckoning to perform a single attack on this enemy, dealing additional damage equal to 100% of the damage blocked. Each time Celestial Stratagem is obtained, this effect can be triggered once. (If the ship is under other control effects, it cannot be released)
  - **Ⅳ** at `+T3` — Celestial StratagemIV (星辰+15)
    Cross Attack, first plunders 100% Accumulator from targets, then deals 360% S-ATK damage to targets. Grants all allies Eye of True Sight until the end of the battle. Increases all allies' Penetration by 200% for 2 rounds. Increases the damage dealt of all allies by 80% for 2 rounds. Applies Forbid Accumulator Recovery effects to targets (can only recover Accumulator in the two conditions: normal attack and "if Accumulator is less than xx, recover to xx"), for 2 rounds. Grants self the Celestial Stratagem effect for 2 rounds. Lastly, you recover 100 Accumulator. <em>Celestial Stratagem:</em> When next enemy uses a skill, Starborn could block this skill attack damage (except for subsequent damage), and Starborn will release Stratagem's Reckoning to perform a single attack on this enemy, dealing additional damage equal to 200% of the damage blocked, and there is a 50% chance to lock the attacked enemy for 2 rounds. Each time Celestial Stratagem is obtained, this effect can be triggered once. (If the ship is under other control effects, it cannot be released)

**Slot 2 — Skyfire Stratagem** (id 1876, unlocks at `+3`)
  - **Ⅰ** at `+3` — Skyfire StratagemⅠ (星辰+3)
    (Takes effect at the start of battle) At the start of battle, gain [Skyfire Stratagem], lasting for 2 rounds. When taking lethal damage, immune to this lethal damage and recover 100% of Max HP and Accumulator. (In a single battle, each trigger has a 1-round cooldown, during which it cannot be triggered again or be granted [Skyfire Stratagem], and shares cooldown rounds with [Time Reversal] and [Blizzard])
  - **Ⅱ** at `+9` — Skyfire StratagemⅡ (星辰+9)
    (Takes effect at the start of battle) At the start of battle and when casting a skill, gain [Skyfire Stratagem], lasting for 2 rounds. When taking lethal damage, immune to this lethal damage and recover 100% of Max HP and Accumulator. (In a single battle, each trigger has a 1-round cooldown, during which it cannot be triggered again or be granted [Skyfire Stratagem], and shares cooldown rounds with [Time Reversal] and [Blizzard])
  - **Ⅲ** at `+T1` — Skyfire StratagemⅢ (星辰+17)
    (Takes effect at the start of battle) At the start of battle and when casting a skill, gain [Skyfire Stratagem], lasting for 2 rounds. When taking lethal damage, immune to this lethal damage and recover 100% of Max HP and Accumulator. (In a single battle, each trigger has a 1-round cooldown, during which it cannot be triggered again or be granted [Skyfire Stratagem], and shares cooldown rounds with [Time Reversal] and [Blizzard]) When casting a skill, the ally with the highest S-ATK (excluding self) gains additionally [Celestial Stratagem].
  - **Ⅳ** at `+T4` — Skyfire StratagemIV (星辰+20)
    (Takes effect at the start of battle) At the start of battle and when casting a skill, gain [Skyfire Stratagem], lasting for 2 rounds. When taking lethal damage, immune to this lethal damage and recover 100% of Max HP and Accumulator. (In a single battle, each trigger has a 1-round cooldown, during which it cannot be triggered again or be granted [Skyfire Stratagem], and shares cooldown rounds with [Time Reversal] and [Blizzard]) When casting a skill, the ally with the highest S-ATK (excluding self) gains additionally [Celestial Stratagem]. When the ally (who has [Celestial Stratagem]) casts a skill, there is a 75% chance to gain Hunter Focus (the attack always hits, ignores Dodge, Evasive and Time Ward). When the ally (who has [Celestial Stratagem]) casts a skill, it will first remove all enemies' Invisible and Dark Conceal states,

**Slot 3 — Strategist** (id 1877, unlocks at `+5`)
  - **Ⅰ** at `+5` — StrategistⅠ (星辰+5)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP +60% Damage increase (absolute value) +15% Damage reduction (absolute value) +15%
  - **Ⅱ** at `+11` — StrategistⅡ (星辰+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP +90% Damage increase (absolute value) +20% Damage reduction (absolute value) +20%
  - **Ⅲ** at `+T` — StrategistⅢ (星辰+16)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP +120% Damage increase (absolute value) +25% Damage reduction (absolute value) +25%
  - **Ⅳ** at `+T2` — StrategistIV (星辰+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP +150% Damage increase (absolute value) +30% Damage reduction (absolute value) +30%

### Augment cost (per step)
- `+1` — 5× Ranger Chip · 100,000 money
- `+2` — 10× Ranger Chip · 200,000 money
- `+3` — 21× Ranger Chip · 300,000 money
- `+4` — 28× Ranger Chip · 500,000 money
- `+5` — 35× Ranger Chip · 800,000 money
- `+6` — 42× Ranger Chip · 10× Pandora Power Core
- `+7` — 49× Ranger Chip · 50× Pandora Power Core
- `+8` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Starborn Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Starborn Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Starborn Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Starborn Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Starborn Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Starborn Ship Part · 100× Alien Essence · 100× Transcendence Core

---

## 604 · Roselle 洛瑟儿
**Role** Ranger · **Attack** physical · **Generation** old
**Ratings** Damage 9/10 · Defence 7/10 · Assist 10/10

### Signature skill
- **Ⅰ** at `+0` — Extreme Annihilation (洛瑟儿+0)
  Cross Attack, deals 200% S-ATK damage to targets. Lastly, you recover 100 Accumulator.
- **Ⅱ** at `+T4` — Counterforce Field (洛瑟儿+20)
  _(no English description shipped)_
- **Ⅲ** at `Second Awaken` — Counterforce Field (洛瑟儿+20)
  _(no English description shipped)_
- **Ⅳ** at `Awaken +3` — Counterforce Field (洛瑟儿+20)
  _(no English description shipped)_
- **Ⅴ** at `Awaken +4` — Counterforce Field (洛瑟儿+20)
  _(no English description shipped)_

### Augment cost (per step)
- `+1` — 5× Ranger Chip · 100,000 money
- `+2` — 10× Ranger Chip · 200,000 money
- `+3` — 21× Ranger Chip · 300,000 money
- `+4` — 28× Ranger Chip · 500,000 money
- `+5` — 35× Ranger Chip · 800,000 money
- `+6` — 42× Ranger Chip · 10× Pandora Power Core
- `+7` — 49× Ranger Chip · 50× Pandora Power Core
- `+8` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Roselle Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Roselle Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Roselle Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Roselle Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Roselle Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Roselle Ship Part · 100× Alien Essence · 100× Transcendence Core

---

## 605 · Clarissa 克拉丽莎
**Role** Ranger · **Attack** physical · **Generation** latest
**Ratings** Damage 9/10 · Defence 10/10 · Assist 7/10

### Skill panels
**Slot 1 — Time Rift** (id 1890, unlocks at `+0`)
  - **Ⅰ** at `+0` — Time RiftⅠ (克拉丽莎+0)
    Cross Attack, plunders 20% of the target's S-ATK and 50% Hit Rate, then deals 300% S-ATK damage to hit targets. Gains Eye of True Sight for 2 rounds. Lastly, recovers 100 Accumulator.
  - **Ⅱ** at `+6` — Time RiftⅡ (克拉丽莎+2)
    Cross Attack, plunders 30% of the target's S-ATK and 80% Hit Rate, then deals 320% S-ATK damage to hit targets. Gains Eye of True Sight for 2 rounds. After each skill cast, increases all allies' S-ATK and Crit ATK by 80%, up to a maximum of 240% S-ATK and 240% Crit ATK, lasting 99 rounds. Lastly, recovers 100 Accumulator.
  - **Ⅲ** at `+10` — Time RiftⅢ (克拉丽莎+6)
    Cross Attack, plunders 40% of the target's S-ATK and 100% Hit Rate, then deals 340% S-ATK damage to hit targets. Gains Eye of True Sight for 2 rounds. After each skill cast, increases all allies' S-ATK and Crit ATK by 80%, up to a maximum of 240% S-ATK and 240% Crit ATK, lasting 99 rounds. Binds one enemy hero of a prioritized Type for 2 rounds in the order of Striker, Destroyer, Rover, Protector, Flagship, Ranger (if the highest priority Type is dead or absent, selects the next Type in order; bound units cannot act). Lastly, recovers 100 Accumulator.
  - **Ⅳ** at `+15` — Time RiftIV (克拉丽莎+9)
    Cross Attack, plunders 50% of the target's S-ATK and 150% Hit Rate, then deals 380% S-ATK damage to hit targets. Gains Eye of True Sight for 2 rounds. Deals True Damage equal to 300% of the first stage skill attack damage to the enemy ship with the lowest HP. After each skill cast, increases all allies' S-ATK and Crit ATK by 80%, up to a maximum of 240% S-ATK and 240% Crit ATK, lasting 99 rounds. Binds one enemy hero of a prioritized Type for 2 rounds in the order of Striker, Destroyer, Rover, Protector, Flagship, Ranger (if the highest priority Type is dead or absent, selects the next Type in order; bound units cannot act). Lastly, recovers 100 Accumulator.

**Slot 2 — Circulating Shield** (id 1891, unlocks at `+2`)
  - **Ⅰ** at `+2` — Circulating ShieldⅠ (克拉丽莎+2)
    (Takes effect at the start of battle) When casting a skill, all allies gain the [Circulating Shield], lasting 2 rounds. Allies with [Circulating Shield] will have any damage exceeding 40% of their max HP nullified once, after which the shield is removed.
  - **Ⅱ** at `+9` — Circulating ShieldⅡ (克拉丽莎+9)
    (Takes effect at the start of battle) When casting a skill, all allies gain the [Circulating Shield], lasting 2 rounds. Allies with [Circulating Shield] will have any damage exceeding 30% of their max HP nullified once, after which the shield is removed.
  - **Ⅲ** at `+T` — Circulating ShieldⅢ (克拉丽莎+16)
    (Takes effect at the start of battle) When casting a skill, all allies gain the [Circulating Shield], lasting 2 rounds. Allies with [Circulating Shield] will have any damage exceeding 20% of their max HP nullified once, after which the shield is removed. During the [Binding] status, the affected targets takes 50% increased damage, and has a 30% chance to die instantly when damaged. (Ignores immunity to lethal damage and instant destruction)
  - **Ⅳ** at `+T3` — Circulating ShieldIV (克拉丽莎+19)
    (Takes effect at the start of battle) When casting a skill, all allies gain the [Circulating Shield], lasting 2 rounds. Allies with [Circulating Shield] will have any damage exceeding 10% of their max HP nullified once, after which the shield is removed. During the [Binding] status, the affected targets takes 50% increased damage, and has a 30% chance to die instantly when damaged. (Ignores immunity to lethal damage and instant destruction) When casting a skill, there is a 50% chance to additionally apply [Binding] on a random enemy.

**Slot 3 — Willpower Surge** (id 1892, unlocks at `+4`)
  - **Ⅰ** at `+4` — Willpower SurgeⅠ (克拉丽莎+4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +60% S-ATK: +60% DMG Bonus (Absolute Value): +15% Crit ATK (Absolute Value) +15%
  - **Ⅱ** at `+10` — Willpower SurgeⅡ (克拉丽莎+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +90% S-ATK: +90% DMG Bonus (Absolute Value): +20% Crit ATK (Absolute Value) +20%
  - **Ⅲ** at `+14` — Willpower SurgeⅢ (克拉丽莎+14)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +120% S-ATK: +120% DMG Bonus (Absolute Value): +25% Crit ATK (Absolute Value) +25%
  - **Ⅳ** at `+T2` — Willpower SurgeIV (克拉丽莎+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +150% S-ATK: +150% DMG Bonus (Absolute Value): +30% Crit ATK (Absolute Value) +30%

**Slot 4 — Tactical Reboot** (id 1893, unlocks at `+3`)
  - **Ⅰ** at `+3` — Tactical RebootⅠ (克拉丽莎+3)
    (Takes effect at the start of battle) During battle preparation, different effects take place depending on the ship's placement. (Effects activate at the start of battle and upon each revival or rebirth) [Front Row]: Upon death, instant destruction of a random enemy. (Ignores immunity to lethal damage and instant destruction) [Middle Row]: Upon death, a random ally takes an immediate action. (If the selected ally in a state of inability to act, this effect does not trigger) [Back Row]: Upon death, a random ally gains [Dark Conceal], immune to attacks and skill effects for 1 round.
  - **Ⅱ** at `+13` — Tactical RebootⅡ (克拉丽莎+13)
    (Takes effect at the start of battle) During battle preparation, different effects take place depending on the ship's placement. (Effects activate at the start of battle and upon each revival or rebirth) [Front Row]: Upon death, instant destruction of a random enemy. (Ignores immunity to lethal damage and instant destruction) [Middle Row]: Upon death, a random ally takes an immediate action. (If the selected ally in a state of inability to act, this effect does not trigger) [Back Row]: Upon death, a random ally gains [Dark Conceal], immune to attacks and skill effects for 1 round. At the start of battle, all allies gain [Circulating Shield] for 2 rounds.
  - **Ⅲ** at `+T1` — Tactical RebootⅢ (克拉丽莎+17)
    (Takes effect at the start of battle) During battle preparation, different effects take place depending on the ship's placement. (Effects activate at the start of battle and upon each revival or rebirth) [Front Row]: Upon death, instant destruction of a random enemy. (Ignores immunity to lethal damage and instant destruction) [Middle Row]: Upon death, a random ally takes an immediate action. (If the selected ally in a state of inability to act, this effect does not trigger) [Back Row]: Upon death, a random ally gains [Dark Conceal], immune to attacks and skill effects for 1 round. At the start of battle, all allies gain [Circulating Shield] for 2 rounds. While active, [Circulating Shield] triggers 3 times on the ally with the highest S-ATK at the start of battle (excluding self).
  - **Ⅳ** at `+T4` — Tactical RebootIV (克拉丽莎+20)
    (Takes effect at the start of battle) During battle preparation, different effects take place depending on the ship's placement. (Effects activate at the start of battle and upon each revival or rebirth) [Front Row]: Upon death, instant destruction of 2 random enemies. (Ignores immunity to lethal damage and instant destruction) [Middle Row]: Upon death, 2 random allies takes an immediate action. (If the selected ally in a state of inability to act, this effect does not trigger) [Back Row]: Upon death, 2 random allies gains [Dark Conceal], immune to attacks and skill effects for 1 round. At the start of battle, all allies gain [Circulating Shield] for 2 rounds. While active, [Circulating Shield] triggers 3 times on the ally with the highest S-ATK at the start of battle (excluding self).

### Augment cost (per step)
- `+1` — 5× Ranger Chip · 100,000 money
- `+2` — 10× Ranger Chip · 200,000 money
- `+3` — 21× Ranger Chip · 300,000 money
- `+4` — 28× Ranger Chip · 500,000 money
- `+5` — 35× Ranger Chip · 800,000 money
- `+6` — 42× Ranger Chip · 10× Pandora Power Core
- `+7` — 49× Ranger Chip · 50× Pandora Power Core
- `+8` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Voyage Honor Token - Tyxion · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Voyage Honor Token - Tyxion · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Voyage Honor Token - Tyxion · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Voyage Honor Token - Tyxion · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Voyage Honor Token - Tyxion · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Voyage Honor Token - Tyxion · 100× Alien Essence · 100× Transcendence Core

---

## 612 · Ouros 欧罗斯
**Role** Ranger · **Attack** physical · **Generation** latest
**Ratings** Damage 9/10 · Defence 7/10 · Assist 10/10

### Skill panels
**Slot 1 — Interference Pulse** (id 1917, unlocks at `+0`)
  - **Ⅰ** at `+0` — Interference PulseⅠ (欧罗斯+0)
    Vertical Attack, deals 280% S-ATK damage to the target, applies [Interference Pulse] to all enemies, lasting 2 rounds. All allies can gain 50 Accumulator. Then recovers 100 Accumulator for self at the end. [Interference Pulse]: When the skill is cast, there is a 50% chance that Accumulator cannot be recovered.
  - **Ⅱ** at `+6` — Interference PulseⅡ (欧罗斯+2)
    Vertical Attack, deals 300% S-ATK damage to the target, applies [Interference Pulse] to all enemies, lasting 2 rounds. Has a 100% chance to gains 1 round of invisibility. All allies can gain 50 Accumulator. Then recovers 100 Accumulator for self at the end. [Interference Pulse]: When the skill is cast, there is a 50% chance that Accumulator cannot be recovered.
  - **Ⅲ** at `+10` — Interference PulseⅢ (欧罗斯+6)
    Vertical Attack, deals 320% S-ATK damage to the target, applies [Interference Pulse] to all enemies, lasting 2 rounds. Increases all allies' S-ATK and S-ATK damage by 120%, and has a 100% chance to gains 1 round of invisibility. All allies can gain 50 Accumulator. Then recovers 100 Accumulator for self at the end. [Interference Pulse]: When the skill is cast, there is a 50% chance that Accumulator cannot be recovered.
  - **Ⅳ** at `+15` — Interference PulseIV (欧罗斯+9)
    Vertical Attack, deals 340% S-ATK damage to the target, applies [Interference Pulse] to all enemies, lasting 2 rounds. Increases all allies' S-ATK and S-ATK damage by 120%, and has a 100% chance to gains 1 round of invisibility. The ally with the highest S-ATK (excluding yourself) gains [Overwhelming Suppression], lasting until the end of battle or that ally death (only one ally can have this effect at a time). All allies can gain 50 Accumulator. Then recovers 100 Accumulator for self at the end. [Interference Pulse]: When the skill is cast, there is a 50% chance that Accumulator cannot be recovered. [Overwhelming Suppression]: When the skill is cast, it is guaranteed to crit, and there is a 50% chance (probability for each target is calculated independently) to apply Weakness to all enemies, reducing all their attributes by 50% for 2 rounds.

**Slot 2 — Signal Cloaking** (id 1918, unlocks at `+2`)
  - **Ⅰ** at `+2` — Signal CloakingⅠ (欧罗斯+2)
    (Takes effect at the start of battle) At the start of battle, all enemies are inflicted with [Interference Pulse], lasting 2 rounds.
  - **Ⅱ** at `+9` — Signal CloakingⅡ (欧罗斯+9)
    (Takes effect at the start of battle) At the start of battle, all enemies are inflicted with [Interference Pulse], lasting 2 rounds. When casting a skill, there is a 50% chance to disable Eye of True Sight for all enemies.
  - **Ⅲ** at `+T` — Signal CloakingⅢ (欧罗斯+16)
    (Takes effect at the start of battle) At the start of battle, all enemies are inflicted with [Interference Pulse], lasting 2 rounds. The ally with the highest S-ATK (excluding yourself) gains [Overwhelming Suppression], lasting until the end of battle or that ally death (only one ally can have this effect at a time). When casting a skill, there is a 50% chance to disable Eye of True Sight for all enemies.
  - **Ⅳ** at `+T3` — Signal CloakingIV (欧罗斯+19)
    (Takes effect at the start of battle) At the start of battle, all enemies are inflicted with [Interference Pulse], lasting 2 rounds. The ally with the highest S-ATK (excluding yourself) gains [Overwhelming Suppression], lasting until the end of battle or that ally death (only one ally can have this effect at a time). When casting a skill, there is a 50% chance to disable Eye of True Sight for all enemies. Enemies affected by [Interference Pulse] have a 50% chance to change their skill to a single attack, and randomly against a random allied unit (from their own formation) when casting. (Prioritizes unit positioned at the front of the formation, with lower priority than Taunt.)

**Slot 3 — Insight** (id 1919, unlocks at `+4`)
  - **Ⅰ** at `+4` — InsightⅠ (欧罗斯+4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +60% S-ATK: +60% DMG Bonus (Absolute Value): +15% Crit ATK (Absolute Value) +15%
  - **Ⅱ** at `+10` — InsightⅡ (欧罗斯+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +90% S-ATK: +90% DMG Bonus (Absolute Value): +20% Crit ATK (Absolute Value) +20%
  - **Ⅲ** at `+14` — InsightⅢ (欧罗斯+14)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +120% S-ATK: +120% DMG Bonus (Absolute Value): +25% Crit ATK (Absolute Value) +25%
  - **Ⅳ** at `+T2` — InsightIV (欧罗斯+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +150% S-ATK: +150% DMG Bonus (Absolute Value): +30% Crit ATK (Absolute Value) +30%

**Slot 4 — Supernova: Overlimit Suppression** (id 1920, unlocks at `+3`)
  - **Ⅰ** at `+3` — Supernova: Overlimit SuppressionⅠ (欧罗斯+3)
    (Takes effect at the start of battle) At the start of battle, self gains 2 rounds of invisibility.
  - **Ⅱ** at `+13` — Supernova: Overlimit SuppressionⅡ (欧罗斯+13)
    (Takes effect at the start of battle) At the start of battle, self gains 2 rounds of invisibility. When receiving lethal damage, self will block this damage and gain [Dark Conceal] for 1 round, becoming immune to attacks and skill effects. (Can only activate once per battle.)
  - **Ⅲ** at `+T1` — Supernova: Overlimit SuppressionⅢ (欧罗斯+17)
    (Takes effect at the start of battle) At the start of battle, self gains 2 rounds of invisibility. When receiving lethal damage (including ignores immunity to lethal attacks and instant destruction effects), self will block this damage and gain [Dark Conceal] for 1 round, becoming immune to attacks and skill effects. (Can only activate once per battle.)
  - **Ⅳ** at `+T4` — Supernova: Overlimit SuppressionIV (欧罗斯+20)
    (Takes effect at the start of battle) At the start of battle, self gains 2 rounds of invisibility. When receiving lethal damage (ignores immunity to lethal and instant destruction effects), self will block the damage and gain [Dark Conceal] for 1 round, making her immune to attacks and skill effects. (Can only trigger once per battle) When using a skill, self additionally gains the active skill effect of an ally with the [Overlimit Suppression] status. (If that ally dies, the acquired effect is retained until it is replaced by another ally; only one ally’s skill can be acquired at a time. Cannot acquire skill effects gained from Lieutenant, Potential Chip, or other sources.) If there are other members of the Supernova Blades Fleet (Aiolia, Mu, Karon, Teda, Ulysses) in the team, they gain the [Overlimit Suppression] effect at the start of battle, lasting for 99 rounds. (Allies granted [Overlimit Suppression] by this effect only receive this buff effect. When casting a skill, Ouros can only gain the active skill effect of the ally with the highest S-ATK among own formation.)

### Augment cost (per step)
- `+1` — 5× Ranger Chip · 100,000 money
- `+2` — 10× Ranger Chip · 200,000 money
- `+3` — 21× Ranger Chip · 300,000 money
- `+4` — 28× Ranger Chip · 500,000 money
- `+5` — 35× Ranger Chip · 800,000 money
- `+6` — 42× Ranger Chip · 10× Pandora Power Core
- `+7` — 49× Ranger Chip · 50× Pandora Power Core
- `+8` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Elenia Exclusive Chip · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Elenia Exclusive Chip · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Elenia Exclusive Chip · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Elenia Exclusive Chip · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Elenia Exclusive Chip · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Elenia Exclusive Chip · 100× Alien Essence · 100× Transcendence Core

---

## 618 · Karen Thorne 凯伦·索恩
**Role** Ranger · **Attack** physical · **Generation** latest
**Ratings** Damage 9/10 · Defence 7/10 · Assist 10/10

### Skill panels
**Slot 1 — Soul Terror Mark** (id 1941, unlocks at `+0`)
  - **Ⅰ** at `+0` — Soul Terror MarkⅠ (凯伦・索恩+0)
    Vertical Attack, plunders 50% of the target's S-ATK and 75% of their Penetration (absolute value) for 2 rounds, then deals 340% S-ATK damage to the target and depletes targets' Accumulator. Lastly, recovers 100 Accumulator.
  - **Ⅱ** at `+7` — Soul Terror MarkⅡ (凯伦・索恩+3)
    Vertical Attack, plunders 50% of the target's S-ATK and 75% of their Penetration (absolute value) for 2 rounds, then deals 360% S-ATK damage to the target and depletes targets' Accumulator. Grants a Reflect Shield to itself and 2 random allies, they can reflect 80% received damage, lasting 2 rounds. Lastly, recovers 100 Accumulator.
  - **Ⅲ** at `+15` — Soul Terror MarkⅢ (凯伦・索恩+7)
    Vertical Attack, plunders 50% of the target's S-ATK and 75% of their Penetration (absolute value) for 2 rounds, then deals 380% S-ATK damage to the target and depletes targets' Accumulator. Grants a Reflect Shield to itself and 2 random allies, they can reflect 80% received damage, lasting 2 rounds. Has a 50% chance to Weaken all enemies (probability for each target calculated separately), deducting 40% of targets' stats for 1 round. Lastly, recovers 100 Accumulator.
  - **Ⅳ** at `+T3` — Soul Terror MarkIV (凯伦・索恩+15)
    Vertical Attack, plunders 75% of the target's S-ATK and 100% of their Penetration (absolute value) for 2 rounds, then deals 400% S-ATK damage to the target and depletes targets' Accumulator. Grants a Reflect Shield to itself and 2 random allies, they can reflect 80% received damage, lasting 2 rounds. Has a 50% chance to Weaken all enemies (probability for each target calculated separately), deducting 40% of targets' stats for 1 round. On the first skill cast at the start of BATTLE, 2 random allies additionally gain Dark Conceal for 2 rounds. Lastly, recovers 100 Accumulator.

**Slot 2 — Shadow Empowerment** (id 1942, unlocks at `+3`)
  - **Ⅰ** at `+3` — Shadow EmpowermentⅠ (凯伦・索恩+3)
    (Takes effect at the start of battle) After being hit by an S-ATK, gains Evasion, guaranteeing a dodge against enemy attacks (Lower priority than guaranteed hit), lasting until the next skill cast or for 1 round, whichever comes first. (Effect activates after taking damage.)
  - **Ⅱ** at `+9` — Shadow EmpowermentⅡ (凯伦・索恩+9)
    (Takes effect at the start of battle) After being hit by an S-ATK, gains Evasion, guaranteeing a dodge against enemy attacks (Lower priority than guaranteed hit), lasting until the next skill cast or for 1 round, whichever comes first. (Effect activates after taking damage.) At the start of battle, grants a Reflect Shield to itself and 2 random allies, they can reflect 80% received damage, lasting 2 rounds.
  - **Ⅲ** at `+T1` — Shadow EmpowermentⅢ (凯伦・索恩+17)
    (Takes effect at the start of battle) After being hit by an S-ATK, gains Evasion, guaranteeing a dodge against enemy attacks (Lower priority than guaranteed hit), lasting until the next skill cast or for 1 round, whichever comes first. (Effect activates after taking damage.) At the start of battle, grants a Reflect Shield to itself and 2 random allies, they can reflect 80% received damage, lasting 2 rounds. Upon death, all allies turn invisible for 2 rounds and gain a Rebirth effect, recovering immediately upon death with 100% of initial HP and 150 Accumulator. (unaffected by forbidding revival effects)
  - **Ⅳ** at `+T4` — Shadow EmpowermentIV (凯伦・索恩+20)
    (Takes effect at the start of battle) After being hit by an S-ATK, gains Evasion, guaranteeing a dodge against enemy attacks (Lower priority than guaranteed hit), lasting until the next skill cast or for 2 round, whichever comes first. (Effect activates after taking damage.) At the start of battle, grants a Reflect Shield to itself and 2 random allies, they can reflect 80% received damage, lasting 2 rounds. Upon death, all allies turn invisible for 2 rounds and gain a Rebirth effect, recovering immediately upon death with 100% of initial HP and 150 Accumulator. (unaffected by forbidding revival effects) Upon death, removes all allies' forbidding revival effects and revive limit effects. (This effect does not apply to already defeated allies or itself)

**Slot 3 — Night Spirit** (id 1943, unlocks at `+5`)
  - **Ⅰ** at `+5` — Night SpiritⅠ (凯伦・索恩+5)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP +60% Damage increase (absolute value) +15% Damage reduction (absolute value) +15%
  - **Ⅱ** at `+11` — Night SpiritⅡ (凯伦・索恩+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP +90% Damage increase (absolute value) +20% Damage reduction (absolute value) +20%
  - **Ⅲ** at `+T` — Night SpiritⅢ (凯伦・索恩+16)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP +120% Damage increase (absolute value) +25% Damage reduction (absolute value) +25%
  - **Ⅳ** at `+T2` — Night SpiritIV (凯伦・索恩+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP +150% Damage increase (absolute value) +30% Damage reduction (absolute value) +30%

### Augment cost (per step)
- `+1` — 5× Ranger Chip · 100,000 money
- `+2` — 10× Ranger Chip · 200,000 money
- `+3` — 21× Ranger Chip · 300,000 money
- `+4` — 28× Ranger Chip · 500,000 money
- `+5` — 35× Ranger Chip · 800,000 money
- `+6` — 42× Ranger Chip · 10× Pandora Power Core
- `+7` — 49× Ranger Chip · 50× Pandora Power Core
- `+8` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Elenia Exclusive Chip · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Elenia Exclusive Chip · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Elenia Exclusive Chip · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Elenia Exclusive Chip · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Elenia Exclusive Chip · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Elenia Exclusive Chip · 100× Alien Essence · 100× Transcendence Core

---

## 622 · Zeno 泽诺
**Role** Ranger · **Attack** physical · **Generation** latest
**Ratings** Damage 9/10 · Defence 7/10 · Assist 10/10

### Skill panels
**Slot 1 — Crystal Surge** (id 1956, unlocks at `+0`)
  - **Ⅰ** at `+0` — Crystal SurgeⅠ (泽诺+0)
    Vertical Attack, deals 320% S-ATK damage to targets. Grants all allies 120% S-ATK increases damage and +150% Crit ATK for 2 rounds. Applies [Stellar Eclipse] to 2 random enemies until the end of BATTLE. Lastly, recovers 100 Accumulator. [Stellar Eclipse]: The affected enemies’s S-ATK is reduced by 120%.
  - **Ⅱ** at `+6` — Crystal SurgeⅡ (泽诺+2)
    Vertical Attack, first removes buffs from targets, deals 360% S-ATK damage to targets. Grants all allies 120% S-ATK increases damage and +150% Crit ATK for 2 rounds. Applies [Stellar Eclipse] to 2 random enemies until the end of BATTLE. Lastly, recovers 100 Accumulator. [Stellar Eclipse]: The affected enemies’s S-ATK is reduced by 120%.
  - **Ⅲ** at `+10` — Crystal SurgeⅢ (泽诺+6)
    Vertical Attack, first removes buffs from targets, deals 380% S-ATK damage to targets. Grants all allies 120% S-ATK increases damage and +150% Crit ATK for 2 rounds. Gains Eye of True Sight for 99 rounds. Applies [Stellar Eclipse] to 2 random enemies until the end of BATTLE. Lastly, recovers 100 Accumulator. [Stellar Eclipse]: The affected enemies’s S-ATK is reduced by 120%. When casting skills, there is a 50% chance to miss. (Lower priority than guaranteed hit.)
  - **Ⅳ** at `+15` — Crystal SurgeIV (泽诺+9)
    Vertical Attack, first removes buffs from targets, deals 400% S-ATK damage to targets. Grants all allies 120% S-ATK increases damage and +150% Crit ATK for 2 rounds. Gains Eye of True Sight for 99 rounds. Applies [Stellar Eclipse] to 2 random enemies until the end of BATTLE. Lastly, recovers 100 Accumulator. [Stellar Eclipse]: The affected enemies’s S-ATK is reduced by 120%. When casting skills, there is a 75% chance to miss. (Lower priority than guaranteed hit.)

**Slot 2 — Crystal Glare** (id 1957, unlocks at `+2`)
  - **Ⅰ** at `+2` — Crystal GlareⅠ (泽诺+2)
    (Takes effect at the start of battle) Own S-ATK are guaranteed to crit.
  - **Ⅱ** at `+9` — Crystal GlareⅡ (泽诺+9)
    (Takes effect at the start of battle) Own S-ATK are guaranteed to crit. After the enemies with [Stellar Eclipse] uses a skill, there is a 50% chance they cannot recover Accumulator.
  - **Ⅲ** at `+T` — Crystal GlareⅢ (泽诺+16)
    (Takes effect at the start of battle) Own S-ATK are guaranteed to crit and can target enemies in [Dark Conceal]. After the enemies with [Stellar Eclipse] uses a skill, there is a 50% chance they cannot recover Accumulator. If the S-ATK doesn't kill an enemy, 1 extra S-ATK is launched as a follow-up attack.
  - **Ⅳ** at `+T3` — Crystal GlareIV (泽诺+19)
    (Takes effect at the start of battle) Own S-ATK are guaranteed to crit and can target enemies in [Dark Conceal]. After the enemies with [Stellar Eclipse] uses a skill, there is a 50% chance they cannot recover Accumulator. If the S-ATK doesn't kill an enemy, 1 extra S-ATK is launched as a follow-up attack. When the enemies with [Stellar Eclipse] uses a skill, if the skill effect includes [Slaughter Feast] or [Fatal Pursuit], after casting the skill, they gain [Crystallization], rendering them unable to act for 2 rounds. (This effect cannot be cleansed, isn't affected by immunity)

**Slot 3 — Crystal Vein** (id 1958, unlocks at `+4`)
  - **Ⅰ** at `+4` — Crystal VeinⅠ (泽诺+4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +60% S-ATK: +60% DMG Bonus (Absolute Value): +15% Crit ATK (Absolute Value) +15%
  - **Ⅱ** at `+10` — Crystal VeinⅡ (泽诺+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +90% S-ATK: +90% DMG Bonus (Absolute Value): +20% Crit ATK (Absolute Value) +20%
  - **Ⅲ** at `+14` — Crystal VeinⅢ (泽诺+14)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +120% S-ATK: +120% DMG Bonus (Absolute Value): +25% Crit ATK (Absolute Value) +25%
  - **Ⅳ** at `+T2` — Crystal VeinIV (泽诺+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +150% S-ATK: +150% DMG Bonus (Absolute Value): +30% Crit ATK (Absolute Value) +30%

**Slot 4 — Stellar Eclipse** (id 1959, unlocks at `+3`)
  - **Ⅰ** at `+3` — Stellar EclipseⅠ (泽诺+3)
    (Takes effect at the start of battle) At the start of battle, the enemy with the highest S-ATK gains [Stellar Eclipse] until the end of battle.
  - **Ⅱ** at `+13` — Stellar EclipseⅡ (泽诺+13)
    (Takes effect at the start of battle) At the start of battle, the enemy with the highest S-ATK gains [Stellar Eclipse] until the end of battle. If Zeno affected by certain control effects (Freeze, Lock, Confusion, Forbidding Skill Use, Petrify, Icebound, Entangle), they will be transferred to a random enemy.
  - **Ⅲ** at `+T1` — Stellar EclipseⅢ (泽诺+17)
    (Takes effect at the start of battle) At the start of battle, the enemy with the highest S-ATK gains [Stellar Eclipse] until the end of battle. If Zeno affected by certain control effects (Freeze, Lock, Confusion, Forbidding Skill Use, Petrify, Icebound, Entangle), they will be transferred to a random enemy. Enemies killed by Zeno that are revived will gain [Stellar Eclipse], lasting until the end of battle.
  - **Ⅳ** at `+T4` — Stellar EclipseIV (泽诺+20)
    (Takes effect at the start of battle) At the start of battle, the enemy with the highest S-ATK gains [Stellar Eclipse] until the end of battle. If Zeno affected by certain control effects (Freeze, Lock, Confusion, Forbidding Skill Use, Petrify, Icebound, Entangle), they will be transferred to a random enemy. Enemies killed by Zeno that are revived will gain [Stellar Eclipse], lasting until the end of battle. Enemies with [Stellar Eclipse] cannot receive Rebirth effects from themselves or allies (including effects from Lieutenants and Legendary Equipment).

### Augment cost (per step)
- `+1` — 5× Ranger Chip · 100,000 money
- `+2` — 10× Ranger Chip · 200,000 money
- `+3` — 21× Ranger Chip · 300,000 money
- `+4` — 28× Ranger Chip · 500,000 money
- `+5` — 35× Ranger Chip · 800,000 money
- `+6` — 42× Ranger Chip · 10× Pandora Power Core
- `+7` — 49× Ranger Chip · 50× Pandora Power Core
- `+8` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Zeno Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Zeno Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Zeno Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Zeno Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Zeno Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Zeno Ship Part · 100× Alien Essence · 100× Transcendence Core

---

## 632 · Kariel 卡里尔
**Role** Ranger · **Attack** physical · **Generation** latest
**Ratings** Damage 9/10 · Defence 7/10 · Assist 10/10

### Skill panels
**Slot 1 — Nano Scorch** (id 1988, unlocks at `+0`)
  - **Ⅰ** at `+0` — Nano ScorchⅠ (卡里尔+0)
    Cross Attack, deals 280% S-ATK damage to targets. Applies [Nano Scorch] to 2 random enemies the end of BATTLE. Lastly, recovers 100 Accumulator. [Nano Scorch]: When a linked enemy takes S-ATK damage, all other enemies linked to it take true damage equal to 50% of the damage received.
  - **Ⅱ** at `+6` — Nano ScorchⅡ (卡里尔+2)
    Cross Attack, deals 300% S-ATK damage to targets. Reduces the target's DEF and S-DEF by 75% for 2 rounds. Applies [Nano Scorch] to 2 random enemies the end of BATTLE. Lastly, recovers 100 Accumulator. [Nano Scorch]: When a linked enemy takes S-ATK damage, all other enemies linked to it take true damage equal to 50% of the damage received.
  - **Ⅲ** at `+10` — Nano ScorchⅢ (卡里尔+6)
    Cross Attack, deals 320% S-ATK damage to targets. Reduces the target's DEF and S-DEF by 75% for 2 rounds. Purifies all allies' abnormal statuses and control effects, and applies [Nano Scorch] to 2 random enemies the end of BATTLE. Lastly, recovers 100 Accumulator. [Nano Scorch]: When a linked enemy takes S-ATK damage, all other enemies linked to it take true damage equal to 50% of the damage received.
  - **Ⅳ** at `+15` — Nano ScorchIV (卡里尔+9)
    Cross Attack, deals 350% S-ATK damage to targets. Reduces the target's DEF and S-DEF by 75% for 2 rounds. Purifies all allies' abnormal statuses and control effects, clears the target's Accumulator, and applies [Nano Scorch] to 2 random enemies the end of BATTLE. Lastly, recovers 100 Accumulator. [Nano Scorch]: When a linked enemy takes S-ATK damage, all other enemies linked to it take true damage equal to 50% of the damage received.

**Slot 2 — Rebel Call** (id 1989, unlocks at `+2`)
  - **Ⅰ** at `+2` — Rebel CallⅠ (卡里尔+2)
    (Takes effect at the start of battle) At the start of battle, applies [Nano Scorch] to 2 random enemies.
  - **Ⅱ** at `+9` — Rebel CallⅡ (卡里尔+9)
    (Takes effect at the start of battle) At the start of battle, applies [Nano Scorch] to 2 random enemies. When a linked enemy is affected by certain control effects (Freeze, Brittle, Lock, Confuse, Forbidding Skill Use, Petrify, Icebound and Entangle), the same effect is applied to the other linked enemies.
  - **Ⅲ** at `+T` — Rebel CallⅢ (卡里尔+16)
    (Takes effect at the start of battle) At the start of battle, applies [Nano Scorch] to 2 random enemies. When a linked enemy is affected by certain control effects (Freeze, Brittle, Lock, Confuse, Forbidding Skill Use, Petrify, Icebound and Entangle), the same effect is applied to the other linked enemies. When self is affected by certain control effects (Freeze, Brittle, Lock, Confuse, Forbidding Skill Use, Petrify, Icebound and Entangle), the same effect is applied to enemies with [Nano Scorch].
  - **Ⅳ** at `+T3` — Rebel CallIV (卡里尔+19)
    (Takes effect at the start of battle) At the start of battle, applies [Nano Scorch] to 2 random enemies. When a linked enemy is affected by certain control effects (Freeze, Brittle, Lock, Confuse, Forbidding Skill Use, Petrify, Icebound and Entangle), the same effect is applied to the other linked enemies. (ignoring immunity and protection effects.) When self is affected by certain control effects (Freeze, Brittle, Lock, Confuse, Forbidding Skill Use, Petrify, Icebound and Entangle), the same effect is applied to enemies with [Nano Scorch].（ignoring immunity and protection effects.）

**Slot 3 — Ember** (id 1990, unlocks at `+4`)
  - **Ⅰ** at `+4` — EmberⅠ (卡里尔+4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP +60% Damage increase (absolute value) +15% Damage reduction (absolute value) +15%
  - **Ⅱ** at `+10` — EmberⅡ (卡里尔+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP +90% Damage increase (absolute value) +20% Damage reduction (absolute value) +20%
  - **Ⅲ** at `+14` — EmberⅢ (卡里尔+14)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP +120% Damage increase (absolute value) +25% Damage reduction (absolute value) +25%
  - **Ⅳ** at `+T2` — EmberIV (卡里尔+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP +150% Damage increase (absolute value) +30% Damage reduction (absolute value) +30%

**Slot 4 — Disintegrate** (id 1991, unlocks at `+3`)
  - **Ⅰ** at `+3` — DisintegrateⅠ (卡里尔+4)
    (Takes effect at the start of battle) Upon death, has a 100% chance to Lock the enemy affected by [Nano Scorch] for 2 rounds.
  - **Ⅱ** at `+13` — DisintegrateⅡ (卡里尔+11)
    (Takes effect at the start of battle) Upon death, has a 100% chance to Lock the enemy affected by [Nano Scorch] for 2 rounds. When any ally uses a skill, there is a 25% chance to instantly destroy enemy under control effects (ignoring immunity and protection effects, probability for each target calculated separately). If she dies, this effect is removed.
  - **Ⅲ** at `+T1` — DisintegrateⅢ (卡里尔+14)
    (Takes effect at the start of battle) Upon death, has a 100% chance to Lock the enemy affected by [Nano Scorch] for 2 rounds. When any ally uses a skill, there is a 25% chance to instantly destroy enemy under control effects (ignoring immunity and protection effects, probability for each target calculated separately). If she dies, this effect is removed. When using a skill, if 2 or more enemies are already afflicted with [Nano Scorch], there is a 50% chance to instantly destroy enemy with [Nano Scorch] (ignoring immunity and protection effects, probability for each target calculated separately).
  - **Ⅳ** at `+T4` — DisintegrateIV (卡里尔+18)
    (Takes effect at the start of battle) Upon death, has a 100% chance to Lock the enemy affected by [Nano Scorch] for 2 rounds, and dispel the Rebirth effect from enemy afflicted with [Nano Scorch]. When any ally uses a skill, there is a 25% chance to instantly destroy enemy under control effects (ignoring immunity and protection effects, probability for each target calculated separately). If she dies, this effect is removed. When using a skill, if 2 or more enemies are already afflicted with [Nano Scorch], there is a 50% chance to instantly destroy enemy with [Nano Scorch] (ignoring immunity and protection effects, probability for each target calculated separately), and the ally with the highest S-ATK (excluding self) will take an action immediately.

### Augment cost (per step)
- `+1` — 5× Ranger Chip · 100,000 money
- `+2` — 10× Ranger Chip · 200,000 money
- `+3` — 21× Ranger Chip · 300,000 money
- `+4` — 28× Ranger Chip · 500,000 money
- `+5` — 35× Ranger Chip · 800,000 money
- `+6` — 42× Ranger Chip · 10× Pandora Power Core
- `+7` — 49× Ranger Chip · 50× Pandora Power Core
- `+8` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Kariel's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Kariel's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Kariel's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Kariel's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Kariel's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Kariel's Ship Part · 100× Alien Essence · 100× Transcendence Core

---

## 635 · Kalastor 卡拉斯托
**Role** Ranger · **Attack** physical · **Generation** latest
**Ratings** Damage 8/10 · Defence 7/10 · Assist 10/10

### Skill panels
**Slot 1 — Starbreak Thrust** (id 2000, unlocks at `+0`)
  - **Ⅰ** at `+0` — Starbreak ThrustⅠ (卡拉斯托+0)
    Vertical Attack, first removes buff from targets, deals 350% S-ATK damage to the target. Lastly, recovers 100 Accumulator.
  - **Ⅱ** at `+6` — Starbreak ThrustⅡ (卡拉斯托+2)
    Vertical Attack, first removes buff from targets, deals 380% S-ATK damage to the target, increases all allies' S-ATK by 200% until the end of the battle. Lastly, recovers 100 Accumulator.
  - **Ⅲ** at `+10` — Starbreak ThrustⅢ (卡拉斯托+6)
    Vertical Attack, first removes buff from targets, deals 400% S-ATK damage to the target, increases all allies' S-ATK by 200% until the end of the battle, and reduces the target's S-DEF by 75% until the end of the battle. Lastly, recovers 100 Accumulator.
  - **Ⅳ** at `+T` — Starbreak ThrustIV (卡拉斯托+9)
    Vertical Attack, first removes buff from targets, deals 450% S-ATK damage to the target, increases all allies' S-ATK by 200% until the end of the battle, and reduces the target's S-DEF by 75% until the end of the battle. Has a 100% chance to inflict [Petrify] on the first enemy in the attack line for 2 rounds. Lastly, recovers 100 Accumulator.

**Slot 2 — Boulder Barrier** (id 2001, unlocks at `+2`)
  - **Ⅰ** at `+2` — Boulder BarrierⅠ (卡拉斯托+2)
    (Takes effect at the start of battle) At the start of battle and each time a skill is cast, all allies gain a shield that blocks 2 attacks, lasting 2 rounds.
  - **Ⅱ** at `+9` — Boulder BarrierⅡ (卡拉斯托+9)
    (Takes effect at the start of battle) At the start of battle and each time a skill is cast, all allies gain a shield that blocks 2 attacks, lasting 2 rounds. When using a skill, there is a 50% chance to additionally inflict [Petrify] on an enemy, lasting 2 rounds.
  - **Ⅲ** at `+15` — Boulder BarrierⅢ (卡拉斯托+16)
    (Takes effect at the start of battle) At the start of battle and each time a skill is cast, all allies gain a shield that blocks 2 attacks, lasting 2 rounds. When using a skill, there is a 50% chance to additionally inflict [Petrify] on an enemy, lasting 2 rounds. At the start of battle and upon each revival or rebirth, all allies gain Boulder Barrier, which is removed after triggering once. Boulder Barrier: When affected by control effects (Lock, Confuse, Exile, Freeze, Petrify, Brittle, Icebound, Entangle, Starbind, Binding and Crystallization), the corresponding effect is cleared and immediately triggers a Single attack with 500% S-ATK. This attack has a 100% chance to inflict petrify on the first enemy in a vertical line, lasting for 2 rounds.
  - **Ⅳ** at `+T3` — Boulder BarrierIV (卡拉斯托+19)
    (Takes effect at the start of battle) At the start of battle and each time a skill is cast, all allies gain a shield that blocks 2 attacks, lasting 2 rounds. When using a skill, there is a 50% chance to additionally inflict [Petrify] on an enemy, lasting 2 rounds. All [Petrify] effects applied by all allies are enforced, ignoring immunity and protection effects. At the start of battle and upon each revival or rebirth, all allies gain Boulder Barrier, which is removed after triggering once. Boulder Barrier: When affected by control effects (Lock, Confuse, Exile, Freeze, Petrify, Brittle, Icebound, Entangle, Starbind, Binding and Crystallization), the corresponding effect is cleared and immediately triggers a Single attack with 500% S-ATK. This attack has a 100% chance to inflict petrify on the first enemy in a vertical line, lasting for 2 rounds. Also grants a Shield that blocks 1 instance of any type of damage, which is removed after taking damage.

**Slot 3 — Desolate Boulder** (id 2002, unlocks at `+4`)
  - **Ⅰ** at `+4` — Desolate BoulderⅠ (卡拉斯托+4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +60% S-ATK: +60% DMG Bonus (Absolute Value): +15% Crit ATK (Absolute Value) +15%
  - **Ⅱ** at `+10` — Desolate BoulderⅡ (卡拉斯托+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +90% S-ATK: +90% DMG Bonus (Absolute Value): +20% Crit ATK (Absolute Value) +20%
  - **Ⅲ** at `+14` — Desolate BoulderⅢ (卡拉斯托+14)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +120% S-ATK: +120% DMG Bonus (Absolute Value): +25% Crit ATK (Absolute Value) +25%
  - **Ⅳ** at `+T2` — Desolate BoulderIV (卡拉斯托+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): ATK: +150% S-ATK: +150% DMG Bonus (Absolute Value): +30% Crit ATK (Absolute Value) +30%

**Slot 4 — Sanctum Law** (id 2003, unlocks at `+3`)
  - **Ⅰ** at `+3` — Sanctum LawⅠ (卡拉斯托+3)
    (Takes effect at the start of battle) When Kalastor casts a skill, if the hit enemy's S-ATK is significantly lower than his own, he gains an extra effect from Sanctum Law. (If the hit enemy's S-ATK is less than or equal to 2 times Kalastor's ATK, the condition is met. S-ATK is based on the value at the start of battle and is not affected by in-BATTLE buffs/debuffs. If multiple enemies are hit, the effect triggers as long as any enemy meets the condition.) Sanctum Law: Randomly revives 2 allies (not affected by forbidding revival effects), restoring them to 100% max HP and Accumulator.
  - **Ⅱ** at `+13` — Sanctum LawⅡ (卡拉斯托+13)
    (Takes effect at the start of battle) When Kalastor casts a skill, if the hit enemy's S-ATK is significantly lower than his own, he gains an extra effect from Sanctum Law. (If the hit enemy's S-ATK is less than or equal to 2 times Kalastor's ATK, the condition is met. S-ATK is based on the value at the start of battle and is not affected by in-BATTLE buffs/debuffs. If multiple enemies are hit, the effect triggers as long as any enemy meets the condition.) Sanctum Law: Randomly revives 2 allies (not affected by forbidding revival effects), restoring them to 100% max HP and Accumulator. Kalastor’s S-ATK has a 100% chance for instant destruction of the first enemy in a vertical line (ignores immunity to instant destruction).
  - **Ⅲ** at `+T1` — Sanctum LawⅢ (卡拉斯托+17)
    (Takes effect at the start of battle) When Kalastor casts a skill, if the hit enemy's S-ATK is significantly lower than his own, he gains an extra effect from Sanctum Law. (If the hit enemy's S-ATK is less than or equal to 2 times Kalastor's ATK, the condition is met. S-ATK is based on the value at the start of battle and is not affected by in-BATTLE buffs/debuffs. If multiple enemies are hit, the effect triggers as long as any enemy meets the condition.) Sanctum Law: Randomly revives 2 allies (not affected by forbidding revival effects), restoring them to 100% max HP and Accumulator. Kalastor’s S-ATK has a 100% chance for instant destruction of the first enemy in a vertical line (ignores immunity to instant destruction). Enemies killed by this attack can only be revived once (including Rebirth). After reaching the revival limit, they cannot be revived or Rebirth by any means (including revivals and rebirths unaffected by revival prohibition), lasting until the end of battle.
  - **Ⅳ** at `+T4` — Sanctum LawIV (卡拉斯托+20)
    (Takes effect at the start of battle) When Kalastor casts a skill, he gains the effect provided by Sanctum Law. If the enemy current formation's Force is significantly lower than own formation in this battle, all allies gain the effect provided by Sanctum Law when casting skills. (This condition is met when the enemy's Force is less than or equal to twice own Force; Force is based on the value at the start of battle and is not affected by in-battle buffs/debuffs.) Sanctum Law: Randomly revives 2 allies (not affected by forbidding revival effects), restoring them to 100% max HP and Accumulator. Kalastor’s S-ATK has a 100% chance for instant destruction of the first enemy in a vertical line (ignores immunity to instant destruction). Enemies killed by this attack can only be revived once (including Rebirth). After reaching the revival limit, they cannot be revived or Rebirth by any means (including revivals and rebirths unaffected by revival prohibition), lasting until the end of battle.

### Augment cost (per step)
- `+1` — 5× Ranger Chip · 100,000 money
- `+2` — 10× Ranger Chip · 200,000 money
- `+3` — 21× Ranger Chip · 300,000 money
- `+4` — 28× Ranger Chip · 500,000 money
- `+5` — 35× Ranger Chip · 800,000 money
- `+6` — 42× Ranger Chip · 10× Pandora Power Core
- `+7` — 49× Ranger Chip · 50× Pandora Power Core
- `+8` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Voyage Commemorative Coin - Stonecore Sanctum · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Voyage Commemorative Coin - Stonecore Sanctum · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Voyage Commemorative Coin - Stonecore Sanctum · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Voyage Commemorative Coin - Stonecore Sanctum · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Voyage Commemorative Coin - Stonecore Sanctum · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Voyage Commemorative Coin - Stonecore Sanctum · 100× Alien Essence · 100× Transcendence Core

---

## 640 · Linore 莉诺尔
**Role** Ranger · **Attack** physical · **Generation** latest
**Ratings** Damage 7/10 · Defence 10/10 · Assist 9/10

### Skill panels
**Slot 1 — Heatwave Cheers** (id 2020, unlocks at `+0`)
  - **Ⅰ** at `+0` — Heatwave CheersⅠ (莉诺尔+0)
    Cross Attack, deals 320% S-ATK damage to targets hit. Gains Eye of True Sight until the end of the battle. Lastly, you recover 100 Accumulator.
  - **Ⅱ** at `+6` — Heatwave CheersⅡ (莉诺尔+2)
    Cross Attack, deals 360% S-ATK damage to targets hit. Gains Eye of True Sight until the end of the battle. All allies gain a Shield equal to 80% of max HP (cannot stack, recasting refreshes the effect). Lastly, you recover 100 Accumulator.
  - **Ⅲ** at `+10` — Heatwave CheersⅢ (莉诺尔+6)
    Cross Attack, first plunders 100% Accumulator from the target, then deals 420% S-ATK damage to targets hit. Gains Eye of True Sight until the end of the battle. All allies gain a Shield equal to 80% of max HP (cannot stack, recasting refreshes the effect). Lastly, you recover 100 Accumulator.
  - **Ⅳ** at `+15` — Heatwave CheersIV (莉诺尔+9)
    Cross Attack, first plunders 100% Accumulator from the target, then deals 450% S-ATK damage to targets hit. Gains Eye of True Sight until the end of the battle. All allies gain a Shield equal to 80% of max HP (cannot stack; recasting refreshes the effect). All allies gain 30% increased S-ATK damage and 30% S-ATK, stacking up to 3 times, lasting until the end of the battle. Lastly, you recover 100 Accumulator.

**Slot 2 — Morale Surge** (id 2021, unlocks at `+2`)
  - **Ⅰ** at `+2` — Morale SurgeⅠ (莉诺尔+2)
    (Takes effect at the start of battle) At the start of battle and each time a skill is cast, ally with the highest S-ATK at the start of battle gains [Morale Surge], lasting until the end of battle or until that unit dies. (If the selected unit dies, another unit will be chosen; cannot select self) [Morale Surge]: When casting a skill, deals True Damage equal to 250% of the first attack's S-ATK damage to the enemy with the lowest HP.
  - **Ⅱ** at `+9` — Morale SurgeⅡ (莉诺尔+9)
    (Takes effect at the start of battle) At the start of battle and each time a skill is cast, ally with the highest S-ATK at the start of battle gains [Morale Surge], lasting until the end of battle or until that unit dies. (If the selected unit dies, another unit will be chosen; cannot select self) [Morale Surge]: When casting a skill, deals True Damage equal to 250% of the first attack's S-ATK damage to the enemy with the lowest HP. When casting a skill, increases all allies' Crit ATK by 30%, stacking up to 3 times and lasting until the end of battle.
  - **Ⅲ** at `+T` — Morale SurgeⅢ (莉诺尔+16)
    (Takes effect at the start of battle) At the start of battle and each time a skill is cast, ally with the highest S-ATK at the start of battle gains [Morale Surge], lasting until the end of battle or until that unit dies. (If the selected unit dies, another unit will be chosen; cannot select self) [Morale Surge]: When casting a skill, deals True Damage equal to 250% of the first attack's S-ATK damage to the enemy with the lowest HP. When casting a skill, increases all allies' Crit ATK by 30%, stacking up to 3 times and lasting until the end of battle. When casting a skill, increases all allies' damage dealt to controlled units by 10%, stacking up to 3 times and lasting until the end of battle.
  - **Ⅳ** at `+T3` — Morale SurgeIV (莉诺尔+19)
    (Takes effect at the start of battle) At the start of battle and each time a skill is cast, ally with the highest S-ATK at the start of battle gains [Morale Surge], lasting until the end of battle or until that unit dies. (If the selected unit dies, another unit will be chosen; cannot select self) [Morale Surge]: When casting a skill, deals True Damage equal to 250% of the first attack's S-ATK damage to the enemy with the lowest HP. When casting a skill, increases all allies' Crit ATK by 30%, stacking up to 3 times and lasting until the end of battle. When casting a skill, increases all allies' damage dealt to controlled units by 10%, stacking up to 3 times and lasting until the end of battle. When casting a skill, the unit with [Morale Surge] immediately takes 1 action.

**Slot 3 — Inspire** (id 2022, unlocks at `+4`)
  - **Ⅰ** at `+4` — InspireⅠ (莉诺尔+4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP +60% Damage increase (absolute value) +15% Damage reduction (absolute value) +15%
  - **Ⅱ** at `+10` — InspireⅡ (莉诺尔+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP +90% Damage increase (absolute value) +20% Damage reduction (absolute value) +20%
  - **Ⅲ** at `+14` — InspireⅢ (莉诺尔+14)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP +120% Damage increase (absolute value) +25% Damage reduction (absolute value) +25%
  - **Ⅳ** at `+T2` — InspireIV (莉诺尔+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP +150% Damage increase (absolute value) +30% Damage reduction (absolute value) +30%

**Slot 4 — Unity Dance** (id 2023, unlocks at `+3`)
  - **Ⅰ** at `+3` — Unity DanceⅠ (莉诺尔+3)
    (Takes effect at the start of battle) At the start of battle, increases all allies' S-ATK by 120% until the end of the battle.
  - **Ⅱ** at `+13` — Unity DanceⅡ (莉诺尔+13)
    (Takes effect at the start of battle) At the start of battle, increases all allies' S-ATK by 120% until the end of the battle. When casting a skill, there is a 100% chance to grant Rebirth to units with [Morale Surge], and an additional 50% chance to grant Rebirth to own, lasting for 2 rounds. (Revives immediately upon death, restoring 100% HP and Accumulator as at the start of battle, unaffected by revive restriction effects)
  - **Ⅲ** at `+T1` — Unity DanceⅢ (莉诺尔+17)
    (Takes effect at the start of battle) At the start of battle, increases all allies' S-ATK by 120% until the end of the battle. When casting a skill, there is a 100% chance to grant Rebirth to units with [Morale Surge], and an additional 50% chance to grant Rebirth to own, lasting for 2 rounds. (Revives immediately upon death, restoring 100% HP and Accumulator as at the start of battle, unaffected by revive restriction effects.) When any ally casts a skill, restores 25 Accumulator to all other allies except self.
  - **Ⅳ** at `+T4` — Unity DanceIV (莉诺尔+20)
    (Takes effect at the start of battle) At the start of battle, increases all allies' S-ATK by 120% until the end of the battle. When casting a skill, there is a 100% chance to grant Rebirth to units with [Morale Surge], and an additional 50% chance to grant Rebirth to own, lasting for 2 rounds. (Revives immediately upon death, restoring 100% HP and Accumulator as at the start of battle, unaffected by revive restriction effects) When any ally casts a skill, restores 25 Accumulator to all other allies except self. At the start of battle and each time a skill is cast, units with [Morale Surge] gain an additional effect: when attacking an Enemy, ignores the target's current HP and treats the target as having only 30% HP; this effect is removed after one skill attack. (Applicable cases: effects that require checking the target's remaining HP; does not affect effects that require the target's HP ratio to be above a certain value to activate)

### Augment cost (per step)
- `+1` — 5× Ranger Chip · 100,000 money
- `+2` — 10× Ranger Chip · 200,000 money
- `+3` — 21× Ranger Chip · 300,000 money
- `+4` — 28× Ranger Chip · 500,000 money
- `+5` — 35× Ranger Chip · 800,000 money
- `+6` — 42× Ranger Chip · 10× Pandora Power Core
- `+7` — 49× Ranger Chip · 50× Pandora Power Core
- `+8` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+9` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+10` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+11` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+12` — 49× Ranger Chip · 50× Pandora Power Crystal · 50× Pandora Power Core
- `+13` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+14` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+15` — 98× Ranger Chip · 100× Pandora Power Crystal · 100× Pandora Power Core
- `+T` — 15× Linore's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Linore's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Linore's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Linore's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Linore's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Linore's Ship Part · 100× Alien Essence · 100× Transcendence Core

---
