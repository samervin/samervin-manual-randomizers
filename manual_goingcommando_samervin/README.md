# Ratchet and Clank: Going Commando

Manual version: Not set yet

Work in progress!

TODOs:

- Fill out all location access logic!
- Confirm whether bugs from RaC persist
- Check precise handling of Weapon Envy in a first playthrough
- Check what happens if you get wrench upgrades out of order
- Unlike RaC, GC is perfectly happy to spawn you at a continue point when you save and reload, rather than always at your ship. Be sure you have the items you need, or be prepared to cheat!
- Sometimes, for reasons unknown, you have to save and reload in order to get the game to recognize your items properly. This applies to the secret Oozla boss, Clank backpacks, and probably others.
- The secret Oozla boss can be defeated with just the wrench. It takes over 20 minutes to do with no wrench upgrades, which is thoroughly unfun. It takes about 6 minutes to do with the third wrench upgrade, which might be fine, but the biggest hurdle is having a low health/armor bar.
- I have a new category, Combat Weapon, as a way to gate fight logic. Most weapons are combat weapons. There may need to be a Power Weapon category later.

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
