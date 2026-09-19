# Galaxy Legends — SSS Rovers (36 heroes)

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
| 331 | Bernard | 伯纳德 | 6 | 7 | 9 | old |
| 358 | Arthur | 麦加登 | 7 | 7 | 10 | old |
| 378 | Light Watcher | 光明守望者 | 7 | 7 | 7 | old |
| 388 | Grosso | 格罗索 | 7 | 6 | 7 | old |
| 403 | Arc | 阿克 | 4 | 5 | 8 | old |
| 426 | Afsan | 阿夫赛 | 6 | 7 | 8 | old |
| 445 | Anubis | 阿努比斯 | 7 | 7 | 8 | old |
| 450 | Vaccine | 疫苗 | 6 | 8 | 9 | old |
| 462 | Alastor | 阿拉斯托尔 | 8 | 7 | 10 | old |
| 488 | Sh'eenaz | 希恩娜兹 | 8 | 7 | 10 | old |
| 495 | Xel'Nagir | 萨尔纳加 | 6 | 8 | 9 | old |
| 502 | Ilexis | 伊莱克斯 | 8 | 7 | 10 | old |
| 509 | Atropos | 阿特洛波斯 | 6 | 8 | 9 | old |
| 519 | Lucy | 露西 | 6 | 8 | 9 | old |
| 524 | Sasha | 萨莎 | 6 | 8 | 9 | old |
| 525 | Lister | 李斯特 | 6 | 8 | 9 | old |
| 532 | Amanda | 阿曼达 | 6 | 8 | 9 | old |
| 533 | Solaris | 索拉里斯 | 7 | 7 | 8 | latest |
| 540 | Vivian | 薇薇安 | 6 | 8 | 9 | latest |
| 545 | Balthasar | 巴尔萨 | 6 | 8 | 9 | latest |
| 550 | Valdi | 瓦尔迪 | 6 | 8 | 9 | latest |
| 558 | Liesel | 莉洁儿 | 6 | 8 | 9 | latest |
| 562 | Ashley | 艾希 | 6 | 8 | 9 | latest |
| 570 | Camille | 卡洛琳 | 6 | 8 | 9 | latest |
| 577 | Mira | 米拉 | 6 | 8 | 9 | latest |
| 578 | Night Phantom | 幽夜 | 8 | 7 | 10 | latest |
| 585 | Zander | 赞德 | 8 | 7 | 10 | latest |
| 593 | Lorna | 洛娜 | 6 | 8 | 9 | latest |
| 596 | Entropy·Zero | 熵·零 | 8 | 7 | 10 | old |
| 599 | Caster | 卡斯特 | 8 | 8 | 10 | latest |
| 606 | Narin | 奈恩 | 6 | 8 | 9 | latest |
| 610 | Sirius Gray | 西里斯・格雷 | 7 | 9 | 10 | latest |
| 616 | Ulysses | 尤丽缇丝 | 6 | 8 | 10 | latest |
| 626 | Dong Xue | 冬雪 | 8 | 7 | 10 | latest |
| 631 | Xelos | 赛洛斯 | 8 | 7 | 10 | latest |
| 642 | Flakvod | 弗拉克沃德 | 7 | 8 | 10 | latest |

---

## 331 · Bernard 伯纳德
**Role** Rover · **Attack** physical · **Generation** old
**Ratings** Damage 6/10 · Defence 7/10 · Assist 9/10

### Signature skill
- **Ⅰ** at `+0` — Blade of Bond (4月WD徘徊者)
  Vertical attack, deals 145% S-ATK damage, reduces hitting targets' 75% accumulator. At the same time reduces hitting targets' 90% ATK and increases 60% Crit for all friendly ships. The effect lasts for 1 round.
- **Ⅱ** at `+T4` — Blade of BondⅡ (伯纳德)
  Vertical attack, deals 180% S-ATK damage, reduces hitting targets' 100% accumulator. At the same time reduces hitting targets' 90% ATK and increases 80% Crit for all friendly ships. The effect lasts for 1 round.

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
- `+T` — 15× Bernard Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Bernard Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Bernard Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Bernard Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Bernard Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Bernard Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 358 · Arthur 麦加登
**Role** Rover · **Attack** physical · **Generation** old
**Ratings** Damage 7/10 · Defence 7/10 · Assist 10/10

### Signature skill
- **Ⅰ** at `+0` — Revive - Battle Continuation (新wd徘徊复活)
  Single attack, deals 188% S-ATK damage and revives all destroyed friendly ships and restores 60% HP (initial status) and 100% Accumulator for them.
- **Ⅱ** at `+T4` — Revive - Battle ContinuationⅡ (麦加登，重生.再战)
  Single attack, deals 220% S-ATK damage and revives all destroyed friendly ships and restores 100% HP (initial status) and 100% Accumulator for them.

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
- `+T` — 15× Arthur Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Arthur Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Arthur Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Arthur Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Arthur Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Arthur Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 378 · Light Watcher 光明守望者
**Role** Rover · **Attack** physical · **Generation** old
**Ratings** Damage 7/10 · Defence 7/10 · Assist 7/10

### Signature skill
- **Ⅰ** at `+0` — Force Strike Ⅰ (尤达大师)
  Cross attack, deals 300% S-ATK damage and casts a weakening effect on targets which get hit, decreasing all stats on those affected by 50% for 1 round. It also increases S-DEF by 70% and DEF by 70% for 2 friendly ships with the lowest HP (except the ship itself) on the team for 2 rounds and recovers 75 Accumulators for the ship itself.
- **Ⅱ** at `+T2` — Force Strike Ⅱ (光明守望者，尤达大师)
  Cross attack, deals 350% S-ATK damage and casts a weakening effect on targets which get hit, decreasing all stats on those affected by 50% for 1 round. It also increases S-DEF by 90% and DEF by 90% for 2 friendly ships with the lowest HP (except the ship itself) on the team for 2 rounds and recovers 100 Accumulators for the ship itself.
- **III** at `+T4` — Force Strike III (光明守望者T4，尤达大师)
  Cross attack, deals 380% S-ATK damage and casts a weakening effect on targets which get hit, decreasing all stats on those affected by 60% for 1 round. It also increases S-DEF by 120% and DEF by 120% for 2 friendly ships with the lowest HP (except the ship itself) on the team for 2 rounds. Also heals the 2 allies (except the ship itself) with the least HP for 40%. Lastly, recovers 100 Accumulators for the ship itself.

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
- `+T` — 15× Light Watcher Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Light Watcher Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Light Watcher Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Light Watcher Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Light Watcher Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Light Watcher Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 388 · Grosso 格罗索
**Role** Rover · **Attack** physical · **Generation** old
**Ratings** Damage 7/10 · Defence 6/10 · Assist 7/10

### Signature skill
- **Ⅰ** at `+0` — Shadow Rage (4月wd)
  Vertical attack, deals 300% S-ATK damage; then it has a 75% chance to increase 50% ATK for all Heroes in the team; in addition, it will increase 1M ATK for all Heroes in the team. Then recovers 25 Accumulator for all Heroes in the team and 100 more Accumulator for self.
- **II** at `+T4` — Shadow Rage II (格罗索T4,暗影之怒)
  Vertical attack, first plunders 40% Accumulator from the target, then deals 350% S-ATK damage. Subsequently, there's a 100% chance to increase all allies' ATK by 70% and further increase by 1.2 million. Adds 50 Accumulator to all allies and 100 Accumulator to self.

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
- `+T` — 15× Grosso Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Grosso Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Grosso Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Grosso Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Grosso Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Grosso Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 403 · Arc 阿克
**Role** Rover · **Attack** physical · **Generation** old
**Ratings** Damage 4/10 · Defence 5/10 · Assist 8/10

### Signature skill
- **Ⅰ** at `+0` — Voodoo Mastery (阿克，巫毒法术)
  Vertical Attack, deals 300% S-ATK damage, and each target will take additional S-ATK damage equal to (target's current Accumulator x 0.5)%. The max Accumulator is 300. It also has a 70% chance to inflict the Death Code on hit targets for 2 rounds. If a target is destroyed with the Death Code, the destroyed target will induce a cross explosion which will deal 500% S-ATK to the enemies in range. Then, it heals itself and two teammates with the lowest HP (healing coefficient 300%). In addition, recovers 100 Accumulator for itself.
- **Ⅱ** at `+T2` — Voodoo Mastery Ⅱ (阿克+T2)
  Vertical Attack, deals 350% S-ATK damage, and each target will take additional S-ATK damage equal to (target's current Accumulator x 0.5)%. The max Accumulator is 300. It also has a 80% chance to inflict the Death Code on hit targets for 2 rounds. If a target is destroyed with the Death Code, the destroyed target will induce a cross explosion which will deal 500% S-ATK to the enemies in range. Then, it heals itself and two teammates with the lowest HP (healing coefficient 300%). In addition, recovers 100 Accumulator for itself.
- **III** at `+T4` — Voodoo Mastery III (阿克，巫毒法术)
  Vertical Attack, deals 380% S-ATK damage, and each target will take additional S-ATK damage equal to target's current Accumulator x 1%. The max Accumulator is 300. It also has a 100% chance to inflict the Death Code on hit targets for 2 rounds. If a target is destroyed with the Death Code, the destroyed target will induce a cross explosion which will deal 550% S-ATK to the enemies in range. Then, it heals itself and two teammates with the lowest HP (healing coefficient 350%). In addition, recovers 100 Accumulator for itself.

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
- `+T` — 15× Arc’s Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Arc’s Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Arc’s Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Arc’s Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Arc’s Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Arc’s Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 426 · Afsan 阿夫赛
**Role** Rover · **Attack** physical · **Generation** old
**Ratings** Damage 6/10 · Defence 7/10 · Assist 8/10

### Signature skill
- **I** at `+0` — Rumble Roaring I (阿夫赛，震撼咆哮)
  Cross attack, deal 300% S-ATK damage to targets and curse them for 2 rounds; when the curse is over, the hit targets will suffer 500% S-ATK damage. It can also revive all defeated teammates and recover them to 80% of the initial HP and 100% of the initial Accumulator and reduce hit targets’ Hit Rate by 50% for 1 round. Shields will also be activated for two teammates (self and teammates just revived are not included) with the lowest HP percentage so they can become immune to lock and weaken debuffs for 2 rounds. In addition, recover 100 Accumulator for self.
- **II** at `+T2` — Rumble Roaring II (阿夫赛+T2)
  Cross attack, deal 320% S-ATK damage to targets and curse them for 2 rounds; when the curse is over, the hit targets will suffer 600% S-ATK damage. It can also revive all defeated teammates and recover them to 90% of the initial HP and 100% of the initial Accumulator and reduce hit targets’ Hit Rate by 50% for 1 round. Shields will also be activated for two teammates (self and teammates just revived are not included) with the lowest HP percentage so they can become immune to lock and weaken debuffs for 2 rounds. In addition, recover 100 Accumulator for self.
- **III** at `+T2` — Rumble RoaringIII (阿夫赛+T2)
  Cross attack, deal 340% S-ATK damage to targets and curse them for 2 rounds; when the curse is over, the hit targets will suffer 800% S-ATK damage. It can also revive all defeated teammates and recover them to 100% of the initial HP and 100% of the initial Accumulator and reduce hit targets’ Hit Rate by 70% for 1 round. Shields will also be activated for all allies (teammates just revived are not included) so they can become immune to Lock and Weaken debuffs for 2 rounds. In addition, recover 100 Accumulator for self.

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
- `+T` — 15× Afsan's Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Afsan's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Afsan's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Afsan's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Afsan's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Afsan's Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 445 · Anubis 阿努比斯
**Role** Rover · **Attack** physical · **Generation** old
**Ratings** Damage 7/10 · Defence 7/10 · Assist 8/10

### Signature skill
- **Ⅰ** at `+0` — Guide of Souls (阿努比斯，灵魂引渡)
  Cross attack, plunder 50% Accumulator and 18 million HP from the targets and then deal 300% S-ATK damage to them. Restore 50 Accumulator and 25% of max HP for all teammates. Increase all friendly units' (including self) ATK, DEF, S-ATK, and S-DEF by 50% for 1 round. Recover 100 Accumulator for self.
- **II** at `+T` — Guide of SoulsII (阿努比斯+T，灵魂引渡)
  Cross attack, plunder 55% Accumulator and 20 million HP from the targets and then deal 300% S-ATK damage to them. Restore 50 Accumulator and 35% of max HP for all teammates. Increase all friendly units' (including self) ATK, DEF, S-ATK, and S-DEF by 60% for 1 round. Recover 100 Accumulator for self.
- **Ⅲ** at `+T` — Guide of SoulsⅢ (阿努比斯+T，灵魂引渡)
  Cross attack, plunders 60% Accumulator and 30 million HP from targets and then deals 350% S-ATK damage. Restores 60 Accumulator and 40% of max HP for all friendly units (excluding self). Then, increases all friendly units' ATK, DEF, S-ATK, and S-DEF by 80%, for 1 round. Finally, recovers 100 Accumulator for self.

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
- `+T` — 12× Anubis's Ship Parts · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 16× Anubis's Ship Parts · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 22× Anubis's Ship Parts · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 30× Anubis's Ship Parts · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Anubis's Ship Parts · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Anubis's Ship Parts · 140× Alien Essence · 140× Transcendence Core

---

## 450 · Vaccine 疫苗
**Role** Rover · **Attack** physical · **Generation** old
**Ratings** Damage 6/10 · Defence 8/10 · Assist 9/10

### Signature skill
- **Ⅰ** at `+0` — Life Force (疫苗，生命之力)
  Cross attack, deals 280% S-ATK damage, plunders 50% of S-DEF & DEF from targets, and has a 100% chance (probability for each target is calculated independently) to expose invisible enemies. At the same time, increases all friendly units' (including self) ATK, S-ATK, DEF, and S-DEF by 100%, for 2 rounds. Restores 40% of max HP for all teammates(including self), then links with all friendly ships, taking 90% of team damage and activates a BUFF for self to reduce received damage by 70%, for 2 rounds. Also has a 60% chance (probability for each type is calculated independently) of making all friendly units immune to Weaken, Lock and Freeze, and all types of Accumulators plunder debuffs from the enemy,for 2 rounds. Then recovers 100 Accumulator for self.
- **Ⅱ** at `+T` — Life ForceⅡ (疫苗，生命之力Ⅱ)
  Cross attack, deals 300% S-ATK damage, plunders 60% of S-DEF & DEF from targets, and has a 100% chance (probability for each target is calculated independently) to expose invisible enemies. At the same time, increases all friendly units' (including self) ATK, S-ATK, DEF, and S-DEF by 100%, for 2 rounds. Restores 50% of max HP for all teammates(including self), then links with all friendly ships, taking 90% of team damage and activates a BUFF for self to reduce received damage by 80%, for 2 rounds. Also has a 70% chance (probability for each type is calculated independently) of making all friendly units immune to Weaken, Lock and Freeze, and all types of Accumulators plunder debuffs from the enemy,for 2 rounds. Then recovers 100 Accumulator for self.
- **Ⅲ** at `+T3` — Life ForceⅢ (疫苗，生命之力Ⅲ)
  Cross attack, deals 330% S-ATK damage, plunders 60% of S-DEF & DEF from targets, and has a 100% chance (probability for each target is calculated independently) to expose invisible enemies. At the same time, increases all friendly units' (including self) ATK, S-ATK, DEF, and S-DEF by 100%, for 2 rounds. Restores 50% of max HP for all teammates(including self), then links with all friendly ships, taking 90% of team damage and activates a BUFF for self to reduce received damage by 80%, for 2 rounds. Also has a 80% chance (probability for each type is calculated independently) of making all friendly units immune to Weaken, Lock and Freeze, and all types of Accumulators plunder debuffs from the enemy,for 2 rounds. It has a 50% chance to revive all defeated teammates and restores 100% HP and 100% Accumulator for them (the rate for each target will be settled independently,does not add a buff effect to this skill). Then recovers 100 Accumulator for self.
- **IV** at `+T4` — Life Force IV (疫苗，生命之力IV)
  Cross attack, deals 350% S-ATK damage, plunders 80% of S-DEF & DEF from targets, and has a 100% chance (probability for each target calculated separately) to expose invisible enemies. At the same time, increases all friendly units' (including self) ATK, S-ATK, DEF, and S-DEF by 120%, for 2 rounds. Restores 50% of max HP for all teammates (including self), and then links with all friendly ships, taking 90% of team damage, while Vaccine takes damage passed through a link once that is no more than 40% of its max HP; Activates a BUFF for self to reduce received damage by 80%, for 2 rounds. Also has a 100% chance (probability for each type calculated separately) of making all friendly units immune to Weaken, Lock, Freeze, Confuse and all types of Accumulators plunder and forbidding skill use debuffs from the enemy, for 2 rounds. Has a 80% chance to be immune to Instant Destruction for 1 round and an 80% chance to revive all defeated teammates and restore 100% HP and 100% Accumulator for them (probability for each target calculated separately, and does not add a buff effect to this skill, which isn't affected by forbidding revival effects). Also recovers 100 Accumulator.
- **Ⅴ** at `Awaken` — — (疫苗T4，触发技能)
  _(no English description shipped)_

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
- `+T` — 15× Vaccine Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Vaccine Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Vaccine Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Vaccine Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Vaccine Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Vaccine Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 462 · Alastor 阿拉斯托尔
**Role** Rover · **Attack** physical · **Generation** old
**Ratings** Damage 8/10 · Defence 7/10 · Assist 10/10

### Signature skill
- **Ⅰ** at `+0` — Hell's Judgment Ⅰ (地狱审判)
  Cross attack, deals 300% S-ATK damage. First, clears all buffs from targets, then clears their Accumulator. There is a 100% chance to confuse all enemy Rovers for 1 round, and a 100% chance to decrease targets' DEF and S-DEF by 80% for 1 round. Also, it makes self immune to 1 lethal attack for 1 round. Finally, recovers 100 Accumulator for self.
- **Ⅱ** at `+T` — Hell's JudgmentⅡ (阿拉斯托尔，地狱审判Ⅰ)
  Cross attack, deals 340% S-ATK damage. First, clears all buffs from targets, then clears their Accumulator. There is a 100% chance to confuse all enemy Rovers for 1 round, and a 100% chance to decrease targets' DEF and S-DEF by 90% for 1 round. Also, it makes self immune to 1 lethal attack for 1 round. Finally, recovers 100 Accumulator for self.
- **Ⅲ** at `+T3` — Hell's JudgmentⅢ (阿拉斯托尔，地狱审判Ⅱ)
  Cross attack, first clears all buffs from targets, then plunders 75% Accumulator from them and deals 380% S-ATK damage. Confuses all enemy Rovers for 1 round. It also has a 100% chance to Weaken targets and enemy Rovers, reducing all of their stats by 70% for 1 round. Decrease targets' DEF and S-DEF by 90% for 1 round. Also, it makes self immune to 1 lethal attack for 1 round. Finally, recovers 100 Accumulator for self.
- **IV** at `+T4` — Hell's JudgmentIV (阿拉斯托尔，地狱审判Ⅱ)
  Cross attack, first clears all buffs from targets, then plunders 100% Accumulator from them and deals 420% S-ATK damage. Confuses all enemy Rovers and targets for 2 rounds. It also has a 100% chance to Weaken targets and enemy Rovers, reducing all of their stats by 70% for 1 round. Decrease targets' DEF and S-DEF by 90% for 1 round. Also, it makes self immune to 1 lethal attack for 1 round. Has a 100% chance to remove Rebirth (including Rebirth effects of Lieutenants and legendary equipment) effects from all enemies. Finally, recovers 100 Accumulator for self. Gains an Extra Effect at the start of battle and with each skill cast. This extra effect grants a 100% chance to instantly destroy (ignores immunity to lethal attacks and instant destruction) 2 random enemies upon death.
- **Ⅴ** at `Awaken` — — (阿拉斯托尔，死亡触发技能)
  _(no English description shipped)_

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
- `+T` — 15× Alastor Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Alastor Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Alastor Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Alastor Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Alastor Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Alastor Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 488 · Sh'eenaz 希恩娜兹
**Role** Rover · **Attack** physical · **Generation** old
**Ratings** Damage 8/10 · Defence 7/10 · Assist 10/10

### Signature skill
- **Ⅰ** at `+0` — Soul LamentⅠ (希恩纳兹，窃魂歌咏)
  Cross attack; plunders 30% Accumulator from targets before dealing 300% S-ATK damage and reducing their Hit Rate by 40% (absolute value). Increases all friendly units' Dodge by 40% for 2 rounds. There's also a 50% chance to Confuse targets for 2 rounds. Finally, recovers 100 Accumulator. Each time it or a friendly unit successfully Dodges an enemy attack, it gains one stack of Soul Stealer (starts with 1 stack, max 4 stacks). Loses all additional stacks (reverting back to the initial 1 stack) upon death.Its ability changes with each stack of Soul Stealer, which provides the following additional effects when casting the skill: 1 stack: Gains an Evasive ability that allows it to Dodge enemy attacks for 2 rounds. 2 stacks: Overloads hit targets. Casting a skill in Overload consumes 50% more Accumulator and reduces the S-ATK damage dealt by 50% for 1 round. 3 stacks: Each stack of Soul Stealer increases all friendly units' damage dealt by 10% and reduces S-ATK damage taken by 10% for 2 rounds. 4 stacks: Has all skill effects of stacks 1 to 3. Also has a 50% chance to apply Rebirth to all friendly units (probability calculated separately for each unit) for 1 round; Rebirth revives units immediately upon death and restores them to 80% of their max HP and 100% Accumulator.
- **Ⅱ** at `+T` — Soul LamentⅡ (希恩纳兹，窃魂歌咏)
  Cross attack; plunders 40% Accumulator from targets before dealing 350% S-ATK damage and reducing their Hit Rate by 60% (absolute value). Increases all friendly units' Dodge by 60% for 2 rounds. There's also a 50% chance to Confuse targets for 2 rounds. Finally, recovers 100 Accumulator.Each time it or a friendly unit successfully Dodges an enemy attack, it gains one stack of Soul Stealer (starts with 1 stack, max 4 stacks). Loses all additional stacks (reverting back to the initial 1 stack) upon death.Its ability changes with each stack of Soul Stealer, which provides the following additional effects when casting the skill:1 stack: Gains an Evasive ability that allows it to Dodge enemy attacks for 2 rounds.2 stacks: Overloads hit targets. Casting a skill in Overload consumes 50% more Accumulator and reduces the S-ATK damage dealt by 50% for 1 round.3 stacks: Each stack of Soul Stealer increases all friendly units' damage dealt by 12% and reduces S-ATK damage taken by 12% for 2 rounds.4 stacks: Has all skill effects of stacks 1 to 3. Also has a 50% chance to apply Rebirth to all friendly units (probability calculated separately for each unit) for 1 round; Rebirth revives units immediately upon death and restores them to 100% of their max HP and 100% Accumulator.
- **Ⅲ** at `+T3` — Soul LamentⅢ (希恩纳兹，窃魂歌咏)
  Cross attack; plunders 40% Accumulator from targets before dealing 350% S-ATK damage and reducing their Hit Rate by 60% (absolute value). Increases all friendly units' Dodge by 60% for 2 rounds. There's also a 60% chance to Confuse targets for 2 rounds. Finally, recovers 100 Accumulator.Each time it or a friendly unit successfully Dodges an enemy attack, it gains one stack of Soul Stealer (starts with 1 stack, max 4 stacks). Loses all additional stacks (reverting back to the initial 1 stack) upon death.Its ability changes with each stack of Soul Stealer, which provides the following additional effects when casting the skill:1 stack: Gains an Evasive ability that allows it to Dodge enemy attacks for 2 rounds. Has an extra 80% chance to apply an Evasive ability to 2 random allied units (except for yourself) for 2 rounds. Sh'eenaz's Evasive ability has a 100% chance to fully avoid some control effects (Freeze, Lock, Confuse, Forbidding Skill Use), debuffs (Weaken), and Instant Destruction. 2 stacks: Overloads hit targets. Casting a skill in Overload consumes 50% more Accumulator and reduces the S-ATK damage dealt by 50% for 1 round.3 stacks: Each stack of Soul Stealer increases all friendly units' damage dealt by 12% and reduces S-ATK damage taken by 12% for 2 rounds.4 stacks: Has all skill effects of stacks 1 to 3. Also has a 50% chance to apply Rebirth to all friendly units (probability calculated separately for each unit) for 1 round; Rebirth revives units immediately upon death and restores them to 100% of their max HP and 100% Accumulator.
- **IV** at `+T4` — Soul LamentIV (希恩纳兹T4，窃魂歌咏IV)
  Cross attack; plunders 50% Accumulator from targets before dealing 380% S-ATK damage and reducing their Hit Rate by 80% (absolute value). Increases all friendly units' Dodge by 80% for 2 rounds. There's also a 75% chance to Confuse targets for 2 rounds. Finally, recovers 100 Accumulator. Each time it or a friendly unit successfully Dodges an enemy attack, it gains one stack of Soul Stealer (starts with 1 stack, max 4 stacks). Loses all additional stacks (reverting back to the initial 1 stack) upon death.Its ability changes with each stack of Soul Stealer, which provides the following additional effects when casting the skill:1 stack: Gains an Evasive ability that allows it to Dodge enemy attacks for 2 rounds. Has an extra 100% chance to apply an Evasive ability to 2 random allied units (except for yourself) for 2 rounds. Sh'eenaz's Evasive ability has a 100% chance to fully avoid some control effects (Freeze, Lock, Confuse, Forbidding Skill Use, Petrify, Icebound, Entangle), debuffs (Weaken), and Instant Destruction. 2 stacks: Overloads hit targets. Casting a skill in Overload consumes 80% more Accumulator and reduces the S-ATK damage dealt by 60% for 1 round. 3 stacks: Each stack of Soul Stealer increases all friendly units' damage dealt by 15% and reduces S-ATK damage taken by 15% for 2 rounds.4 stacks: Has all skill effects of stacks 1 to 3. Also has a 75% chance to apply Rebirth to all friendly units (probability calculated separately for each unit) for 1 round; Rebirth revives units immediately upon death and restores them to 100% of their max HP and 100% Accumulator. Gains 4 stacks of Soul Stealer for 2 rounds, applies an Evasive ability to self and a random allied unit for 2 rounds.

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
- `+T` — 15× Sh'eenaz Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Sh'eenaz Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Sh'eenaz Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Sh'eenaz Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Sh'eenaz Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Sh'eenaz Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 495 · Xel'Nagir 萨尔纳加
**Role** Rover · **Attack** physical · **Generation** old
**Ratings** Damage 6/10 · Defence 8/10 · Assist 9/10

### Signature skill
- **Ⅰ** at `+0` — Morning Star (萨尔纳加，晨星之灵)
  Cross attack, deals 220% S-ATK damage. Gain 1 stack of Soul Light for each skill cast and whenever an enemy dies (stacks up to 5 times and lasts until the end of battle. Stacks are lost upon death.) Whenever an allied unit (except the ship itself) receives lethal damage (including instant death), 1 stack of Soul Light is expended to block that damage and clear all stat debuffs. When an enemy unit is resurrected, 1 stack of Soul Light is expended to reduce its HP and Accumulator after revival by 20%. Each stack of Soul Light expended costs your 18 million HP. There's also a 50% chance to apply a Rebirth effect for yourself to revive immediately upon death, recovering 100% HP and 100 Accumulator, for 1 round. Finally, recovers 100 Accumulator.
- **Ⅱ** at `+T` — Morning StarⅡ (萨尔纳加，晨星之灵)
  Cross attack, deals 240% S-ATK damage. Gain 2 stacks of Soul Light for each skill cast and 1 stack of Soul Light whenever an enemy dies (stacks up to 5 times and lasts until the end of battle. Stacks are lost upon death.) Whenever an allied unit (including self) receives lethal damage (including instant death), 1 stack of Soul Light is expended to block that damage and clear all stat debuffs and control effects. When an enemy unit is resurrected, 1 stack of Soul Light is expended to reduce its HP and Accumulator after revival by 30%. Each stack of Soul Light expended costs your 18 million HP. There's also a 50% chance to apply a Rebirth effect for yourself to revive immediately upon death, recovering 100% HP and 100 Accumulator, for 1 round. Finally, recovers 100 Accumulator.
- **Ⅲ** at `+T3` — Morning StarⅢ (萨尔纳加，晨星之灵)
  Cross attack, deals 260% S-ATK damage. Gain 2 stacks of Soul Light for each skill cast and whenever an enemy dies (stacks up to 5 times and lasts until the end of battle. Stacks are lost upon death.) Whenever an allied unit (including self) receives lethal damage (including instant death), 1 stack of Soul Light is expended to block that damage and clear all stat debuffs and control effects, as well as recover 50% of max HP and 50 Accumulator. When an enemy unit is resurrected, 1 stack of Soul Light is expended to reduce its HP and Accumulator after revival by 40%. Each stack of Soul Light expended costs your 15 million HP. There's also a 70% chance to apply a Rebirth effect for yourself to revive immediately upon death, recovering 100% HP and 100 Accumulator, for 1 round. Finally, recovers 100 Accumulator.
- **IV** at `+T4` — Morning StarIV (萨尔纳加，晨星之灵)
  Cross attack, deals 300% S-ATK damage. Gain 2 stacks of Soul Light for each skill cast and whenever an enemy dies (stacks up to 5 times and lasts until the end of battle. Stacks are lost upon death.) Whenever an allied unit (including self) receives lethal damage (including instant death), 1 stack of Soul Light is expended to block that damage and clear all stat debuffs and control effects, as well as recover 100% of max HP and 100 Accumulator. When an enemy unit is resurrected, 1 stack of Soul Light is expended to reduce its HP and Accumulator after revival by 80%. Has a 70% chance to grant yourself Rebirth (Lieutenant rebirth effects are prioritized) for 1 round. Upon death, you will be revived with HP and Accumulator equal to 100% of your initial state. Finally, recovers 100 Accumulator.

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
- `+T` — 15× Xel'Nagir Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Xel'Nagir Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Xel'Nagir Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Xel'Nagir Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Xel'Nagir Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Xel'Nagir Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 502 · Ilexis 伊莱克斯
**Role** Rover · **Attack** physical · **Generation** old
**Ratings** Damage 8/10 · Defence 7/10 · Assist 10/10

### Signature skill
- **Ⅰ** at `+0` — Revenge AttackⅠ (复仇反击)
  Cross Attack, deals 280% S-ATK damage to targets. Has a 40% chance to make the target consume an extra 20% Accumulator to cast skills, lasting for 1 round. Gives 3 random allied ships a 30% chance, lasting for 1 round, to cause the same effect to a random enemy for 1 round when inflicted with control effects (Freeze, Confuse, Lock). Has a 50% chance to instantly destroy a random enemy ship upon death for 2 rounds. Lastly, you recover 100 Accumulator.
- **Ⅱ** at `+T` — Revenge AttackⅡ (复仇反击)
  Cross Attack, deals 300% S-ATK damage to targets. Has a 60% chance to make the target consume an extra 40% Accumulator to cast skills, lasting for 1 round. Gives 3 random allied ships a 50% chance, lasting for 2 rounds, to cause the same effect to a random enemy for 1 round when inflicted with control effects (Freeze, Confuse, Lock, Forbidding Skill Use). Has a 60% chance to make allied heroes of a certain class ignore enemy immunity or protection against their skills with control effects (Freeze, Lock, Confuse, Forbidding Skill Use, Entangle, Petrify, Icebound) or debuffs (Poison, Weaken) for 1 round (Priority of Hero Class: Striker, Ranger, Destroyer, Rover, Protector, Flagship. If heroes of a certain class are dead or missing, next class will be chosen in the order of priority). Has an 80% chance to instantly destroy a random enemy ship upon death for 2 rounds. Lastly, you recover 100 Accumulator.
- **Ⅲ** at `+T3` — Revenge AttackⅢ (复仇反击)
  Cross Attack, deals 320% S-ATK damage to targets. Has a 70% chance to make the target consume an extra 50% Accumulator to cast skills, lasting for 1 round. Gives 3 random allied ships a 75% chance, lasting for 2 rounds, to cause the same effect to a random enemy, which lasts for 1 round and ignores immunity, when inflicted with control effects (Freeze, Confuse, Lock, Forbidding Skill Use, Entangle). Has an 80% chance to make allied heroes of a certain class ignore enemy immunity or protection against their skills with control effects (Freeze, Lock, Confuse, Forbidding Skill Use, Entangle, Petrify, Icebound) or debuffs (Poison, Weaken) for 1 round (Priority of Hero Class: Striker, Ranger, Destroyer, Rover, Protector, Flagship. If heroes of a certain class are dead or missing, next class will be chosen in the order of priority). Has a 100% chance to instantly destroy a random enemy ship upon death for 2 rounds. Lastly, you recover 100 Accumulator.
- **IV** at `+T4` — Revenge Attack IV (复仇反击)
  Cross Attack, deals 340% S-ATK damage to targets. Has a 75% chance to make the target consume an extra 65% Accumulator to cast skills, lasting for 1 round. Gives all allied ships a 75% chance, lasting for 2 rounds, to cause the same effect to a random enemy, which lasts for 1 round and ignores immunity, when inflicted with control effects (Freeze, Confuse, Lock, Forbidding Skill Use, Entangle, Petrify, Icebound). Has a 100% chance to make allied heroes of a certain class ignore enemy immunity or protection against their skills with control effects (Freeze, Lock, Confuse, Forbidding Skill Use, Entangle, Petrify, Icebound) or debuffs (Poison, Weaken) for 1 round (Priority of Hero Class: Striker, Ranger, Destroyer, Rover, Protector, Flagship. If heroes of a certain class are dead or missing, next class will be chosen in the order of priority). Has a 100% chance to instantly destroy 2 random enemy ships upon death for 2 rounds. Lastly, you recover 100 Accumulator.

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
- `+T` — 15× Ilexis Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Ilexis Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Ilexis Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Ilexis Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Ilexis Ship Part · 130× Inert Alloy · 100× Heated Alloy
- `Awaken` — 180× Ilexis Ship Part · 130× Inert Alloy · 100× Heated Alloy

---

## 509 · Atropos 阿特洛波斯
**Role** Rover · **Attack** physical · **Generation** old
**Ratings** Damage 6/10 · Defence 8/10 · Assist 9/10

### Signature skill
- **Ⅰ** at `+0` — Nox NightmareⅠ (阿特洛波斯)
  Cross attack, deals 260% S-ATK damage to targets. Has a 50% chance to send 2 random enemies into a [Nightmare] for 2 rounds. When in a [Nightmare], the skills they cast against allies have a 30% lower chance to trigger and the skills they cast against enemies have a 30% chance to instead target their own allies (each skill effect is calculated individually; [Nightmare] cannot change the target for Energy Transfer and Nebula EMP). Units with [Nightmare] have a 50% chance to spread the Nightmare to 1 random ally when acting. If a unit with [Nightmare] dies, a 2-round [Nightmare] effect is spread to 1 random ally. Should all enemy units be affected by [Nightmare], they will be unable to act until they die (this effect can only trigger 1 time per battle but this trigger chance resets whenever Atropos is revived). Lastly, you recover 100 Accumulator.
- **Ⅱ** at `+T` — Nox NightmareⅡ (阿特洛波斯)
  Cross attack, deals 280% S-ATK damage to targets. Has a 60% chance to send 2 random enemies into a [Nightmare] for 2 rounds. When in a [Nightmare], the skills they cast against allies have a 40% lower chance to trigger and the skills they cast against enemies have a 40% chance to instead target their own allies (each skill effect is calculated individually; [Nightmare] cannot change the target for Energy Transfer and Nebula EMP). Units with [Nightmare] have a 50% chance to spread the Nightmare to 1 random ally when acting. If a unit with [Nightmare] dies, a 2-round [Nightmare] effect is spread to 1 random ally. Should all enemy units be affected by [Nightmare], they will be unable to act until they die (this effect can only trigger 1 time per battle but this trigger chance resets whenever Atropos is revived). Lastly, you recover 100 Accumulator.
- **Ⅲ** at `+T3` — Nox NightmareⅢ (阿特洛波斯)
  Cross attack, deals 300% S-ATK damage to targets. Has an 80% chance to send 2 random enemies into a [Nightmare] for 2 rounds. When in a [Nightmare], the skills they cast against allies have a 50% lower chance to trigger and the skills they cast against enemies have a 50% chance to instead target their own allies (each skill effect is calculated individually; [Nightmare] cannot change the target for Energy Transfer and Nebula EMP). Units in the [Nightmare] state cast skills, 50% of them will cast an instant kill on a random unit in the [Nightmare] state; Units with [Nightmare] have a 50% chance to spread the Nightmare to 1 random ally when acting. If a unit with [Nightmare] dies, a 2-round [Nightmare] effect is spread to 1 random ally. Should all enemy units be affected by [Nightmare], they will be unable to act until they die (this effect can only trigger 1 time per battle but this trigger chance resets whenever Atropos is revived). Lastly, you recover 100 Accumulator.
- **Ⅳ** at `+T4` — —
  _(no English description shipped)_

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
- `+T` — 15× Atropos Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Atropos Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Atropos Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Atropos Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Atropos Ship Part · 100× Alien Essence · 100× Transcendence Core

---

## 519 · Lucy 露西
**Role** Rover · **Attack** physical · **Generation** old
**Ratings** Damage 6/10 · Defence 8/10 · Assist 9/10

### Signature skill
- **I** at `+0` — Warp SpeedI (露西，超速运转I)
  Cross attack, deals 240% S-ATK damage. Lucy gains 1 Warp Energy whenever an ally uses a skill and 1 Warp Energy for every 3rd allied Normal Attack. Warp Energy stacks up to 7, each stack giving Lucy 5% damage reduction and 10% DEF and S-DEF. If Lucy uses a skill when at 7 stacks of Warp Energy, Lucy expends all stacks and increases the damage of the ally with the highest attack (the highest of ATK and S-ATK) by 40% for 2 rounds. Debuffs and status effects of the ally with the highest attack are also cleared before acting next (does not apply to extra actions on the original turn), and it can attack 2 times in a row. Lastly, you recover 100 Accumulator.
- **II** at `+T` — Warp SpeedII (露西，超速运转II)
  Cross attack, deals 260% S-ATK damage. Lucy gains 1 Warp Energy whenever an ally uses a skill and 1 Warp Energy for every 3rd allied Normal Attack. Warp Energy stacks up to 7, each stack giving Lucy 8% damage reduction and 12% DEF and S-DEF. If Lucy uses a skill when at 7 stacks of Warp Energy, Lucy expends all stacks and increases the damage of the ally with the highest attack (the highest of ATK and S-ATK) by 50% for 2 rounds. Debuffs and status effects of the ally with the highest attack are also cleared before acting next (does not apply to extra actions on the original turn), and it can attack 2 times in a row. Lastly, you recover 100 Accumulator.
- **III** at `+T3` — Warp SpeedIII (露西，超速运转III)
  Cross attack, deals 280% S-ATK damage. Lucy gains 1 Warp Energy whenever an ally uses a skill and 1 Warp Energy for every 3rd allied Normal Attack. Warp Energy stacks up to 7, each stack giving Lucy 10% damage reduction and 15% DEF and S-DEF. If Lucy uses a skill when at 7 stacks of Warp Energy, Lucy expends all stacks and increases the damage of the ally with the highest attack (the highest of ATK and S-ATK) by 60% for 2 rounds. Debuffs and status effects of the ally with the highest attack are also cleared before acting next (does not apply to extra actions on the original turn), and it can attack 2 times in a row. Has a 50% chance to revive all allies (probability for each target calculated separately) and restores 100% of their initial HP and 100 Accumulator. Lastly, you recover 100 Accumulator. Lucy gains a shield (lasts until the end of the battle) that withstands 1 instance of lethal damage at the start of battle.
- **IV** at `+T4` — Warp SpeedIV (露西，超速运转IV)
  Cross attack, deals 320% S-ATK damage. Lucy gains 1 Warp Energy whenever an ally uses a skill and 1 Warp Energy for every 3rd allied Normal Attack. Warp Energy stacks up to 7, each stack giving Lucy 12% damage reduction and 18% DEF and S-DEF. If Lucy uses a skill when at 7 stacks of Warp Energy, Lucy expends all stacks and increases the damage of the ally with the highest attack (the highest of ATK and S-ATK) by 80% for 2 rounds and applies a shield that withstands 1 instance of lethal damage lasting 1 round. Debuffs and status effects of the ally with the highest attack are also cleared before acting next (does not apply to extra actions on the original turn), its Accumulator increases to 150 if below 150 Accumulator, and it can attack 2 times in a row. Has a 75% chance to revive all allies (probability for each target calculated separately) and restores 100% of their initial HP and 100 Accumulator. Lastly, you recover 100 Accumulator. Lucy gains a shield (lasts until the end of the battle) that withstands 1 instance of lethal damage at the start of battle.

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
- `+T` — 15× Lucy Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Lucy Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Lucy Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Lucy Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Lucy Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Lucy Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 524 · Sasha 萨莎
**Role** Rover · **Attack** physical · **Generation** old
**Ratings** Damage 6/10 · Defence 8/10 · Assist 9/10

### Signature skill
- **Ⅰ** at `+0` — Super Healing (麦基之怒)
  Cross attack, deals 240% S-ATK damage and heals all allies for 30% of max HP. Lastly, you recover 100 Accumulator.

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
- `+T` — 15× Sasha Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Sasha Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Sasha Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Sasha Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Sasha Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Sasha Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 525 · Lister 李斯特
**Role** Rover · **Attack** physical · **Generation** old
**Ratings** Damage 6/10 · Defence 8/10 · Assist 9/10

### Signature skill
- **I** at `+0` — Energy BlockI (李斯特，能源封禁I)
  Cross attack, deals 300% S-ATK damage and reduces the ATK, S-ATK and E-ATK of all enemies by 25% for 2 rounds (does not stack but ignores all immunities and protection effects). Has a 50% chance to Confuse the target for 2 rounds and a 50% chance to apply 1 stack of [Energy Block]. Units that already have [Energy Block] gain 1 stack of [Energy Block] for 2 rounds (stacks up to 4). Upon reaching 4 stacks, all stacks of [Energy Block] are consumed and that unit's skills are set to a 2-round cooldown, during which no skills can be triggered. Also puts all of the unit's skills on a 1-round cooldown when it is next revived. Lastly, you recover 100 Accumulator.
- **II** at `+T` — Energy BlockII (李斯特，能源封禁II)
  Cross attack, deals 320% S-ATK damage and reduces the ATK, S-ATK and E-ATK of all enemies by 30% for 2 rounds (does not stack but ignores all immunities and protection effects). Also reveals all of the enemy's invisible units. Has a 50% chance to Confuse the target for 2 rounds and a 50% chance to apply 1 stack of [Energy Block]. Units that already have [Energy Block] gain 1 stack of [Energy Block] for 2 rounds (stacks up to 4). Upon reaching 4 stacks, all stacks of [Energy Block] are consumed and that unit's skills are set to a 2-round cooldown, during which no skills can be triggered. Also puts all of the unit's skills on a 1-round cooldown when it is next revived. Lastly, you recover 100 Accumulator.
- **III** at `+T3` — Energy BlockIII (李斯特，能源封禁III)
  Cross attack, deals 360% S-ATK damage and reduces the ATK, S-ATK and E-ATK of all enemies by 40% (does not stack but ignores all immunities and protection effects) and increases the damage of all allies by 20% for 2 rounds. Also reveals all of the enemy's invisible units. Has a 50% chance to Confuse (ignores immunities and protection effects) the target for 2 rounds and a 50% chance to apply 1 stack of [Energy Block] for 2 rounds (enemies affected by Confuse gain 1 extra stack of [Energy Block]). Units that already have [Energy Block] gain 1 stack of [Energy Block] (stacks up to 4). Also, whenever allies use skills, they apply 1 stack of [Energy Block] for 2 rounds to a random enemy that already has [Energy Block]. Upon reaching 4 stacks, all stacks of [Energy Block] are consumed and that unit's skills are set to a 2-round cooldown, during which no skills can be triggered and allies cannot buff or apply skill effects to it (blocked buff and skill effects have no effect) for 2 rounds. Also puts all of the unit's skills on a 1-round cooldown when it is next revived. Lastly, you recover 100 Accumulator. Puts the skills of 1 random enemy on a 1-round cooldown at the start of battle, prevents its allies from buffing or applying skill effects to it (blocked buff and skill effects have no effect) for 1 round, and applies 1 stack of [Energy Block] to 2 random enemies.
- **IV** at `+T4` — Energy BlockIV (李斯特，能源封禁IV)
  Cross attack, deals 380% S-ATK damage and reduces the ATK, S-ATK and E-ATK of all enemies by 45% (does not stack but ignores all immunities and protection effects) and increases the damage of all allies by 30% for 2 rounds. Also reveals all of the enemy's invisible units. Has a 65% chance to Confuse (ignores immunities and protection effects) the target for 2 rounds and a 100% chance to apply 1 stack of [Energy Block] for 2 rounds (enemies affected by Confuse gain 1 extra stack of [Energy Block]). Units that already have [Energy Block] gain 1 stack of [Energy Block] (stacks up to 4). Also, whenever allies use skills, they apply 1 stack of [Energy Block] for 2 rounds to a random enemy that already has [Energy Block]. Each stack of Energy Block increases the damage the unit takes by 15%. Upon reaching 4 stacks, all stacks of [Energy Block] are consumed and that unit's skills are set to a 2-round cooldown, during which no skills can be triggered and allies cannot buff or apply skill effects to it (blocked buff and skill effects have no effect) for 2 rounds. Also applies forbidding revival and rebirth (a unit that dies while this effect is active cannot revive or rebirth) for 2 rounds and increases the damage it takes by 75%. Also puts all of the unit's skills on a 1-round cooldown when it is next revived. Lastly, you recover 100 Accumulator. Puts the skills of 1 random enemy on a 1-round cooldown at the start of battle, prevents its allies from buffing or applying skill effects to it (blocked buff and skill effects have no effect) for 1 round, applies forbidding revival and rebirth (a unit that dies while this effect is active cannot revive or rebirth) for 1 round and increases the damage it takes by 75%, and applies 1 stack of [Energy Block] to 2 random enemies.

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
- `+T` — 15× Lister Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Lister Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Lister Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Lister Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Lister Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Lister Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 532 · Amanda 阿曼达
**Role** Rover · **Attack** physical · **Generation** old
**Ratings** Damage 6/10 · Defence 8/10 · Assist 9/10

### Signature skill
- **Ⅰ** at `+0` — Fervent TideⅠ (阿曼达0~15阶，狂欢浪潮)
  Cross attack; deals 280% S-ATK damage. Amanda has a 50% chance each to cast [Fervent Dance] and [Dance of Joy] whenever she casts a skill. Once she's cast each skill at least once, she'll instead cast [Revelry Tide] for the remainder of that battle (does not reset upon death).[Fervent Dance]: Select a random allied unit of a class based on the following order: Destroyer, Striker, Ranger, Flagship, Rover or Protector (target is chosen in descending order if none of the previous class can be found) and apply a shield lasting 1 round that blocks 1 attack, has a 50% chance to enable the unit to act again on its next round but deal 60% less damage on that extra action (does not stack with similar effects, extra 1 action will not take effect on itself), and gives it an extra effect lasting 1 round: if the target is a Destroyer, Striker or Ranger, it deals 0.5% extra damage for each 1% of max HP it is missing; if the target is a Protector, Rover or Flagship, its skills have a 40% chance to Confuse the enemy for 1 round. Lastly, you recover 100 Accumulator.[Dance of Joy]: Heal all allies for 30% of max HP and cleanse debuffs and crowd-control effects (Freeze, Lock, Confuse) and Forbidding Skill Use. All allies also gain 20% S-ATK damage reduction for 2 rounds. Has a 30% chance to revive dead allies to 100% of their initial HP and Accumulator (probability calculated individually for each unit). Lastly, you recover 100 Accumulator.[Revelry Tide]: Has the effects of both [Fervent Dance] and [Dance of Joy].
- **Ⅱ** at `+T` — Fervent TideⅡ (阿曼达T~T2阶，狂欢浪潮)
  Cross attack; deals 300% S-ATK damage. Amanda has a 50% chance each to cast [Fervent Dance] and [Dance of Joy] whenever she casts a skill. Once she's cast each skill at least once, she'll instead cast [Revelry Tide] for the remainder of that battle (does not reset upon death).[Fervent Dance]: Select a random allied unit of a class based on the following order: Destroyer, Striker, Ranger, Flagship, Rover or Protector (target is chosen in descending order if none of the previous class can be found) and apply a shield lasting 1 round that blocks 1 attack, has a 75% chance to enable the unit to act again on its next round but deal 50% less damage on that extra action (does not stack with similar effects, extra 1 action will not take effect on itself), and gives it an extra effect lasting 1 round: if the target is a Destroyer, Striker or Ranger, it deals 1% extra damage for each 1% of max HP it is missing; if the target is a Protector, Rover or Flagship, its skills have a 50% chance to Confuse the enemy for 1 round. Lastly, you recover 100 Accumulator.[Dance of Joy]: Heal all allies for 40% of max HP and cleanse debuffs and crowd-control effects (Freeze, Lock, Confuse, Petrify, Icebound, Entangle, Weaken) and Forbidding Skill Use. All allies also gain 30% S-ATK damage reduction for 2 rounds. Has a 40% chance to revive dead allies to 100% of their initial HP and Accumulator (probability calculated individually for each unit). Has a 40% chance to make all allies invisible (probability calculated individually for each unit) for 1 round. Lastly, you recover 100 Accumulator.[Revelry Tide]: Has the effects of both [Fervent Dance] and [Dance of Joy].
- **Ⅲ** at `+T3` — Fervent TideⅢ (阿曼达T3阶，狂欢浪潮)
  Cross attack; deals 320% S-ATK damage. Amanda has a 50% chance each to cast [Fervent Dance] and [Dance of Joy] whenever she casts a skill. Once she's cast each skill at least once, she'll instead cast [Revelry Tide] for the remainder of that battle (does not reset upon death).[Fervent Dance]: Select a random allied unit of a class based on the following order: Destroyer, Striker, Ranger, Flagship, Rover or Protector (target is chosen in descending order if none of the previous class can be found) and apply a shield lasting 1 round that blocks 1 attack, has a 100% chance to enable the unit to act again on its next round but deal 40% less damage on that extra action (does not stack with similar effects, extra 1 action will not take effect on itself), and gives it an extra effect lasting 1 round: if the target is a Destroyer, Striker or Ranger, it deals 1.5% extra damage for each 1% of max HP it is missing; if the target is a Protector, Rover or Flagship, its skills removes the target's buffs, after which they have a 50% chance to Confuse the enemy for 1 round. Lastly, you recover 100 Accumulator.[Dance of Joy]: Heal all allies for 40% of max HP and cleanse debuffs and crowd-control effects (Freeze, Lock, Confuse, Petrify, Icebound, Entangle, Weaken) and Forbidding Skill Use. All allies also gain 40% S-ATK damage reduction for 2 rounds. Has a 50% chance to revive dead allies to 100% of their initial HP and Accumulator (probability calculated individually for each unit). Has a 50% chance to make all allies invisible (probability calculated individually for each unit) for 1 round. Lastly, you recover 100 Accumulator.[Revelry Tide]: Has the effects of both [Fervent Dance] and [Dance of Joy].
- **IV** at `+T4` — Fervent TideIV (阿曼达T4阶，狂欢浪潮)
  Cross attack; deals 350% S-ATK damage. Amanda has a 50% chance each to cast [Fervent Dance] and [Dance of Joy] whenever she casts a skill. Once she's cast each skill at least once, she'll instead cast [Revelry Tide] for the remainder of that battle (does not reset upon death).[Fervent Dance]: Select a random allied unit of a class based on the following order: Destroyer, Striker, Ranger, Flagship, Rover or Protector (target is chosen in descending order if none of the previous class can be found) and apply a shield lasting 1 round that blocks 2 attacks, granting it immunity to skill effects (except for skill damage and subsequent damage) while the shield is active, has a 100% chance to enable the unit to act again on its next round but deal 35% less damage on that extra action (does not stack with similar effects, extra 1 action will not take effect on itself), and gives it an extra effect lasting 1 round: if the target is a Destroyer, Striker or Ranger, it deals 2% extra damage for each 1% of max HP it is missing; if the target is a Protector, Rover or Flagship, its skills removes the target's buffs, after which they have a 50% chance to Confuse the enemy for 1 round. Lastly, you recover 100 Accumulator.[Dance of Joy]: Heal all allies for 50% of max HP and cleanse debuffs and crowd-control effects (Freeze, Lock, Confuse, Petrify, Icebound, Entangle, Weaken) and Forbidding Skill Use. All allies also gain 40% S-ATK damage reduction for 2 rounds. Has a 60% chance to revive dead allies to 100% of their initial HP and Accumulator (probability calculated individually for each unit). Has a 70% chance to make all allies invisible (probability calculated individually for each unit) for 1 round. Lastly, you recover 100 Accumulator.[Revelry Tide]: Has the effects of both [Fervent Dance] and [Dance of Joy].

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
- `+T` — 15× Amanda Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Amanda Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Amanda Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Amanda Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Amanda Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Amanda Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 533 · Solaris 索拉里斯
**Role** Rover · **Attack** physical · **Generation** latest
**Ratings** Damage 7/10 · Defence 7/10 · Assist 8/10

### Skill panels
**Slot 1 — Phantom** (id 1540, unlocks at `+0`)
  - **Ⅰ** at `+0` — PhantomⅠ (索拉里斯+0，精神幻影I)
    Cross attack, deals 280% S-ATK damage. Each skill cast has a 50% chance to create Phantoms (cannot create a Phantom of Solaris) out of 1 random ships of the enemy's starting lineup (Phantoms cannot appear on locations where ships, not summonings, started the battle or on locations where there is a ship). Up to 2 can exist at a time. Lastly, you recover 100 Accumulator. Phantom: Possesses the same skills as the original ship but takes 50% more damage and deals 50% reduced damage. Phantoms gain 50% of the original ship's attributes. All Phantoms vanish if Solaris dies and cannot be revived or rebirthed. (Note: If a Phantom casts a skill with a unique effect that another of your ships can cast, such as Unyielding or Energy Transfer, the effect of the last skill cast prevails.)(Only 1 Phantom may exist of the same ship at a time)
  - **Ⅱ** at `+5` — PhantomⅡ (索拉里斯+5，精神幻影II)
    Cross attack, deals 300% S-ATK damage. Each skill cast has an 80% chance to create Phantoms (cannot create a Phantom of Solaris) out of 1 random ships of the enemy's starting lineup (Phantoms cannot appear on locations where ships, not summonings, started the battle or on locations where there is a ship). Up to 1 can exist at a time. If there are already 2 active Phantoms, apply a shield that blocks 1 attack (for 1 round) to all Phantoms and heal them for 30% of max HP. Lastly, you recover 100 Accumulator. Phantom: Possesses the same skills as the original ship but takes 40% more damage and deals 40% reduced damage. Phantoms gain 60% of the original ship's attributes. All Phantoms vanish if Solaris dies and cannot be revived or rebirthed. (Note: If a Phantom casts a skill with a unique effect that another of your ships can cast, such as Unyielding or Energy Transfer, the effect of the last skill cast prevails.)(Only 1 Phantom may exist of the same ship at a time)
  - **Ⅲ** at `+9` — PhantomⅢ (索拉里斯+9，精神幻影III)
    Cross attack, deals 320% S-ATK damage. Each skill cast has a 100% chance to create Phantoms (cannot create a Phantom of Solaris) out of 1 random ships of the enemy's starting lineup (Phantoms cannot appear on locations where ships, not summonings, started the battle or on locations where there is a ship). Up to 2 can exist at a time. If there are already 2 active Phantoms, apply a shield that blocks 1 attack (for 1 round) and Forbidding Skill Use (for 2 rounds) to all Phantoms and heal them for 50% of max HP. Also buff all Phantoms to increase their attributes by 8% for 2 rounds, stacking up to 3 times. Lastly, you recover 100 Accumulator. Phantom: Possesses the same skills as the original ship but takes 30% more damage and deals 30% reduced damage. Phantoms gain 70% of the original ship's attributes. All Phantoms vanish if Solaris dies and cannot be revived or rebirthed. (Note: If a Phantom casts a skill with a unique effect that another of your ships can cast, such as Unyielding or Energy Transfer, the effect of the last skill cast prevails.)(Only 1 Phantom may exist of the same ship at a time)
  - **Ⅳ** at `+15` — PhantomIV (索拉里斯+13，精神幻影IV)
    Cross attack, deals 340% S-ATK damage. Each skill cast has a 100% chance to create Phantoms (cannot create a Phantom of Solaris) out of 2 random ships of the enemy's starting lineup (Phantoms cannot appear on locations where ships, not summonings, started the battle or on locations where there is a ship). Up to 2 can exist at a time. If there are already 2 active Phantoms, apply a shield that blocks 1 attack (for 1 round) and Forbidding Skill Use (for 2 rounds) to all Phantoms and heal them for 50% of max HP. Also buff all Phantoms to increase their attributes by 10% for 2 rounds, stacking up to 5 times. Lastly, you recover 100 Accumulator. Phantom: Possesses the same skills as the original ship but takes 30% more damage and deals 20% reduced damage. Phantoms gain 80% of the original ship's attributes. All Phantoms vanish if Solaris dies and cannot be revived or rebirthed. (Note: If a Phantom casts a skill with a unique effect that another of your ships can cast, such as Unyielding or Energy Transfer, the effect of the last skill cast prevails.)(Only 1 Phantom may exist of the same ship at a time)

**Slot 2 — Stellar Form** (id 1541, unlocks at `+2`)
  - **Ⅰ** at `+2` — Stellar FormⅠ (索拉里斯技能2)
    Solaris starts each battle with immunity to Freeze, Lock and Confuse. These last until the end of battle.
  - **Ⅱ** at `+6` — Stellar FormⅡ (索拉里斯技能2)
    Solaris starts each battle with immunity to Freeze, Lock, Confuse and Forbidding Skill Use. These last until the end of battle.
  - **Ⅲ** at `+10` — Stellar FormⅢ (索拉里斯技能2)
    Solaris starts each battle with immunity to Freeze, Lock, Confuse, Forbidding Skill Use, Petrify and Icebound. These last until the end of battle.
  - **Ⅳ** at `+T` — Stellar FormIV (索拉里斯技能2)
    Solaris starts each battle with immunity to Freeze, Lock, Confuse, Forbidding Skill Use, Petrify, Icebound, Entangle and Weaken. These last until the end of battle.

**Slot 3 — Stellar Power** (id 1542, unlocks at `+3`)
  - **Ⅰ** at `+3` — Stellar PowerⅠ (索拉里斯技能3)
    (Takes effect at the start of battle.) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +30% ATK: +30% DEF: +30% S-ATK: +30% S-DEF: +30%
  - **Ⅱ** at `+8` — Stellar PowerⅡ (索拉里斯技能3)
    (Takes effect at the start of battle.) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +60% ATK: +60% DEF: +60% S-ATK: +60% S-DEF: +60%
  - **Ⅲ** at `+11` — Stellar PowerⅢ (索拉里斯技能3)
    (Takes effect at the start of battle.) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +100% ATK: +90% DEF: +90% S-ATK: +90% S-DEF: +90%
  - **Ⅳ** at `+T3` — Stellar PowerIV (索拉里斯技能3)
    (Takes effect at the start of battle.) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +150% ATK: +120% DEF: +120% S-ATK: +120% S-DEF: +120%

**Slot 4 — Phantom Assault** (id 1543, unlocks at `+10`)
  - **Ⅰ** at `+10` — Phantom AssaultⅠ (索拉里斯技能4)
    (Takes effect at the start of battle.) Solaris recovers 40% of max HP whenever a Phantom is destroyed.
  - **Ⅱ** at `+T1` — Phantom AssaultⅡ (索拉里斯技能4)
    (Takes effect at the start of battle.)Solaris recovers 40% of max HP whenever a Phantom is destroyed. When one or more Phantoms are alive, 50% of the damage Solaris takes is instead distributed among his Phantoms.
  - **Ⅲ** at `+T2` — Phantom AssaultⅢ (索拉里斯技能4)
    (Takes effect at the start of battle.) Solaris recovers 40% of max HP whenever a Phantom is destroyed. When one or more Phantoms are alive, 50% of the damage Solaris takes is instead distributed among his Phantoms. Whenever a Phantom is destroyed, the attributes of Phantoms created after this are increased by 15%. This effect stacks. Phantoms can gain up to 120% of the original ship's initial attributes.
  - **Ⅳ** at `+T4` — Phantom AssaultIV (索拉里斯技能4)
    (Takes effect at the start of battle.) Solaris recovers 40% of max HP whenever a Phantom is destroyed. When one or more Phantoms are alive, 50% of the damage Solaris takes is instead distributed among his Phantoms. Whenever a Phantom is destroyed, the attributes of Phantoms created after this are increased by 15%. This effect stacks. Phantoms can gain up to 120% of the original ship's initial attributes. Whenever a Phantom is about to be destroyed (whether destroyed by an enemy or because Solaris dies), (effect does not trigger if a Phantom is instantly killed by an attack that ignores Immunity), they gain Dark Conceal (cannot be targeted) and are cleansed of all crowd-control effects (Freeze, Lock, Confuse, Petrify, Icebound, Entangle, Forbidding Skill Use) and Weaken. They also gain up to 150 Accumulator if they have less than that, and get to act 1 time immediately after the currently unit's action before they are destroyed.

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
- `+T` — 15× Solaris Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Solaris Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Solaris Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Solaris Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Solaris Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Solaris Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 540 · Vivian 薇薇安
**Role** Rover · **Attack** physical · **Generation** latest
**Ratings** Damage 6/10 · Defence 8/10 · Assist 9/10

### Skill panels
**Slot 1 — Tides of Fury** (id 1569, unlocks at `+0`)
  - **Ⅰ** at `+0` — Tides of FuryⅠ (薇薇安技能描述)
    Cross Attack, deals 280% S-ATK damage to targets. Applies Tidal Blessing at the start of battle to the ally with the highest S-ATK and 2 other random allies (up to 3 units can have Tidal Blessing at a time) for 3 rounds. Also heals all allies for 25% of max HP. Lastly, you recover 100 Accumulator. Tidal Blessing: Grants 20 Accumulator when applied, and reduces damage taken by 35%.
  - **Ⅱ** at `+7` — Tides of FuryⅡ (薇薇安技能描述)
    Cross Attack, deals 300% S-ATK damage to targets. Applies Tidal Blessing at the start of battle to the ally with the highest S-ATK and 2 other random allies (up to 3 units can have Tidal Blessing at a time) for 3 rounds. Allies that gain Tidal Blessing also gain Eye of True Sight for 2 rounds. Allies with Tidal Blessing are cleansed of crowd-control effects (Freeze, Lock and Confuse) and stat debuffs (including Weaken; does not affect debuffs caused by legendary equipment). Also heals all allies for 30% of max HP. Lastly, you recover 100 Accumulator. Tidal Blessing: Grants 40 Accumulator, Always Hit and Always Crit when applied, and reduces damage taken by 45%.
  - **Ⅲ** at `+13` — Tides of FuryⅢ (薇薇安技能描述)
    Cross Attack, deals 320% S-ATK damage to targets. Applies Tidal Blessing at the start of battle to the ally with the highest S-ATK and 2 other random allies (up to 3 units can have Tidal Blessing at a time) for 3 rounds. Allies that gain Tidal Blessing also gain Eye of True Sight for 2 rounds. Allies with Tidal Blessing are cleansed of crowd-control effects (Freeze, Lock, Confuse and Forbidding Skill Use) and stat debuffs (including Weaken; does not affect debuffs caused by legendary equipment). Also heals all allies for 35% of max HP. Lastly, you recover 100 Accumulator. Tidal Blessing: Grants 60 Accumulator, Always Hit and Always Crit when applied, and increases Crit ATK by 120% and reduces damage taken by 55%.
  - **Ⅳ** at `+15` — Tides of FuryIV (薇薇安技能描述)
    Cross Attack, deals 360% S-ATK damage to targets. Applies Tidal Blessing at the start of battle to the ally with the highest S-ATK and 2 other random allies (up to 3 units can have Tidal Blessing at a time) for 3 rounds. Enables the ally alive with the most S-ATK at the start of the battle to act an extra time immediately (this effect has an internal cooldown of 1 round and cannot affect Vivian). Allies that gain Tidal Blessing also gain Eye of True Sight for 2 rounds. Allies with Tidal Blessing are cleansed of crowd-control effects (Freeze, Lock, Confuse, Forbidding Skill Use, Petrify, Icebound and Entangle) and stat debuffs (including Weaken; does not affect debuffs caused by legendary equipment). Also heals all allies for 40% of max HP. Lastly, you recover 100 Accumulator. Tidal Blessing: Grants 100 Accumulator, Always Hit and Always Crit when applied, and increases Crit ATK by 150% and reduces damage taken by 65%. The skill's damage increases by 0.5% for each Accumulator above 100 spent during skill cast (up to a maximum of 100%).

**Slot 2 — Tidal Blessing** (id 1570, unlocks at `+3`)
  - **Ⅰ** at `+3` — Tidal BlessingⅠ (薇薇安+9，触发技能)
    Takes effect at the start of battle: Applies Tidal Blessing to the ally with the highest S-ATK and 2 other random allies (up to 3 units can have Tidal Blessing at a time) for 3 rounds.
  - **Ⅱ** at `+9` — Tidal BlessingⅡ (薇薇安+17，触发技能)
    Takes effect at the start of battle: Applies Tidal Blessing to the ally with the highest S-ATK and 2 other random allies (up to 3 units can have Tidal Blessing at a time) for 3 rounds. Vivian is cleansed of crowd-control effects (Freeze, Lock and Confuse) and stat debuffs (including Weaken; does not affect debuffs caused by legendary equipment) each round before acting.
  - **Ⅲ** at `+T1` — Tidal BlessingⅢ (薇薇安+20，触发技能)
    Takes effect at the start of battle: Applies Tidal Blessing to the ally with the highest S-ATK and 2 other random allies (up to 3 units can have Tidal Blessing at a time) for 3 rounds. Vivian is cleansed of crowd-control effects (Freeze, Lock, Confuse and Forbidding Skill Use) and stat debuffs (including Weaken; does not affect debuffs caused by legendary equipment) each round before acting. Vivian has a 60% chance (probability for each target is calculated independently) whenever she casts a skill to apply Rebirth (revives with 100% of initial HP and 100 Accumulator upon death) to herself and units with Tidal Blessing for 2 rounds.
  - **Ⅳ** at `+T4` — Tidal BlessingIV (薇薇安技能描述)
    Takes effect at the start of battle: Applies Tidal Blessing to the ally with the highest S-ATK and 2 other random allies (up to 3 units can have Tidal Blessing at a time) for 3 rounds. Vivian is cleansed of crowd-control effects (Freeze, Lock, Confuse, Forbidding Skill Use, Petrify, Icebound and Entangle) and stat debuffs (including Weaken; does not affect debuffs caused by legendary equipment) each round before acting. Vivian has an 80% chance (probability for each target is calculated independently) whenever she casts a skill to apply Rebirth (revives with 100% of initial HP and 100 Accumulator upon death) to herself and units with Tidal Blessing for 2 rounds. Vivian applies an Extra Effect on the ally with the most S-ATK at the start of the battle with each skill cast. This effect lasts 1 round and makes the ally able to attack again if its skill attack kills an enemy (doesn't stack with similar effects).

**Slot 3 — Tidal Power** (id 1571, unlocks at `+5`)
  - **Ⅰ** at `+5` — Tidal PowerⅠ (立即行动)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +30% DEF: +30% S-DEF: +30% DMG Reduction (Absolute Value): +15%
  - **Ⅱ** at `+11` — Tidal PowerⅡ (薇薇安技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +60% DEF: +50% S-DEF: +50% DMG Reduction (Absolute Value): +20%
  - **Ⅲ** at `+T2` — Tidal PowerⅢ (薇薇安技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +90% DEF: +70% S-DEF: +70% DMG Reduction (Absolute Value): +25%
  - **Ⅳ** at `+T3` — Tidal PowerIV (薇薇安技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +120% DEF: +90% S-DEF: +90% DMG Reduction (Absolute Value): +30%

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
- `+T` — 15× Vivian Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Vivian Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Vivian Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Vivian Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Vivian Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Vivian Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 545 · Balthasar 巴尔萨
**Role** Rover · **Attack** physical · **Generation** latest
**Ratings** Damage 6/10 · Defence 8/10 · Assist 9/10

### Skill panels
**Slot 1 — Oblivion Beam** (id 1599, unlocks at `+0`)
  - **Ⅰ** at `+0` — Oblivion BeamⅠ (巴尔萨+19，复活后混乱)
    Cross Attack, deals 280% S-ATK damage to targets plus True Damage equal to 2% of their max HP for each stack of debuff (Scorch, Gale Corrosion, Plague, Energy Block and Nebula EMP) they are affected by. Reduces all targets' DEF and S-DEF by 40% for 2 rounds. Also reveals all of the enemy's invisible units. Lastly, you recover 100 Accumulator.
  - **Ⅱ** at `+5` — Oblivion BeamⅡ (巴尔萨技能描述，无实际意义)
    Cross Attack, deals 300% S-ATK damage to targets plus True Damage equal to 3% of their max HP for each stack of debuff (Scorch, Gale Corrosion, Plague, Energy Block and Nebula EMP) they are affected by and reduces their Accumulator (not affected by immunity) equal to 5 times their debuff stacks. Reduces all targets' DEF and S-DEF by 50% for 2 rounds. Also reveals all of the enemy's invisible units. Lastly, you recover 100 Accumulator.
  - **Ⅲ** at `+9` — Oblivion BeamⅢ (巴尔萨技能描述，无实际意义)
    Cross Attack, deals 320% S-ATK damage to targets plus True Damage equal to 4% of their max HP for each stack of debuff (Scorch, Gale Corrosion, Plague, Energy Block and Nebula EMP) they are affected by and reduces their Accumulator (not affected by immunity) equal to 7 times their debuff stacks. Reduces all targets' healing recovery and healing effects by 100% and their DEF and S-DEF by 60% for 2 rounds. Also reveals all of the enemy's invisible units. Lastly, you recover 100 Accumulator.
  - **Ⅳ** at `+15` — Oblivion BeamIV (巴尔萨技能描述，无实际意义)
    Cross Attack, deals 360% S-ATK damage to targets plus True Damage equal to 6% of their max HP for each stack of debuff (Scorch, Gale Corrosion, Plague, Energy Block and Nebula EMP) they are affected by and reduces their Accumulator (not affected by immunity) equal to 10 times their debuff stacks. Reduces all targets' healing recovery and healing effects by 100%, their DEF and S-DEF by 70% and all skills they use will cost an extra 50% Accumulator for 2 rounds. Also reveals all of the enemy's invisible units. Lastly, you recover 100 Accumulator.

**Slot 2 — Source of Oblivion** (id 1600, unlocks at `+2`)
  - **Ⅰ** at `+2` — Source of OblivionⅠ (巴尔萨技能描述，无实际意义)
    (Takes effect at the start of battle) When casting a skill, all enemies with either Scorch, Gale Corrosion, Plague, Energy Block or Nebula EMP have their damage dealt reduced by 40% and damage taken increased by 40% for 2 rounds.
  - **Ⅱ** at `+7` — Source of OblivionⅡ (巴尔萨技能描述，无实际意义)
    (Takes effect at the start of battle) When casting a skill, all enemies with either Scorch, Gale Corrosion, Plague, Energy Block or Nebula EMP have their damage dealt reduced by 40% and damage taken increased by 40% for 2 rounds. Casting a skill increases all enemies' Scorch, Gale Corrosion, Energy Block and Nebula EMP debuff stacks by 1 and their Plague debuff stacks by 2.
  - **Ⅲ** at `+11` — Source of OblivionⅢ (巴尔萨技能描述，无实际意义)
    (Takes effect at the start of battle) When casting a skill, all enemies with either Scorch, Gale Corrosion, Plague, Energy Block or Nebula EMP have their damage dealt reduced by 40% and damage taken increased by 40% for 2 rounds. Casting a skill increases all enemies' Scorch, Gale Corrosion, Energy Block and Nebula EMP debuff stacks by 1 and their Plague debuff stacks by 2. Casting a skill immediately activates 1 Scorch and Plague damage over time effect and 1 Scorch Accumulator reduction effect.
  - **Ⅳ** at `+T3` — Source of OblivionIV (巴尔萨技能描述，无实际意义)
    (Takes effect at the start of battle) When casting a skill, all enemies with either Scorch, Gale Corrosion, Plague, Energy Block or Nebula EMP have their damage dealt reduced by 40% and damage taken increased by 40% for 2 rounds. Casting a skill increases all enemies' Scorch, Gale Corrosion, Energy Block and Nebula EMP debuff stacks by 1 and their Plague debuff stacks by 2. Casting a skill immediately activates 1 Scorch and Plague damage over time effect and 1 Scorch Accumulator reduction effect. Any enemy with Plague, Scorch, Gale Corrosion, Energy Block or Nebula EMP becomes affected by Confuse (not affected by immunity) for 1 round when revived.

**Slot 3 — Savage Physique** (id 1601, unlocks at `+3`)
  - **Ⅰ** at `+3` — Savage PhysiqueⅠ (巴尔萨技能描述，无实际意义)
    (Takes effect at the start of battle.) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +30% ATK: +30% DEF: +30% S-ATK: +30% S-DEF: +30%
  - **Ⅱ** at `+7` — Savage PhysiqueⅡ (巴尔萨技能描述，无实际意义)
    (Takes effect at the start of battle.) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +60% ATK: +60% DEF: +60% S-ATK: +60% S-DEF: +60%
  - **Ⅲ** at `+11` — Savage PhysiqueⅢ (巴尔萨技能描述，无实际意义)
    (Takes effect at the start of battle.) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +100% ATK: +90% DEF: +90% S-ATK: +90% S-DEF: +90%
  - **Ⅳ** at `+T` — Savage PhysiqueIV (巴尔萨技能描述，无实际意义)
    (Takes effect at the start of battle.) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +150% ATK: +120% DEF: +120% S-ATK: +120% S-DEF: +120%

**Slot 4 — Ether Simulation** (id 1602, unlocks at `+10`)
  - **Ⅰ** at `+10` — Ether SimulationⅠ (巴尔萨技能描述，无实际意义)
    (Takes effect at the start of battle) Casting a skill increases the damage dealt of all allies by 40% and reduces their damage taken by 40% for 2 rounds.
  - **Ⅱ** at `+T1` — Ether SimulationⅡ (巴尔萨技能描述，无实际意义)
    (Takes effect at the start of battle) Casting a skill increases the damage dealt of all allies by 40% and reduces their damage taken by 40% for 2 rounds. Casting a skill increases the stacks of allies' Domination, Soul Stealer, Seed of Life and Fury buffs by 1.
  - **Ⅲ** at `+T2` — Ether SimulationⅢ (巴尔萨技能描述，无实际意义)
    (Takes effect at the start of battle) Casting a skill increases the damage dealt of all allies by 40% and reduces their damage taken by 40% for 2 rounds. Casting a skill increases the stacks of allies' Domination, Soul Stealer, Seed of Life and Fury buffs by 1. When casting a skill, all allies with the Domination, Soul Stealer, Seed of Life, or Fury buffs have their crowd-control effects (Freeze, Lock, Confuse, Petrify, Icebound, Entangle and Forbidding Skill Use) removed before they act for the next 2 rounds.
  - **Ⅳ** at `+T4` — Ether SimulationIV (巴尔萨技能描述，无实际意义)
    (Takes effect at the start of battle) Casting a skill increases the damage dealt of all allies by 40% and reduces their damage taken by 40% for 2 rounds. Casting a skill increases the stacks of allies' Domination, Soul Stealer, Seed of Life and Fury buffs by 1. When casting a skill, all allies with the Domination, Soul Stealer, Seed of Life or Fury buffs have their crowd-control effects (Freeze, Lock, Confuse, Petrify, Icebound, Entangle and Forbidding Skill Use) removed before they act for the next 2 rounds. When casting a skill, Balthasar copies the skill effect of an ally (can copy: Domination, Windfury Blades, Fury and Warp Energy) in order from row 1 to 3. Units at the front of the formation are copied from first (only 1 skill effect can be copied at a time, and this lasts for 99 rounds or until Balthasar dies; skill must be used again after revival to copy skills.).

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
- `+T` — 15× Balthasar Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Balthasar Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Balthasar Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Balthasar Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Balthasar Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Balthasar Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 550 · Valdi 瓦尔迪
**Role** Rover · **Attack** physical · **Generation** latest
**Ratings** Damage 6/10 · Defence 8/10 · Assist 9/10

### Skill panels
**Slot 1 — Fall of the False Moon** (id 1640, unlocks at `+0`)
  - **Ⅰ** at `+0` — Fall of the False MoonⅠ (瓦尔迪)
    Cross Attack, deals 260% S-ATK damage to targets. Duplicates "False Moon" for 99 rounds, if "False Moon" already exists, its HP is restored to 100%. Lastly, you recover 100 Accumulator. "False Moon": Initially has HP equal to 40% of Valdy's maximum HP. When all allies take attack damage, 40% of the damage received will be transferred to the False Moon. If the shared damage exceeds the current HP of the False Moon, the overflow part of the damage will be borne by Valdy.The False Moon will disappear and become ineffective when its HP reaches 0.
  - **Ⅱ** at `+5` — Fall of the False MoonⅡ (瓦尔迪)
    Cross Attack, deals 280% S-ATK damage to targets. Duplicates "False Moon" for 99 rounds, if "False Moon" already exists, its HP is restored to 100%.Applies 3 stacks of "Lunar Eclipse" to 3 random enemy units, lasting 99 rounds. Lastly, recovers 100 Accumulator. "False Moon": Initially has HP equal to 60% of Valdy's maximum HP. When all allies take attack damage, 45% of the damage received will be transferred to the False Moon. If the shared damage exceeds the current HP of the False Moon, the overflow part of the damage will be borne by Valdy.The False Moon will disappear and become ineffective when its HP reaches 0. "Lunar Eclipse": Maximum of 3 stacks. Each time the affected unit is hit by an S-ATK, one stack is removed and detonated, deducting HP equal to 50% of the sum of Valdy's S-ATK and ATK at the start of the battle.
  - **Ⅲ** at `+9` — Fall of the False MoonⅢ (瓦尔迪)
    Cross Attack, deals 300% S-ATK damage to targets. Duplicates "False Moon" for 99 rounds, if "False Moon" already exists, its HP is restored to 100%.Applies 3 stacks of "Lunar Eclipse" to 3 random enemy units, lasting 99 rounds. Reduces the target's DEF and S-DEF by 75% for 2 rounds. Lastly, recovers 100 Accumulator. "False Moon": Initially has HP equal to 80% of Valdy's maximum HP. When all allies take attack damage, 50% of the damage received will be transferred to the False Moon. If the shared damage exceeds the current HP of the False Moon, the overflow part of the damage will be borne by Valdy.The False Moon will disappear and become ineffective when its HP reaches 0. "Lunar Eclipse": Maximum of 3 stacks. Each time the affected unit is hit by an S-ATK, one stack is removed and detonated, deducting HP equal to 60% of the sum of Valdy's S-ATK and ATK at the start of the battle.
  - **Ⅳ** at `+15` — Fall of the False MoonIV (瓦尔迪)
    Cross Attack, deals 320% S-ATK damage to targets. Duplicates "False Moon" for 99 rounds, if "False Moon" already exists, its HP is restored to 100%.Applies 3 stacks of "Lunar Eclipse" to 3 random enemy units, lasting 99 rounds. Reduces the target's DEF and S-DEF by 75% for 2 rounds. Increases the entire team's ATK and S-ATK by 100% for 2 rounds. Lastly, recovers 100 Accumulator. "False Moon": Initially has HP equal to 100% of Valdy's maximum HP. When all allies take attack damage, 60% of the damage received will be transferred to the False Moon. If the shared damage exceeds the current HP of the False Moon, the overflow part of the damage will be nullified.The False Moon will disappear and become ineffective when its HP reaches 0. "Lunar Eclipse": Maximum of 3 stacks. Each time the affected unit is hit by an S-ATK, one stack is removed and detonated, deducting HP equal to 80% of the sum of Valdy's S-ATK and ATK at the start of the battle.

**Slot 2 — False Moon** (id 1641, unlocks at `+2`)
  - **Ⅰ** at `+2` — False MoonⅠ (瓦尔迪)
    (Effective immediately at the start of the battle) At the start of the battle, duplicate "False Moon", initially having HP equal to 100% of Valdy's maximum HP.
  - **Ⅱ** at `+7` — False MoonⅡ (瓦尔迪)
    (Effective immediately at the start of the battle) At the start of the battle, duplicate "False Moon", initially having HP equal to 100% of Valdy's maximum HP. When the 【False Moon】 is present, all allies' damage dealt is increased by 25%. In PVE battles, it will be further increased by an additional 25%.
  - **Ⅲ** at `+11` — False MoonⅢ (瓦尔迪)
    (Effective immediately at the start of the battle) At the start of the battle, duplicate "False Moon", initially having HP equal to 100% of Valdy's maximum HP. When the 【False Moon】 is present, all allies' damage dealt is increased by 25%. In PVE battles, it will be further increased by an additional 25%. 【False Moon】Damage taken from Starswap is reduced by 50%, and HP is increased to 150% of the maximum HP at the start of the battle with Valdi.
  - **Ⅳ** at `+T4` — False MoonIV (瓦尔迪)
    (Effective immediately at the start of the battle) At the start of the battle, duplicate "False Moon", initially having HP equal to 100% of Valdy's maximum HP. When the 【False Moon】 is present, all allies' damage dealt is increased by 25%. In PVE battles, it will be further increased by an additional 25%. 【False Moon】Damage taken from Starswap is reduced by 50%, and HP is increased to 150% of the maximum HP at the start of the battle with Valdi. When the 【False Moon】 is present, if our units are affected by control effects and attribute debuffs, there is a 50% chance to immediately cleanse these effects and debuffs. (Including: Freeze, Lock, Confusion, Petrification, Frostbite, Entanglement, Skill Casting Prohibition, and Weakening; Attack Reduction, Defense Reduction, Damage Dealt Reduction)

**Slot 3 — Blessing of the Moon** (id 1642, unlocks at `+3`)
  - **Ⅰ** at `+3` — Blessing of the MoonⅠ (瓦尔迪)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +60% ATK: +30% S-ATK: +30% DMG Reduction (Absolute Value): +15%
  - **Ⅱ** at `+8` — Blessing of the MoonⅡ (瓦尔迪)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +90% ATK: +60% S-ATK: +60% DMG Reduction (Absolute Value): +20%
  - **Ⅳ** at `+13` — Blessing of the MoonIV (瓦尔迪)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +150% ATK: +120% S-ATK: +120% DMG Reduction (Absolute Value): +30%
  - **Ⅴ** at `+T` — —
    _(no English description shipped)_

**Slot 4 — Lunar Eclipse** (id 1643, unlocks at `+10`)
  - **Ⅰ** at `+10` — Lunar EclipseⅠ (瓦尔迪)
    (Takes effect at the start of battle) Units under "Lunar Eclipse" will receive 20% increased final damage.
  - **Ⅱ** at `+T1` — Lunar EclipseⅡ (瓦尔迪)
    (Takes effect at the start of battle) Units under "Lunar Eclipse" will receive 20% increased final damage. Detonating "Lunar Eclipse" increases the HP deduction to 120% of the sum of Valdy's ATK and S-ATK at the start of the battle, and in PvE battles, each detonation can cause an additional instance of damage.
  - **Ⅲ** at `+T2` — Lunar EclipseⅢ (瓦尔迪)
    (Takes effect at the start of battle) Units under "Lunar Eclipse" will receive 20% increased final damage. Detonating "Lunar Eclipse" increases the HP deduction to 120% of the sum of Valdy's ATK and S-ATK at the start of the battle, and in PvE battles, each detonation can cause an additional instance of damage. When triggering "Lunar Eclipse", if "False Moon" exists, the damage dealt will restore an equivalent amount of HP for "False Moon".
  - **Ⅳ** at `+T3` — Lunar EclipseIV (瓦尔迪)
    (Takes effect at the start of battle) Units under "Lunar Eclipse" will receive 20% increased final damage. Detonating "Lunar Eclipse" increases the HP deduction to 120% of the sum of Valdy's ATK and S-ATK at the start of the battle, and in PvE battles, each detonation can cause an additional instance of damage. When triggering "Lunar Eclipse", if "False Moon" exists, the damage dealt will restore an equivalent amount of HP for "False Moon". Units under "Lunar Eclipse" need to consume an additional 50% Accumulator when casting skills, the increased Accumulator received will be reduced by 50% (except for effects that increase to xx points if the target's Accumulator is less than xx points), and the S-ATK damage dealt will be reduced by 50%.

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
- `+T` — 15× Valdi's Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Valdi's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Valdi's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Valdi's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Valdi's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Valdi's Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 558 · Liesel 莉洁儿
**Role** Rover · **Attack** physical · **Generation** latest
**Ratings** Damage 6/10 · Defence 8/10 · Assist 9/10

### Skill panels
**Slot 1 — Fear Spread** (id 1689, unlocks at `+0`)
  - **Ⅰ** at `+0` — Fear SpreadⅠ (波妮技能描述)
    Cross Attack, deals 280% S-ATK damage to targets. Reduces the target's ATK and S-ATK by 50% for 2 rounds.There's a 40% chance to apply a Damage Conduction Link to all enemy units (probability calculated individually for each unit). When a linked enemy takes damage from normal attacks and S-ATKs, it deals 20% Conducted Damage to other linked units (true damage, and it's not affected by shields that resist damage), lasting 3 rounds. Lastly, recovers 100 Accumulator.
  - **Ⅱ** at `+7` — Fear SpreadⅡ (波妮技能描述)
    Cross Attack, deals 300% S-ATK damage to the targets. Reduces the target's ATK and S-ATK by 50% for 2 rounds. Decreases the target's S-DEF and DEF by 50% for 2 rounds.There's a 60% chance to apply a Damage Conduction Link to all enemy units (probability calculated individually for each unit). When a linked enemy takes damage from normal attacks and S-ATKs, it deals 25% Conducted Damage to other linked units (true damage, and it's not affected by shields that resist damage), lasting 3 rounds. Lastly, recovers 100 Accumulator.
  - **Ⅲ** at `+13` — Fear SpreadⅢ (波妮技能描述)
    Cross Attack, deals 320% S-ATK damage to targets. Reduces the target's ATK and S-ATK by 50% for 2 rounds. Decreases the target's S-DEF and DEF by 50% for 2 rounds. Grants Eye of True Sight to all allies for 2 rounds.There's a 80% chance to apply a Damage Conduction Link to all enemy units (probability calculated individually for each unit). When a linked enemy takes damage from normal attacks and S-ATKs, it deals 30% Conducted Damage to other linked units (true damage, and it's not affected by shields that resist damage), lasting 3 rounds. Lastly, recovers 100 Accumulator.
  - **Ⅳ** at `+15` — Fear SpreadⅣ (波妮技能描述)
    Cross Attack, deals 340% S-ATK damage to the targets. Reduces the target's ATK and S-ATK by 50% for 2 rounds. Causes the attacked target to consume an additional 50% Accumulator when casting skills, and reduces the skill damage they deal by 30% for 2 rounds.There's a 80% chance to apply a Damage Conduction Link to all enemy units (probability calculated individually for each unit). When a linked enemy takes damage from normal attacks and S-ATKs, it deals 40% Conducted Damage to other linked units (true damage, and it's not affected by shields that resist damage), lasting 3 rounds. Lastly, recovers 100 Accumulator.

**Slot 2 — Death Link** (id 1690, unlocks at `+3`)
  - **Ⅰ** at `+3` — Death LinkⅠ (波妮技能描述)
    (Takes effect at the start of battle) When an enemy with a link is affected by control effects (Freeze, Lock, Confuse, Petrify, Icebound, Entangle, Forbidding Skill Use), there is an 80% chance to inflict the same control effect for 1 round on a random linked enemy.
  - **Ⅱ** at `+9` — Death LinkⅡ (波妮技能描述)
    (Takes effect at the start of battle) When an enemy with a link is affected by control effects (Freeze, Lock, Confuse, Petrify, Icebound, Entangle, Forbidding Skill Use), there is an 80% chance to inflict the same control effect for 1 round on a random linked enemy. Control effects caused by links can ignore the target's immunity and protection status.
  - **Ⅲ** at `+T3` — Death LinkⅢ (波妮技能描述)
    (Takes effect at the start of battle) When an enemy with a link is affected by control effects (Freeze, Lock, Confuse, Petrify, Icebound, Entangle, Forbidding Skill Use), there is an 80% chance to inflict the same control effect for 1 round on a random linked enemy. Control effects caused by links can ignore the target's immunity and protection status. Upon death, instantly kills 2 random enemy units (ignores immunity to instant destruction).
  - **Ⅳ** at `+T4` — Death LinkⅣ (波妮技能描述)
    (Takes effect at the start of battle) When an enemy with a link is affected by control effects (Freeze, Lock, Confuse, Petrify, Icebound, Entangle, Forbidding Skill Use), there is an 80% chance to inflict the same control effect for 1 round on a random linked enemy. Control effects caused by links can ignore the target's immunity and protection status. Upon death, instantly kills 2 random enemy units (ignores immunity to instant destruction). When an enemy with link dies, clears the Accumulator of all enemies with link (ignores immunity and protective statuses).

**Slot 3 — Blessing of the Stars** (id 1691, unlocks at `+5`)
  - **Ⅰ** at `+5` — Blessing of the StarsⅠ (波妮技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +30% DEF: +30% S-DEF: +30% DMG Reduction (Absolute Value): +15%
  - **Ⅱ** at `+11` — Blessing of the StarsⅡ (波妮技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +60% DEF: +50% S-DEF: +50% DMG Reduction (Absolute Value): +20%
  - **Ⅲ** at `+T1` — Blessing of the StarsⅢ (波妮技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +90% DEF: +70% S-DEF: +70% DMG Reduction (Absolute Value): +25%
  - **Ⅳ** at `+T2` — Blessing of the StarsⅣ (波妮技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +120% DEF: +90% S-DEF: +90% DMG Reduction (Absolute Value): +30%

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
- `+T` — 15× Liesel's Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Liesel's Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Liesel's Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Liesel's Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Liesel's Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Liesel's Part · 140× Alien Essence · 140× Transcendence Core

---

## 562 · Ashley 艾希
**Role** Rover · **Attack** physical · **Generation** latest
**Ratings** Damage 6/10 · Defence 8/10 · Assist 9/10

### Skill panels
**Slot 1 — Deep Cold** (id 1709, unlocks at `+0`)
  - **Ⅰ** at `+0` — Deep ColdⅠ (艾希技能描述)
    Cross Attack, deals 280% S-ATK damage to targets. Applies Song of Ice to self for 3 rounds. Lastly, recovers 100 Accumulator. Song of Ice: During its duration, if the target with this buff is about to be affected by control effects (Freeze, Lock, Confuse), Song of Ice is consumed to negate the effect (After the immunity effect is determined, it will be determined to be negated).
  - **Ⅱ** at `+5` — Deep ColdⅡ (艾希技能描述)
    Cross Attack, deals 300% S-ATK damage to targets. Applies Song of Ice to self for 3 rounds. Increases all allies' ATK and S-ATK by 40% for 2 rounds. Lastly, recovers 100 Accumulator. Song of Ice: During its duration, if the target with this buff is about to be affected by control effects (Freeze, Lock, Confuse, Petrify, Icebound, Entangle), Song of Ice is consumed to negate the effect (After the immunity effect is determined, it will be determined to be negated).
  - **Ⅲ** at `+9` — Deep ColdⅢ (艾希技能描述)
    Cross Attack, deals 320% S-ATK damage to targets. Applies Song of Ice to self for 3 rounds. Increases all allies' ATK and S-ATK by 50% for 2 rounds. Increases all allies' DMG Reduction (Absolute Value) by 30% for 2 rounds. Lastly, recovers 100 Accumulator. Song of Ice: During its duration, if the target with this buff is about to be affected by control effects (Freeze, Lock, Confuse, Petrify, Icebound, Entangle, Forbidding Skill Use, Starbind), Song of Ice is consumed to negate the effect (After the immunity effect is determined, it will be determined to be negated).
  - **Ⅳ** at `+15` — Deep ColdⅣ (艾希技能描述)
    Cross Attack, deals 350% S-ATK damage to targets. Applies Song of Ice to self for 3 rounds. Increases all allies' ATK and S-ATK by 70% for 2 rounds. Increases all allies' DMG Reduction (Absolute Value) by 50% for 2 rounds. Adds 30 Accumulator to all allies. Lastly, recovers 100 Accumulator. Song of Ice: During its duration, if the target with this buff is about to be affected by control effects (Freeze, Lock, Confuse, Petrify, Icebound, Entangle, Forbidding Skill Use, Starbind, Binding) and Energy Block, Song of Ice is consumed to negate the effect (After the immunity effect is determined, it will be determined to be negated).

**Slot 2 — Song of Ice** (id 1710, unlocks at `+2`)
  - **Ⅰ** at `+2` — Song of IceⅠ (艾希技能描述)
    (Takes effect at the start of battle) During the duration of Song of Ice, when the target with this buff is about to receive lethal damage, the damage will be negated, Song of Ice is removed, and the target enters Cryosleep (each ship can enter Cryosleep up to 2 times), lasting for 1 round. Cryosleep: Unable to act, immune to instant destruction, takes no attack damage, and converts S-ATK damage into HP equal to 50% of the damage amount. Excess HP that exceeds the target's maximum HP is converted into a shield, with a maximum shield value equal to 100% of the target's maximum HP.
  - **Ⅱ** at `+7` — Song of IceⅡ (艾希技能描述)
    (Takes effect at the start of battle) During the duration of Song of Ice, when the target with this buff is about to receive lethal damage, the damage will be negated, Song of Ice is removed, and the target enters Cryosleep (each ship can enter Cryosleep up to 2 times), lasting for 1 round. Cryosleep: Unable to act, immune to instant destruction, takes no attack damage, and converts S-ATK damage into HP equal to 50% of the damage amount. Excess HP that exceeds the target's maximum HP is converted into a shield, with a maximum shield value equal to 100% of the target's maximum HP. During Cryosleep, unaffected by instant destruction that ignores immunity.
  - **Ⅲ** at `+11` — Song of IceⅢ (艾希技能描述)
    (Takes effect at the start of battle) During the duration of Song of Ice, when the target with this buff is about to receive lethal damage, the damage will be negated, Song of Ice is removed, and the target enters Cryosleep (each ship can enter Cryosleep up to 2 times), lasting for 1 round. Cryosleep: Unable to act, immune to instant destruction, takes no attack damage, and converts S-ATK damage into HP equal to 50% of the damage amount. Excess HP that exceeds the target's maximum HP is converted into a shield, with a maximum shield value equal to 100% of the target's maximum HP. During Cryosleep, unaffected by instant destruction that ignores immunity. After Cryosleep, the damage caused by the first skill cast is increased by 100%.
  - **Ⅳ** at `+T3` — Song of IceⅣ (艾希技能描述)
    (Takes effect at the start of battle) During the duration of Song of Ice, when the target with this buff is about to receive lethal damage, the damage will be negated, Song of Ice is removed, and the target enters Cryosleep (each ship can enter Cryosleep up to 2 times), lasting for 1 round. Cryosleep: Unable to act, immune to instant destruction, takes no attack damage, and converts S-ATK damage into HP equal to 50% of the damage amount. Excess HP that exceeds the target's maximum HP is converted into a shield, with a maximum shield value equal to 100% of the target's maximum HP. During Cryosleep, unaffected by instant destruction that ignores immunity. After Cryosleep, the damage caused by the first skill cast is increased by 100%. After being revived, Ashley resets the number of times Cryosleep can be triggered for all allies.

**Slot 3 — Blessing of Ice** (id 1711, unlocks at `+3`)
  - **Ⅰ** at `+3` — Blessing of IceⅠ (艾希技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +60% DEF: +30% S-DEF: +30% DMG Reduction (Absolute Value): +15%
  - **Ⅱ** at `+8` — Blessing of IceⅡ (艾希技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +90% DEF: +60% S-DEF: +60% DMG Reduction (Absolute Value): +20%
  - **Ⅲ** at `+13` — Blessing of IceⅢ (艾希技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +120% DEF: +90% S-DEF: +90% DMG Reduction (Absolute Value): +25%
  - **Ⅳ** at `+T` — Blessing of IceⅣ (艾希技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +150% DEF: +120% S-DEF: +120% DMG Reduction (Absolute Value): +30%

**Slot 4 — Cryosleep** (id 1712, unlocks at `+10`)
  - **Ⅰ** at `+10` — CryosleepⅠ (艾希技能描述)
    (Takes effect at the start of battle) The targets for Song of Ice are changed to: Applies to 3 random allies, excluding those who already have Song of Ice or are in Cryosleep, for 3 rounds.
  - **Ⅱ** at `+T1` — CryosleepⅡ (艾希技能描述)
    (Takes effect at the start of battle) The targets for Song of Ice are changed to: Applies to 3 random allies, excluding those who already have Song of Ice or are in Cryosleep, for 3 rounds. Ships with Song of Ice ignore 50% of the target's S-DEF and DEF when casting skills.
  - **Ⅲ** at `+T2` — CryosleepⅢ (艾希技能描述)
    (Takes effect at the start of battle) The targets for Song of Ice are changed to: Applies to 3 random allies, excluding those who already have Song of Ice or are in Cryosleep, for 3 rounds. Ships with Song of Ice ignore 50% of the target's S-DEF and DEF when casting skills. At the start of battle, applies Song of Ice to 3 random allies for 3 rounds.
  - **Ⅳ** at `+T4` — CryosleepⅣ (艾希技能描述)
    (Takes effect at the start of battle) The targets for Song of Ice are changed to: Applies to 3 random allies, excluding those who already have Song of Ice or are in Cryosleep, for 3 rounds. Ships with Song of Ice ignore 50% of the target's S-DEF and DEF when casting skills. At the start of battle, applies Song of Ice to 3 random allies for 3 rounds. Ships with Song of Ice have a 45% chance to freeze the target for 2 rounds when casting a skill, ignoring the target's immunity effects, and increasing the damage they take by 30%.

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
- `+T` — 15× Ashley's Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Ashley's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Ashley's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Ashley's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Ashley's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Ashley's Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 570 · Camille 卡洛琳
**Role** Rover · **Attack** physical · **Generation** latest
**Ratings** Damage 6/10 · Defence 8/10 · Assist 9/10

### Skill panels
**Slot 1 — Battle-Hardened** (id 1755, unlocks at `+0`)
  - **Ⅰ** at `+0` — Battle-HardenedⅠ (卡洛琳技能描述)
    Cross Attack, deals 240% S-ATK damage to targets. Casts [Polarity Reversal] for 2 rounds. Lastly, recovers 100 Accumulator. [Polarity Reversal]: Converts excess Damage Reduction, Crit ATK RED, and Block for the Rangers, Strikers, and Destroyers that exceed 200%, into Damage Increase, Crit ATK, and Penetration respectively. Conversion is at a 100% rate, up to a maximum of 80% (absolute value).
  - **Ⅱ** at `+7` — Battle-HardenedⅡ (卡洛琳技能描述)
    Cross Attack, deals 260% S-ATK damage to hit targets. Casts "Polarity Reversal" on all allies, lasting 2 rounds. Camille gains additional skill effects in battle as she casts skills more frequently, lasting until the end of the battle (count resets upon death): gains "Nano Armor" on the first cast. Lastly, recovers 100 Accumulator. [Polarity Reversal]: Converts excess Damage Reduction, Crit ATK RED, and Block for the Rangers, Strikers, and Destroyers that exceed 200%, into Damage Increase, Crit ATK, and Penetration respectively. Conversion is at a 100% rate, up to a maximum of 80% (absolute value). [Nano Armor]: Restores 40% of Max HP to all allies and reduces damage taken by 55% for 2 rounds.
  - **Ⅲ** at `+9` — Battle-HardenedⅢ (卡洛琳技能描述)
    Cross Attack, deals 280% S-ATK damage to hit targets. Casts [Polarity Reversal] on all allies, lasting 2 rounds. Camille gains additional skill effects in battle as she casts skills more often, lasting until the end of the battle (count resets upon death): gains [Nano Armor] on the first cast, and [Energy Shield] on the second cast. Lastly, recovers 100 Accumulator. [Polarity Reversal]: Converts excess Damage Reduction, Crit ATK RED, and Block for the Rangers, Strikers, and Destroyers that exceed 200%, into Damage Increase, Crit ATK, and Penetration respectively. Conversion is at a 100% rate, up to a maximum of 80% (absolute value). [Nano Armor]: Restores 40% of Max HP to all allies and reduces damage taken by 55% for 2 rounds. [Energy Shield]: Grants the Rangers, Strikers, and Destroyers a shield that blocks 1 attack, lasting 2 rounds.
  - **Ⅳ** at `+15` — Battle-HardenedⅣ (卡洛琳技能描述)
    Cross Attack, deals 300% S-ATK damage to hit targets. Casts "Polarity Reversal" on all allies, lasting 2 rounds. Camille gains additional skill effects in battle as she casts skills more times, lasting until the end of the battle (count resets after death): gains "Nano Armor" on the first cast, "Energy Shield" on the second cast, and "Lockdown" on the third cast. Lastly, recovers 100 Accumulator. [Polarity Reversal]: Converts excess Damage Reduction, Crit ATK RED, and Block for the Rangers, Strikers, and Destroyers that exceed 200%, into Damage Increase, Crit ATK, and Penetration respectively. Conversion is at a 100% rate, up to a maximum of 80% (absolute value). [Nano Armor]: Restores 40% of Max HP to all allies and reduces damage taken by 55% for 2 rounds. [Energy Shield]: Grants the Rangers, Strikers, and Destroyers a shield that blocks 1 attack, lasting 2 rounds. 【Lockdown】: Grants a 50% chance for the Protectors, Rovers, and Flagships to lock their targets for 2 rounds when casting skills.

**Slot 2 — Module Enhancement** (id 1756, unlocks at `+3`)
  - **Ⅰ** at `+3` — Module EnhancementⅠ (卡洛琳技能描述)
    (Takes effect at the start of battle) Casting [Polarity Reversal] grants an additional effect: Converts excess Damage Increase, Crit Damage for the Protectors and Rovers that exceed 200%, into Damage Reduction, Crit ATK RED respectively. Conversion is at a 100% rate, up to a maximum of 80% (absolute value).
  - **Ⅱ** at `+11` — Module EnhancementⅡ (卡洛琳技能描述)
    (Takes effect at the start of battle) Casting [Polarity Reversal] grants an additional effect: Converts excess Damage Increase, Crit Damage for the Protectors and Rovers that exceed 200%, into Damage Reduction, Crit ATK RED respectively. Conversion is at a 100% rate, up to a maximum of 80% (absolute value). Upon casting [Energy Shield], additionally grants a Deflection Force Field to our Protectors and Rovers. The field can resist 240% vertical damage dealt by vertical and cross attacks for self and the teammate behind for 2 rounds. The damage to resist is determined by ATK, S-ATK when releasing the skill.
  - **Ⅲ** at `+T3` — Module EnhancementⅢ (卡洛琳技能描述)
    (Takes effect at the start of battle) Casting [Polarity Reversal] grants an additional effect: Converts excess Damage Increase, Crit Damage for the Protectors and Rovers that exceed 200%, into Damage Reduction, Crit ATK RED respectively. Conversion is at a 100% rate, up to a maximum of 80% (absolute value). Upon casting [Energy Shield], additionally grants a Deflection Force Field to our Protectors and Rovers. The field can resist 240% vertical damage dealt by vertical and cross attacks for self and the teammate behind for 2 rounds. The damage to resist is determined by ATK, S-ATK when releasing the skill. Casting [Lockdown] grants an additional effect: ignores the target's immunity effects.
  - **Ⅳ** at `+T4` — Module EnhancementⅣ (卡洛琳技能描述)
    (Takes effect at the start of battle) Casting [Polarity Reversal] grants an additional effect: Converts excess Damage Increase, Crit Damage for the Protectors and Rovers that exceed 200%, into Damage Reduction, Crit ATK RED respectively. Conversion is at a 100% rate, up to a maximum of 80% (absolute value). Upon casting [Energy Shield], additionally grants a Deflection Force Field to our Protectors and Rovers. The field can resist 240% vertical damage dealt by vertical and cross attacks for self and the teammate behind for 2 rounds. The damage to resist is determined by ATK, S-ATK when releasing the skill. Casting [Lockdown] grants an additional effect: ignores the target's immunity effects. When casting a skill, there is a 50% chance to revive all allies with 100% of their initial HP and Accumulator (probability calculated individually for each unit, unaffected by forbidding revival effects).

**Slot 3 — War Enthusiasm** (id 1757, unlocks at `+5`)
  - **Ⅰ** at `+5` — War EnthusiasmⅠ (卡洛琳技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +30% DEF: +30% S-DEF: +30% DMG Reduction (Absolute Value): +15%
  - **Ⅱ** at `+13` — War EnthusiasmⅡ (卡洛琳技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +60% DEF: +50% S-DEF: +50% DMG Reduction (Absolute Value): +20%
  - **Ⅲ** at `+T` — War EnthusiasmⅢ (卡洛琳技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +90% DEF: +70% S-DEF: +70% DMG Reduction (Absolute Value): +25%
  - **Ⅳ** at `+T1` — War EnthusiasmⅣ (卡洛琳技能描述)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +120% DEF: +90% S-DEF: +90% DMG Reduction (Absolute Value): +30%

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
- `+T` — 15× Camille's Ship Part · 40× Inert Alloy · 30× Heated Alloy
- `+T1` — 25× Camille's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Camille's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Camille's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Camille's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Camille's Ship Part · 140× Alien Essence · 140× Transcendence Core

---

## 577 · Mira 米拉
**Role** Rover · **Attack** physical · **Generation** latest
**Ratings** Damage 6/10 · Defence 8/10 · Assist 9/10

### Skill panels
**Slot 1 — Power Field** (id 1795, unlocks at `+0`)
  - **Ⅰ** at `+0` — Power FieldⅠ (米拉+0)
    Cross Attack, deals 280% S-ATK damage to hit targets. Grants all allies an Accumulator Steal buff, which steals 20% of the target's Accumulator when attacking. Increases all allies' damage by 30% for 2 rounds. Recovers 20 Accumulator for all allies, and finally recovers 100 Accumulator for self.
  - **Ⅱ** at `+7` — Power FieldⅡ (米拉+7)
    Cross Attack, deals 300% S-ATK damage to targets. Grants all allies an Accumulator Steal buff, stealing 30% of the target's Accumulator when attacking. All allies gain guaranteed critical hits and deal 30% increased damage for 2 rounds. Recovers 30 Accumulator for all allies, and finally recovers 100 Accumulator for self.
  - **Ⅲ** at `+15` — Power FieldⅢ (米拉+15)
    Cross Attack, deals 320% S-ATK damage to targets. Grants all allies an Accumulator Steal buff, stealing 40% of the target's Accumulator when attacking. All allies gain guaranteed critical hits and deal 35% increased damage, and the ally with the highest S-ATK gains an additional 35% damage boost for 2 rounds. Recovers 40 Accumulator for all allies, and finally recovers 100 Accumulator for self.
  - **Ⅳ** at `+T3` — Power FieldIV (米拉+19)
    Cross Attack, deals 350% S-ATK damage to targets. Grants all allies an Accumulator Steal buff, stealing 50% of the target's Accumulator before attacking. All allies gain guaranteed critical hits and deal 40% increased damage, and the ally with the highest S-ATK gains an additional 40% damage boost and an extra skill effect: deals True Damage equal to 200% of the first attack's S-ATK damage to the enemy with the lowest HP for 2 rounds. Recovers 50 Accumulator for all allies, and finally recovers 100 Accumulator for self.

**Slot 2 — Energy Tide** (id 1796, unlocks at `+3`)
  - **Ⅰ** at `+3` — Energy TideⅠ (米拉)
    (Takes effect at the start of battle) Accumulator Steal effect activates at the start of battle.
  - **Ⅱ** at `+11` — Energy TideⅡ (米拉)
    (Takes effect at the start of battle) Accumulator Steal effect activates at the start of battle. The skill's damage increases by 0.3% for each Accumulator spent above 100 during the ally ship's skill cast. (up to a maximum of 60%).
  - **Ⅲ** at `+T1` — Energy TideⅢ (米拉)
    (Takes effect at the start of battle) Accumulator Steal effect activates at the start of battle. Friendly ships' Accumulator steal is enforced, ignoring any immunity and protection effects. The skill's damage increases by 0.4% for each Accumulator spent above 100 during the ally ship's skill cast. (up to a maximum of 80%).
  - **Ⅳ** at `+T4` — Energy TideIV (米拉)
    (Takes effect at the start of battle) Accumulator Steal effect activates at the start of battle. Friendly ships' Accumulator steal is enforced, ignoring any immunity and protection effects. The skill's damage increases by 0.5% for each Accumulator spent above 100 during the ally ship's skill cast. (up to a maximum of 100%). The friendly ship with the highest S-ATK gains: If the S-ATK doesn't kill an enemy, 1 extra S-ATK is launched as a follow-up attack.

**Slot 3 — Optimization Engine** (id 1797, unlocks at `+5`)
  - **Ⅰ** at `+5` — Optimization EngineⅠ (米拉)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +30% DEF: +30% S-DEF: +30% DMG Reduction (Absolute Value): +15%
  - **Ⅱ** at `+12` — Optimization EngineⅡ (米拉)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +60% DEF: +50% S-DEF: +50% DMG Reduction (Absolute Value): +20%
  - **Ⅲ** at `+T` — Optimization EngineⅢ (米拉)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +90% DEF: +70% S-DEF: +70% DMG Reduction (Absolute Value): +25%
  - **Ⅳ** at `+T2` — Optimization EngineIV (米拉)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +120% DEF: +90% S-DEF: +90% DMG Reduction (Absolute Value): +30%

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
- `+T` — 15× Mira's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Mira's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Mira's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Mira's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Mira's Ship Part · 130× Inert Alloy · 100× Heated Alloy
- `Awaken` — 180× Mira's Ship Part · 130× Inert Alloy · 100× Heated Alloy

---

## 578 · Night Phantom 幽夜
**Role** Rover · **Attack** physical · **Generation** latest
**Ratings** Damage 8/10 · Defence 7/10 · Assist 10/10

### Skill panels
**Slot 1 — Shadow Veil** (id 1799, unlocks at `+0`)
  - **Ⅰ** at `+0` — Shadow VeilⅠ (幽夜+0)
    All attack; deals 250% S-ATK damage to hit targets. Has a 100% chance to applay [Shadow Veil] to 1 random enemy for 2 rounds (will not target ships already affected by this effect). Lastly, recovers 100 Accumulator. [Shadow Veil]: The affected target's final damage is reduced by 20%, and skill attack type changes to single attack (including damage and skill effects. Taunt effect still takes precedence. Except for subsequent damage).
  - **Ⅱ** at `+5` — Shadow VeilⅡ (幽夜+5)
    All attack; deals 260% S-ATK damage to hit targets. Turn all allies invisible for 2 rounds. Has a 100% chance to applay [Shadow Veil] to 1 random enemy for 2 rounds (will not target ships already affected by this effect). Lastly, recovers 100 Accumulator. [Shadow Veil]: The affected target's final damage is reduced by 30%, and skill attack type changes to single attack (including damage and skill effects. Taunt effect still takes precedence. Except for subsequent damage).
  - **Ⅲ** at `+10` — Shadow VeilⅢ (幽夜+10)
    All attack; deals 280% S-ATK damage to hit targets. Turn all allies invisible for 2 rounds. Has a 50% chance to Weaken all enemies (probability for each target calculated separately), deducting 50% of targets' stats for 1 round. Has a 100% chance to applay [Shadow Veil] to 1 random enemy for 2 rounds (will not target ships already affected by this effect). Lastly, recovers 100 Accumulator. [Shadow Veil]: The affected target's final damage is reduced by 40%, and skill attack type changes to single attack (including damage and skill effects. Taunt effect still takes precedence. Except for subsequent damage).
  - **Ⅳ** at `+T` — Shadow VeilIV (幽夜+16)
    All attack; deals 300% S-ATK damage to hit targets. Turn all allies invisible for 2 rounds. Has a 50% chance to Weaken all enemies (probability for each target calculated separately), deducting 50% of targets' stats for 1 round. Has a 100% chance to applay [Shadow Veil] to 1 random enemy for 2 rounds (will not target ships already affected by this effect). When the skill is first used, the ally with the highest ATK that is not in the [Dark Conceal] will gain [Dark Conceal] for 2 rounds (Ships that are not in [Dark Conceal] take priority). Lastly, recovers 100 Accumulator. [Shadow Veil]: The affected target's final damage is reduced by 50%, and skill attack type changes to single attack (including damage and skill effects. Taunt effect still takes precedence. Except for subsequent damage).

**Slot 2 — Shadow Invasion** (id 1800, unlocks at `+3`)
  - **Ⅰ** at `+3` — Shadow InvasionⅠ (幽夜+3)
    (Takes effect at the start of battle) At the start of battle, applies the following effect to all enemies: Upon revival after death, they will gain [Shadow Veil] for 2 rounds.
  - **Ⅱ** at `+9` — Shadow InvasionⅡ (幽夜+9)
    (Takes effect at the start of battle) At the start of battle, applies the following effect to all enemies: Upon revival after death, they will gain [Shadow Veil] for 2 rounds. At the start of battle, the enemy with the highest S-ATK will enter [Shadow Veil] state for 2 rounds.
  - **Ⅲ** at `+T1` — Shadow InvasionⅢ (幽夜+17)
    (Takes effect at the start of battle) At the start of battle, applies the following effect to all enemies: Upon revival after death, they will gain [Shadow Veil] for 2 rounds. At the start of battle, the enemy with the highest S-ATK will enter [Shadow Veil] state for 2 rounds. Ships under [Shadow Veil] have a 50% chance to be instantly killed after taking action.
  - **Ⅳ** at `+T4` — Shadow InvasionIV (幽夜+20)
    (Takes effect at the start of battle) At the start of battle, applies the following effect to all enemies: Upon revival after death, they will gain [Shadow Veil] for 2 rounds. At the start of battle, the enemy with the highest S-ATK (can target enemies in the invisible or Dark Conceal states) will enter [Shadow Veil] state for 2 rounds. Ships under [Shadow Veil] have a 70% chance to be instantly killed after taking action. (Ignores immunity to lethal damage and instant destruction)

**Slot 3 — Abyss Shelter** (id 1802, unlocks at `+4`)
  - **Ⅰ** at `+4` — Abyss ShelterⅠ (幽夜+4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +60% DEF: +30% S-DEF: +30% DMG Reduction (Absolute Value): +15%
  - **Ⅱ** at `+10` — Abyss ShelterⅡ (幽夜+10)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +90% DEF: +60% S-DEF: +60% DMG Reduction (Absolute Value): +20%
  - **Ⅲ** at `+15` — Abyss ShelterⅢ (幽夜+15)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +120% DEF: +90% S-DEF: +90% DMG Reduction (Absolute Value): +25%
  - **Ⅳ** at `+T2` — Abyss ShelterIV (幽夜+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +150% DEF: +120% S-DEF: +120% DMG Reduction (Absolute Value): +30%

**Slot 4 — Mist Amulet** (id 1801, unlocks at `+5`)
  - **Ⅰ** at `+5` — Mist AmuletⅠ (幽夜+5)
    (Takes effect at the start of battle) At the start of battle, all allies gain a shield that blocks 1 attack, lasting 2 rounds.
  - **Ⅱ** at `+11` — Mist AmuletⅡ (幽夜+11)
    (Takes effect at the start of battle) At the start of battle, all allies gain a shield that blocks 1 attack, lasting 2 rounds. Weakening effects applied by self are enforced, ignoring immunity and protection effects.
  - **Ⅲ** at `+T` — Mist AmuletⅢ (幽夜+16)
    (Takes effect at the start of battle) At the start of battle, all allies gain a shield that blocks 1 attack, lasting 2 rounds. Weakening effects applied by self are enforced, ignoring immunity and protection effects. Ships under [Shadow Veil] have their final damage reduced to 70%.
  - **Ⅳ** at `+T3` — Mist AmuletIV (幽夜+19)
    (Takes effect at the start of battle) At the start of battle, all allies gain a shield that blocks 1 attack, lasting 2 rounds. Weakening effects applied by self are enforced, ignoring immunity and protection effects. Ships under [Shadow Veil] have their final damage reduced to 80%. When all allies receive lethal damage from enemies, they survive with at least 1 HP, enter Dark Conceal state for 1 round, and gain a Rebirth effect, recovering immediately upon death with 100% of initial HP and 150 Accumulator. (Can take effect once per battle)

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
- `+T` — 15× Night Phantom's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Night Phantom's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Night Phantom's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Night Phantom's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Night Phantom's Ship Part · 130× Inert Alloy · 100× Heated Alloy
- `Awaken` — 180× Night Phantom's Ship Part · 130× Inert Alloy · 100× Heated Alloy

---

## 585 · Zander 赞德
**Role** Rover · **Attack** physical · **Generation** latest
**Ratings** Damage 8/10 · Defence 7/10 · Assist 10/10

### Skill panels
**Slot 1 — Wind Erosion** (id 1824, unlocks at `+0`)
  - **Ⅰ** at `+0` — Wind ErosionⅠ (赞德+0)
    Cross Attack, deals 320% S-ATK damage to targets. Applies [Wind Erosion] to a random enemy for 99 rounds. Lastly, recovers 100 Accumulator. Wind Erosion: Before the affected target acts, it takes damage equal to 10% of max HP and loses 20 Accumulator. If it is in these abnormal statuses (Lock, Freeze), these statuses will spread to all adjacent targets (if there are no adjacent heroes, the spread cannot occur. The spread effect is same as the original status). Debuffs gained by targets with [Wind Erosion] due to spreading will not spread again.
  - **Ⅱ** at `+6` — Wind ErosionⅡ (赞德+6)
    Cross Attack, deals 340% S-ATK damage to targets. There's a 40% chance to gain Evasion, guaranteeing a dodge against enemy attacks for 1 round. Applies [Wind Erosion] to a random enemy for 99 rounds. Lastly, recovers 100 Accumulator. Wind Erosion: Before the affected target acts, it takes damage equal to 15% of max HP and loses 40 Accumulator. If it is in these abnormal statuses (Lock, Freeze, Confusion), these statuses will spread to all adjacent targets (if there are no adjacent heroes, the spread cannot occur. The spread effect is same as the original status). Debuffs gained by targets with [Wind Erosion] due to spreading will not spread again.
  - **Ⅲ** at `+10` — Wind ErosionⅢ (赞德+10)
    Cross Attack, deals 360% S-ATK damage to targets. There's a 60% chance to gain Evasion, guaranteeing a dodge against enemy attacks for 1 round. Applies [Wind Erosion] to a random enemy for 99 rounds. Lastly, recovers 100 Accumulator. Wind Erosion: Before the affected target acts, it takes damage equal to 20% of max HP and loses 60 Accumulator. If it is in these abnormal statuses (Lock, Freeze, Confusion), these statuses will spread to all adjacent targets (if there are no adjacent heroes, the spread cannot occur. The spread effect is same as the original status). Debuffs gained by targets with [Wind Erosion] due to spreading will not spread again.
  - **Ⅳ** at `+15` — Wind ErosionIV (赞德+15)
    Cross Attack, deals 400% S-ATK damage to targets. Has a 50% chance to disable all enemies' Eye of True Sight and an 80% chance to gain Evasion, guaranteeing a dodge against enemy attacks for 1 round. Applies [Wind Erosion] to a random enemy for 99 rounds. Lastly, recovers 100 Accumulator. Wind Erosion: Before the affected target acts, it takes damage equal to 30% of max HP and loses 100 Accumulator. If it is in these abnormal statuses (Lock, Freeze, Confusion, Entangle), these statuses will spread to all adjacent targets (if there are no adjacent heroes, the spread cannot occur. The spread effect is same as the original status). Debuffs gained by targets with [Wind Erosion] due to spreading will not spread again.

**Slot 2 — Whispering Winds** (id 1825, unlocks at `+2`)
  - **Ⅰ** at `+2` — Whispering WindsⅠ (赞德+2)
    (Takes effect at the start of battle) At the start of battle, all allies gain Evasion, guaranteeing a dodge against enemy attacks for 1 round. (Lower priority than guaranteed hit)
  - **Ⅱ** at `+9` — Whispering WindsⅡ (赞德+9)
    (Takes effect at the start of battle) At the start of battle, all allies gain an evasion effect, guaranteeing a dodge against enemy attacks for 1 round. (Lower priority than guaranteed hit) At the start of battle, all allies gain [Whispering Winds]. [Whispering Winds]: Each time an ally is attacked, there is a 20% chance to gain one of the following effects (probability for each effect is calculated independently, and multiple effects can be triggered.): The attacked ally gains an evasion, guaranteeing a dodge against enemy attacks for 1 round. The attacked ally become invisible for 1 round.
  - **Ⅲ** at `+T` — Whispering WindsⅢ (赞德+16)
    (Takes effect at the start of battle) At the start of battle, all allies gain Evasion, guaranteeing a dodge against enemy attacks for 1 round. (Lower priority than guaranteed hit) At the start of battle, there is a 100% chance to apply [Wind Erosion] to a random enemy for 99 rounds. At the start of battle, all allies gain [Whispering Winds]. [Whispering Winds]: Each time an ally is attacked, there is a 30% chance to gain one of the following effects (probability for each effect is calculated independently, and multiple effects can be triggered.): The attacked ally gains an evasion, guaranteeing a dodge against enemy attacks for 1 round. The attacked ally become invisible for 1 round.
  - **Ⅳ** at `+T4` — Whispering WindsIV (赞德+20)
    (Takes effect at the start of battle) At the start of battle, all allies gain Evasion, guaranteeing a dodge against enemy attacks for 1 round. (Lower priority than guaranteed hit) At the start of battle, there is a 100% chance to apply Wind Erosion to a random enemy, and an additional 50% chance to apply Wind Erosion to a random enemy unit, lasting 99 rounds. At the start of battle, all allies gain [Whispering Winds]. [Whispering Winds]: Each time an ally is attacked, there is a 30% chance to gain one of the following effects (probability for each effect is calculated independently, and multiple effects can be triggered.): The attacked ally gains an evasion, guaranteeing a dodge against enemy attacks for 1 round. The attacked ally become invisible for 1 round. The attacked ally gains [Dark Conceal] for 1 round.

**Slot 3 — Sandstorm Convergence** (id 1826, unlocks at `+4`)
  - **Ⅰ** at `+4` — Sandstorm ConvergenceⅠ (赞德+4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +60% DEF: +30% S-DEF: +30% DMG Reduction (Absolute Value): +15%
  - **Ⅱ** at `+10` — Sandstorm ConvergenceⅡ (赞德+10)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +90% DEF: +60% S-DEF: +60% DMG Reduction (Absolute Value): +20%
  - **Ⅲ** at `+14` — Sandstorm ConvergenceⅢ (赞德+14)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +120% DEF: +90% S-DEF: +90% DMG Reduction (Absolute Value): +25%
  - **Ⅳ** at `+T2` — Sandstorm ConvergenceIV (赞德+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +150% DEF: +120% S-DEF: +120% DMG Reduction (Absolute Value): +30%

**Slot 4 — Sandstorm Wasteland** (id 1827, unlocks at `+3`)
  - **Ⅰ** at `+3` — Sandstorm WastelandⅠ (赞德+3)
    (Takes effect at the start of battle) Sand dances in the air, causing confusion among enemies. When using a skill, all enemies gain 20% Miss, with a chance to make attacks miss (cannot make guaranteed hits miss), lasting for 99 rounds.
  - **Ⅱ** at `+13` — Sandstorm WastelandⅡ (赞德+13)
    (Takes effect at the start of battle) Sand dances in the air, causing confusion among enemies. When using a skill, all enemies gain 25% Miss, with a chance to make attacks miss (cannot make guaranteed hits miss), lasting for 99 rounds. When the targets with [Wind Erosion] are under control effects (Lock, Freeze, Confuse, Entangle), their immunity and protective effects will not activate.
  - **Ⅲ** at `+T1` — Sandstorm WastelandⅢ (赞德+17)
    (Takes effect at the start of battle) Sand dances in the air, causing confusion among enemies. When using a skill, all enemies gain 30% Miss, with a chance to make attacks miss (cannot make guaranteed hits miss), lasting for 99 rounds. When the targets with [Wind Erosion] are under control effects (Lock, Freeze, Confuse, Entangle), their immunity and protective effects will not activate. After the target with [Wind Erosion] uses a skill, the control effects (Lock, Freeze, Confuse, Entangle) applied to its adjacent ships will ignore their immunity and protective effects.
  - **Ⅳ** at `+T3` — Sandstorm WastelandIV (赞德+19)
    (Takes effect at the start of battle) Sand dances in the air, causing confusion among enemies. When using a skill, all enemies gain 50% Miss, with a chance to make attacks miss (cannot make guaranteed hits miss), lasting for 99 rounds. When the targets with [Wind Erosion] are under control effects (Lock, Freeze, Confuse, Entangle), their immunity and protective effects will not activate. After the target with [Wind Erosion] uses a skill, the control effects (Lock, Freeze, Confuse, Entangle) applied to its adjacent ships will ignore their immunity and protective effects. Debuffs that can be spread by [Wind Erosion] increased: Starbound, Binding, Energy Block, Scorch.

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
- `+T` — 15× Zander's Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Zander's Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Zander's Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Zander's Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Zander's Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Zander's Part · 100× Alien Essence · 100× Transcendence Core

---

## 593 · Lorna 洛娜
**Role** Rover · **Attack** physical · **Generation** latest
**Ratings** Damage 6/10 · Defence 8/10 · Assist 9/10

### Skill panels
**Slot 1 — Serene Melody** (id 1853, unlocks at `+0`)
  - **Ⅰ** at `+0` — Serene MelodyⅠ (洛娜+0)
    Cross Attack, deals 280% S-ATK damage to targets. Reduces all of the target's defenses by 50% for 2 rounds. Lastly, you recover 100 Accumulator.
  - **Ⅱ** at `+7` — Serene MelodyⅡ (洛娜+7)
    Cross attack, absorb 60% Accumulator from all female enemies and 40% S-ATK from all male enemies, then deals 300% S-ATK damage to hit targets. Reduces all targets' DEF by 60% for 2 rounds. Lastly, you recover 100 Accumulator.
  - **Ⅲ** at `+15` — Serene MelodyⅢ (洛娜+15)
    Cross Attack, absorb 80% Accumulator from all female enemies and 50% S-ATK from all male enemies, then deals 320% S-ATK damage to hit targets. Reduces all defenses of hit targets by 60% for 2 rounds. Has a 50% chance to gain <span style="color:#FFD700;">Serene Melody</span>. Lastly, you recover 100 Accumulator. <span style="color:#FFD700;">Serene Melody</span>: Grants 150 Accumulator to a random male ally. Purifies abnormal status and control effects from a random female ally.
  - **Ⅳ** at `+T4` — Serene MelodyIV (洛娜+19（被动组合）)
    Cross attack, absorb 100% Accumulator from all female enemies and 60% S-ATK from male enemies, then deals 360% S-ATK damage to hit targets. Reduces all targets' DEF by 75% for 2 rounds. There's a 50% chance to gain [Serene Melody]. Finally, recovers 100 Accumulator. [Serene Melody]: All male allies gain 150 Accumulator and one random male ally gets an immediate action. One random female ally gains [Dark Conceal] for 1 round, making her immune to attacks and skill effects, and purifies all female allies' abnormal statuses and control effects.

**Slot 2 — Harmonious Melody** (id 1854, unlocks at `+3`)
  - **Ⅰ** at `+3` — Harmonious MelodyⅠ (洛娜+3)
    (Takes effect at the start of battle) Increases all allies' S-ATK by 30% until the end of the battle.
  - **Ⅱ** at `+9` — Harmonious MelodyⅡ (洛娜+9)
    (Takes effect at the start of battle) Increases all allies' S-ATK by 40% until the end of the battle. When any male ally uses an S-ATK, all allies' damage dealt is increased by 15% for 2 rounds, stacking up to 3 times. When any female ally uses an S-ATK, all allies' damage taken is reduced by 15% for 2 rounds, stacking up to 3 times.
  - **Ⅲ** at `+T1` — Harmonious MelodyⅢ (洛娜+17)
    (Takes effect at the start of battle) Increases S-ATK of all allies by 60% until the end of the battle. When any male ally uses an S-ATK, all allies' damage dealt increases by 20% for 2 rounds, stacking up to 3 times. When any female ally uses an S-ATK, all allies' damage taken decreases by 20% for 2 rounds, stacking up to 3 times. When any male ally uses an S-ATK, there is a 30% chance to instantly kill a random enemy. When any female ally uses an S-ATK, all enemies' damage taken increases by 30% for 2 rounds.
  - **Ⅳ** at `+T3` — Harmonious MelodyIV (洛娜+19)
    (Takes effect at the start of battle) Increases S-ATK of all allies by 80% until the end of the battle. When any male ally uses an S-ATK, increases damage dealt by all allies by 30% for 2 rounds, stacking up to 3 times. When any female ally uses an S-ATK, reduces damage taken by all allies by 30% for 2 rounds, stacking up to 3 times. When any male ally uses an S-ATK, there is a 30% chance to instantly destroy a random enemy unit (ignores immunity to lethal attacks and instant destruction effects). When any female ally uses an S-ATK, increases damage taken by all enemies by 50% for 2 rounds.

**Slot 3 — Revelation** (id 1855, unlocks at `+5`)
  - **Ⅰ** at `+5` — RevelationⅠ (洛娜+5)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +30% DEF: +30% S-DEF: +30% DMG Reduction (Absolute Value): +15%
  - **Ⅱ** at `+11` — RevelationⅡ (洛娜+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +60% DEF: +50% S-DEF: +50% DMG Reduction (Absolute Value): +20%
  - **Ⅲ** at `+T` — RevelationⅢ (洛娜+16)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +90% DEF: +70% S-DEF: +70% DMG Reduction (Absolute Value): +25%
  - **Ⅳ** at `+T2` — RevelationIV (洛娜+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +120% DEF: +90% S-DEF: +90% DMG Reduction (Absolute Value): +30%

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
- `+T` — 15× Lorna's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Lorna's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Lorna's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Lorna's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Lorna's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Lorna's Ship Part · 100× Alien Essence · 100× Transcendence Core

---

## 596 · Entropy·Zero 熵·零
**Role** Rover · **Attack** physical · **Generation** old
**Ratings** Damage 8/10 · Defence 7/10 · Assist 10/10

### Signature skill
- **Ⅰ** at `+0` — Electromagnetic Impact (熵·零+0)
  Cross Attack, deals 200% S-ATK damage to targets. Lastly, you recover 100 Accumulator.
- **Ⅱ** at `+T4` — Command Distortion (熵·零+20)
  _(no English description shipped)_

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
- `+T` — 15× Entropy·Zero's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Entropy·Zero's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Entropy·Zero's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Entropy·Zero's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Entropy·Zero's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Entropy·Zero's Ship Part · 100× Alien Essence · 100× Transcendence Core

---

## 599 · Caster 卡斯特
**Role** Rover · **Attack** physical · **Generation** latest
**Ratings** Damage 8/10 · Defence 8/10 · Assist 10/10

### Skill panels
**Slot 1 — Abyssal Whisper** (id 1871, unlocks at `+0`)
  - **Ⅰ** at `+0` — Abyssal WhisperⅠ (卡斯特+0)
    All attack; deals 240% S-ATK damage to targets. Has a 55% chance to apply a link damage to all enemies (probability calculated individually for each unit). When an enemy with the link takes normal attacks or skill damage, it will deal 25% link damage to other linked enemies for 2 rounds (True Damage that ignores shields' damage reduction, and damage caused by this effect cannot trigger other link damages). Lastly, recover 100 Accumulator.
  - **Ⅱ** at `+6` — Abyssal WhisperⅡ (卡斯特+2（被动组合）)
    All attack; deals 260% S-ATK damage to targets. Gains Eye of True Sight for 2 rounds. Has a 60% chance to apply a link damage to all enemies (probability calculated individually for each unit). When an enemy with the link takes normal attacks or skill damage, it will deal 30% link damage to other linked enemies for 2 rounds (True Damage that ignores shields' damage reduction, and damage caused by this effect cannot trigger other link damage). Lastly, recover 100 Accumulator.
  - **Ⅲ** at `+10` — Abyssal WhisperⅢ (卡斯特+6)
    All attack; deals 280% S-ATK damage to targets. Gains Eye of True Sight for 2 rounds. Has a 75% chance to apply a link damage to all enemies (probability calculated individually for each unit). When an enemy with the link takes normal attacks or skill damage, it will deal 40% link damage to other linked enemies for 2 rounds (True Damage that ignores shields' damage reduction, and damage caused by this effect cannot trigger other link damage). Has a 100% chance to inflict [Abyssal Fear] on all enemies for 2 rounds. Lastly, recover 100 Accumulator. [Abyssal Fear]: When the affected target using a skill, there is a 50% chance to put self into the Freeze, Lock, Confuse status for 1 round (probability calculated individually for each unit)
  - **Ⅳ** at `+15` — Abyssal WhisperIV (卡斯特+9（被动组合）)
    All attack; deals 300% S-ATK damage to targets. Gains Eye of True Sight for 2 rounds. Has a 80% chance to apply a link damage to all enemies (probability calculated individually for each unit). When an enemy with the link takes normal attacks or skill damage, it will deal 50% link damage to other linked enemies for 2 rounds (True Damage that ignores shields' damage reduction, and damage caused by this effect cannot trigger other link damage). Has a 100% chance to inflict [Abyssal Fear] on all enemies for 2 rounds. Has a 100% chance to apply [Abyssal Whisper] to the enemy with the highest S-ATK, lasting until the end of the battle or this enemy dies. (can target enemies in the invisible or Dark Conceal states, and only one enemy can be affected by this effect at a time.) Lastly, recover 100 Accumulator. [Abyssal Fear]: When the affected target using a skill, there is a 50% chance to put self into the Freeze, Lock, Confuse status for 1 round (probability calculated individually for each unit). [Abyssal Whisper]: When the affected target using a skill, none of this skill's effects will take effect.

**Slot 2 — Terrifying Illusion** (id 1872, unlocks at `+2`)
  - **Ⅰ** at `+2` — Terrifying IllusionⅠ (卡斯特+2)
    (Takes effect at the start of battle) When casting a skill, reduce the target's DEF by 75% for 2 rounds.
  - **Ⅱ** at `+9` — Terrifying IllusionⅡ (卡斯特+9)
    (Takes effect at the start of battle) When casting a skill, reduce the target's DEF by 75% for 2 rounds, and dispel the rebirth effect of linked enemies.
  - **Ⅲ** at `+T` — Terrifying IllusionⅢ (卡斯特+16)
    (Takes effect at the start of battle) When casting a skill, reduce the target's DEF by 75% for 2 rounds, and dispel the rebirth effect of linked enemies. When taking S-ATK damage, if there is an [Abyssal Whisper] enemy, 50% of the damage is shared with that enemy. When the [Abyssal Whisper] enemy dies, cleanse all allies of abnormal statuses and crowd-control effects.
  - **Ⅳ** at `+T4` — Terrifying IllusionIV (卡斯特+20)
    (Takes effect at the start of battle) When casting a skill, reduce the target's DEF by 75% for 2 rounds, and dispel the rebirth effect of linked enemies. When taking S-ATK damage, if there is an [Abyssal Whisper] enemy, 70% of the damage is shared with that enemy. When the [Abyssal Whisper] enemy dies, cleanse all allies of abnormal statuses and crowd-control effects. When casting a skill, additionally gain the active skill effect of the enemy in [Abyssal Whisper]. (If the enemy dies, the gained effect remains until it be applied to another ally. Only one enemy's skill can be gained at a time. Skills obtained from Lieutenants, Potential Chips, or any other sources cannot be gained.)

**Slot 3 — Fear** (id 1873, unlocks at `+4`)
  - **Ⅰ** at `+4` — FearⅠ (卡斯特+4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +60% DEF: +30% S-DEF: +30% DMG Reduction (Absolute Value): +15%
  - **Ⅱ** at `+10` — FearⅡ (卡斯特+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +90% DEF: +60% S-DEF: +60% DMG Reduction (Absolute Value): +20%
  - **Ⅲ** at `+14` — FearⅢ (卡斯特+14)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +120% DEF: +90% S-DEF: +90% DMG Reduction (Absolute Value): +25%
  - **Ⅳ** at `+T2` — FearIV (卡斯特+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +150% DEF: +120% S-DEF: +120% DMG Reduction (Absolute Value): +30%

**Slot 4 — Lost Memories** (id 1874, unlocks at `+3`)
  - **Ⅰ** at `+3` — Lost MemoriesⅠ (卡斯特+3)
    (Takes effect at the start of battle) During battle preparation, different skill effects take effect based on the formation ships' placement. (Takes effect at the start of battle and each time it revives or rebirths). 【Front Row】: Gains a shield that can block 1 attack for 2 rounds. 【Middle Row】: There is 50% chance to gain Evasion, guaranteeing a dodge against enemy attacks for 2 rounds. (Lower priority than guaranteed hit). 【Back Row】: Gains Invisibility, lasting 2 rounds.
  - **Ⅱ** at `+13` — Lost MemoriesⅡ (卡斯特+13)
    (Takes effect at the start of battle) During battle preparation, different skill effects take effect based on the formation ships' placement. (Takes effect at the start of battle and each time it revives or rebirths). 【Front Row】: Gains a shield that can block 1 attack for 2 rounds. 【Middle Row】: There is 50% chance to gain Evasion, guaranteeing a dodge against enemy attacks for 2 rounds. (Lower priority than guaranteed hit). 【Back Row】: Gains Invisibility, lasting 2 rounds. At the start of battle, there is a 100% chance to inflict all enemies with [Abyssal Fear], lasting 2 rounds.
  - **Ⅲ** at `+T1` — Lost MemoriesⅢ (卡斯特+17)
    (Takes effect at the start of battle) During battle preparation, different skill effects take effect based on the formation ships' placement. (Takes effect at the start of battle and each time it revives or rebirths). 【Front Row】: Gains a Directional Shield for 2 rounds, if attacked during its duration, the Directional Shield is removed when the next ship takes action. 【Middle Row】: Gains Evasion, guaranteeing a dodge against enemy attacks for 2 rounds. (Lower priority than guaranteed hit). 【Back Row】: Gains [Dark Conceal] for 2 rounds, making him/her immune to attacks and skill effects, At the start of battle, there is a 100% chance to inflict all enemies with [Abyssal Fear], lasting 2 rounds. Has a 100% chance to apply [Abyssal Whisper] to the enemy with the highest S-ATK (can target enemies in the invisible or Dark Conceal states), lasting until the end of the battle or this enemy dies.
  - **Ⅳ** at `+T3` — Lost MemoriesIV (卡斯特+19)
    (Takes effect at the start of battle) During battle preparation, different skill effects take effect based on the formation ships' placement. (Takes effect at the start of battle and each time it revives or rebirths). 【Front Row】: Gains a Directional Shield for 2 rounds, if attacked during its duration, the Directional Shield is removed when the next ship takes action. 【Middle Row】: Gains Evasion, guaranteeing a dodge against enemy attacks for 2 rounds. (Lower priority than guaranteed hit). 【Back Row】: Gains [Dark Conceal] for 2 rounds, making him/her immune to attacks and skill effects, At the start of battle, there is a 100% chance to inflict all enemies with [Abyssal Fear], lasting 2 rounds. Has a 100% chance to apply [Abyssal Whisper] to the enemy with the highest S-ATK (can target enemies in the invisible or Dark Conceal states), lasting until the end of the battle or this enemy dies. At the start of battle and when casting a skill, if the enemy be applied [Abyssal Whisper], his [Slaughter Feast] and [Fatal Pursuit] are nullified. (If Caster dies, the effect is removed)

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
- `+T` — 15× Eric Valk's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Eric Valk's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Eric Valk's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Eric Valk's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Eric Valk's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Eric Valk's Ship Part · 100× Alien Essence · 100× Transcendence Core

---

## 606 · Narin 奈恩
**Role** Rover · **Attack** physical · **Generation** latest
**Ratings** Damage 6/10 · Defence 8/10 · Assist 9/10

### Skill panels
**Slot 1 — Starcore Pulse** (id 1894, unlocks at `+0`)
  - **Ⅰ** at `+0` — Starcore PulseⅠ (奈恩+0)
    Cross Attack, plunders 50% of the target's S-DEF and 75% of their Accumulator, then deals 280% S-ATK damage to the target. Increases all allies 20 Accumulator, and finally recovers 100 Accumulator.
  - **Ⅱ** at `+7` — Starcore PulseⅡ (奈恩+3(被动))
    Cross Attack, plunders 50% of the target's S-DEF and 75% of their Accumulator, then deals 300% S-ATK damage to the target. All allies gain [Starcore Pulse] for 2 rounds.Increases all allies 30 Accumulator, and finally recovers 100 Accumulator. [Starcore Pulse]: The affected targets gain 20 Accumulator after using a skill.
  - **Ⅲ** at `+15` — Starcore PulseⅢ (奈恩+7)
    Cross Attack, plunders 50% of the target's S-DEF and 75% of their Accumulator, then deals 320% S-ATK damage to the target. Increases all allies' damage by 60% for 2 rounds. All allies gain [Starcore Pulse] for 2 rounds.Increases all allies 50 Accumulator, and finally recovers 100 Accumulator. [Starcore Pulse]: The affected targets gain 30 Accumulator after using a skill.
  - **Ⅳ** at `+T3` — Starcore PulseIV (奈恩+9(被动))
    Cross Attack, plunders 75% of the target's S-DEF and 100% of their Accumulator, then deals 360% S-ATK damage to the target. Has a 40% chance to Lock all enemies (probability for each target is calculated independently) for 2 rounds. Increases all allies' damage by 100% for 2 rounds. All allies gain [Starcore Pulse] for 2 rounds.Increases all allies 100 Accumulator, and finally recovers 100 Accumulator. [Starcore Pulse]: The affected targets gain 50 Accumulator after using a skill.

**Slot 2 — Dataflux Sync** (id 1895, unlocks at `+3`)
  - **Ⅰ** at `+3` — Dataflux SyncⅠ (奈恩+3)
    (Takes effect at the start of battle) Deals S-ATK damage to all controlled enemies and increases damage they take by 30% for 5 rounds.
  - **Ⅱ** at `+9` — Dataflux SyncⅡ (奈恩+9)
    (Takes effect at the start of battle) At the start of battle, all allies gain [Starcore Pulse] for 2 rounds. Deals S-ATK damage to all controlled enemies and increases damage they take by 30% for 5 rounds.
  - **Ⅲ** at `+T1` — Dataflux SyncⅢ (奈恩+17)
    (Takes effect at the start of battle) At the start of battle, all allies gain [Starcore Pulse] for 2 rounds. Deals S-ATK damage to all controlled enemies and increases damage they take by 40% for 5 rounds. The skill's damage increases by 0.3% for each Accumulator point spent above 100 points by allies with [Starcore Pulse] when they cast skills (maximum 60%).
  - **Ⅳ** at `+T4` — Dataflux SyncIV (奈恩+20)
    (Takes effect at the start of battle) At the start of battle, all allies gain [Starcore Pulse] for 2 rounds. Deals S-ATK damage to all controlled enemies and increases damage they take by 60% for 5 rounds. This effect makes the target unable to block damage. The skill's damage increases by 0.4% for every Accumulator point spent above 100 by allies with [Starcore Pulse] when casting skills (maximum: 80%). Allies with [Starcore Pulse] gain an additional 10 Accumulator each time they or their allies gain Accumulator through skill effects. (If multiple sources provide different Accumulator recovery effects, this effect can trigger multiple times. This effect does not apply to the 'gain up to XXX Accumulator if below threshold' effect.)

**Slot 3 — Neural Focus** (id 1896, unlocks at `+5`)
  - **Ⅰ** at `+5` — Neural FocusⅠ (奈恩+5)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +30% DEF: +30% S-DEF: +30% DMG Reduction (Absolute Value): +15%
  - **Ⅱ** at `+11` — Neural FocusⅡ (奈恩+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +60% DEF: +50% S-DEF: +50% DMG Reduction (Absolute Value): +20%
  - **Ⅲ** at `+T` — Neural FocusⅢ (奈恩+16)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +90% DEF: +70% S-DEF: +70% DMG Reduction (Absolute Value): +25%
  - **Ⅳ** at `+T2` — Neural FocusIV (奈恩+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +120% DEF: +90% S-DEF: +90% DMG Reduction (Absolute Value): +30%

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
- `+T` — 15× Narin Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Narin Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Narin Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Narin Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Narin Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Narin Ship Part · 100× Alien Essence · 100× Transcendence Core

---

## 610 · Sirius Gray 西里斯・格雷
**Role** Rover · **Attack** physical · **Generation** latest
**Ratings** Damage 7/10 · Defence 9/10 · Assist 10/10

### Skill panels
**Slot 1 — Whiskey Ember** (id 1909, unlocks at `+0`)
  - **Ⅰ** at `+0` — Whiskey EmberⅠ (西里斯・格雷+0)
    Cross Attack, deals 280% S-ATK damage to targets. Grants all allies [Tipsy Warmth] for 2 rounds; this effect can be triggered again after 1 round. Finally, restores 100 Accumulator. [Tipsy Warmth]: While this effect is active, if the ally is about to be affected by a control effect (Freeze, Lock, Confuse, Petrify, Icebound, Entangle, Forbidding Skill Use), [Tipsy Warmth] will be consumed to block the control effect. (Immunity effects are checked first, then this effect; effects of the same type cannot stack.).
  - **Ⅱ** at `+6` — Whiskey EmberⅠ (西里斯・格雷+3)
    Cross Attack, first removes buffs from all targets, deals 300% S-ATK damage to targets. Grants all allies [Tipsy Warmth] for 2 rounds; this effect can be triggered again after 1 round. Finally, restores 100 Accumulator. [Tipsy Warmth]: While this effect is active, if the ally is about to be affected by a control effect (Freeze, Lock, Confuse, Petrify, Icebound, Entangle, Forbidding Skill Use), [Tipsy Warmth] will be consumed to block the control effect. (Immunity effects are checked first, then this effect; effects of the same type cannot stack.).
  - **Ⅲ** at `+10` — Whiskey EmberⅡ (西里斯・格雷+6)
    Cross Attack, first removes buffs from all targets, deals 320% S-ATK damage to targets. All allies gain 80% DMG Reduction, lasting until the end of battle. Grants all allies [Tipsy Warmth] for 2 rounds; this effect can be triggered again after 1 round. Finally, restores 100 Accumulator. [Tipsy Warmth]: While this effect is active, if the ally is about to be affected by a control effect (Freeze, Lock, Confuse, Petrify, Icebound, Entangle, Forbidding Skill Use), [Tipsy Warmth] will be consumed to block the control effect. (Immunity effects are checked first, then this effect; effects of the same type cannot stack.).
  - **Ⅳ** at `+15` — Whiskey EmberⅡ (西里斯・格雷+9)
    Cross Attack, first removes buffs from all targets, deals 340% S-ATK damage to targets. Increases all allies' ATK and S-ATK by 70% for 2 rounds. All allies gain 80% DMG Reduction, lasting until the end of battle. Grants all allies [Tipsy Warmth] for 2 rounds; this effect can be triggered again after 1 round. Finally, restores 100 Accumulator. [Tipsy Warmth]: While this effect is active, if the ally is about to be affected by a control effect (Freeze, Lock, Confuse, Petrify, Icebound, Entangle, Forbidding Skill Use), [Tipsy Warmth] will be consumed to block the control effect. (Immunity effects are checked first, then this effect; effects of the same type cannot stack.).

**Slot 2 — Tipsy Warmth** (id 1910, unlocks at `+2`)
  - **Ⅰ** at `+2` — Tipsy WarmthⅠ (西里斯・格雷+2)
    (Takes effect at the start of battle) At the start of battle, applies [Tipsy Warmth] to all allies for 2 rounds.
  - **Ⅱ** at `+9` — Tipsy WarmthⅡ (西里斯・格雷+9)
    (Takes effect at the start of battle) At the start of battle, applies [Tipsy Warmth] to all allies for 2 rounds. While [Tipsy Warmth] is active, when allies uses a skill, any Healing Reduction and Healing prevented effects are removed, then restores 40% of their max HP.
  - **Ⅲ** at `+T` — Tipsy WarmthⅢ (西里斯・格雷+16)
    (Takes effect at the start of battle) At the start of battle, applies [Tipsy Warmth] to all allies for 2 rounds. While [Tipsy Warmth] is active, when allies uses a skill, any Healing Reduction and Healing prevented effects are removed, then restores 40% of their max HP. When casting a skill, there is a 50% chance to Confuse on enemies in vertical line for 1 round, and a 50% chance to Weaken attack on enemies in vertical line, deducting 50% of targets' stats for 1 round. (Probability for each target calculated separately.)
  - **Ⅳ** at `+T3` — Tipsy WarmthIV (西里斯・格雷+19)
    (Takes effect at the start of battle) At the start of battle, applies [Tipsy Warmth] to all allies for 2 rounds. While [Tipsy Warmth] is active, when allies uses a skill, any Healing Reduction and Healing prevented effects are removed, then restores 40% of their max HP. When casting a skill, there is a 50% chance to Confuse on target enemies for 1 round, and a 50% chance to Weaken attack on target enemies, deducting 50% of targets' stats for 1 round. (Probability for each target calculated separately.) While [Tipsy Warmth] is active, if the ally is about to be affected lethal damage (ignores immunity to lethal attacks and instant destruction effects), the damage is negated, and the ally gains a shield equal to 100% of their max HP (cannot stack,resets upon repeated skill use), lasting 2 rounds. (Each ally can trigger this effect up to 2 times per battle)

**Slot 3 — Hidden Blade Bartender** (id 1911, unlocks at `+4`)
  - **Ⅰ** at `+4` — Hidden Blade BartenderⅠ (西里斯・格雷+4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +60% DEF: +30% S-DEF: +30% DMG Reduction (Absolute Value): +15%
  - **Ⅱ** at `+10` — Hidden Blade BartenderⅡ (西里斯・格雷+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +90% DEF: +60% S-DEF: +60% DMG Reduction (Absolute Value): +20%
  - **Ⅲ** at `+14` — Hidden Blade BartenderⅢ (西里斯・格雷+14)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +120% DEF: +90% S-DEF: +90% DMG Reduction (Absolute Value): +25%
  - **Ⅳ** at `+T2` — Hidden Blade BartenderIV (西里斯・格雷+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +150% DEF: +120% S-DEF: +120% DMG Reduction (Absolute Value): +30%

**Slot 4 — Blazing Spirits** (id 1912, unlocks at `+3`)
  - **Ⅰ** at `+3` — Blazing SpiritsⅠ (西里斯・格雷+3)
    (Takes effect at the start of battle) When casting a skill, there is a 50% chance to disable all enemies' Eye of True Sight. (Probability for each target calculated separately.)
  - **Ⅱ** at `+13` — Blazing SpiritsⅡ (西里斯・格雷+13)
    (Takes effect at the start of battle) When casting a skill, there is a 50% chance to disable all enemies' Eye of True Sight. (Probability for each target calculated separately.) When casting a skill, all enemies gain 50% Miss, with a chance to make attacks miss, lasting for 99 rounds. (Cannot make guaranteed hits miss.)
  - **Ⅲ** at `+T1` — Blazing SpiritsⅢ (西里斯・格雷+17)
    (Takes effect at the start of battle) When casting a skill, there is a 50% chance to disable all enemies' Eye of True Sight. (Probability for each target calculated separately.) When casting a skill, all enemies gain 50% Miss, with a chance to make attacks miss, lasting for 99 rounds. (Cannot make guaranteed hits miss.) Weaken and Confuse applied by self are forced to take effect, ignoring any immunity and protection effects.
  - **Ⅳ** at `+T4` — Blazing SpiritsIV (西里斯・格雷+20)
    (Takes effect at the start of battle) When casting a skill, there is a 50% chance to disable all enemies' Eye of True Sight. (Probability for each target calculated separately.) When casting a skill, all enemies gain 50% Miss, with a chance to make attacks miss, lasting for 99 rounds. (Cannot make guaranteed hits miss.) Weaken and Confuse applied by self are forced to take effect, ignoring any immunity and protection effects. While [Tipsy Warmth] is active, additional negative effects can be blocked: Energy Block, Magnetic Hyperspace Bomb, and Shadow Veil.

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
- `+T` — 15× Elenia Exclusive Chip · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Elenia Exclusive Chip · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Elenia Exclusive Chip · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Elenia Exclusive Chip · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Elenia Exclusive Chip · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Elenia Exclusive Chip · 100× Alien Essence · 100× Transcendence Core

---

## 616 · Ulysses 尤丽缇丝
**Role** Rover · **Attack** physical · **Generation** latest
**Ratings** Damage 6/10 · Defence 8/10 · Assist 10/10

### Skill panels
**Slot 1 — Ground State Pulse Bomb** (id 1933, unlocks at `+0`)
  - **Ⅰ** at `+0` — Ground State Pulse BombⅠ (尤丽缇丝+0)
    Cross Attack, deals 280% S-ATK damage to targets and applies Sympathetic Resonance to them for 2 rounds. Lastly, recovers 100 Accumulator. [Sympathetic Resonance]: When any ally attacks an enemy with this status, all allies recover 10% of their max HP. (If multiple enemies with this status are hit at the same time, the effect can trigger multiple times.)
  - **Ⅱ** at `+6` — Ground State Pulse BombⅠ (尤丽缇丝+2)
    Cross Attack, deals 300% S-ATK damage and reduces all of the target's defenses by 50% to targets and applies Sympathetic Resonance to them for 2 rounds. Lastly, recovers 100 Accumulator. [Sympathetic Resonance]: When any ally attacks an enemy with this status, all allies recover 10% of their max HP. (If multiple enemies with this status are hit at the same time, the effect can trigger multiple times.)
  - **Ⅲ** at `+10` — Ground State Pulse BombⅠ (尤丽缇丝+6)
    Cross Attack, deals 320% S-ATK damage and reduces all of the target's defenses by 75% to targets and applies Sympathetic Resonance to them for 2 rounds. Lastly, recovers 100 Accumulator. [Sympathetic Resonance]: When any ally attacks an enemy with this status, all allies recover 10% of their max HP and 20 Accumulator. (If multiple enemies with this status are hit at the same time, the effect can trigger multiple times.)
  - **Ⅳ** at `+15` — Ground State Pulse BombⅠ (尤丽缇丝+9)
    Cross Attack, deals 340% S-ATK damage and reduces all of the target's defenses by 75% to targets, and increases the damage dealt of all allies by 60%, and applies Sympathetic Resonance to them for 2 rounds. Lastly, recovers 100 Accumulator. [Sympathetic Resonance]: When any ally attacks an enemy with this status, all allies recover 10% of their max HP and 20 Accumulator. (If multiple enemies with this status are hit at the same time, the effect can trigger multiple times.)

**Slot 2 — Energy Circulation Core** (id 1934, unlocks at `+2`)
  - **Ⅰ** at `+2` — Energy Circulation CoreⅠ (尤丽缇丝+2)
    (Takes effect at the start of battle) At the start of battle, Ulysses enters the [Energy Circulation] state and begins collecting energy. Each time an ally casts a skill or normal attack, 1 energy is collected, up to a maximum of 7. The ally with the highest S-ATK (excluding herself) is granted the [Energy Build] state, lasting until the end of battle or until the ally is defeated. When it is her turn to cast a skill, if the maximum energy has been reached, all energy will be consumed, switching the unit in [Energy Build] state to [Overdrive] state for 1 round, then reverting to [Energy Build] state. (While in [Overdrive] state, the effects provided by [Energy Build] still apply.) [Energy Build]: After casting a skill, additionally restores 50 Accumulator. [Overdrive]: When casting a skill, consumes 20% of max HP (at least 10% HP will be retained), converting it into a shield equal to 300% of the HP consumed (shields can stack, up to a maximum of 500% of starting HP at the beginning of battle).
  - **Ⅱ** at `+9` — Energy Circulation CoreⅡ (尤丽缇丝+9)
    (Takes effect at the start of battle) At the start of battle, Ulysses enters the [Energy Circulation] state and begins collecting energy. Each time an ally casts a skill or normal attack, 1 energy is collected, up to a maximum of 7. The ally with the highest S-ATK (excluding herself) is granted the [Energy Build] state, lasting until the end of battle or until the ally is defeated. When it is her turn to cast a skill, if the maximum energy has been reached, all energy will be consumed, switching the unit in [Energy Build] state to [Overdrive] state for 1 round, then reverting to [Energy Build] state. (While in [Overdrive] state, the effects provided by [Energy Build] still apply.) [Energy Build]: After casting a skill, additionally restores 50 Accumulator. After casting a skill, increases own S-ATK by 10% (stacks up to 10 times), lasting until the end of battle. [Overdrive]: When casting a skill, consumes 20% of max HP (at least 10% HP will be retained), converting it into a shield equal to 300% of the HP consumed (shields can stack, up to a maximum of 500% of starting HP at the beginning of battle). Before taking action, first purifies own control status, then proceeds with the follow-up actions.
  - **Ⅲ** at `+T` — Energy Circulation CoreⅢ (尤丽缇丝+16)
    (Takes effect at the start of battle) At the start of battle, Ulysses enters the [Energy Circulation] state and begins collecting energy. Each time an ally casts a skill or normal attack, 1 energy is collected, up to a maximum of 7. The ally with the highest S-ATK (excluding herself) is granted the [Energy Build] state, lasting until the end of battle or until the ally is defeated. When it is her turn to cast a skill, if the maximum energy has been reached, all energy will be consumed, switching the unit in [Energy Build] state to [Overdrive] state for 1 round, then reverting to [Energy Build] state. (While in [Overdrive] state, the effects provided by [Energy Build] still apply.) [Energy Build]: After casting a skill, additionally restores 50 Accumulator. After casting a skill, increases own S-ATK by 10% (stacks up to 10 times), lasting until the end of battle. [Overdrive]: When casting a skill, consumes 20% of max HP (at least 10% HP will be retained), converting it into a shield equal to 300% of the HP consumed (shields can stack, up to a maximum of 500% of starting HP at the beginning of battle). Before taking action, first purifies own control status, then proceeds with the follow-up actions. For any skill consumed, the skill's damage increases by 0.2% for each Accumulator spent above 100 Accumulator. (up to a maximum of 60%).
  - **Ⅳ** at `+T3` — Energy Circulation CoreIV (尤丽缇丝+19)
    (Takes effect at the start of battle) At the start of battle, Ulysses enters the [Energy Circulation] state and begins collecting energy. Each time an ally casts a skill or normal attack, 1 energy is collected, up to a maximum of 7. The ally with the highest S-ATK (excluding herself) is granted the [Energy Build] state, lasting until the end of battle or until the ally is defeated. When it is her turn to cast a skill, if the maximum energy has been reached, all energy will be consumed, switching the unit in [Energy Build] state to [Overdrive] state for 1 round, then reverting to [Energy Build] state. (While in [Overdrive] state, the effects provided by [Energy Build] still apply.) [Energy Build]: After casting a skill, additionally restores 50 Accumulator. After casting a skill, increases own S-ATK and Crit ATK by 10% (stacks up to 10 times), lasting until the end of battle. [Overdrive]: When casting a skill, consumes 20% of max HP (at least 10% HP will be retained), converting it into a shield equal to 300% of the HP consumed (shields can stack, up to a maximum of 500% of starting HP at the beginning of battle). Before taking action, first purifies own control status, then proceeds with the follow-up actions. For any skill consumed, the skill's damage increases by 0.4% for each Accumulator spent above 100 Accumulator. (up to a maximum of 120%). Finally, deals true damage equal to 200% of the Total S-ATK Damage of the initial hit to the enemy ship with the lowest HP.

**Slot 3 — Circuit Loop** (id 1935, unlocks at `+4`)
  - **Ⅰ** at `+4` — Circuit LoopⅠ (尤丽缇丝+4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +60% DEF: +30% S-DEF: +30% DMG Reduction (Absolute Value): +15%
  - **Ⅱ** at `+10` — Circuit LoopⅡ (尤丽缇丝+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +90% DEF: +60% S-DEF: +60% DMG Reduction (Absolute Value): +20%
  - **Ⅲ** at `+14` — Circuit LoopⅢ (尤丽缇丝+14)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +120% DEF: +90% S-DEF: +90% DMG Reduction (Absolute Value): +25%
  - **Ⅳ** at `+T2` — Circuit LoopIV (尤丽缇丝+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +150% DEF: +120% S-DEF: +120% DMG Reduction (Absolute Value): +30%

**Slot 4 — Supernova・Critical Overdrive** (id 1936, unlocks at `+3`)
  - **Ⅰ** at `+3` — Supernova・Critical OverdriveⅠ (尤丽缇丝+3)
    (Takes effect at the start of battle) At the start of battle, all enemies gain [Sympathetic Resonance] for 2 rounds, and enemies with [Sympathetic Resonance] take 20% more damage.
  - **Ⅱ** at `+13` — Supernova・Critical OverdriveⅡ (尤丽缇丝+13)
    (Takes effect at the start of battle) At the start of battle, all enemies gain [Sympathetic Resonance] for 2 rounds, and enemies with [Sympathetic Resonance] take 30% more damage. The maximum energy required to trigger [Energy Circulation] is reduced to 6 stacks.
  - **Ⅲ** at `+T1` — Supernova・Critical OverdriveⅢ (尤丽缇丝+17)
    (Takes effect at the start of battle) At the start of battle, all enemies gain [Sympathetic Resonance] for 2 rounds, and enemies with [Sympathetic Resonance] take 40% more damage. The maximum energy required to trigger [Energy Circulation] is reduced to 5 stacks. [Energy Build] state gains an additional effect: After casting a skill, there is a 50% chance to return 10% of the Accumulator spent on that skill. (If the ally has the effect "does not consume Accumulator when casting skills", the return still applies.)
  - **Ⅳ** at `+T4` — Supernova・Critical OverdriveIV (尤丽缇丝+20)
    (Takes effect at the start of battle) At the start of battle, all enemies gain [Sympathetic Resonance] for 2 rounds, and enemies with [Sympathetic Resonance] take 40% more damage. The maximum energy required to trigger [Energy Circulation] is reduced to 5 stacks. [Energy Build] state gains an additional effect: After casting a skill, there is a 50% chance to return 10% of the Accumulator spent on that skill. (If the ally has the effect "does not consume Accumulator when casting skills", the return still applies.) [Overdrive] state gains an additional effect: Can act one extra time during its own turn. (Similar effects do not stack.) If there are other members of the Supernova Blades Fleet (Aiolia, Ouros, Mu, Karon, Teda) in the team, they gain the effect provided by [Energy Build] at the start of battle. If the member is Mu, they also gain the effect of [Overdrive] for 2 turns.

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
- `+T` — 15× Elenia Exclusive Chip · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Elenia Exclusive Chip · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Elenia Exclusive Chip · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Elenia Exclusive Chip · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Elenia Exclusive Chip · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Elenia Exclusive Chip · 100× Alien Essence · 100× Transcendence Core

---

## 626 · Dong Xue 冬雪
**Role** Rover · **Attack** physical · **Generation** latest
**Ratings** Damage 8/10 · Defence 7/10 · Assist 10/10

### Skill panels
**Slot 1 — Frostscar Aurora** (id 1968, unlocks at `+0`)
  - **Ⅰ** at `+0` — Frostscar AuroraⅠ (冬雪+0)
    Cross Attack, deals 340% S-ATK damage, reduces the DEF and S-DEF of hit targets by 80% for 2 rounds. Lastly, recovers 100 Accumulator.
  - **Ⅱ** at `+6` — Frostscar AuroraⅡ (冬雪+3)
    Cross Attack, deals 360% S-ATK damage, reduces the DEF and S-DEF of hit targets by 80% for 2 rounds. Has a 50% chance to apply Weakness to the target, reducing all their Attributes by 50% for 2 rounds. Lastly, recovers 100 Accumulator.
  - **Ⅲ** at `+10` — Frostscar AuroraⅢ (冬雪+6)
    Cross Attack, deals 380% S-ATK damage, locks all enemy Rovers and hit targets for 2 rounds. Reduces the DEF and S-DEF of hit targets by 80% for 2 rounds. Has a 50% chance to apply Weakness to the target, reducing all their Attributes by 50% for 2 rounds. Lastly, recovers 100 Accumulator.
  - **Ⅳ** at `+15` — Frostscar AuroraIV (冬雪+10)
    Cross Attack, clears all buffs from the target, plunders 100% of the target's Accumulator, and deals 420% S-ATK damage, locks all enemy Rovers and hit targets for 2 rounds. Reduces the DEF and S-DEF of hit targets by 90% for 2 rounds. Has a 50% chance to apply Weakness to the target, reducing all their Attributes by 50% for 2 rounds. Lastly, recovers 100 Accumulator.

**Slot 2 — Clear Heart** (id 1969, unlocks at `+2`)
  - **Ⅰ** at `+2` — Clear HeartⅠ (冬雪+2)
    (Takes effect at the start of battle) At the start of battle, gain [Clear Heart]. [Clear Heart]: Starts at 0 stack, up to 5 stacks, lasts until the end of battle, and is removed upon death. Gain 1 stack each time she casts a skill. When each ally (including herself) would take lethal damage, if you have [Clear Heart] stacks, consume 1 stack to make them immune to that instance of lethal damage.
  - **Ⅱ** at `+9` — Clear HeartⅡ (冬雪+9)
    (Takes effect at the start of battle) At the start of battle, gain [Clear Heart]. [Clear Heart]: Starts at 0 stack, up to 5 stacks, lasts until the end of battle, and is removed upon death. Gain 2 stacks each time she casts a skill. When each ally (including herself) would take lethal damage, if you have [Clear Heart] stacks, consume 1 stack to make them immune to that instance of lethal damage. When an enemy revives, if you have [Clear Heart] stacks, consume 1 stack to reduce their HP and Accumulator by 50% after revival.
  - **Ⅲ** at `+T` — Clear HeartⅢ (冬雪+16)
    (Takes effect at the start of battle) At the start of battle, gain [Clear Heart]. [Clear Heart]: Starts at 0 stack, up to 5 stacks, lasts until the end of battle, and is removed upon death. Gain 2 stacks each time she casts a skill. When each ally (including herself) would take lethal damage, if you have [Clear Heart] stacks, consume 1 stack to make them immune to that instance of lethal damage. When an enemy revives, if you have [Clear Heart] stacks, consume 1 stack to reduce their HP and Accumulator by 50% after revival. After [Clear Heart] blocks lethal damage, remove all debuffs and control effects from that ally, and restore HP and Accumulator equal to 100% of its Max HP.
  - **Ⅳ** at `+T3` — Clear HeartIV (冬雪+19)
    (Takes effect at the start of battle) At the start of battle, gain [Clear Heart]. [Clear Heart]: Starts at 0 stack, up to 5 stacks, lasts until the end of battle, and is removed upon death. Gain 3 stacks each time she casts a skill. When each ally (including herself) would take lethal damage, if you have [Clear Heart] stacks, consume 1 stack to make them immune to that instance of lethal damage. When an enemy revives, if you have [Clear Heart] stacks, consume 1 stack to reduce their HP and Accumulator by 90% after revival. After [Clear Heart] blocks lethal damage, remove all debuffs and control effects from that ally, and restore HP and Accumulator equal to 100% of its Max HP. Additionally, there is a 50% chance to gain Dark Conceal, making them immune to attacks and skill effects for 1 round.

**Slot 3 — Clear Mirror** (id 1970, unlocks at `+4`)
  - **Ⅰ** at `+4` — Clear MirrorⅠ (冬雪+4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +30% DEF: +30% S-DEF: +30% DMG Reduction (Absolute Value): +15%
  - **Ⅱ** at `+10` — Clear MirrorⅡ (冬雪+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +60% DEF: +50% S-DEF: +50% DMG Reduction (Absolute Value): +20%
  - **Ⅲ** at `+14` — Clear MirrorⅢ (冬雪+14)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +90% DEF: +70% S-DEF: +70% DMG Reduction (Absolute Value): +25%
  - **Ⅳ** at `+T2` — Clear MirrorIV (冬雪+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +120% DEF: +90% S-DEF: +90% DMG Reduction (Absolute Value): +30%

**Slot 4 — Conviction Convergence** (id 1971, unlocks at `+3`)
  - **Ⅰ** at `+3` — Conviction ConvergenceⅠ (冬雪+3)
    (Takes effect at the start of battle) At the start of battle, self gains [Clear Heart] with initial stack increased to 2.
  - **Ⅱ** at `+13` — Conviction ConvergenceⅡ (冬雪+13)
    (Takes effect at the start of battle) At the start of battle, self gains [Clear Heart] with initial stack increased to 2. At the start of battle, grants all allies immune to freezing, locking, confusion, petrification, Icebound, Brittle, entangling, prohibiting the use of skills, weakening, as well as immunity to instant destruction, lasting until the end of battle. (Effect is removed upon death)
  - **Ⅲ** at `+T1` — Conviction ConvergenceⅢ (冬雪+17)
    (Takes effect at the start of battle) At the start of battle, self gains [Clear Heart] with initial stack increased to 2. At the start of battle, grants all allies immune to freezing, locking, confusion, petrification, Icebound, Brittle, entangling, prohibiting the use of skills, weakening, as well as immunity to instant destruction, lasting until the end of battle. (Effect is removed upon death) After any ally uses a skill, the ally that used the skill gains 80% increased damage, stacking up to 3 times, lasting until the end of battle.
  - **Ⅳ** at `+T4` — Conviction ConvergenceIV (冬雪+20)
    (Takes effect at the start of battle) At the start of battle, self gains [Clear Heart] with initial stack increased to 2. At the start of battle, grants all allies immune to freezing, locking, confusion, petrification, Icebound, Brittle, entangling, prohibiting the use of skills, weakening, as well as immunity to instant destruction, lasting until the end of battle. (Effect is removed upon death) After any ally uses a skill, the ally that used the skill gains 80% increased damage, stacking up to 3 times, lasting until the end of battle. When Dong Xue uses a skill, it additionally weakens all enemy Rovers, and her chance to inflict Weakening is increased to 75%, with the reduced attributes increased to 75%.

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
- `+T` — 15× Dong Xue's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Dong Xue's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Dong Xue's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Dong Xue's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Dong Xue's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Dong Xue's Ship Part · 100× Alien Essence · 100× Transcendence Core

---

## 631 · Xelos 赛洛斯
**Role** Rover · **Attack** physical · **Generation** latest
**Ratings** Damage 8/10 · Defence 7/10 · Assist 10/10

### Skill panels
**Slot 1 — Omni-Seal** (id 1984, unlocks at `+0`)
  - **Ⅰ** at `+0` — Omni-SealⅠ (赛洛斯+0)
    Cross Attack, deals 260% S-ATK damage to the target. Increases all allies' Penetration by 200% for 99 rounds. Gains Eye of True Sight for 99 rounds. Lastly, recover 100 Accumulator.
  - **Ⅱ** at `+6` — Omni-SealⅡ (赛洛斯+2)
    Cross Attack, plunders 75% Accumulator from the target, then deals 280% S-ATK damage to the target. Increases all allies' Penetration by 200% for 99 rounds. Gains Eye of True Sight for 99 rounds. Lastly, recover 100 Accumulator.
  - **Ⅲ** at `+10` — Omni-SealⅢ (赛洛斯+6)
    Cross Attack, plunders 75% Accumulator from the target, then deals 300% S-ATK damage to the target. Increases all allies' Penetration and Crit ATK by 200% by 200% for 99 rounds. Gains Eye of True Sight for 99 rounds. Lastly, recover 100 Accumulator.
  - **Ⅳ** at `+15` — Omni-SealIV (赛洛斯+9)
    Cross Attack, plunders 75% Accumulator from the target (ignores immunity), then deals 320% S-ATK damage to the target. Increases all allies' Penetration and Crit ATK by 200% by 200% for 99 rounds. Gains Eye of True Sight for 99 rounds, and has a 100% chance to expose the enemy's invisible ships. Lastly, recover 100 Accumulator.

**Slot 2 — Omni-Counter** (id 1985, unlocks at `+2`)
  - **Ⅰ** at `+2` — Omni-CounterⅠ (赛洛斯+2)
    (Takes effect at the start of battle) At the start of battle, gain [Omni-Counter] until the end of battle. [Omni-Counter]: Starts at 0 stacks, up to a maximum of 3 stacks. Each time you or an enemy casts a skill, gain 1 charge. When reaching 3 charge, if not under control and with sufficient Accumulator, immediately cast an extra All Attack from [Omni-Counter]. This skill has the same effect as [Omni-Seal] and deals 280% S-ATK. (If this skill is not triggered because of control effects or insufficient Accumulator, it will be replaced by this skill on your next action.)
  - **Ⅱ** at `+9` — Omni-CounterⅡ (赛洛斯+9)
    (Takes effect at the start of battle) At the start of battle, gain [Omni-Counter] until the end of battle. [Omni-Counter]: Starts at 0 stacks, up to a maximum of 3 stacks. Each time you or an enemy casts a skill, gain 1 charge. When reaching 3 charge, if not under control and with sufficient Accumulator, immediately cast an extra All Attack from [Omni-Counter]. This skill has the same effect as [Omni-Seal] and deals 300% S-ATK. (If this skill is not triggered because of control effects or insufficient Accumulator, it will be replaced by this skill on your next action.) [Omni-Counter] has a 50% chance to lock all enemies for 2 rounds.
  - **Ⅲ** at `+T` — Omni-CounterⅢ (赛洛斯+16)
    (Takes effect at the start of battle) At the start of battle, gain [Omni-Counter] until the end of battle. [Omni-Counter]: Starts at 0 stacks, up to a maximum of 3 stacks. Each time you or an enemy casts a skill, gain 1 charge. When reaching 3 charge, if not under control and with sufficient Accumulator, immediately cast an extra All Attack from [Omni-Counter]. This skill has the same effect as [Omni-Seal] and deals 320% S-ATK. (If this skill is not triggered because of control effects or insufficient Accumulator, it will be replaced by this skill on your next action.) [Omni-Counter] has a 50% chance to lock all enemies for 2 rounds. While under [Omni-Counter], enemies cannot trigger [Slaughter Feast] and [Fatal Pursuit]. (If Xelos dies, this effect disappears.)
  - **Ⅳ** at `+T3` — Omni-CounterIV (赛洛斯+20)
    (Takes effect at the start of battle) At the start of battle, gain [Omni-Counter] until the end of battle. [Omni-Counter]: Starts at 0 stacks, up to a maximum of 3 stacks. Each time you or an enemy casts a skill, gain 1 charge. When reaching 3 charge, if not under control and with sufficient Accumulator, immediately cast an extra All Attack from [Omni-Counter]. This skill has the same effect as [Omni-Seal] and deals 340% S-ATK. (If this skill is not triggered because of control effects or insufficient Accumulator, it will be replaced by this skill on your next action.) [Omni-Counter] has a 50% chance to lock all enemies for 2 rounds, and a 100% chance to make all enemies lock control effects unable to be purified for 2 rounds. While under [Omni-Counter], when enemies are about to trigger [Slaughter Feast] and [Fatal Pursuit], they cannot take effect. If Xelos is not unable to act, immediately release [Omni-Counter], and this skill has an additional 100% chance to lock for 1 round. (If the enemy is untargetable, the Lock effect does not apply. If Xelos dies, this effect disappears.)

**Slot 3 — Starbrain Boost** (id 1986, unlocks at `+4`)
  - **Ⅰ** at `+4` — Starbrain BoostⅠ (赛洛斯+4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +60% DEF: +30% S-DEF: +30% DMG Reduction (Absolute Value): +15%
  - **Ⅱ** at `+10` — Starbrain BoostⅡ (赛洛斯+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +90% DEF: +60% S-DEF: +60% DMG Reduction (Absolute Value): +20%
  - **Ⅲ** at `+14` — Starbrain BoostⅢ (赛洛斯+14)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +120% DEF: +90% S-DEF: +90% DMG Reduction (Absolute Value): +25%
  - **Ⅳ** at `+T2` — Starbrain BoostIV (赛洛斯+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): HP: +150% DEF: +120% S-DEF: +120% DMG Reduction (Absolute Value): +30%

**Slot 4 — Nano Fade** (id 1987, unlocks at `+3`)
  - **Ⅰ** at `+3` — Nano FadeⅠ (赛洛斯+3)
    (Takes effect at the start of battle) At the start of battle, self gains 2 rounds of invisibility.
  - **Ⅱ** at `+13` — Nano FadeⅡ (赛洛斯+13)
    (Takes effect at the start of battle) At the start of battle, self gains 2 rounds of invisibility. When an ally deals S-ATK damage, they heal themselves for 40% of the damage dealt.
  - **Ⅲ** at `+T1` — Nano FadeⅢ (赛洛斯+17)
    (Takes effect at the start of battle) At the start of battle, self gains 2 rounds of invisibility. When an ally deals S-ATK damage, they heal themselves for 40% of the damage dealt. Lock effects applied by self are forced to take effect, ignoring any immunity and protection effects.
  - **Ⅳ** at `+T4` — Nano FadeIV (赛洛斯+19)
    (Takes effect at the start of battle) At the start of battle, self gains 2 rounds of invisibility. When an ally deals S-ATK damage, they heal themselves for 40% of the damage dealt. Lock effects applied by self are forced to take effect, ignoring any immunity and protection effects. When casting [Omni-Counter], instantly destroy enemies with less than 50% HP (ignores immunity to lethal attacks and instant destruction effects).

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
- `+T` — 15× Xelos's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Xelos's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Xelos's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Xelos's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Xelos's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Xelos's Ship Part · 100× Alien Essence · 100× Transcendence Core

---

## 642 · Flakvod 弗拉克沃德
**Role** Rover · **Attack** physical · **Generation** latest
**Ratings** Damage 7/10 · Defence 8/10 · Assist 10/10

### Skill panels
**Slot 1 — Shard Shock** (id 2028, unlocks at `+0`)
  - **Ⅰ** at `+0` — Shard ShockⅠ (弗拉克沃德+0)
    All Attack, first plunders 50% Accumulator from targets, then deals 300% S-ATK damage to targets. Lastly, recovers 100 Accumulator.
  - **Ⅱ** at `+6` — Shard ShockⅡ (弗拉克沃德+6)
    All Attack, first plunders 50% Accumulator from targets, then deals 320% S-ATK damage to targets. Gains Eye of True Sight until the end of the battle. Lastly, recovers 100 Accumulator.
  - **Ⅲ** at `+10` — Shard ShockⅢ (弗拉克沃德+10)
    All Attack, first plunders 50% Accumulator from targets, then deals 350% S-ATK damage to targets. Gains Eye of True Sight until the end of the battle. Grants all allies turn invisible for 2 rounds. Lastly, recovers 100 Accumulator.
  - **Ⅳ** at `+15` — Shard ShockIV (弗拉克沃德+15)
    All Attack, first plunders 50% Accumulator from targets, then deals 400% S-ATK damage to targets. Gains Eye of True Sight until the end of the battle. Grants all allies turn invisible for 2 rounds. Has a 50% chance to inflict Weaken on all Enemies (Probability for each target calculated separately), reducing all Attributes by 50% for 1 round. Lastly, recovers 100 Accumulator.

**Slot 2 — Corrosion Pulse** (id 2029, unlocks at `+2`)
  - **Ⅰ** at `+2` — Corrosion PulseⅠ (弗拉克沃德+2)
    (Takes effect at the start of battle) When own dies, the Enemy with the highest S-ATK gains [Corrosion Pulse] (including units in Invisible and Dark Conceal states; if the unit cannot be targeted, a random enemy will be selected). [Corrosion Pulse]: The affected target’s final damage is reduced by 75%. After casting a skill, there is a 50% chance to become confused for 2 rounds.
  - **Ⅱ** at `+9` — Corrosion PulseⅡ (弗拉克沃德+9)
    (Takes effect at the start of battle) When own dies, the Enemy with the highest S-ATK gains [Corrosion Pulse] (including units in Invisible and Dark Conceal states; if the unit cannot be targeted, a random enemy will be selected). [Corrosion Pulse]: The affected target’s final damage is reduced by 75%. After casting a skill, there is a 50% chance to become confused for 2 rounds. If self has already died, when the [Corrosion Pulse] unit casts a skill, there is a 50% chance to revive self and restore 100% HP and 150 Accumulator to initial state (unaffected by forbidding revival effects).
  - **Ⅲ** at `+T` — Corrosion PulseⅢ (弗拉克沃德+16)
    (Takes effect at the start of battle) When own dies, the Enemy with the highest S-ATK gains [Corrosion Pulse] (including units in Invisible and Dark Conceal states; if the unit cannot be targeted, a random enemy will be selected). [Corrosion Pulse]: The affected target’s final damage is reduced by 75%. After casting a skill, there is a 50% chance to become confused for 2 rounds. If self has already died, when the [Corrosion Pulse] unit casts a skill, there is a 50% chance to revive self and restore 100% HP and 150 Accumulator to initial state (unaffected by forbidding revival effects). When casting a skill, removes Eye of True Sight from all Enemies.
  - **Ⅳ** at `+T4` — Corrosion PulseIV (弗拉克沃德+20)
    (Takes effect at the start of battle) When own dies, the Enemy with the highest S-ATK gains [Corrosion Pulse] (including units in Invisible and Dark Conceal states; if the unit cannot be targeted, a random enemy will be selected). [Corrosion Pulse]: The affected target’s final damage is reduced by 75%. After casting a skill, there is a 50% chance to become confused for 2 rounds. If self has already died, when the [Corrosion Pulse] unit casts a skill, there is a 100% chance to revive self and restore 100% HP and 150 Accumulator to initial state (unaffected by forbidding revival effects). When casting a skill, removes Eye of True Sight from all Enemies. The first skill cast at the start of battle makes all Enemies unable to target units in [Dark Conceal] for 2 rounds.

**Slot 3 — Circuit Charge** (id 2030, unlocks at `+4`)
  - **Ⅰ** at `+4` — Circuit ChargeⅠ (弗拉克沃德+4)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +60% ATK: +60% Crit ATK (Absolute Value): +30% DMG Bonus (Absolute Value): +15%
  - **Ⅱ** at `+10` — Circuit ChargeⅡ (弗拉克沃德+11)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +90% ATK: +90% Crit ATK (Absolute Value): +40% DMG Bonus (Absolute Value): +20%
  - **Ⅲ** at `+14` — Circuit ChargeⅢ (弗拉克沃德+14)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +120% ATK: +120% Crit ATK (Absolute Value): +50% DMG Bonus (Absolute Value): +25%
  - **Ⅳ** at `+T2` — Circuit ChargeIV (弗拉克沃德+18)
    (Takes effect at the start of battle) Basic Stats Boost (not counting Galactonite, Equipment or Medals): S-ATK: +150% ATK: +150% Crit ATK (Absolute Value): +60% DMG Bonus (Absolute Value): +30%

**Slot 4 — Insulation Surface** (id 2031, unlocks at `+3`)
  - **Ⅰ** at `+3` — Insulation SurfaceⅠ (弗拉克沃德+3)
    (Takes effect at the start of battle) The first time you take damage at the start of battle, the damage will not exceed 50% of your max HP; the excess damage is negated. This effect is removed after taking damage once.
  - **Ⅱ** at `+13` — Insulation SurfaceⅡ (弗拉克沃德+13)
    (Takes effect at the start of battle) The first time you take damage at the start of battle, the damage will not exceed 50% of your max HP; the excess damage is negated. This effect is removed after taking damage once. Upon death, deals true damage equal to 50% of your max HP, distributed among all Enemies.
  - **Ⅲ** at `+T1` — Insulation SurfaceⅢ (弗拉克沃德+17)
    (Takes effect at the start of battle) The first time you take damage at the start of battle, the damage will not exceed 50% of your max HP; the excess damage is negated. This effect is removed after taking damage once. Upon death, deals true damage equal to 50% of your max HP, distributed among all Enemies. If own revive after dying in battle, there is a 50% chance to act immediately.
  - **Ⅳ** at `+T3` — Insulation SurfaceIV (弗拉克沃德+19)
    (Takes effect at the start of battle) The first time you take damage at the start of battle, the damage will not exceed 50% of your max HP; the excess damage is negated. This effect is removed after taking damage once. Upon death, deals true damage equal to 50% of your max HP, distributed among all Enemies. If own revive after dying in battle, there is a 50% chance to act immediately. When first taking damage at the start of battle, immediately inflict [Corrosion Pulse] on the enemy that acted last (if the unit cannot be targeted, a random enemy will be chosen), and removes forbidding revival effects and revive limit effects from all allies. (Effect count resets upon revival after death.)

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
- `+T` — 15× Flakvod's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T1` — 25× Flakvod's Ship Part · 55× Inert Alloy · 40× Heated Alloy
- `+T2` — 35× Flakvod's Ship Part · 75× Inert Alloy · 55× Heated Alloy
- `+T3` — 45× Flakvod's Ship Part · 100× Inert Alloy · 75× Heated Alloy
- `+T4` — 120× Flakvod's Ship Part · 100× Alien Essence · 100× Transcendence Core
- `Awaken` — 180× Flakvod's Ship Part · 100× Alien Essence · 100× Transcendence Core

---
