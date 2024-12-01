# Ratchet and Clank: Going Commando

Manual version: Not set yet

Work in progress!

TODOs:

- Fill out all location access logic!
- Confirm whether bugs from RaC persist
- Check precise handling of Weapon Envy in a first playthrough
- Check what happens if you get wrench upgrades out of order
- Unlike RaC, GC is perfectly happy to spawn you at a continue point when you save and reload, rather than always at your ship. Be sure you have the items you logically need, or be prepared to cheat!
    - This is annoying for a lot of reasons, including "softlock" prevention, so I am modifying the logic a little bit. For missions marked with an asterisk * you may use the item that you actually receive in order to return to your ship, because saving and loading would otherwise force you to be stuck. Treat this as though it was a simple teleporter back to your ship and do not collect anything else using your not-logically-earned item, such as the Platinum Bolt requiring the Tractor Beam on Oozla.
        - Yes, this means that once you find the vanilla glider on Tabora, you have no choice but to collect the vanilla Platinum Bolt at the end of the path. Just ignore it and mark that location as collected once you acquire the Archipelago glider.
- Sometimes, for reasons unknown, you have to save and reload in order to get the game to recognize your items properly. This applies to the secret Oozla boss, Clank backpacks, and possibly others.
- The secret Oozla boss can be defeated with just the wrench. It takes over 20 minutes to do with no wrench upgrades, which is thoroughly unfun. It takes about 6 minutes to do with the third wrench upgrade, which might be fine, but the biggest hurdle is having a low health/armor bar.
- I have a new category, Combat Weapon, as a way to gate fight logic. Most weapons are combat weapons. There may need to be a Power Weapon category later.
- The Heli-Pack seems to be required to make Clank show up. If you don't have Clank, you can grant yourself the Heli-Pack, then die or reload your save.
- The Hydro-Pack works even if you don't have the item listed in your inventory. Whoops!
- The Heli-Pack/Thruster-Pack is logically required to complete Siberius, because if you complete Siberius before Tabora, you'll be taken to Tabora and need Clank to get out of the underground tunnels. (If you unlock Tabora before Siberius, you won't actually be able to fight the thief on Siberius, so just get to the convoy to "win".)

Logical notes:

- [Incomplete] The RYNO II is listed as logically required for the final boss. This is intentional, as it increases the likelihood of going to Yeedil in a middle of a run instead of only at the end, and it makes go mode more clear. It also works around [unconfirmed] ammo bugs, see below.
- You are assumed to have all your regular moves and Omniwrench available, as well as infinite bolts for ammo and NPCs. There is no limit to the experience you may gain for weapons and health.
- [incomplete] The coordinates for the Ship Shack, Grelbin, and Yeedil do not have corresponding cheat codes. Thus, access to these levels requires both the Archipelago coordinates as well as access to the vanilla location where those coordinates are granted (on Notak, Smolg, and Grelbin respectively).
- You may mark the "Nano to the max" skill point as complete once you have all 10 Nanotech Boosts. You do not need to fully upgrade your health.
- [unsure] You may mark the Weapon Envy skill point as complete once you have all weapons (do you need Clank Zapper?) and all 40 Platinum Bolts (do you need all weapon mod shops?). You do not need to fully upgrade all weapons.
- Challenge Mode is not intended or required. [unconfirmed] Megaweapons do not unlock anything in the base game and are not included here. The Clank Zapper is normally only available in Challenge Mode and is [unconfirmed] required for the Weapon Envy skill point, but can be granted early.
- The Special menu items normally locked behind skill points are not locations, thus skill point items are not required

Things not (yet?) included:

- Omniwrench is not an item, thus it is in logic at all times
- Regular movement abilities are not items, thus they are in logic at all times
- Vendor items are not locations and thus you are not required to buy any weapons
- [unsure] Weapon mods are not locations and thus you are not required to buy any weapon mods
- Minigames (arena battles, ship fights, etc.) are not locations unless they grant coordinates, inventory items, or a Platinum Bolt or skill point. This makes e.g. many arena battles and hoverbike races fully optional.
- An alternate victory condition, like Platinum Bolt Hunt

Bugs:

- [unconfirmed] Ammo bugs
- [unconfirmed] Thruster-Pack glide bug (if you haven't saved Clank yet)
- [unconfirmed] Items disappearing from the world if you have already collected them

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
- Low damage: Wrench, Lancer, Chopper, Shield Charger, Bomb Glove, Tesla Claw, Walloper
- Medium damage: Gravity Bomb, Blitz Gun, Miniturret Glove, Seeker Gun, Synthenoid, Lava Gun
- High damage: Pulse Rifle, Bouncer, Minirocket Tube, Plasma Coil, Hoverbomb Gun, Clank Zapper
- Extreme damage: Zodiac, R.Y.N.O. II

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
