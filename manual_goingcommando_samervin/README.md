# Ratchet and Clank: Going Commando

Manual version: Not set yet

Work in progress!

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
- Weapon mods are not locations and thus Platinum Bolts are not required. You may purchase weapon mods freely, as long as you have enough Platinum Bolts both in-game and in-Archipelago to do so.
- There are 24 Weapons, but many of them are ineffective in most fights. Thus, a subset are tagged as Combat Weapons, as a way to gate fight logic. Additionally, a small number are classified as Power Weapons, required for many late-game planets and a handful of other difficult locations.
- The bike race on Joba is open even if you do not have the Biker Helmet.
- The Levitator works even if you do not have Clank.
- Wrench Ninja II logically requires Aranos access for its wrench upgrade. (Once you have the second wrench upgrade, you cannot lose it, even if you later go to Tabora.)

Things not (yet?) included:

- Omniwrench is not an item, thus it is in logic at all times
- Regular movement abilities are not items, thus they are in logic at all times
- Vendor items are not locations and thus you are not required to buy any weapons
- Weapon mods are not locations and thus you are not required to buy any weapon mods
- Minigames (arena battles, ship fights, etc.) are not locations unless they grant coordinates, inventory items, or a Platinum Bolt or skill point. This makes e.g. many arena battles and hoverbike races fully optional.
- An alternate victory condition, like Platinum Bolt Hunt

Bugs:

- Some missions and items will be missing or already appear completed depending on the items you have. For example, if you already have the coordinates for Tabora, you cannot board the train or fight the boss on Siberius. For these locations, simply complete the objective as much as you can before manually marking it as complete.
- The Heli-Pack is required to make Clank appear on your back. If you find the Thruster-Pack first, you'll have to give yourself both, then die or reload your save.
- The Hydro-Pack works in-game even if you don't have the item listed in your inventory. Whoops! There are no locations where it's meaningful, so feel free to use it to save time.
- For certain items and locations, you have to die, or save and reload, in order to get the game to recognize them properly. Clank is the most obvious example, mentioned above. The secret Oozla boss may require a similar death/reload.

Weapon damage values (from [TCRF](https://tcrf.net/Proto:Ratchet_%26_Clank:_Going_Commando/September_4,_2003_build/Debug_mode#WEAPONS)):
- Wrench: 1 -> 2 -> either 4 or 8, hard to tell
- Lancer: 0.5 -> 0.67
- Gravity Bomb: 4 -> 8 (displayed differently on the wiki for some reason)
- Chopper: 1 -> 2
- Blitz Gun: 3 -> 6
- Pulse Rifle: 10 -> 20
- Miniturret Glove: 0.7 -> 4.1 (unsure on exact damage calculation)
- Seeker Gun: 6 -> 6 (x3)
- Synthenoid: 0.75 -> 0.5 (this is surprising)
- Lava Gun: 8 -> 4 (unsure on exact damage calculation)
- Bouncer: 6 -> 12 (unsure on exact damage calculation)
- Minirocket Tube: 12 -> 18
- Spiderbot Glove: 0* (damage calculated elsewhere)
- Plasma Coil: 18 -> 60 (this seems high, unsure on exact damage calculation)
- Hoverbomb Gun: 30 -> 30 (x5)
- Sheepinator: 0*
- Shield Charger: 1 -> 5
- Bomb Glove: 2
- Visibomb Gun: 6
- Decoy Glove: 0*
- Tesla Claw: 2 (unsure on exact damage calculation)
- Walloper: Not listed (but it's not high)
- Zodiac: 100
- R.Y.N.O. II: 100
- Clank Zapper: 16 -> 20

Roughly divided into tiers, these are:
- No damage or major asterisks: Spiderbot, Sheepinator, Visibomb Gun, Decoy Glove
- Low damage: Wrench, Lancer (100/200), Chopper (35/70), Shield Charger, Bomb Glove (70), Tesla Claw (600?), Walloper
- Medium damage: Gravity Bomb (32/64), Blitz Gun (120/240), Miniturret Glove (???), Seeker Gun (150/550), Synthenoid (???), Lava Gun (???)
- High damage: Pulse Rifle (80/160), Bouncer (???), Minirocket Tube (240/360), Plasma Coil (150/???), Hoverbomb Gun (300/1500), Clank Zapper (???)
- Extreme damage: Zodiac (400), R.Y.N.O. II (10000)

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
