# League of Legends — Core Game Mechanics

**Corpus document:** game_mechanics.md  
**Language:** English  
**Scope:** Core Summoner's Rift terminology and stable mechanics used to interpret champion and item data.

> This document is intentionally compact. Champion-specific values, item-specific values, exceptions, and patch-specific changes should be retrieved from the corresponding champion, item, or patch document.

---

## Attack Damage

**Mechanic:** Attack Damage  
**Abbreviation:** AD  
**Category:** Offensive stat

Attack Damage is the stat primarily used by basic attacks and by abilities that include an AD ratio.

- **Base AD** is the champion's innate attack damage, including normal level growth.
- **Bonus AD** is attack damage gained from sources such as items, runes, buffs, or abilities.
- **Total AD** is base AD plus bonus AD.
- An effect written as `60% AD` scales with total AD unless it explicitly says `bonus AD`.

---

## Ability Power

**Mechanic:** Ability Power  
**Abbreviation:** AP  
**Category:** Offensive stat

Ability Power increases effects that contain an AP ratio.

An expression such as `80% AP` means the effect gains an amount equal to 80% of the champion's current Ability Power. AP does not automatically increase every spell; the spell must have an AP scaling in its data.

---

## Armor

**Mechanic:** Armor  
**Category:** Defensive stat

Armor reduces incoming physical damage.

For non-negative Armor, the standard damage multiplier is:

`Physical damage multiplier = 100 / (100 + Armor)`

Example: 100 Armor corresponds to a 0.5 multiplier, so incoming physical damage is reduced by 50% before other applicable modifiers.

Armor reduction and armor penetration can lower the effective Armor used in damage calculation.

---

## Magic Resistance

**Mechanic:** Magic Resistance  
**Abbreviation:** MR  
**Category:** Defensive stat

Magic Resistance reduces incoming magic damage.

For non-negative Magic Resistance, the standard damage multiplier is:

`Magic damage multiplier = 100 / (100 + Magic Resistance)`

Example: 100 Magic Resistance corresponds to a 0.5 multiplier.

Magic resistance reduction and magic penetration can lower the effective resistance used in damage calculation.

---

## Physical Damage

**Mechanic:** Physical Damage  
**Category:** Damage type

Physical damage is normally mitigated by Armor. Many basic attacks and AD-oriented abilities deal physical damage.

Physical damage is distinct from magic damage and true damage, so the target's Armor is the primary resistance relevant to it.

---

## Magic Damage

**Mechanic:** Magic Damage  
**Category:** Damage type

Magic damage is normally mitigated by Magic Resistance. Many AP-oriented abilities and some item effects deal magic damage.

Magic damage is distinct from physical damage and true damage.

---

## True Damage

**Mechanic:** True Damage  
**Category:** Damage type

True damage normally ignores Armor and Magic Resistance.

Because it does not use those resistances, increasing Armor or Magic Resistance does not directly reduce ordinary true damage. Specific game effects may still modify damage before or after other calculations when explicitly stated.

---

## Ability Haste

**Mechanic:** Ability Haste  
**Abbreviation:** AH  
**Category:** Cooldown stat

Ability Haste increases how frequently abilities affected by haste can be cast.

The standard relationship is:

`Cooldown reduction fraction = Ability Haste / (100 + Ability Haste)`

Equivalent cooldown multiplier:

`New cooldown = Base cooldown × 100 / (100 + Ability Haste)`

Examples:

- 0 Ability Haste → 100% of the original cooldown.
- 50 Ability Haste → about 66.7% of the original cooldown.
- 100 Ability Haste → 50% of the original cooldown.

Some cooldowns are static or explicitly marked as not affected by Ability Haste.

---

## Cooldown

**Mechanic:** Cooldown  
**Category:** Ability mechanic

A cooldown is the waiting period before an ability or effect can normally be used again.

Cooldown values can vary by ability rank. Ability Haste modifies cooldowns only when the ability or effect is allowed to benefit from haste.

A **static cooldown** is a cooldown interval that is specifically designed not to be reduced by normal Ability Haste.

---

## Attack Speed

**Mechanic:** Attack Speed  
**Abbreviation:** AS  
**Category:** Offensive stat

Attack Speed determines the frequency of basic attacks.

Champion data commonly distinguishes:

- **Base Attack Speed**
- **Attack Speed Ratio**
- **Attack Speed growth**
- **Bonus Attack Speed**

Attack Speed growth and bonus Attack Speed interact with the champion's attack speed ratio. Champion-specific passives can modify this behavior, so the champion's own mechanics take precedence.

---

## Critical Strike

**Mechanic:** Critical Strike  
**Abbreviation:** Crit  
**Category:** Offensive mechanic

Critical Strike Chance is the probability that an eligible basic attack or effect critically strikes.

A standard critical strike deals more damage than a normal basic attack. Some champions and items modify critical strike damage, convert critical strike chance into another effect, or allow abilities to critically strike under special rules.

If an ability says it can critically strike, use that ability's own critical-strike rules rather than assuming ordinary basic-attack behavior.

---

## Attack Range

**Mechanic:** Attack Range  
**Category:** Combat range

Attack Range is the distance from which a champion can issue a normal basic attack against a valid target.

Champions are broadly classified as melee or ranged, but individual abilities and empowered attacks can temporarily use ranges different from the champion's normal attack range.

---

## Movement Speed

**Mechanic:** Movement Speed  
**Abbreviation:** MS  
**Category:** Mobility stat

Movement Speed determines how quickly a unit moves across the map.

Effects may grant:

- flat Movement Speed,
- percentage Movement Speed,
- bonus Movement Speed,
- temporary increases or reductions.

League applies internal rules and soft caps to very high or very low movement speeds. When an ability gives a specific movement-speed formula or cap, that specific rule takes precedence.

---

## Lethality

**Mechanic:** Lethality  
**Category:** Physical penetration stat

Lethality is a flat Armor penetration stat intended to increase physical damage against targets by lowering the Armor considered for the attack or effect.

It applies to physical damage calculations and does not directly penetrate Magic Resistance.

---

## Armor Penetration

**Mechanic:** Armor Penetration  
**Category:** Physical penetration stat

Armor Penetration reduces the amount of enemy Armor considered when calculating physical damage.

It can appear as flat penetration or percentage penetration. Different effects can also reduce a target's Armor directly. These mechanics are not interchangeable, even though all can increase physical damage dealt to armored targets.

---

## Magic Penetration

**Mechanic:** Magic Penetration  
**Category:** Magic penetration stat

Magic Penetration reduces the amount of enemy Magic Resistance considered when calculating magic damage.

It can appear as flat penetration or percentage penetration. Magic Resistance reduction is a related but distinct mechanic.

---

## Life Steal

**Mechanic:** Life Steal  
**Category:** Sustain stat

Life Steal restores health from eligible basic-attack damage according to the effect's rules.

It is primarily associated with basic attacks and effects specifically classified to apply Life Steal. Ability damage does not automatically benefit from Life Steal.

---

## Omnivamp

**Mechanic:** Omnivamp  
**Category:** Sustain stat

Omnivamp heals the source for a portion of eligible damage dealt.

Its effectiveness can depend on the type of damage or effect, and some effects may apply reduced healing to area-of-effect or non-champion damage. When an item or champion specifies its own healing restrictions, those rules take precedence.

---

## Healing

**Mechanic:** Healing  
**Category:** Sustain mechanic

Healing restores missing Health up to the unit's normal maximum Health unless another mechanic explicitly allows excess healing or bonus Health.

Healing can be modified by effects such as Heal and Shield Power, champion abilities, item passives, or healing-reduction effects.

---

## Shield

**Mechanic:** Shield  
**Category:** Defensive mechanic

A shield absorbs eligible incoming damage before Health is lost.

Shields may:

- absorb all damage types or only specific types,
- last for a fixed duration,
- decay over time,
- scale with Health, AD, AP, resistances, or other stats.

Different shields follow their own stacking and replacement rules when specified.

---

## Heal and Shield Power

**Mechanic:** Heal and Shield Power  
**Category:** Utility stat

Heal and Shield Power increases eligible healing and shielding performed by the unit.

It does not mean that every source of healing or shielding is affected; individual effects can have exceptions.

---

## Grievous Wounds

**Mechanic:** Grievous Wounds  
**Category:** Healing reduction

Grievous Wounds is a debuff that reduces healing received by the affected unit.

The exact reduction and application conditions should be taken from the current item, champion, or system data when relevant.

---

## Crowd Control

**Mechanic:** Crowd Control  
**Abbreviation:** CC  
**Category:** Control mechanic

Crowd Control is a family of effects that limit a unit's actions or movement.

Common forms include:

- slow,
- root,
- stun,
- knockup,
- knockback,
- fear,
- charm,
- taunt,
- silence,
- suppression,
- sleep,
- nearsight,
- polymorph,
- grounding.

Different crowd-control types have different interaction rules. For example, some displacement effects are not reduced by ordinary Tenacity.

---

## Tenacity

**Mechanic:** Tenacity  
**Category:** Crowd-control resistance stat

Tenacity reduces the duration of eligible crowd-control effects.

Tenacity does not reduce every form of crowd control. Displacements such as knockups and knockbacks, and certain special control effects, can follow separate rules.

---

## Slow

**Mechanic:** Slow  
**Category:** Crowd control

A slow reduces Movement Speed without completely preventing movement.

Slow strength and duration are defined by the individual ability or item. Multiple slows can interact according to League's crowd-control rules rather than simply adding together.

---

## Root

**Mechanic:** Root  
**Category:** Crowd control

A root prevents normal movement for its duration but does not inherently prevent every other action.

The target may still be able to attack or cast some abilities unless another effect also prevents those actions.

---

## Stun

**Mechanic:** Stun  
**Category:** Crowd control

A stun prevents the affected unit from moving, attacking, or normally casting abilities for the duration.

Eligible stun duration can be reduced by Tenacity.

---

## Knockup and Knockback

**Mechanic:** Displacement  
**Common forms:** Knockup, Knockback  
**Category:** Crowd control

Displacements forcibly move or suspend a target.

They are mechanically distinct from ordinary stuns and roots. Their displacement component is generally not shortened by ordinary Tenacity, though an ability can combine a displacement with another control effect.

---

## On-Hit

**Mechanic:** On-Hit  
**Category:** Attack interaction

An on-hit effect is applied when an eligible attack or effect successfully hits a target.

Basic attacks normally apply on-hit effects. Some abilities explicitly apply on-hit effects at full or reduced effectiveness, while others do not.

---

## On-Attack

**Mechanic:** On-Attack  
**Category:** Attack interaction

On-attack effects trigger when an eligible attack is declared or fired, depending on the specific mechanic.

On-attack and on-hit are distinct. An effect can trigger on-attack without being an on-hit effect, and vice versa.

---

## Basic Attack

**Mechanic:** Basic Attack  
**Category:** Combat action

A basic attack is a champion's standard attack against a valid target.

Basic attacks normally use Attack Damage, Attack Speed, Attack Range, and can interact with Critical Strike, Life Steal, on-hit effects, and on-attack effects.

Champion passives can significantly modify normal basic-attack behavior.

---

## Ability Rank

**Mechanic:** Ability Rank  
**Category:** Ability progression

Most basic abilities have five ranks and most ultimate abilities have three ranks, although exceptions exist.

When a value is written as:

`80 / 120 / 160 / 200 / 240`

the values correspond to successive ranks of that ability.

---

## Scaling Ratio

**Mechanic:** Scaling Ratio  
**Category:** Ability calculation

A scaling ratio determines how much a stat contributes to an effect.

Examples:

- `+80% AP` means add 0.8 × Ability Power.
- `+60% bonus AD` means add 0.6 × bonus Attack Damage.
- `+100% AD` normally means add 1.0 × total Attack Damage.
- `+5% maximum Health` means the effect scales with the specified unit's maximum Health.

Always identify whose stat the formula refers to: the caster, target, ally, or another defined unit.

---

## Base Damage

**Mechanic:** Base Damage  
**Category:** Ability calculation

Base Damage is the fixed numeric component of an ability before scaling ratios and other modifiers.

For a formula such as:

`100 + 60% AP`

`100` is the base damage and `60% AP` is the scaling component.

---

## Maximum Health and Missing Health

**Mechanic:** Health-based scaling  
**Category:** Ability calculation

Health-based effects can reference different quantities:

- **Maximum Health:** the unit's full current Health capacity.
- **Current Health:** the Health the unit has at that moment.
- **Missing Health:** maximum Health minus current Health.
- **Bonus Health:** Health gained beyond the champion's base Health progression.

These quantities are not interchangeable.

---

## Resource

**Mechanic:** Champion Resource  
**Category:** Ability cost system

Champions can use different resources, including Mana, Energy, Fury, Rage, Heat, or champion-specific resources. Some champions use no conventional resource.

Ability costs must be interpreted using the champion's own resource type.

---

## Mana

**Mechanic:** Mana  
**Category:** Champion resource

Mana is consumed by many champion abilities and regenerates over time.

Maximum Mana, Mana regeneration, and ability Mana costs can scale independently. Some items and effects interact specifically with Mana.

---

## Energy

**Mechanic:** Energy  
**Category:** Champion resource

Energy is a rapidly regenerating resource used by some champions.

Energy users generally have a fixed or champion-specific maximum resource and rely on regeneration or ability mechanics rather than large Mana pools.

---

## Adaptive Force

**Mechanic:** Adaptive Force  
**Category:** Offensive stat conversion

Adaptive Force grants either Attack Damage or Ability Power depending on which conversion is more beneficial for the champion under the game's adaptive-stat rules.

When a source grants Adaptive Force, the resulting stat is not simultaneously granted as both AD and AP.

---

## Melee and Ranged

**Mechanic:** Attack Type  
**Category:** Champion classification

Champions are classified as melee or ranged for many systems.

This classification can affect item effects, runes, damage values, slow values, and other mechanics. An individual ability having long range does not automatically change a champion's melee/ranged classification.

---

## Area of Effect

**Mechanic:** Area of Effect  
**Abbreviation:** AoE  
**Category:** Effect targeting

An Area-of-Effect ability or effect can affect multiple units or an area rather than only one target.

Some healing, damage, vamp, and item mechanics apply different effectiveness to AoE effects.

---

## Projectile

**Mechanic:** Projectile  
**Category:** Ability delivery

A projectile is an effect that travels through game space toward a direction, location, or target.

Projectile abilities can have properties such as speed, width, collision behavior, and spell-shield interactions. Not every ranged ability is a projectile.

---

## Spell Shield

**Mechanic:** Spell Shield  
**Category:** Defensive interaction

A spell shield blocks an eligible incoming hostile spell or spell effect.

Some multi-part abilities have special spell-shield behavior, so the champion ability data should be used when it explicitly marks an interaction as special.

---

## Execute

**Mechanic:** Execute  
**Category:** Damage / kill mechanic

An execute kills a target when the execute condition is satisfied rather than behaving exactly like ordinary damage.

The health threshold and eligible target types are defined by the specific ability or item.

---

## Takedown

**Mechanic:** Takedown  
**Category:** Combat event

A takedown generally refers to receiving credit for a champion kill or assist.

Many champion and item effects trigger from takedowns within a stated time window after participating in damage or combat.

---

## Cooldown Refund

**Mechanic:** Cooldown Refund  
**Category:** Cooldown interaction

A cooldown refund reduces the remaining cooldown of an ability or effect.

A flat refund such as `1 second` removes that amount from the remaining cooldown. Individual mechanics can specify whether the refund itself interacts with Ability Haste.

---

## Summoner's Rift

**Mechanic:** Summoner's Rift  
**Category:** Game mode / map

Summoner's Rift is the primary standard map and game mode used as the scope of this corpus.

Values specific to Arena, ARAM, URF, League Classic, or other modes should not be assumed to apply to Summoner's Rift unless explicitly stated.
