# Evidencia de selección de configuración de Chunking

## 1. Medición del corpus

**Corpus:** LoL Knowledge & Patch Assistant

**Documentos:** 5

- `champion_abilities_26.19.md`: **294427 palabras**
- `champion_stats_26.19.md`: **17988 palabras**
- `game_mechanics.md`: **2552 palabras**
- `items_26.19.md`: **19810 palabras**
- `patch_notes.md`: **894 palabras**

**TOTAL:** 335671 palabras

## 2. Comparación inicial de configuraciones

### Configuración 200/40

- Chunks totales: **2099**
- Promedio de palabras por chunk: **199.82**

- `champion_abilities_26.19.md`: 1840 chunks | último chunk: 187 palabras
- `champion_stats_26.19.md`: 113 chunks | último chunk: 68 palabras
- `game_mechanics.md`: 16 chunks | último chunk: 152 palabras
- `items_26.19.md`: 124 chunks | último chunk: 130 palabras
- `patch_notes.md`: 6 chunks | último chunk: 94 palabras

### Configuración 300/60

- Chunks totales: **1400**
- Promedio de palabras por chunk: **299.55**

- `champion_abilities_26.19.md`: 1227 chunks | último chunk: 187 palabras
- `champion_stats_26.19.md`: 75 chunks | último chunk: 228 palabras
- `game_mechanics.md`: 11 chunks | último chunk: 152 palabras
- `items_26.19.md`: 83 chunks | último chunk: 130 palabras
- `patch_notes.md`: 4 chunks | último chunk: 174 palabras

### Configuración 400/80

- Chunks totales: **1049**
- Promedio de palabras por chunk: **399.61**

- `champion_abilities_26.19.md`: 920 chunks | último chunk: 347 palabras
- `champion_stats_26.19.md`: 56 chunks | último chunk: 388 palabras
- `game_mechanics.md`: 8 chunks | último chunk: 312 palabras
- `items_26.19.md`: 62 chunks | último chunk: 290 palabras
- `patch_notes.md`: 3 chunks | último chunk: 254 palabras

## 3. Prueba cualitativa — Q de Annie

Texto utilizado para localizar el contenido: `### Q — Disintegrate`

### Configuración 200/40

### Chunk 82

- Source: `champion_abilities_26.19.md`
- Index: `82`
- Palabras: `200`

```text
any form of cast-inhibiting crowd control. **Cost:** 60 OTHER **Cooldown:** 4 / 3 / 2 seconds **Technical data:** Targeting: Location / Auto | Damage type: MAGIC_DAMAGE | Cast time: none | Target range: 750 **Notes:** Toggled abilities do not count as ability activations for the purposes of on-cast effects such as Spellblade and triggering Force Pulse's passive. Glacial Storm's slow leaves a trail that is visible even if the target is stealthed. Glacial Storm deals 3 half ticks at 200 / 267 / 333 radius for a total of 1.5 normal damage ticks before it starts dealing empowered damage at 400 radius. Stasis via Zhonya's Hourglass doesn't interrupt Glacial Storm. Tahm Kench's Devour does interrupt (allied and enemy) Glacial Storm. --- ## Annie ### P — Pyromania **Champion:** Annie **Champion ID:** 1 **Ability Slot:** P **Ability Name:** Pyromania **Effect 1:** Innate - Pyromania: Annie generates a stack of Pyromania whenever she hits an enemy with Disintegrate or casts her other abilities, stacking up to 4 times, at which she gains Energized. **Effect 2:** Energized: Annie empowers her next cast of Disintegrate, Incinerate, or Summon: Tibbers to consume all Pyromania stacks to stun enemies hit for 1.25 / 1.5 / 1.75
```

### Chunk 83 **← ENCONTRADO**

- Source: `champion_abilities_26.19.md`
- Index: `83`
- Palabras: `200`

```text
abilities, stacking up to 4 times, at which she gains Energized. **Effect 2:** Energized: Annie empowers her next cast of Disintegrate, Incinerate, or Summon: Tibbers to consume all Pyromania stacks to stun enemies hit for 1.25 / 1.5 / 1.75 (based on level) seconds. **Effect 3:** Annie gains maximum stacks of Pyromania when the game starts and upon respawning. She will lose Energized and all Pyromania stacks upon death. **Technical data:** Targeting: Passive **Notes:** Annie does not lose any stacks upon entering or exiting resurrection. Stacks are gained even if the ability is blocked by spell shield. Pyromania's current stacks are represented by a counter under Annie's health bar, visible to all players. It lights up when the empowered effect is available. ### Q — Disintegrate **Champion:** Annie **Champion ID:** 1 **Ability Slot:** Q **Ability Name:** Disintegrate **Effect 1:** Active: Annie hurls a fireball at the target enemy that deals magic damage. **Scaling:** - **Magic Damage:** 80 / 125 / 170 / 215 / 260 + 80% AP **Effect 2:** If this kills the target, Disintegrate's cooldown is reduced by 50% and its mana cost is refunded. **Cost:** 60 / 65 / 70 / 75 / 80 MANA **Cooldown:** 4
```

### Chunk 84

- Source: `champion_abilities_26.19.md`
- Index: `84`
- Palabras: `200`

```text
170 / 215 / 260 + 80% AP **Effect 2:** If this kills the target, Disintegrate's cooldown is reduced by 50% and its mana cost is refunded. **Cost:** 60 / 65 / 70 / 75 / 80 MANA **Cooldown:** 4 seconds **Technical data:** Targeting: Unit | Damage type: MAGIC_DAMAGE | Cast time: 0.25 | Target range: 625 **Notes:** Disintegrate will also grant the cooldown reduction and mana cost refund if the target is dead upon the missile's arrival. If the target becomes untargetable, dies, or is too far away or no longer in sight during the cast time, this ability will cancel but does not go on cooldown nor pay its cost (if applicable). ### W — Incinerate **Champion:** Annie **Champion ID:** 1 **Ability Slot:** W **Ability Name:** Incinerate **Effect 1:** Active: Annie releases fire in a cone in the target direction, dealing magic damage to enemies hit. **Scaling:** - **Magic Damage:** 70 / 110 / 150 / 190 / 230 + 80% AP **Cost:** 70 / 75 / 80 / 85 / 90 MANA **Cooldown:** 7 seconds **Technical data:** Targeting: Direction | Damage type: MAGIC_DAMAGE | Cast time: 0.25 **Notes:** Incinerate can hit targets behind Annie, provided their radius
```

### Configuración 300/60

### Chunk 54

- Source: `champion_abilities_26.19.md`
- Index: `54`
- Palabras: `300`

```text
rain of ice and hail at the target location, dealing magic damage every 0.5 seconds to enemies within and slowing them for 1 second, refreshing every 0.5 seconds while they remain inside. **Scaling:** - **Magic Damage per Tick:** 15 / 22.5 / 30 + 6.25% AP - **Slow:** 20% / 30% / 40% **Effect 3:** The blizzard increases in size over 1.5 seconds. At maximum size, Glacial Storm is empowered to deal 300% damage and increase the effectiveness of its slow by 50%, which also instead lasts 1.5 seconds and refreshes every 0.25 seconds. **Scaling:** - **Empowered Damage per Tick:** 45 / 67.5 / 90 + 18.75% AP - **Empowered Slow:** 30% / 45% / 60% **Effect 4:** Toggling Glacial Storm off triggers a final tick of damage and incurs its full cooldown. Glacial Storm is toggled off automatically if Anivia moves too far away from the blizzard or becomes unable to pay the mana cost, or is affected by any form of cast-inhibiting crowd control. **Cost:** 60 OTHER **Cooldown:** 4 / 3 / 2 seconds **Technical data:** Targeting: Location / Auto | Damage type: MAGIC_DAMAGE | Cast time: none | Target range: 750 **Notes:** Toggled abilities do not count as ability activations for the purposes of on-cast effects such as Spellblade and triggering Force Pulse's passive. Glacial Storm's slow leaves a trail that is visible even if the target is stealthed. Glacial Storm deals 3 half ticks at 200 / 267 / 333 radius for a total of 1.5 normal damage ticks before it starts dealing empowered damage at 400 radius. Stasis via Zhonya's Hourglass doesn't interrupt Glacial Storm. Tahm Kench's Devour does interrupt (allied and enemy) Glacial Storm. --- ## Annie ### P — Pyromania **Champion:** Annie **Champion ID:** 1 **Ability Slot:** P **Ability Name:** Pyromania **Effect 1:**
```

### Chunk 55 **← ENCONTRADO**

- Source: `champion_abilities_26.19.md`
- Index: `55`
- Palabras: `300`

```text
/ 267 / 333 radius for a total of 1.5 normal damage ticks before it starts dealing empowered damage at 400 radius. Stasis via Zhonya's Hourglass doesn't interrupt Glacial Storm. Tahm Kench's Devour does interrupt (allied and enemy) Glacial Storm. --- ## Annie ### P — Pyromania **Champion:** Annie **Champion ID:** 1 **Ability Slot:** P **Ability Name:** Pyromania **Effect 1:** Innate - Pyromania: Annie generates a stack of Pyromania whenever she hits an enemy with Disintegrate or casts her other abilities, stacking up to 4 times, at which she gains Energized. **Effect 2:** Energized: Annie empowers her next cast of Disintegrate, Incinerate, or Summon: Tibbers to consume all Pyromania stacks to stun enemies hit for 1.25 / 1.5 / 1.75 (based on level) seconds. **Effect 3:** Annie gains maximum stacks of Pyromania when the game starts and upon respawning. She will lose Energized and all Pyromania stacks upon death. **Technical data:** Targeting: Passive **Notes:** Annie does not lose any stacks upon entering or exiting resurrection. Stacks are gained even if the ability is blocked by spell shield. Pyromania's current stacks are represented by a counter under Annie's health bar, visible to all players. It lights up when the empowered effect is available. ### Q — Disintegrate **Champion:** Annie **Champion ID:** 1 **Ability Slot:** Q **Ability Name:** Disintegrate **Effect 1:** Active: Annie hurls a fireball at the target enemy that deals magic damage. **Scaling:** - **Magic Damage:** 80 / 125 / 170 / 215 / 260 + 80% AP **Effect 2:** If this kills the target, Disintegrate's cooldown is reduced by 50% and its mana cost is refunded. **Cost:** 60 / 65 / 70 / 75 / 80 MANA **Cooldown:** 4 seconds **Technical data:** Targeting: Unit | Damage type: MAGIC_DAMAGE | Cast time: 0.25 | Target range: 625 **Notes:** Disintegrate will
```

### Chunk 56

- Source: `champion_abilities_26.19.md`
- Index: `56`
- Palabras: `300`

```text
170 / 215 / 260 + 80% AP **Effect 2:** If this kills the target, Disintegrate's cooldown is reduced by 50% and its mana cost is refunded. **Cost:** 60 / 65 / 70 / 75 / 80 MANA **Cooldown:** 4 seconds **Technical data:** Targeting: Unit | Damage type: MAGIC_DAMAGE | Cast time: 0.25 | Target range: 625 **Notes:** Disintegrate will also grant the cooldown reduction and mana cost refund if the target is dead upon the missile's arrival. If the target becomes untargetable, dies, or is too far away or no longer in sight during the cast time, this ability will cancel but does not go on cooldown nor pay its cost (if applicable). ### W — Incinerate **Champion:** Annie **Champion ID:** 1 **Ability Slot:** W **Ability Name:** Incinerate **Effect 1:** Active: Annie releases fire in a cone in the target direction, dealing magic damage to enemies hit. **Scaling:** - **Magic Damage:** 70 / 110 / 150 / 190 / 230 + 80% AP **Cost:** 70 / 75 / 80 / 85 / 90 MANA **Cooldown:** 7 seconds **Technical data:** Targeting: Direction | Damage type: MAGIC_DAMAGE | Cast time: 0.25 **Notes:** Incinerate can hit targets behind Annie, provided their radius intersects with the cone hitbox. This ability will cast from wherever the caster is at the end of the cast time. ### E — Molten Shield **Champion:** Annie **Champion ID:** 1 **Ability Slot:** E **Ability Name:** Molten Shield **Effect 1:** Active: Annie grants herself or the target allied champion and Tibbers a shield for 3 seconds and 20% : 50% (based on level) bonus movement speed that decays over 1.5 seconds. **Scaling:** - **Shield Strength:** 60 / 95 / 130 / 165 / 200 + 40% AP **Effect 2:** While Molten Shield is active, enemies that deal damage to it
```

### Configuración 400/80

### Chunk 40

- Source: `champion_abilities_26.19.md`
- Index: `40`
- Palabras: `400`

```text
260 / 310 + 110% AP **Cost:** 50 MANA **Cooldown:** 4 seconds **Technical data:** Targeting: Unit | Damage type: MAGIC_DAMAGE | Cast time: 0.25 | Target range: 600 **Notes:** The damage of Frostbite is calculated once it hits. If the target's mark from being hit by Flash Frost or a fully formed Glacial Storm wears off while the projectile is traveling, the damage is not doubled. Frostbite has a different sound effect when it hits a target for double damage. If the target becomes untargetable, dies, or is too far away or no longer in sight during the cast time, this ability will cancel but does not go on cooldown nor pay its cost (if applicable). ### R — Glacial Storm **Champion:** Anivia **Champion ID:** 34 **Ability Slot:** R **Ability Name:** Glacial Storm **Effect 1:** Passive: Flash Frost's slow strength is increased. **Scaling:** - **Slow Strength Increase:** 0% / 10% / 20% **Effect 2:** Toggle: Anivia calls forth a driving rain of ice and hail at the target location, dealing magic damage every 0.5 seconds to enemies within and slowing them for 1 second, refreshing every 0.5 seconds while they remain inside. **Scaling:** - **Magic Damage per Tick:** 15 / 22.5 / 30 + 6.25% AP - **Slow:** 20% / 30% / 40% **Effect 3:** The blizzard increases in size over 1.5 seconds. At maximum size, Glacial Storm is empowered to deal 300% damage and increase the effectiveness of its slow by 50%, which also instead lasts 1.5 seconds and refreshes every 0.25 seconds. **Scaling:** - **Empowered Damage per Tick:** 45 / 67.5 / 90 + 18.75% AP - **Empowered Slow:** 30% / 45% / 60% **Effect 4:** Toggling Glacial Storm off triggers a final tick of damage and incurs its full cooldown. Glacial Storm is toggled off automatically if Anivia moves too far away from the blizzard or becomes unable to pay the mana cost, or is affected by any form of cast-inhibiting crowd control. **Cost:** 60 OTHER **Cooldown:** 4 / 3 / 2 seconds **Technical data:** Targeting: Location / Auto | Damage type: MAGIC_DAMAGE | Cast time: none | Target range: 750 **Notes:** Toggled abilities do not count as ability activations for the purposes of on-cast effects such as Spellblade and triggering Force Pulse's passive. Glacial Storm's slow leaves a trail that is visible even if the target is stealthed. Glacial Storm deals 3 half ticks at 200
```

### Chunk 41 **← ENCONTRADO**

- Source: `champion_abilities_26.19.md`
- Index: `41`
- Palabras: `400`

```text
any form of cast-inhibiting crowd control. **Cost:** 60 OTHER **Cooldown:** 4 / 3 / 2 seconds **Technical data:** Targeting: Location / Auto | Damage type: MAGIC_DAMAGE | Cast time: none | Target range: 750 **Notes:** Toggled abilities do not count as ability activations for the purposes of on-cast effects such as Spellblade and triggering Force Pulse's passive. Glacial Storm's slow leaves a trail that is visible even if the target is stealthed. Glacial Storm deals 3 half ticks at 200 / 267 / 333 radius for a total of 1.5 normal damage ticks before it starts dealing empowered damage at 400 radius. Stasis via Zhonya's Hourglass doesn't interrupt Glacial Storm. Tahm Kench's Devour does interrupt (allied and enemy) Glacial Storm. --- ## Annie ### P — Pyromania **Champion:** Annie **Champion ID:** 1 **Ability Slot:** P **Ability Name:** Pyromania **Effect 1:** Innate - Pyromania: Annie generates a stack of Pyromania whenever she hits an enemy with Disintegrate or casts her other abilities, stacking up to 4 times, at which she gains Energized. **Effect 2:** Energized: Annie empowers her next cast of Disintegrate, Incinerate, or Summon: Tibbers to consume all Pyromania stacks to stun enemies hit for 1.25 / 1.5 / 1.75 (based on level) seconds. **Effect 3:** Annie gains maximum stacks of Pyromania when the game starts and upon respawning. She will lose Energized and all Pyromania stacks upon death. **Technical data:** Targeting: Passive **Notes:** Annie does not lose any stacks upon entering or exiting resurrection. Stacks are gained even if the ability is blocked by spell shield. Pyromania's current stacks are represented by a counter under Annie's health bar, visible to all players. It lights up when the empowered effect is available. ### Q — Disintegrate **Champion:** Annie **Champion ID:** 1 **Ability Slot:** Q **Ability Name:** Disintegrate **Effect 1:** Active: Annie hurls a fireball at the target enemy that deals magic damage. **Scaling:** - **Magic Damage:** 80 / 125 / 170 / 215 / 260 + 80% AP **Effect 2:** If this kills the target, Disintegrate's cooldown is reduced by 50% and its mana cost is refunded. **Cost:** 60 / 65 / 70 / 75 / 80 MANA **Cooldown:** 4 seconds **Technical data:** Targeting: Unit | Damage type: MAGIC_DAMAGE | Cast time: 0.25 | Target range: 625 **Notes:** Disintegrate will also grant the cooldown reduction and mana cost refund if the target is dead upon the missile's arrival. If the
```

### Chunk 42

- Source: `champion_abilities_26.19.md`
- Index: `42`
- Palabras: `400`

```text
170 / 215 / 260 + 80% AP **Effect 2:** If this kills the target, Disintegrate's cooldown is reduced by 50% and its mana cost is refunded. **Cost:** 60 / 65 / 70 / 75 / 80 MANA **Cooldown:** 4 seconds **Technical data:** Targeting: Unit | Damage type: MAGIC_DAMAGE | Cast time: 0.25 | Target range: 625 **Notes:** Disintegrate will also grant the cooldown reduction and mana cost refund if the target is dead upon the missile's arrival. If the target becomes untargetable, dies, or is too far away or no longer in sight during the cast time, this ability will cancel but does not go on cooldown nor pay its cost (if applicable). ### W — Incinerate **Champion:** Annie **Champion ID:** 1 **Ability Slot:** W **Ability Name:** Incinerate **Effect 1:** Active: Annie releases fire in a cone in the target direction, dealing magic damage to enemies hit. **Scaling:** - **Magic Damage:** 70 / 110 / 150 / 190 / 230 + 80% AP **Cost:** 70 / 75 / 80 / 85 / 90 MANA **Cooldown:** 7 seconds **Technical data:** Targeting: Direction | Damage type: MAGIC_DAMAGE | Cast time: 0.25 **Notes:** Incinerate can hit targets behind Annie, provided their radius intersects with the cone hitbox. This ability will cast from wherever the caster is at the end of the cast time. ### E — Molten Shield **Champion:** Annie **Champion ID:** 1 **Ability Slot:** E **Ability Name:** Molten Shield **Effect 1:** Active: Annie grants herself or the target allied champion and Tibbers a shield for 3 seconds and 20% : 50% (based on level) bonus movement speed that decays over 1.5 seconds. **Scaling:** - **Shield Strength:** 60 / 95 / 130 / 165 / 200 + 40% AP **Effect 2:** While Molten Shield is active, enemies that deal damage to it take magic damage. This may only occur once per enemy per cast for each active Molten Shield. **Scaling:** - **Magic Damage:** 25 / 35 / 45 / 55 / 65 + 40% AP **Cost:** 60 / 65 / 70 / 75 / 80 MANA **Cooldown:** 10 seconds **Technical data:** Targeting: Unit / Auto | Damage type: MAGIC_DAMAGE | Cast time: none | Target range: 800 **Notes:** Molten Shield does not deal damage to turrets when attacked by them. Molten Shield has a forgiveness radius of 175 units. Attacks that are dodged or miss against the shielded target will not cause
```

## 4. Prueba cualitativa — E de Thresh

Texto utilizado para localizar el contenido: `### E — Flay`

### Configuración 200/40

### Chunk 1453

- Source: `champion_abilities_26.19.md`
- Index: `1453`
- Palabras: `200`

```text
Passage **Effect 1:** Active: Thresh throws his lantern to the target location over 0.5 seconds, lasting for 6 seconds while he remains nearby and granting sight of its surroundings. If Thresh moves too far away from the lantern, it returns back to him immediately. **Effect 2:** Thresh and the first allied champion to come near the lantern are granted a shield for 4 seconds. An ally can select the lantern while in proximity of it, dashing to Thresh and gaining the shield. **Scaling:** - **Shield Strength:** 50 / 70 / 90 / 110 / 130 + 2 per Soul collected **Effect 3:** An ally cannot select the lantern while immobilized, grounded, or silenced. The lantern will not expire from Thresh moving too far away if he is dashing with Deathly Leap. **Cost:** 50 / 55 / 60 / 65 / 70 MANA **Cooldown:** 21 / 20 / 19 / 18 / 17 seconds **Technical data:** Targeting: Location | Cast time: none | Target range: 950 **Notes:** The dashing ally will track Thresh if he changes locations. They will dash to Thresh's previous location if he is too far away or moves beyond 2200 units. The lantern is considered a unit
```

### Chunk 1454 **← ENCONTRADO**

- Source: `champion_abilities_26.19.md`
- Index: `1454`
- Palabras: `200`

```text
none | Target range: 950 **Notes:** The dashing ally will track Thresh if he changes locations. They will dash to Thresh's previous location if he is too far away or moves beyond 2200 units. The lantern is considered a unit and can be targeted by an allied Teleport, Leap Strike, Shunpo, and Safeguard. It is untargetable to enemies. The lantern blocks pathing of units like minions and champions. The lantern's duration and maximum leash range are each displayed as a circle on the ground. Thresh will gain Dark Passage's shield from moving out of leash range of the lantern. When the lantern returns to Thresh, the first ally champion to come in contact with Thresh while he has Dark Passage's shield will also gain a shield as long as no other ally has the shield. Dark Passage is special cased to trigger Guardian. ### E — Flay **Champion:** Thresh **Champion ID:** 412 **Ability Slot:** E **Ability Name:** Flay **Effect 1:** Passive: Thresh's basic attacks are empowered to deal bonus magic damage, with the AD ratio increasing over 10 seconds without basic attacking enemies. **Scaling:** - **Minimum Bonus Magic Damage:** 1.7 per Soul collected + 0% AD - **Maximum Bonus Magic
```

### Chunk 1455

- Source: `champion_abilities_26.19.md`
- Index: `1455`
- Palabras: `200`

```text
Passive: Thresh's basic attacks are empowered to deal bonus magic damage, with the AD ratio increasing over 10 seconds without basic attacking enemies. **Scaling:** - **Minimum Bonus Magic Damage:** 1.7 per Soul collected + 0% AD - **Maximum Bonus Magic Damage:** 1.7 per Soul collected + 90% AD / 120% AD / 150% AD / 180% AD / 210% AD **Effect 2:** Active: Thresh sweeps his chain across the ground in a broad line and a radius around him, starting behind him and towards the target direction. Enemies hit are dealt magic damage and knocked 200 units in the target direction, and then are slowed for 1 second. **Scaling:** - **Magic Damage:** 65 / 110 / 155 / 200 / 245 + 60% AP - **Slow:** 20% / 25% / 30% / 35% / 40% **Cost:** 60 / 65 / 70 / 75 / 80 MANA **Cooldown:** 13 / 12.25 / 11.5 / 10.75 / 10 seconds **Technical data:** Targeting: Direction | Damage type: MAGIC_DAMAGE | Cast time: 0.3889 **Notes:** Flay's effects start at the start of the cast time. Thresh can cast other spells once the cast time completes, but remains unable to attack and move and use mobility
```

### Configuración 300/60

### Chunk 968

- Source: `champion_abilities_26.19.md`
- Index: `968`
- Palabras: `300`

```text
direction until the missile is fired. This prevents the enemy from knowing where exactly Thresh is aiming at before the cast animation is complete. Death Sentence triggers on-cast effects (such as Spellblade and triggering Force Pulse's passive) once at the start of the cast, and once at the end of the cast. It may trigger on-cast effects a third time when casting Deathly Leap. This is because a separate spell is cast to prevent Thresh from facing towards the target direction immediately, which is (incorrectly) flagged to trigger on-cast effects.(bug) Type Cast time Attacking Disabled Abilities Disabled Movement Disabled Items Usable Shurelya's Battlesong Youmuu's Ghostblade Randuin's Omen Disabled All the other item-actives are disabled Interrupted by N/A Consumables Usable Spells Usable Barrier Clarity Cleanse Exhaust Ghost Heal Ignite Smite Disabled Flash Teleport Recall Hexflash Interrupted by N/A Interrupted by Death, unless protected by Resurrection ### W — Dark Passage **Champion:** Thresh **Champion ID:** 412 **Ability Slot:** W **Ability Name:** Dark Passage **Effect 1:** Active: Thresh throws his lantern to the target location over 0.5 seconds, lasting for 6 seconds while he remains nearby and granting sight of its surroundings. If Thresh moves too far away from the lantern, it returns back to him immediately. **Effect 2:** Thresh and the first allied champion to come near the lantern are granted a shield for 4 seconds. An ally can select the lantern while in proximity of it, dashing to Thresh and gaining the shield. **Scaling:** - **Shield Strength:** 50 / 70 / 90 / 110 / 130 + 2 per Soul collected **Effect 3:** An ally cannot select the lantern while immobilized, grounded, or silenced. The lantern will not expire from Thresh moving too far away if he is dashing with Deathly Leap. **Cost:** 50 / 55 / 60 / 65 /
```

### Chunk 969 **← ENCONTRADO**

- Source: `champion_abilities_26.19.md`
- Index: `969`
- Palabras: `300`

```text
the shield. **Scaling:** - **Shield Strength:** 50 / 70 / 90 / 110 / 130 + 2 per Soul collected **Effect 3:** An ally cannot select the lantern while immobilized, grounded, or silenced. The lantern will not expire from Thresh moving too far away if he is dashing with Deathly Leap. **Cost:** 50 / 55 / 60 / 65 / 70 MANA **Cooldown:** 21 / 20 / 19 / 18 / 17 seconds **Technical data:** Targeting: Location | Cast time: none | Target range: 950 **Notes:** The dashing ally will track Thresh if he changes locations. They will dash to Thresh's previous location if he is too far away or moves beyond 2200 units. The lantern is considered a unit and can be targeted by an allied Teleport, Leap Strike, Shunpo, and Safeguard. It is untargetable to enemies. The lantern blocks pathing of units like minions and champions. The lantern's duration and maximum leash range are each displayed as a circle on the ground. Thresh will gain Dark Passage's shield from moving out of leash range of the lantern. When the lantern returns to Thresh, the first ally champion to come in contact with Thresh while he has Dark Passage's shield will also gain a shield as long as no other ally has the shield. Dark Passage is special cased to trigger Guardian. ### E — Flay **Champion:** Thresh **Champion ID:** 412 **Ability Slot:** E **Ability Name:** Flay **Effect 1:** Passive: Thresh's basic attacks are empowered to deal bonus magic damage, with the AD ratio increasing over 10 seconds without basic attacking enemies. **Scaling:** - **Minimum Bonus Magic Damage:** 1.7 per Soul collected + 0% AD - **Maximum Bonus Magic Damage:** 1.7 per Soul collected + 90% AD / 120% AD / 150% AD / 180% AD / 210% AD
```

### Chunk 970

- Source: `champion_abilities_26.19.md`
- Index: `970`
- Palabras: `300`

```text
Passive: Thresh's basic attacks are empowered to deal bonus magic damage, with the AD ratio increasing over 10 seconds without basic attacking enemies. **Scaling:** - **Minimum Bonus Magic Damage:** 1.7 per Soul collected + 0% AD - **Maximum Bonus Magic Damage:** 1.7 per Soul collected + 90% AD / 120% AD / 150% AD / 180% AD / 210% AD **Effect 2:** Active: Thresh sweeps his chain across the ground in a broad line and a radius around him, starting behind him and towards the target direction. Enemies hit are dealt magic damage and knocked 200 units in the target direction, and then are slowed for 1 second. **Scaling:** - **Magic Damage:** 65 / 110 / 155 / 200 / 245 + 60% AP - **Slow:** 20% / 25% / 30% / 35% / 40% **Cost:** 60 / 65 / 70 / 75 / 80 MANA **Cooldown:** 13 / 12.25 / 11.5 / 10.75 / 10 seconds **Technical data:** Targeting: Direction | Damage type: MAGIC_DAMAGE | Cast time: 0.3889 **Notes:** Flay's effects start at the start of the cast time. Thresh can cast other spells once the cast time completes, but remains unable to attack and move and use mobility spells (such as Flash) until the chain completed its way entirely. Applies area damage on the ability and deals proc damage on the enhanced basic attack. The knockback's airborne debuff is set to last longer than the forced movement, but gets removed as soon as the forced movement from Flay ends or is overridden by another. Flay's passive's buff icon changes colors depending on charge level. At 100%, Thresh's scythe will glow green and a sound effect will play. 0 - 50% 50 - 75% 75% - 100% 100% Runaan's Hurricane's Wind's Fury will apply Flay's passive to each enemy
```

### Configuración 400/80

### Chunk 726

- Source: `champion_abilities_26.19.md`
- Index: `726`
- Palabras: `400`

```text
direction until the missile is fired. This prevents the enemy from knowing where exactly Thresh is aiming at before the cast animation is complete. Death Sentence triggers on-cast effects (such as Spellblade and triggering Force Pulse's passive) once at the start of the cast, and once at the end of the cast. It may trigger on-cast effects a third time when casting Deathly Leap. This is because a separate spell is cast to prevent Thresh from facing towards the target direction immediately, which is (incorrectly) flagged to trigger on-cast effects.(bug) Type Cast time Attacking Disabled Abilities Disabled Movement Disabled Items Usable Shurelya's Battlesong Youmuu's Ghostblade Randuin's Omen Disabled All the other item-actives are disabled Interrupted by N/A Consumables Usable Spells Usable Barrier Clarity Cleanse Exhaust Ghost Heal Ignite Smite Disabled Flash Teleport Recall Hexflash Interrupted by N/A Interrupted by Death, unless protected by Resurrection ### W — Dark Passage **Champion:** Thresh **Champion ID:** 412 **Ability Slot:** W **Ability Name:** Dark Passage **Effect 1:** Active: Thresh throws his lantern to the target location over 0.5 seconds, lasting for 6 seconds while he remains nearby and granting sight of its surroundings. If Thresh moves too far away from the lantern, it returns back to him immediately. **Effect 2:** Thresh and the first allied champion to come near the lantern are granted a shield for 4 seconds. An ally can select the lantern while in proximity of it, dashing to Thresh and gaining the shield. **Scaling:** - **Shield Strength:** 50 / 70 / 90 / 110 / 130 + 2 per Soul collected **Effect 3:** An ally cannot select the lantern while immobilized, grounded, or silenced. The lantern will not expire from Thresh moving too far away if he is dashing with Deathly Leap. **Cost:** 50 / 55 / 60 / 65 / 70 MANA **Cooldown:** 21 / 20 / 19 / 18 / 17 seconds **Technical data:** Targeting: Location | Cast time: none | Target range: 950 **Notes:** The dashing ally will track Thresh if he changes locations. They will dash to Thresh's previous location if he is too far away or moves beyond 2200 units. The lantern is considered a unit and can be targeted by an allied Teleport, Leap Strike, Shunpo, and Safeguard. It is untargetable to enemies. The lantern blocks pathing of units like minions and champions. The lantern's duration and maximum leash range are each displayed as a
```

### Chunk 727 **← ENCONTRADO**

- Source: `champion_abilities_26.19.md`
- Index: `727`
- Palabras: `400`

```text
none | Target range: 950 **Notes:** The dashing ally will track Thresh if he changes locations. They will dash to Thresh's previous location if he is too far away or moves beyond 2200 units. The lantern is considered a unit and can be targeted by an allied Teleport, Leap Strike, Shunpo, and Safeguard. It is untargetable to enemies. The lantern blocks pathing of units like minions and champions. The lantern's duration and maximum leash range are each displayed as a circle on the ground. Thresh will gain Dark Passage's shield from moving out of leash range of the lantern. When the lantern returns to Thresh, the first ally champion to come in contact with Thresh while he has Dark Passage's shield will also gain a shield as long as no other ally has the shield. Dark Passage is special cased to trigger Guardian. ### E — Flay **Champion:** Thresh **Champion ID:** 412 **Ability Slot:** E **Ability Name:** Flay **Effect 1:** Passive: Thresh's basic attacks are empowered to deal bonus magic damage, with the AD ratio increasing over 10 seconds without basic attacking enemies. **Scaling:** - **Minimum Bonus Magic Damage:** 1.7 per Soul collected + 0% AD - **Maximum Bonus Magic Damage:** 1.7 per Soul collected + 90% AD / 120% AD / 150% AD / 180% AD / 210% AD **Effect 2:** Active: Thresh sweeps his chain across the ground in a broad line and a radius around him, starting behind him and towards the target direction. Enemies hit are dealt magic damage and knocked 200 units in the target direction, and then are slowed for 1 second. **Scaling:** - **Magic Damage:** 65 / 110 / 155 / 200 / 245 + 60% AP - **Slow:** 20% / 25% / 30% / 35% / 40% **Cost:** 60 / 65 / 70 / 75 / 80 MANA **Cooldown:** 13 / 12.25 / 11.5 / 10.75 / 10 seconds **Technical data:** Targeting: Direction | Damage type: MAGIC_DAMAGE | Cast time: 0.3889 **Notes:** Flay's effects start at the start of the cast time. Thresh can cast other spells once the cast time completes, but remains unable to attack and move and use mobility spells (such as Flash) until the chain completed its way entirely. Applies area damage on the ability and deals proc damage on the enhanced basic attack. The knockback's airborne debuff is set to last longer than the forced movement, but
```

### Chunk 728

- Source: `champion_abilities_26.19.md`
- Index: `728`
- Palabras: `400`

```text
Direction | Damage type: MAGIC_DAMAGE | Cast time: 0.3889 **Notes:** Flay's effects start at the start of the cast time. Thresh can cast other spells once the cast time completes, but remains unable to attack and move and use mobility spells (such as Flash) until the chain completed its way entirely. Applies area damage on the ability and deals proc damage on the enhanced basic attack. The knockback's airborne debuff is set to last longer than the forced movement, but gets removed as soon as the forced movement from Flay ends or is overridden by another. Flay's passive's buff icon changes colors depending on charge level. At 100%, Thresh's scythe will glow green and a sound effect will play. 0 - 50% 50 - 75% 75% - 100% 100% Runaan's Hurricane's Wind's Fury will apply Flay's passive to each enemy hit, with the secondary targets taking minimum damage (charge resets upon hitting the primary target). The enhanced attack applies other on-hit effects and can critically strike as normal (the bonus damage cannot). Flay's passive enhanced attack can be dodged (the enhanced attack is not consumed and the charge is not reset) and blocked (the enhanced attack is consumed and the charge is reset). The empowered attack will not trigger against structures nor wards. PENDING FOR TEST:: Enhanced attack's interactions with blinding effects (regarding both bonus damage and charge reset). Type Cast time Attacking Disabled Abilities Disabled Movement Disabled Items Usable Shurelya's Battlesong Youmuu's Ghostblade Randuin's Omen Disabled All the other item-actives are disabled Interrupted by N/A Consumables Usable Spells Usable Barrier Clarity Cleanse Exhaust Ghost Heal Ignite Smite Disabled Flash Teleport Recall Hexflash Interrupted by N/A Interrupted by Death, unless protected by Resurrection ### R — The Box **Champion:** Thresh **Champion ID:** 412 **Ability Slot:** R **Ability Name:** The Box **Effect 1:** Active: Thresh erects a pentagon of spectral walls around him that each last for 5 seconds. A wall will break upon enemy champion contact, dealing magic damage and slowing them by 99% for 2 seconds. After the first wall breaks, the rest will deal no damage and slow for only 1 second. **Scaling:** - **Magic Damage:** 250 / 400 / 550 + 100% AP **Effect 2:** Enemies that break a wall cannot do so again for 1 second. **Cost:** 100 MANA **Cooldown:** 120 / 100 / 80 seconds **Technical data:** Targeting: Auto | Damage type: MAGIC_DAMAGE | Cast
```

## 5. Prueba cualitativa — Manamune

Texto utilizado para localizar el contenido: `**Item:** Manamune`

### Configuración 200/40

### Chunk 2034

- Source: `items_26.19.md`
- Index: `65`
- Palabras: `200`

```text
fragile foes ### Shop - Total price: 2750 gold - Sell price: 1100 gold ### Stats - 100 Ability Power - 600 Mana - 10 Ability Haste ### Components - Lost Chapter (ID 3802) - Hextech Alternator (ID 3145) ### Effects **Passive: Echo** (Cooldown: 12 s) Gain 6 Echo stacks. Dealing ability damage to an enemy consumes all Echo stacks to deal 75 (+ 5% AP) bonus magic damage to them and, for each stack consumed beyond the first, an additional enemy within 600 units of them, firing an orb at each secondary target that impacts after 0.5 to deal the damage. If the number of additional targets fired at is less than the number of stacks consumed,deal an additional 20% damage to the primary target for each remaining Echo stack **Tags:** MAGE --- ## Malignance **Item:** Malignance **Item ID:** 3118 **Tier:** 3 **Rank:** LEGENDARY **Description:** Partner with an ally to protect each other ### Shop - Total price: 2700 gold - Sell price: 1080 gold ### Stats - 90 Ability Power - 600 Mana - 15 Ability Haste ### Components - Lost Chapter (ID 3802) - Blasting Wand (ID 1026) ### Effects **Passive: Scorn** Gain 20 ultimate haste. **Passive:
```

### Chunk 2035 **← ENCONTRADO**

- Source: `items_26.19.md`
- Index: `66`
- Palabras: `200`

```text
gold - Sell price: 1080 gold ### Stats - 90 Ability Power - 600 Mana - 15 Ability Haste ### Components - Lost Chapter (ID 3802) - Blasting Wand (ID 1026) ### Effects **Passive: Scorn** Gain 20 ultimate haste. **Passive: Hatefog** Dealing non-proc damage or pet damage to enemy champions with your ultimate ability creates a 251; 251.8; 253.1; 255.5; 259.8; 267.3; 280.7; 304.2; 345.9; 419.7; 550 (250 + 2^(damage dealt/100)) [based on ultimate's damage instance] radius scorched zone beneath them for 3 seconds, applying a Curse to enemies within that deals 60*3 (+ 5*3% AP) total magic damage over the duration and reduces their magic resistance by 10 (3 second cooldown per target, starts on zone creation). **Aliases:** burn **Tags:** MAGE, ABILITY_HASTE --- ## Manamune **Item:** Manamune **Item ID:** 3004 **Tier:** 3 **Rank:** LEGENDARY **Description:** Increases Attack Damage based on maximum Mana ### Shop - Total price: 2900 gold - Sell price: 1160 gold ### Stats - 35 Attack Damage - 500 Mana - 15 Ability Haste ### Components - Tear of the Goddess (ID 3070) - Caulfield's Warhammer (ID 3133) - Long Sword (ID 1036) ### Effects **Passive: Awe** Grants bonus attack damage equal to 2% maximum mana.
```

### Chunk 2036

- Source: `items_26.19.md`
- Index: `67`
- Palabras: `200`

```text
Damage - 500 Mana - 15 Ability Haste ### Components - Tear of the Goddess (ID 3070) - Caulfield's Warhammer (ID 3133) - Long Sword (ID 1036) ### Effects **Passive: Awe** Grants bonus attack damage equal to 2% maximum mana. **Passive: Manaflow** Grants a charge every 8 seconds, up to 4 charges. Consumes a charge on-hit and whenever affecting an enemy or ally with an ability to grant 3 bonus mana, increased to 6 for champion targets, up to a maximum of 360 bonus mana. Can only be triggered once per cast instance. **Passive: Unnamed** Transforms into Muramana at 360 bonus mana. **Aliases:** Muramana, tear **Tags:** FIGHTER, MARKSMAN, ASSASSIN, ONHIT_EFFECTS --- ## Maw of Malmortius **Item:** Maw of Malmortius **Item ID:** 3156 **Tier:** 3 **Rank:** LEGENDARY **Description:** Grants bonus Attack Damage when Health is low ### Shop - Total price: 3100 gold - Sell price: 1240 gold ### Stats - 60 Attack Damage - 40 Magic Resistance - 15 Ability Haste ### Components - Hexdrinker (ID 3155) - Caulfield's Warhammer (ID 3133) ### Effects **Passive: Lifeline** (Cooldown: 90 s) If you would take magic damage that would reduce you below 30% of your maximum health, you first gain a shield
```

### Configuración 300/60

### Chunk 1356

- Source: `items_26.19.md`
- Index: `43`
- Palabras: `300`

```text
- Total price: 1200 gold - Sell price: 480 gold ### Stats - 40 Ability Power - 300 Mana - 10 Ability Haste ### Components - Amplifying Tome (ID 1052) - Sapphire Crystal (ID 1027) - Glowing Mote (ID 2022) ### Effects **Passive: Enlighten** Upon leveling up, restores 20% of maximum mana over 3 seconds. **Aliases:** mana book **Tags:** MAGE --- ## Luden's Echo **Item:** Luden's Echo **Item ID:** 6655 **Tier:** 3 **Rank:** LEGENDARY **Description:** High burst damage, good against fragile foes ### Shop - Total price: 2750 gold - Sell price: 1100 gold ### Stats - 100 Ability Power - 600 Mana - 10 Ability Haste ### Components - Lost Chapter (ID 3802) - Hextech Alternator (ID 3145) ### Effects **Passive: Echo** (Cooldown: 12 s) Gain 6 Echo stacks. Dealing ability damage to an enemy consumes all Echo stacks to deal 75 (+ 5% AP) bonus magic damage to them and, for each stack consumed beyond the first, an additional enemy within 600 units of them, firing an orb at each secondary target that impacts after 0.5 to deal the damage. If the number of additional targets fired at is less than the number of stacks consumed,deal an additional 20% damage to the primary target for each remaining Echo stack **Tags:** MAGE --- ## Malignance **Item:** Malignance **Item ID:** 3118 **Tier:** 3 **Rank:** LEGENDARY **Description:** Partner with an ally to protect each other ### Shop - Total price: 2700 gold - Sell price: 1080 gold ### Stats - 90 Ability Power - 600 Mana - 15 Ability Haste ### Components - Lost Chapter (ID 3802) - Blasting Wand (ID 1026) ### Effects **Passive: Scorn** Gain 20 ultimate haste. **Passive: Hatefog** Dealing non-proc damage or pet damage to enemy champions with your ultimate ability creates a 251; 251.8; 253.1; 255.5;
```

### Chunk 1357 **← ENCONTRADO**

- Source: `items_26.19.md`
- Index: `44`
- Palabras: `300`

```text
gold - Sell price: 1080 gold ### Stats - 90 Ability Power - 600 Mana - 15 Ability Haste ### Components - Lost Chapter (ID 3802) - Blasting Wand (ID 1026) ### Effects **Passive: Scorn** Gain 20 ultimate haste. **Passive: Hatefog** Dealing non-proc damage or pet damage to enemy champions with your ultimate ability creates a 251; 251.8; 253.1; 255.5; 259.8; 267.3; 280.7; 304.2; 345.9; 419.7; 550 (250 + 2^(damage dealt/100)) [based on ultimate's damage instance] radius scorched zone beneath them for 3 seconds, applying a Curse to enemies within that deals 60*3 (+ 5*3% AP) total magic damage over the duration and reduces their magic resistance by 10 (3 second cooldown per target, starts on zone creation). **Aliases:** burn **Tags:** MAGE, ABILITY_HASTE --- ## Manamune **Item:** Manamune **Item ID:** 3004 **Tier:** 3 **Rank:** LEGENDARY **Description:** Increases Attack Damage based on maximum Mana ### Shop - Total price: 2900 gold - Sell price: 1160 gold ### Stats - 35 Attack Damage - 500 Mana - 15 Ability Haste ### Components - Tear of the Goddess (ID 3070) - Caulfield's Warhammer (ID 3133) - Long Sword (ID 1036) ### Effects **Passive: Awe** Grants bonus attack damage equal to 2% maximum mana. **Passive: Manaflow** Grants a charge every 8 seconds, up to 4 charges. Consumes a charge on-hit and whenever affecting an enemy or ally with an ability to grant 3 bonus mana, increased to 6 for champion targets, up to a maximum of 360 bonus mana. Can only be triggered once per cast instance. **Passive: Unnamed** Transforms into Muramana at 360 bonus mana. **Aliases:** Muramana, tear **Tags:** FIGHTER, MARKSMAN, ASSASSIN, ONHIT_EFFECTS --- ## Maw of Malmortius **Item:** Maw of Malmortius **Item ID:** 3156 **Tier:** 3 **Rank:** LEGENDARY **Description:** Grants bonus Attack Damage when Health is low ### Shop - Total price:
```

### Chunk 1358

- Source: `items_26.19.md`
- Index: `45`
- Palabras: `300`

```text
maximum of 360 bonus mana. Can only be triggered once per cast instance. **Passive: Unnamed** Transforms into Muramana at 360 bonus mana. **Aliases:** Muramana, tear **Tags:** FIGHTER, MARKSMAN, ASSASSIN, ONHIT_EFFECTS --- ## Maw of Malmortius **Item:** Maw of Malmortius **Item ID:** 3156 **Tier:** 3 **Rank:** LEGENDARY **Description:** Grants bonus Attack Damage when Health is low ### Shop - Total price: 3100 gold - Sell price: 1240 gold ### Stats - 60 Attack Damage - 40 Magic Resistance - 15 Ability Haste ### Components - Hexdrinker (ID 3155) - Caulfield's Warhammer (ID 3133) ### Effects **Passive: Lifeline** (Cooldown: 90 s) If you would take magic damage that would reduce you below 30% of your maximum health, you first gain a shield that absorbs 200 / 150 (+ 150% / 112.5% bonus AD) magic damage for 3 seconds. Additionally, triggering this effect grants you 10% omnivamp until the end of combat. **Tags:** FIGHTER, MARKSMAN, ASSASSIN --- ## Mejai's Soulstealer **Item:** Mejai's Soulstealer **Item ID:** 3041 **Tier:** 2 **Rank:** LEGENDARY **Description:** Grants Ability Power for kills and assists ### Shop - Total price: 1500 gold - Sell price: 600 gold ### Stats - 20 Ability Power - 100 Health ### Components - Dark Seal (ID 1082) ### Effects **Passive: Glory** Gain 4 stacks for each champion kill and 2 stacks for each assist, up to a maximum of 25 stacks. For every stack, gain 5 ability power, up to 125 at maximum stacks. If you have at least 10 stacks, also gain 10% bonus movement speed. Lose 10 stacks on death. Stacks are preserved from Dark Seal. **Aliases:** book **Tags:** MAGE, MOVEMENT --- ## Mercurial Scimitar **Item:** Mercurial Scimitar **Item ID:** 3139 **Tier:** 3 **Rank:** LEGENDARY **Description:** Activate to remove all crowd control debuffs and grant massive Move Speed ### Shop - Total
```

### Configuración 400/80

### Chunk 1016

- Source: `items_26.19.md`
- Index: `32`
- Palabras: `400`

```text
- 25% Critical Strike Chance ### Components - Last Whisper (ID 3035) - Noonquiver (ID 6670) ### Effects **Passive: Giant Slayer** Deal 0 to 15 for 16% (1% per 100 bonus health, up to a maximum of 15% at 1500 bonus health.) [based on target's bonus health] increased damage against enemy champions. **Aliases:** lw, ldr, doms **Tags:** MARKSMAN --- ## Lost Chapter **Item:** Lost Chapter **Item ID:** 3802 **Tier:** 2 **Rank:** EPIC **Description:** Restores Mana upon levelling up. ### Shop - Total price: 1200 gold - Sell price: 480 gold ### Stats - 40 Ability Power - 300 Mana - 10 Ability Haste ### Components - Amplifying Tome (ID 1052) - Sapphire Crystal (ID 1027) - Glowing Mote (ID 2022) ### Effects **Passive: Enlighten** Upon leveling up, restores 20% of maximum mana over 3 seconds. **Aliases:** mana book **Tags:** MAGE --- ## Luden's Echo **Item:** Luden's Echo **Item ID:** 6655 **Tier:** 3 **Rank:** LEGENDARY **Description:** High burst damage, good against fragile foes ### Shop - Total price: 2750 gold - Sell price: 1100 gold ### Stats - 100 Ability Power - 600 Mana - 10 Ability Haste ### Components - Lost Chapter (ID 3802) - Hextech Alternator (ID 3145) ### Effects **Passive: Echo** (Cooldown: 12 s) Gain 6 Echo stacks. Dealing ability damage to an enemy consumes all Echo stacks to deal 75 (+ 5% AP) bonus magic damage to them and, for each stack consumed beyond the first, an additional enemy within 600 units of them, firing an orb at each secondary target that impacts after 0.5 to deal the damage. If the number of additional targets fired at is less than the number of stacks consumed,deal an additional 20% damage to the primary target for each remaining Echo stack **Tags:** MAGE --- ## Malignance **Item:** Malignance **Item ID:** 3118 **Tier:** 3 **Rank:** LEGENDARY **Description:** Partner with an ally to protect each other ### Shop - Total price: 2700 gold - Sell price: 1080 gold ### Stats - 90 Ability Power - 600 Mana - 15 Ability Haste ### Components - Lost Chapter (ID 3802) - Blasting Wand (ID 1026) ### Effects **Passive: Scorn** Gain 20 ultimate haste. **Passive: Hatefog** Dealing non-proc damage or pet damage to enemy champions with your ultimate ability creates a 251; 251.8; 253.1; 255.5; 259.8; 267.3; 280.7; 304.2; 345.9; 419.7; 550 (250 + 2^(damage dealt/100)) [based on ultimate's damage instance] radius scorched zone beneath
```

### Chunk 1017 **← ENCONTRADO**

- Source: `items_26.19.md`
- Index: `33`
- Palabras: `400`

```text
gold - Sell price: 1080 gold ### Stats - 90 Ability Power - 600 Mana - 15 Ability Haste ### Components - Lost Chapter (ID 3802) - Blasting Wand (ID 1026) ### Effects **Passive: Scorn** Gain 20 ultimate haste. **Passive: Hatefog** Dealing non-proc damage or pet damage to enemy champions with your ultimate ability creates a 251; 251.8; 253.1; 255.5; 259.8; 267.3; 280.7; 304.2; 345.9; 419.7; 550 (250 + 2^(damage dealt/100)) [based on ultimate's damage instance] radius scorched zone beneath them for 3 seconds, applying a Curse to enemies within that deals 60*3 (+ 5*3% AP) total magic damage over the duration and reduces their magic resistance by 10 (3 second cooldown per target, starts on zone creation). **Aliases:** burn **Tags:** MAGE, ABILITY_HASTE --- ## Manamune **Item:** Manamune **Item ID:** 3004 **Tier:** 3 **Rank:** LEGENDARY **Description:** Increases Attack Damage based on maximum Mana ### Shop - Total price: 2900 gold - Sell price: 1160 gold ### Stats - 35 Attack Damage - 500 Mana - 15 Ability Haste ### Components - Tear of the Goddess (ID 3070) - Caulfield's Warhammer (ID 3133) - Long Sword (ID 1036) ### Effects **Passive: Awe** Grants bonus attack damage equal to 2% maximum mana. **Passive: Manaflow** Grants a charge every 8 seconds, up to 4 charges. Consumes a charge on-hit and whenever affecting an enemy or ally with an ability to grant 3 bonus mana, increased to 6 for champion targets, up to a maximum of 360 bonus mana. Can only be triggered once per cast instance. **Passive: Unnamed** Transforms into Muramana at 360 bonus mana. **Aliases:** Muramana, tear **Tags:** FIGHTER, MARKSMAN, ASSASSIN, ONHIT_EFFECTS --- ## Maw of Malmortius **Item:** Maw of Malmortius **Item ID:** 3156 **Tier:** 3 **Rank:** LEGENDARY **Description:** Grants bonus Attack Damage when Health is low ### Shop - Total price: 3100 gold - Sell price: 1240 gold ### Stats - 60 Attack Damage - 40 Magic Resistance - 15 Ability Haste ### Components - Hexdrinker (ID 3155) - Caulfield's Warhammer (ID 3133) ### Effects **Passive: Lifeline** (Cooldown: 90 s) If you would take magic damage that would reduce you below 30% of your maximum health, you first gain a shield that absorbs 200 / 150 (+ 150% / 112.5% bonus AD) magic damage for 3 seconds. Additionally, triggering this effect grants you 10% omnivamp until the end of combat. **Tags:** FIGHTER, MARKSMAN, ASSASSIN --- ## Mejai's Soulstealer **Item:** Mejai's Soulstealer
```

### Chunk 1018

- Source: `items_26.19.md`
- Index: `34`
- Palabras: `400`

```text
Haste ### Components - Hexdrinker (ID 3155) - Caulfield's Warhammer (ID 3133) ### Effects **Passive: Lifeline** (Cooldown: 90 s) If you would take magic damage that would reduce you below 30% of your maximum health, you first gain a shield that absorbs 200 / 150 (+ 150% / 112.5% bonus AD) magic damage for 3 seconds. Additionally, triggering this effect grants you 10% omnivamp until the end of combat. **Tags:** FIGHTER, MARKSMAN, ASSASSIN --- ## Mejai's Soulstealer **Item:** Mejai's Soulstealer **Item ID:** 3041 **Tier:** 2 **Rank:** LEGENDARY **Description:** Grants Ability Power for kills and assists ### Shop - Total price: 1500 gold - Sell price: 600 gold ### Stats - 20 Ability Power - 100 Health ### Components - Dark Seal (ID 1082) ### Effects **Passive: Glory** Gain 4 stacks for each champion kill and 2 stacks for each assist, up to a maximum of 25 stacks. For every stack, gain 5 ability power, up to 125 at maximum stacks. If you have at least 10 stacks, also gain 10% bonus movement speed. Lose 10 stacks on death. Stacks are preserved from Dark Seal. **Aliases:** book **Tags:** MAGE, MOVEMENT --- ## Mercurial Scimitar **Item:** Mercurial Scimitar **Item ID:** 3139 **Tier:** 3 **Rank:** LEGENDARY **Description:** Activate to remove all crowd control debuffs and grant massive Move Speed ### Shop - Total price: 3200 gold - Sell price: 1280 gold ### Stats - 50 Attack Damage - 10% Life Steal - 35 Magic Resistance ### Components - Quicksilver Sash (ID 3140) - Pickaxe (ID 1037) - Vampiric Scepter (ID 1053) ### Effects **Active: Quicksilver** (Cooldown: 90 s) Removes all crowd control debuffs (except Airborne) from your champion and grants 50% bonus total movement speed and ghosting for 2 seconds. **Aliases:** merc scim, qss, quicksilver sash, silvermere dawn **Tags:** FIGHTER, MARKSMAN, MOVEMENT --- ## Mercury's Treads **Item:** Mercury's Treads **Item ID:** 3111 **Tier:** 2 **Rank:** BOOTS **Description:** Increases Move Speed and reduces duration of disabling effects ### Shop - Total price: 1250 gold - Sell price: 500 gold ### Stats - 20 Magic Resistance - 45 Movement Speed - 30% Tenacity ### Components - Boots (ID 1001) - Null-Magic Mantle (ID 1033) **Aliases:** boots, mercs --- ## Mikael's Blessing **Item:** Mikael's Blessing **Item ID:** 3222 **Tier:** 3 **Rank:** LEGENDARY **Description:** Activate to remove all disabling effects from an allied champion ### Shop - Total price: 2300 gold - Sell price: 920 gold ###
```

## 6. Comparación específica del overlap

Se mantuvo fijo `chunk_size = 300` y se modificó únicamente el overlap.

### Configuración 300/40

### Chunk 894

- Source: `champion_abilities_26.19.md`
- Index: `894`
- Palabras: `300`

```text
Usable Barrier Clarity Cleanse Exhaust Ghost Heal Ignite Smite Disabled Flash Teleport Recall Hexflash Interrupted by N/A Interrupted by Death, unless protected by Resurrection ### W — Dark Passage **Champion:** Thresh **Champion ID:** 412 **Ability Slot:** W **Ability Name:** Dark Passage **Effect 1:** Active: Thresh throws his lantern to the target location over 0.5 seconds, lasting for 6 seconds while he remains nearby and granting sight of its surroundings. If Thresh moves too far away from the lantern, it returns back to him immediately. **Effect 2:** Thresh and the first allied champion to come near the lantern are granted a shield for 4 seconds. An ally can select the lantern while in proximity of it, dashing to Thresh and gaining the shield. **Scaling:** - **Shield Strength:** 50 / 70 / 90 / 110 / 130 + 2 per Soul collected **Effect 3:** An ally cannot select the lantern while immobilized, grounded, or silenced. The lantern will not expire from Thresh moving too far away if he is dashing with Deathly Leap. **Cost:** 50 / 55 / 60 / 65 / 70 MANA **Cooldown:** 21 / 20 / 19 / 18 / 17 seconds **Technical data:** Targeting: Location | Cast time: none | Target range: 950 **Notes:** The dashing ally will track Thresh if he changes locations. They will dash to Thresh's previous location if he is too far away or moves beyond 2200 units. The lantern is considered a unit and can be targeted by an allied Teleport, Leap Strike, Shunpo, and Safeguard. It is untargetable to enemies. The lantern blocks pathing of units like minions and champions. The lantern's duration and maximum leash range are each displayed as a circle on the ground. Thresh will gain Dark Passage's shield from moving out of leash range of the lantern. When
```

### Chunk 895 **← ENCONTRADO**

- Source: `champion_abilities_26.19.md`
- Index: `895`
- Palabras: `300`

```text
blocks pathing of units like minions and champions. The lantern's duration and maximum leash range are each displayed as a circle on the ground. Thresh will gain Dark Passage's shield from moving out of leash range of the lantern. When the lantern returns to Thresh, the first ally champion to come in contact with Thresh while he has Dark Passage's shield will also gain a shield as long as no other ally has the shield. Dark Passage is special cased to trigger Guardian. ### E — Flay **Champion:** Thresh **Champion ID:** 412 **Ability Slot:** E **Ability Name:** Flay **Effect 1:** Passive: Thresh's basic attacks are empowered to deal bonus magic damage, with the AD ratio increasing over 10 seconds without basic attacking enemies. **Scaling:** - **Minimum Bonus Magic Damage:** 1.7 per Soul collected + 0% AD - **Maximum Bonus Magic Damage:** 1.7 per Soul collected + 90% AD / 120% AD / 150% AD / 180% AD / 210% AD **Effect 2:** Active: Thresh sweeps his chain across the ground in a broad line and a radius around him, starting behind him and towards the target direction. Enemies hit are dealt magic damage and knocked 200 units in the target direction, and then are slowed for 1 second. **Scaling:** - **Magic Damage:** 65 / 110 / 155 / 200 / 245 + 60% AP - **Slow:** 20% / 25% / 30% / 35% / 40% **Cost:** 60 / 65 / 70 / 75 / 80 MANA **Cooldown:** 13 / 12.25 / 11.5 / 10.75 / 10 seconds **Technical data:** Targeting: Direction | Damage type: MAGIC_DAMAGE | Cast time: 0.3889 **Notes:** Flay's effects start at the start of the cast time. Thresh can cast other spells once the cast time completes, but remains unable to attack and move and use mobility
```

### Chunk 896

- Source: `champion_abilities_26.19.md`
- Index: `896`
- Palabras: `300`

```text
Direction | Damage type: MAGIC_DAMAGE | Cast time: 0.3889 **Notes:** Flay's effects start at the start of the cast time. Thresh can cast other spells once the cast time completes, but remains unable to attack and move and use mobility spells (such as Flash) until the chain completed its way entirely. Applies area damage on the ability and deals proc damage on the enhanced basic attack. The knockback's airborne debuff is set to last longer than the forced movement, but gets removed as soon as the forced movement from Flay ends or is overridden by another. Flay's passive's buff icon changes colors depending on charge level. At 100%, Thresh's scythe will glow green and a sound effect will play. 0 - 50% 50 - 75% 75% - 100% 100% Runaan's Hurricane's Wind's Fury will apply Flay's passive to each enemy hit, with the secondary targets taking minimum damage (charge resets upon hitting the primary target). The enhanced attack applies other on-hit effects and can critically strike as normal (the bonus damage cannot). Flay's passive enhanced attack can be dodged (the enhanced attack is not consumed and the charge is not reset) and blocked (the enhanced attack is consumed and the charge is reset). The empowered attack will not trigger against structures nor wards. PENDING FOR TEST:: Enhanced attack's interactions with blinding effects (regarding both bonus damage and charge reset). Type Cast time Attacking Disabled Abilities Disabled Movement Disabled Items Usable Shurelya's Battlesong Youmuu's Ghostblade Randuin's Omen Disabled All the other item-actives are disabled Interrupted by N/A Consumables Usable Spells Usable Barrier Clarity Cleanse Exhaust Ghost Heal Ignite Smite Disabled Flash Teleport Recall Hexflash Interrupted by N/A Interrupted by Death, unless protected by Resurrection ### R — The Box **Champion:** Thresh **Champion ID:** 412 **Ability Slot:** R **Ability Name:** The Box
```

### Configuración 300/60

### Chunk 968

- Source: `champion_abilities_26.19.md`
- Index: `968`
- Palabras: `300`

```text
direction until the missile is fired. This prevents the enemy from knowing where exactly Thresh is aiming at before the cast animation is complete. Death Sentence triggers on-cast effects (such as Spellblade and triggering Force Pulse's passive) once at the start of the cast, and once at the end of the cast. It may trigger on-cast effects a third time when casting Deathly Leap. This is because a separate spell is cast to prevent Thresh from facing towards the target direction immediately, which is (incorrectly) flagged to trigger on-cast effects.(bug) Type Cast time Attacking Disabled Abilities Disabled Movement Disabled Items Usable Shurelya's Battlesong Youmuu's Ghostblade Randuin's Omen Disabled All the other item-actives are disabled Interrupted by N/A Consumables Usable Spells Usable Barrier Clarity Cleanse Exhaust Ghost Heal Ignite Smite Disabled Flash Teleport Recall Hexflash Interrupted by N/A Interrupted by Death, unless protected by Resurrection ### W — Dark Passage **Champion:** Thresh **Champion ID:** 412 **Ability Slot:** W **Ability Name:** Dark Passage **Effect 1:** Active: Thresh throws his lantern to the target location over 0.5 seconds, lasting for 6 seconds while he remains nearby and granting sight of its surroundings. If Thresh moves too far away from the lantern, it returns back to him immediately. **Effect 2:** Thresh and the first allied champion to come near the lantern are granted a shield for 4 seconds. An ally can select the lantern while in proximity of it, dashing to Thresh and gaining the shield. **Scaling:** - **Shield Strength:** 50 / 70 / 90 / 110 / 130 + 2 per Soul collected **Effect 3:** An ally cannot select the lantern while immobilized, grounded, or silenced. The lantern will not expire from Thresh moving too far away if he is dashing with Deathly Leap. **Cost:** 50 / 55 / 60 / 65 /
```

### Chunk 969 **← ENCONTRADO**

- Source: `champion_abilities_26.19.md`
- Index: `969`
- Palabras: `300`

```text
the shield. **Scaling:** - **Shield Strength:** 50 / 70 / 90 / 110 / 130 + 2 per Soul collected **Effect 3:** An ally cannot select the lantern while immobilized, grounded, or silenced. The lantern will not expire from Thresh moving too far away if he is dashing with Deathly Leap. **Cost:** 50 / 55 / 60 / 65 / 70 MANA **Cooldown:** 21 / 20 / 19 / 18 / 17 seconds **Technical data:** Targeting: Location | Cast time: none | Target range: 950 **Notes:** The dashing ally will track Thresh if he changes locations. They will dash to Thresh's previous location if he is too far away or moves beyond 2200 units. The lantern is considered a unit and can be targeted by an allied Teleport, Leap Strike, Shunpo, and Safeguard. It is untargetable to enemies. The lantern blocks pathing of units like minions and champions. The lantern's duration and maximum leash range are each displayed as a circle on the ground. Thresh will gain Dark Passage's shield from moving out of leash range of the lantern. When the lantern returns to Thresh, the first ally champion to come in contact with Thresh while he has Dark Passage's shield will also gain a shield as long as no other ally has the shield. Dark Passage is special cased to trigger Guardian. ### E — Flay **Champion:** Thresh **Champion ID:** 412 **Ability Slot:** E **Ability Name:** Flay **Effect 1:** Passive: Thresh's basic attacks are empowered to deal bonus magic damage, with the AD ratio increasing over 10 seconds without basic attacking enemies. **Scaling:** - **Minimum Bonus Magic Damage:** 1.7 per Soul collected + 0% AD - **Maximum Bonus Magic Damage:** 1.7 per Soul collected + 90% AD / 120% AD / 150% AD / 180% AD / 210% AD
```

### Chunk 970

- Source: `champion_abilities_26.19.md`
- Index: `970`
- Palabras: `300`

```text
Passive: Thresh's basic attacks are empowered to deal bonus magic damage, with the AD ratio increasing over 10 seconds without basic attacking enemies. **Scaling:** - **Minimum Bonus Magic Damage:** 1.7 per Soul collected + 0% AD - **Maximum Bonus Magic Damage:** 1.7 per Soul collected + 90% AD / 120% AD / 150% AD / 180% AD / 210% AD **Effect 2:** Active: Thresh sweeps his chain across the ground in a broad line and a radius around him, starting behind him and towards the target direction. Enemies hit are dealt magic damage and knocked 200 units in the target direction, and then are slowed for 1 second. **Scaling:** - **Magic Damage:** 65 / 110 / 155 / 200 / 245 + 60% AP - **Slow:** 20% / 25% / 30% / 35% / 40% **Cost:** 60 / 65 / 70 / 75 / 80 MANA **Cooldown:** 13 / 12.25 / 11.5 / 10.75 / 10 seconds **Technical data:** Targeting: Direction | Damage type: MAGIC_DAMAGE | Cast time: 0.3889 **Notes:** Flay's effects start at the start of the cast time. Thresh can cast other spells once the cast time completes, but remains unable to attack and move and use mobility spells (such as Flash) until the chain completed its way entirely. Applies area damage on the ability and deals proc damage on the enhanced basic attack. The knockback's airborne debuff is set to last longer than the forced movement, but gets removed as soon as the forced movement from Flay ends or is overridden by another. Flay's passive's buff icon changes colors depending on charge level. At 100%, Thresh's scythe will glow green and a sound effect will play. 0 - 50% 50 - 75% 75% - 100% 100% Runaan's Hurricane's Wind's Fury will apply Flay's passive to each enemy
```

### Configuración 300/80

### Chunk 1056

- Source: `champion_abilities_26.19.md`
- Index: `1056`
- Palabras: `300`

```text
direction until the missile is fired. This prevents the enemy from knowing where exactly Thresh is aiming at before the cast animation is complete. Death Sentence triggers on-cast effects (such as Spellblade and triggering Force Pulse's passive) once at the start of the cast, and once at the end of the cast. It may trigger on-cast effects a third time when casting Deathly Leap. This is because a separate spell is cast to prevent Thresh from facing towards the target direction immediately, which is (incorrectly) flagged to trigger on-cast effects.(bug) Type Cast time Attacking Disabled Abilities Disabled Movement Disabled Items Usable Shurelya's Battlesong Youmuu's Ghostblade Randuin's Omen Disabled All the other item-actives are disabled Interrupted by N/A Consumables Usable Spells Usable Barrier Clarity Cleanse Exhaust Ghost Heal Ignite Smite Disabled Flash Teleport Recall Hexflash Interrupted by N/A Interrupted by Death, unless protected by Resurrection ### W — Dark Passage **Champion:** Thresh **Champion ID:** 412 **Ability Slot:** W **Ability Name:** Dark Passage **Effect 1:** Active: Thresh throws his lantern to the target location over 0.5 seconds, lasting for 6 seconds while he remains nearby and granting sight of its surroundings. If Thresh moves too far away from the lantern, it returns back to him immediately. **Effect 2:** Thresh and the first allied champion to come near the lantern are granted a shield for 4 seconds. An ally can select the lantern while in proximity of it, dashing to Thresh and gaining the shield. **Scaling:** - **Shield Strength:** 50 / 70 / 90 / 110 / 130 + 2 per Soul collected **Effect 3:** An ally cannot select the lantern while immobilized, grounded, or silenced. The lantern will not expire from Thresh moving too far away if he is dashing with Deathly Leap. **Cost:** 50 / 55 / 60 / 65 /
```

### Chunk 1057 **← ENCONTRADO**

- Source: `champion_abilities_26.19.md`
- Index: `1057`
- Palabras: `300`

```text
shield for 4 seconds. An ally can select the lantern while in proximity of it, dashing to Thresh and gaining the shield. **Scaling:** - **Shield Strength:** 50 / 70 / 90 / 110 / 130 + 2 per Soul collected **Effect 3:** An ally cannot select the lantern while immobilized, grounded, or silenced. The lantern will not expire from Thresh moving too far away if he is dashing with Deathly Leap. **Cost:** 50 / 55 / 60 / 65 / 70 MANA **Cooldown:** 21 / 20 / 19 / 18 / 17 seconds **Technical data:** Targeting: Location | Cast time: none | Target range: 950 **Notes:** The dashing ally will track Thresh if he changes locations. They will dash to Thresh's previous location if he is too far away or moves beyond 2200 units. The lantern is considered a unit and can be targeted by an allied Teleport, Leap Strike, Shunpo, and Safeguard. It is untargetable to enemies. The lantern blocks pathing of units like minions and champions. The lantern's duration and maximum leash range are each displayed as a circle on the ground. Thresh will gain Dark Passage's shield from moving out of leash range of the lantern. When the lantern returns to Thresh, the first ally champion to come in contact with Thresh while he has Dark Passage's shield will also gain a shield as long as no other ally has the shield. Dark Passage is special cased to trigger Guardian. ### E — Flay **Champion:** Thresh **Champion ID:** 412 **Ability Slot:** E **Ability Name:** Flay **Effect 1:** Passive: Thresh's basic attacks are empowered to deal bonus magic damage, with the AD ratio increasing over 10 seconds without basic attacking enemies. **Scaling:** - **Minimum Bonus Magic Damage:** 1.7 per Soul collected + 0% AD - **Maximum Bonus Magic
```

### Chunk 1058

- Source: `champion_abilities_26.19.md`
- Index: `1058`
- Palabras: `300`

```text
shield will also gain a shield as long as no other ally has the shield. Dark Passage is special cased to trigger Guardian. ### E — Flay **Champion:** Thresh **Champion ID:** 412 **Ability Slot:** E **Ability Name:** Flay **Effect 1:** Passive: Thresh's basic attacks are empowered to deal bonus magic damage, with the AD ratio increasing over 10 seconds without basic attacking enemies. **Scaling:** - **Minimum Bonus Magic Damage:** 1.7 per Soul collected + 0% AD - **Maximum Bonus Magic Damage:** 1.7 per Soul collected + 90% AD / 120% AD / 150% AD / 180% AD / 210% AD **Effect 2:** Active: Thresh sweeps his chain across the ground in a broad line and a radius around him, starting behind him and towards the target direction. Enemies hit are dealt magic damage and knocked 200 units in the target direction, and then are slowed for 1 second. **Scaling:** - **Magic Damage:** 65 / 110 / 155 / 200 / 245 + 60% AP - **Slow:** 20% / 25% / 30% / 35% / 40% **Cost:** 60 / 65 / 70 / 75 / 80 MANA **Cooldown:** 13 / 12.25 / 11.5 / 10.75 / 10 seconds **Technical data:** Targeting: Direction | Damage type: MAGIC_DAMAGE | Cast time: 0.3889 **Notes:** Flay's effects start at the start of the cast time. Thresh can cast other spells once the cast time completes, but remains unable to attack and move and use mobility spells (such as Flash) until the chain completed its way entirely. Applies area damage on the ability and deals proc damage on the enhanced basic attack. The knockback's airborne debuff is set to last longer than the forced movement, but gets removed as soon as the forced movement from Flay ends or is overridden by another. Flay's passive's buff icon
```

## 7. Criterio de selección

La comparación mostró diferencias claras entre las configuraciones probadas:

- `200/40` produjo la mayor fragmentación del corpus, con **2099 chunks**. En habilidades complejas, como la E de Thresh, la información relevante quedó repartida entre más fragmentos.
- `400/80` redujo el número total a **1049 chunks** y conservó mejor habilidades largas dentro de una sola ventana, pero en varios casos mezcló demasiada información distinta dentro del mismo chunk, especialmente entre habilidades y objetos vecinos.
- `300/60` produjo **1400 chunks** y mostró un equilibrio adecuado entre ambos extremos. Conservó suficiente contexto en habilidades cortas y complejas, mantuvo continuidad mediante el overlap y redujo la mezcla excesiva de conceptos observada con chunks de 400 palabras.

También se comparó el efecto del overlap manteniendo fijo `chunk_size = 300`:

- `300/40` mostró menor redundancia, pero mayor riesgo de cortes entre partes relacionadas.
- `300/80` aumentó la continuidad, pero también la repetición de contenido entre chunks.
- `300/60` ofreció un punto intermedio adecuado para este corpus.

Por estas razones se seleccionó `chunk_size = 300` y `overlap = 60` como configuración final para la etapa de chunking.

## 8. Configuración seleccionada

```text
chunk_size = 300
overlap = 60
chunks generados = 1400
```

La configuración 300/60 fue seleccionada después de comparar distintos tamaños de chunk y distintos valores de overlap. Las pruebas incluyeron habilidades cortas, habilidades complejas, transiciones entre contenido y objetos del corpus.

Esta configuración mostró un equilibrio adecuado entre preservación de contexto y fragmentación, evitando tanto chunks excesivamente pequeños como chunks que mezclaran demasiados conceptos diferentes.