# Ratchet and Clank (PS2)

- Manual version: manual_stable_20241119
- Item count: 57 unique, 96 total
- Location count: 113 total

By default, the goal is to defeat Chairman Drek. However, you may change the goal in the YAML to simply collecting 30 of the 40 available Gold Bolts.

Logical notes:
- The RYNO is listed as logically required for the final boss. This is intentional, as it increases the likelihood of going to Veldin in a middle of a run instead of only at the end, and it makes go mode more clear. It also works around ammo bugs, see below.
- You are assumed to have all your regular moves and Omniwrench available, as well as infinite bolts for ammo and NPCs.

Things not (yet?) included:

- Omniwrench is not an item, thus it is in logic at all times
- Regular movement abilities are not items, thus they are in logic at all times
- Vendor items are not locations and thus you are not expected to buy any weapons
- The RYNO salesman is not a location and thus you are not expected to buy the RYNO
- The Ultra Nanotech (the second tier) is not a location and thus you are not expected to buy it
- The Gold Weapons on Gemlik Base are not locations and thus you are not expected to buy any gold weapons
- The two Goodies menu items you unlock with Skill Points are not items, thus the Skill Points themselves are not in logic
- The two Goodies menu items you unlock with Gold Weapons are not items, thus both Gold Bolt and Gold Weapon items are not in logic
- An alternate victory condition, like Gold Bolt Hunt

Bugs:

- If you use cheat codes to acquire a weapon, ammo for that weapon will not drop from crates, but can be purchased from vendors. However, once you have visited the planet where that weapon is normally purchased from a vendor, you will lose the ability to buy ammo for it (the vendor will offer the weapon for purchase instead) but ammo will start dropping from crates. There are some limited exceptions to these rules, e.g. the Snagglebeast seems to bypass these limitations.
    - The Gadgetron PDA always allows you to buy ammo for weapons you have bought or given yourself.
- If you have the Thruster-Pack but not the Heli-Pack, you will be unable to glide. I didn't discover this until very late in the process of filling out the logic, so there may be a few places that gliding is necessary and not logically accounted for. Give yourself the Heli-Pack if so, and let me know where you needed it!
- If you have the O2 mask before going to Nebula G34, you cannot complete the Clank section, so mark it as completed once it is in-logic.
- If you have the O2 mask before going to Orxon, you cannot complete the two Clank missions, nor can you access the Gold Bolt in the Clank section. Just mark all three as completed once they are in-logic. The elevator that normally goes up from your ship to the second Clank mission will not work, even after completing the Ratchet missions, so the Gold Bolt in the Visibomb tunnel will require making a full loop.
- If you do not have the O2 mask, don't attempt the coolant system on Quartu. You won't be able to complete it, and drowning will freeze the game.
- Neither the Premium Nanotech nor the Ultra Nanotech have any effect if granted via cheat code. You may optionally consider them a license to purchase the corresponding items on Orxon, if you have it unlocked.
- Using an Infobot cheat code usually shows a "Paradox: This message does not exist" message instead of the usual one. This is harmless and the planet is still unlocked.
- Gemlik Base does not check for the O2 mask _or_ the Pilot's Helmet. Neither does Drek's Fleet. The game simply assumes you have these items already.
- Certain items will disappear from the planets if you add them to your inventory before the corresponding mission is complete. For example, Helga won't be at the end of the fitness course on Metropolis if you already own the Swingshot. You won't be softlocked, but the mission checkmark won't complete; just mark the location as completed once you reach the end of the area.


## Magic Combos

Source: https://creepnt.stream/rc/rccombo.html

In the pause menu, hold L1 + R2 and press the code below.

Weapons

- Omniwrench 8000: → □ → ↑ ○ ← ↑ ← ↑ □ □ ↓ ↓ ↓ ↑ ○ ↑ ↓ □ →
- Bomb Glove: → ↑ ↑ ↓ ← ↑ ↑ ↓ ↓ ↓ ↓ □ ↑ ← ↓ ← ← ↑ ↓ ←
- Pyrocitor: ↓ ↑ □ ↑ ↑ ↓ □ □ ○ ↓ ← ↑ → ← → → ○ ○ ← ←
- Blaster: → ○ ↑ ○ → ↑ ← □ → ↑ ↑ ← ← ↓ → □ □ ○ □ ↑
- Glove of Doom: ↑ ↑ → ← □ ↓ ○ ○ ← ○ → ← → ↓ ○ ↓ ← ↓ ○ □
- Mine Glove: → ○ ← → → ○ □ → ↑ □ ← ↓ ↓ → ○ ↓ □ ← → □
- Taunter: □ → ↓ ↓ ← ↓ → → □ ○ ○ ← ↓ → ← → □ → ↓ ↓
- Suck Cannon: ← ↑ □ ↑ ← → → ← ← □ ↑ ↓ ← ○ □ ○ ↑ ← ← ○
- Devastator: ↓ ↓ □ ↓ ↑ → ↓ ← ○ ↓ ← ↑ ○ ○ ← ↓ ← → ↓ ○
- Walloper: □ ↑ ← ← □ ↓ ↓ ○ ↓ → ○ ← ○ ↑ ↑ ↓ ↑ ← □ □
- Visibomb Gun: ← → ○ ← ○ ↑ → ↓ ↓ ↑ □ ↓ ← □ ↑ ← → → ○ ↑
- Decoy Glove: ↑ □ ↓ ↓ ↓ ○ ○ ↑ ← → ← ○ → ← □ ○ ↑ → ↓ ←
- Drone Device: ↓ ↓ → ← ↓ ↑ ○ ↓ → ○ → → ↑ ↓ ↑ ○ → ↑ ↓ ←
- Tesla Claw: ↓ ↑ ↓ ↑ → □ ← ← ○ □ ○ ← → ○ ↑ ← ○ ← ← □
- Morph-o-Ray: ↓ □ □ ↑ ○ → ↑ □ ← → ○ □ ↓ → ↓ → ↓ → → ←
- R.Y.N.O.: □ ○ ○ □ □ ↑ □ → ↑ □ → ↑ □ ← ← □ ○ ↑ ← ○

Gadgets

- Trespasser: ← → ↑ → ↓ ← ↓ → ← ↑ ↓ ← ↓ □ □ ← ○ → □ ↓
- Hydrodisplacer: ↑ ↓ ↑ ↓ ↓ □ ← ← ↑ ← ← → → ← ← → → ○ → →
- Swingshot: → ← ↑ → ↑ ↑ ↑ → □ ↓ ○ ← ○ ↓ □ → ↓ ← → ↑
- Gadgetron PDA: ○ ○ ↑ □ ↑ ← ↓ □ ○ ↑ ← → → ○ ○ → → □ ↑ ←
- Metal Detector: ○ → → ○ ↓ ↓ ↑ → □ ○ ↓ ↑ ↑ ↑ □ ↓ → → □ ○
- Hologuise: □ → ← ↓ □ ← ○ ← ← ○ ← ↓ → ○ → □ → ↑ ○ ↑
- Heli-Pack: ○ ← → □ □ ↑ ← → ↑ ↑ ↑ ↓ ↓ → ← ↓ ○ ↑ → ←
- Thruster-Pack: □ → ← □ □ → □ ↑ ○ ○ ← ← ↑ ↑ ○ ← → ↑ → □
- Hydro-Pack: ← → ↓ ↑ → ↑ ↑ ↓ □ ← → ↑ → ↑ ↑ ↓ ↑ ↓ ○ ↓
- O2 Mask: ← □ ↑ → ↑ ↓ → ↓ ↑ ← ← ↓ ← → ↓ → □ □ → ○
- Sonic Summoner: ↓ → ↓ ← □ ↑ → → ↓ ↑ → ↑ ↓ ↑ → → ← □ □ ↓
- Pilot's Helmet: ↓ ↓ ↑ ↑ ○ □ ↓ ↑ ↓ ↑ ← ↓ ○ □ ↓ □ → ○ ↑ ↓
- Grind Boots: ○ ↓ → □ ↑ → → → ↓ □ → ○ ← □ ← ← ← □ → ↓
- Magneboots: → ← ↑ ↓ ↑ ↓ □ ← → ↑ ○ ← ↑ □ ↑ → ○ ← → ←

Items

- Hoverboard: → ↓ ↓ → ○ ← → → → ↓ ↓ → ○ ← → → → ↓ ↓ →
- Persuader: □ ○ ← ↑ → ↓ ↓ ↑ → ○ ↓ ← ↑ ← ↓ ← ○ ○ → ↓
- Bolt Grabber: ↑ ↑ ↓ □ ↓ ↑ ← → ○ ← ↓ ○ ↑ → ← ↓ □ □ ↓ ↓
- Premium Nanotech: → ← ↑ ○ → □ ↑ → □ ↑ ↓ ○ □ ← ← ↓ ↓ ○ ↓ ↓
- Ultra Nanotech: ↓ □ → → □ ○ □ ← □ ↓ ↑ → ○ □ ○ → → ↑ ○ ↑
- Mapomatic: □ ↑ → ↓ □ □ □ ↑ ↑ ← → □ → → ↓ ↓ ↓ ← → ←
- Zoomerator: ← ○ ↑ ↓ ○ ← ← → ↓ → ○ ↓ □ → → □ ↑ □ ↑ ○
- Raritanium: → ○ ↓ → ○ ↑ ↑ ↓ → ○ □ □ → ↑ ↑ ○ ↓ □ → □
- Codebot: ↑ ← ↑ ← □ ↑ ○ ↑ → → ○ ↓ → → ○ ○ □ ○ ↓ ↑

Planets

- Novalis: □ ○ ← ↑ → ↓ ↓ ↑ → ○ ↓ ← ↑ ← ↓ ← ○ ○ → ↓
- Aridia: ↑ ← ↓ ○ → ← ↑ ↓ ← □ □ → ← ↓ ← → ← ↓ → →
- Kerwan: ← ↑ → □ ↓ □ ○ ↑ ↑ ○ ← ← ↓ ↓ □ □ → → ← ↓
- Eudora: ↑ ↑ □ ← □ ← ○ ← ← □ ○ → ○ → ← ○ ○ ○ → ↑
- Rilgar: ↓ ← → ↓ ← □ ○ ← ↓ ↓ → ○ → ↑ □ ○ ← ← → ↑
- Blarg Station: ↑ ← ↓ ○ ○ ← ↓ ↓ ↓ □ ↓ □ ← ← ↑ ← ← ↑ ○ →
- Umbris: ○ ↑ ↓ ↓ ↑ → ↑ ← □ ↑ → ← ← ← □ ↓ ○ ↑ → ↓
- Batalia: □ ↑ → □ → □ → → → ← □ ↑ ← ↓ □ → → ← ↑ →
- Gaspar: → ← □ ← □ ↓ ← ↓ ○ → □ ↓ ← ↑ ↑ ← ○ → □ ↓
- Orxon: ↓ ↓ □ ← ← → ← → ○ → □ ↓ → ○ ↓ → ↓ ↓ □ ←
- Pokitaru: → ↑ ← ↓ □ ○ → □ → → ↑ → □ ↓ ↓ □ ↑ ○ □ ↑
- Hoven: ○ □ ↑ → □ ↑ ← □ ↑ ○ ○ ← → ← ↓ → ↑ ↓ ○ →
- Gemlik Base: ↑ ↑ → ← → ○ ○ → ↑ ○ → □ ↓ ○ ○ ↓ ← ↑ ↑ ←
- Oltanis: ↓ ← ↑ ↓ ○ → ↓ ○ ↑ ← ← → □ ↑ → ↓ ○ ← ○ □
- Quartu: ○ ↑ ↓ ↑ ↓ ↓ ○ ← ← ↓ ↓ □ ↑ → ↑ ← □ → → ↑
- Kalebo III: □ ↓ ○ ↑ → ○ ← ○ → ← ↑ □ □ ○ ↑ ↓ ↑ ← □ →
- Drek's Fleet: ← □ □ ○ → ○ → □ → ○ → ↑ ↑ □ ← → ○ ↓ ↓ →
- Veldin II: → → ← → ↑ ← □ ← → ↓ ← ○ ↑ □ ↑ → □ ← ↑ ↓
