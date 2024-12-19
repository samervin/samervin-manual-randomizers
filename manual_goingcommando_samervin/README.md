# Ratchet and Clank: Going Commando

- Manual version: manual_stable_20241119
- Item count: 67 unique, 115 total
- Location count: 123 total

By default, the goal is to defeat the Mutant Protopet. However, you may change the goal in the YAML to simply collecting 30 of the 40 available Platinum Bolts.

Logical notes:

- Unlike RaC, GC is perfectly happy to spawn you at a continue point when you save and reload, rather than always at your ship. This can cause "softlocks" if you interpret the Manual logic strictly, so I am modifying the logic a little bit. For missions marked with an asterisk * you may use the item that you actually receive in order to return to your ship, because you would otherwise be stuck even after saving and loading. Treat this as though it was a simple teleporter back to your ship and do not collect anything else using your not-logically-earned item, such as the Platinum Bolt requiring the Tractor Beam on Oozla.
    - Yes, this means that once you find the vanilla glider on Tabora, you have no choice but to collect the vanilla Platinum Bolt at the end of the path. Ignore it and mark that location as collected once you acquire the Archipelago glider.
- Either the Heli-Pack/Thruster-Pack or the Tabora coordinates are logically required to complete Siberius, because if you complete Siberius before unlocking Tabora, you'll be taken to Tabora and need Clank to get out of the underground tunnels. (If you unlock Tabora before Siberius, you won't actually be able to fight the thief on Siberius, so just get to the convoy to "win".)
- Similarly, either the Infiltrator and Levitator or the Aranos coordinates are required to complete Boldan, because if you complete Boldan before unlocking Aranos, you'll be taken to Aranos and need those items to turn off the forcefield. (If you unlock Aranos before Boldan, finding Mr. Fizzwidget doesn't do anything in-game.)
- The RYNO II is listed as logically required for the final boss. This is intentional, as it (slightly) increases the likelihood of going to Yeedil in a middle of a run instead of only at the end, and it makes go mode more clear.
- You are assumed to have all your regular moves and Omniwrench available, as well as infinite bolts for ammo and NPCs. There is no limit to the experience you may gain for weapons and health.
- The coordinates for the Ship Shack, Grelbin, and Yeedil do not have corresponding cheat codes. Thus, access to these levels requires both the Archipelago coordinates as well as access to the vanilla location where those coordinates are granted (on Notak, Smolg, and Grelbin respectively).
- You may mark the "Nano to the max" skill point as complete once you have all 10 Nanotech Boosts. You do not need to fully upgrade your health.
- You may mark the Weapon Envy skill point as complete once you have all 24 weapons. You do not need to fully upgrade any weapons.
- Challenge Mode is not intended or required. Megaweapons do not unlock anything in the base game and are not included here. The Clank Zapper is normally only available in Challenge Mode, but can be granted early.
- The Special menu items normally locked behind skill points are not locations, thus skill point items are not required.
- Weapon mods are not locations. You may purchase weapon mods freely, as long as you have enough Platinum Bolts both in-game and in-Archipelago to do so.
- There are 24 Weapons, but many of them are ineffective in most fights. Thus, a subset are tagged as Combat Weapons, as a way to gate fight logic. Additionally, a small number are classified as Power Weapons, required for many late-game planets and a handful of other difficult locations. See below for the list.
- The bike race on Joba is open even if you do not have the Biker Helmet.
- The Levitator works even if you do not have Clank.
- Wrench Ninja II logically requires Aranos access for its wrench upgrade. (Once you have the second wrench upgrade, you cannot lose it, even if you later go to Tabora.)

Things not (yet?) included:

- Omniwrench is not an item, thus it is in logic at all times
- Regular movement abilities are not items, thus they are in logic at all times
- Vendor items are not locations and thus you are not required to buy any weapons
- Weapon mods are not locations and thus you are not required to buy any weapon mods
- Minigames (arena battles, ship fights, etc.) are not locations unless they grant coordinates, inventory items, or a Platinum Bolt or skill point. This makes e.g. many arena battles and hoverbike races fully optional.

Bugs:

- Some missions and items will be missing or already appear completed depending on the items you have. For example, if you already have the coordinates for Tabora, you cannot board the train or fight the boss on Siberius. For these locations, simply complete the objective as much as you can before manually marking it as complete.
- The Heli-Pack is required to make Clank appear on your back. If you find the Thruster-Pack first, you'll have to give yourself both, then die or reload your save.
- The Hydro-Pack works in-game even if you don't have the item listed in your inventory. Whoops! There are no locations where it's meaningful, so feel free to use it to save time.
- For certain items and locations, you have to die, or save and reload, in order to get the game to recognize them properly. Clank is the most obvious example, mentioned above. The secret Oozla boss may require a similar death/reload.

I used weapon damage values from [TCRF](https://tcrf.net/Proto:Ratchet_%26_Clank:_Going_Commando/September_4,_2003_build/Debug_mode#WEAPONS) plus my own experience to create weapon tiers:

- Not considered in generic fight logic due to extremely low damage or difficult usage: Spiderbot Glove, Sheepinator, Shield Charger, Visibomb Gun, Decoy Glove, Walloper
- Combat weapons, required for low-to-medium difficulty combat: Lancer, Gravity Bomb, Chopper, Blitz Gun, Miniturret Glove, Seeker Gun, Synthenoid, Lava Gun, Bomb Glove, Tesla Claw, Zodiac, Clank Zapper
- Power weapons, required for high difficulty combat: Pulse Rifle, Bouncer, Minirocket Tube, Plasma Coil, Hoverbomb Gun, R.Y.N.O. II
- Ranged weapons, required for a small number of specific encounters: Lancer, Pulse Rifle, Seeker Gun, Minirocket Tube, Plasma Coil, Hoverbomb Gun, R.Y.N.O. II

## Magic Combos

Source: https://creepnt.stream/rc/rccombo.html

In the pause menu, hold L1 + R2 and press the code below.

Weapons

- Omniwrench: → ↑ ↑ ↓ ← ↑ ↑ ↓ ↓ ↓ ↓ □ ↑ ← ↓ ← ← ↑ ↓ ←
- Lancer: → ↓ ↓ → ○ ← → → → ↓ ↓ → ○ ← → → → ↓ ↓ →
- Gravity Bomb: ↑ ← ↓ ○ ○ ← ↓ ↓ ↓ □ ↓ □ ← ← ↑ ← ← ↑ ○ →
- Chopper: ↑ ↓ ↑ ↓ ↓ □ ← ← ↑ ← ← → → ← ← → → ○ → →
- Seeker Gun: ↓ ↓ → ← ↓ ↑ ○ ↓ → ○ → → ↑ ↓ ↑ ○ → ↑ ↓ ←
- Pulse Rifle: □ ○ ○ □ □ ↑ □ → ↑ □ → ↑ □ ← ← □ ○ ↑ ← ○
- Miniturret Glove: ↓ ← → ↓ ← □ ○ ← ↓ ↓ → ○ → ↑ □ ○ ← ← → ↑
- Blitz Gun: ← → ↑ → ↓ ← ↓ → ← ↑ ↓ ← ↓ □ □ ← ○ → □ ↓
- Shield Charger: → ← □ ← □ ↓ ← ↓ ○ → □ ↓ ← ↑ ↑ ← ○ → □ ↓
- Synthenoid: □ → ← ↓ □ ← ○ ← ← ○ ← ↓ → ○ → □ → ↑ ○ ↑
- Lava Gun: ○ ↓ → □ ↑ → → → ↓ □ → ○ ← □ ← ← ← □ → ↓
- Bouncer: □ → ○ ↑ ← → → → → ↑ → ↑ ↑ ○ ← → ↓ □ □ →
- Minirocket Tube: ○ → → ○ ↓ ↓ ↑ → □ ○ ↓ ↑ ↑ ↑ □ ↓ → → □ ○
- Plasma Coil: → ← ↑ ↓ ↑ ↓ □ ← → ↑ ○ ← ↑ □ ↑ → ○ ← → ←
- Hoverbomb Gun: ↑ □ ↓ ↓ ↓ ○ ○ ↑ ← → ← ○ → ← □ ○ ↑ → ↓ ←
- Spiderbot Glove: ○ ○ ↑ □ ↑ ← ↓ □ ○ ↑ ← → → ○ ○ → → □ ↑ ←
- Sheepinator: ↓ ↑ □ ↑ ↑ ↓ □ □ ○ ↓ ← ↑ → ← → → ○ ○ ← ←
- Tesla Claw: □ ↑ ← ← □ ↓ ↓ ○ ↓ → ○ ← ○ ↑ ↑ ↓ ↑ ← □ □
- Bomb Glove: → ← ↑ → ↑ ↑ ↑ → □ ↓ ○ ← ○ ↓ □ → ↓ ← → ↑
- Walloper: ← □ □ ○ → ○ → □ → ○ → ↑ ↑ □ ← → ○ ↓ ↓ →
- Visibomb Gun: □ → ↓ ↓ ← ↓ → → □ ○ ○ ← ↓ → ← → □ → ↓ ↓
- Decoy Glove: → ○ ← → → ○ □ → ↑ □ ← ↓ ↓ → ○ ↓ □ ← → □
- Zodiac: ○ ↑ ↓ ↓ ↑ → ↑ ← □ ↑ → ← ← ← □ ↓ ○ ↑ → ↓
- R.Y.N.O. II: □ ↑ → □ → □ → → → ← □ ↑ ← ↓ □ → → ← ↑ →
- Clank Zapper: ← ↑ □ ↑ ← → → ← ← □ ↑ ↓ ← ○ □ ○ ↑ ← ← ○

Gadgets

- Swingshot: ← → ○ ← ○ ↑ → ↓ ↓ ↑ □ ↓ ← □ ↑ ← → → ○ ↑
- Dynamo: ○ → ○ → □ ↓ → ↓ ← □ ○ → ↓ □ → ↓ ↑ ↓ □ →
- Thermanator: ← ↑ → □ ↓ □ ○ ↑ ↑ ○ ← ← ↓ ↓ □ □ → → ← ↓
- Tractor Beam: ↓ ↓ □ ← ← → ← → ○ → □ ↓ → ○ ↓ → ↓ ↓ □ ←
- Hypnomatic: ← ○ ↑ ↓ ○ ← ← → ↓ → ○ ↓ □ → → □ ↑ □ ↑ ○
- Heli-Pack: ○ ← → □ □ ↑ ← → ↑ ↑ ↑ ↓ ↓ → ← ↓ ○ ↑ → ←
- Thruster-Pack: □ → ← □ □ → □ ↑ ○ ○ ← ← ↑ ↑ ○ ← → ↑ → □
- Grind Boots: ↑ ↑ → ← □ ↓ ○ ○ ← ○ → ← → ↓ ○ ↓ ← ↓ ○ □
- Gravity Boots: ↓ ↑ ↓ ↑ → □ ← ← ○ □ ○ ← → ○ ↑ ← ○ ← ← □
- Charge Boots: → → ← → ↑ ← □ ← → ↓ ← ○ ↑ □ ↑ → □ ← ↑ ↓

Items

- Biker Helmet: ○ □ ↑ → □ ↑ ← □ ↑ ○ ○ ← → ← ↓ → ↑ ↓ ○ →
- Commando Suit: ← □ ↑ → ↑ ↓ → ↓ ↑ ← ← ↓ ← → ↓ → □ □ → ○
- Glider: ↓ □ □ ↑ ○ → ↑ □ ← → ○ □ ↓ → ↓ → ↓ → → ←
- Qwark Statuette: ↑ ↑ → ← → ○ ○ → ↑ ○ → □ ↓ ○ ○ ↓ ← ↑ ↑ ←
- Armor Magnetizer: ↓ ↓ ↑ ↑ ○ □ ↓ ↑ ↓ ↑ ← ↓ ○ □ ↓ □ → ○ ↑ ↓
- Box Breaker: ↓ ← ↑ ↓ ○ → ↓ ○ ↑ ← ← → □ ↑ → ↓ ○ ← ○ □
- Mapper: ↓ → ↓ ← □ ↑ → → ↓ ↑ → ↑ ↓ ↑ → → ← □ □ ↓
- Electrolyzer: ↑ ← ↓ ○ → ← ↑ ↓ ← □ □ → ← ↓ ← → ← ↓ → →
- Infiltrator: ○ ↑ ↓ ↑ ↓ ↓ ○ ← ← ↓ ↓ □ ↑ → ↑ ← □ → → ↑
- Hydro-Pack: ← → ↓ ↑ → ↑ ↑ ↓ □ ← → ↑ → ↑ ↑ ↓ ↑ ↓ ○ ↓
- Levitator: → □ → ↑ ○ ← ↑ ← ↑ □ □ ↓ ↓ ↓ ↑ ○ ↑ ↓ □ →

Planets

- Oozla: → ○ ↓ → ○ ↑ ↑ ↓ → ○ □ □ → ↑ ↑ ○ ↓ □ → □
- Maktar Nebula: ↑ ← ↑ ← □ ↑ ○ ↑ → → ○ ↓ → → ○ ○ □ ○ ↓ ↑
- Endako: ← ↓ ↓ ← ↑ ← □ → ← ← ↑ ↓ → ↑ ↓ ← ← → ○ ○
- Barlow: → ← ↑ ○ → □ ↑ → □ ↑ ↓ ○ □ ← ← ↓ ↓ ○ ↓ ↓
- Feltzin System: ↓ □ → → □ ○ □ ← □ ↓ ↑ → ○ □ ○ → → ↑ ○ ↑
- Notak: ↓ □ ○ ← ↑ ← → → ← ← → ○ ↑ ○ ↑ ← → □ → ←
- Ship Shack: (no code)
- Siberius: ↓ → ← → ↓ → ← → ↓ → ← → ↓ → ← → ↓ → ← →
- Tabora: ↑ ↓ ← ○ □ ↑ → ← ← → ↑ → → □ ← □ ↓ ↑ → □
- Dobbo: → ↓ ← ← ○ ↓ ○ □ ↑ ↑ → ↑ ↑ ↑ ↓ → ↑ □ → ↑
- Hrugis Cloud: □ ↑ ↑ → ↓ ↑ ○ ↑ ↓ → ↑ ↑ □ ↑ → ↓ ○ ○ □ ←
- Joba: ○ □ ← □ ↑ → ○ → □ ← ← ↓ ○ □ ← ↓ ↓ → → ←
- Todano: □ → ← □ ↓ → ↓ ↑ ○ □ ↓ ← → ← ← ← □ ↓ ○ □
- Boldan: ↑ ↓ □ ↑ ← □ → ↓ ← ← □ ↑ □ ↑ ↓ ↓ □ ← ○ ↓
- Aranos 2: ↓ □ ○ ← ← ↑ → → → ← ↓ ↑ ↑ → ← → ↑ ○ □ ↓
- Gorn: ↑ □ ↑ → ← ○ → ↓ □ ↓ ↑ ↓ ← ← → → → □ ← ○
- Snivelak: ← ↑ ← ↑ ○ ○ → ↑ ↓ ↓ □ ↓ → ○ ↓ □ → ○ ← ↓
- Smolg: ○ ↑ ↓ ↑ ○ ← ← ← ○ ↓ □ ↓ ↑ → ← ○ → ↓ □ →
- Damosel: ○ ↑ ↑ ↑ ← ↑ ↓ ← □ ↓ ← ↓ ← ↓ ○ ○ ↑ ↑ ↓ ○
- Grelbin: (no code)
- Yeedil: (no code)
