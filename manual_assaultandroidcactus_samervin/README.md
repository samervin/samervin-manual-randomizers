# assault-android-cactus-manual-randomizer

- Manual version: manual_stable_20241119
- Item count: 144 unique items, 171 total
- Location count: 450

- You start with a random android unlocked. You may freely use your primary and secondary weapons, but you may not pick up power-ups.
- Items unlock the ability to use each power-up. This is per-android, so e.g. Cactus may be able to use Shutdown only while Lemon can only use Firepower. There are two copies of each power-up in the pool; the second one does nothing.
- Items unlock the ability to use EX weapons. This is per-android, so e.g. Holly may have access to her Mega Seeker while Peanut must use her drill.
- The entirety of Zone 1 is always open to unlocked androids.
- Accessing levels in other Zones requires that android's Zone Key.
- Accessing 5-4 and 5-5 boss levels both require that android's Boss Key as well as all three powerups.
- If the "campaign_plus" YAML option is enabled, the 25 Campaign+ levels will be open to all androids. Unlike the regular campaign, Zone 1+ requires a key to access.
- You win when you defeat Collider and Medulla with any android by default. You can change the victory condition to defeating Colider and Medulla with _all_ androids, or Collider+ and Medulla+ with any/all androids, in your player YAML.

Not implemented (yet):
- Additional modes: boss rush, daily drive, infinity drive. Boss rush is the most likely by far: another set of 9 locations, perhaps requiring each boss to first be defeated once with any android. Achieving certain layers on infinity drive (e.g. 15 and 25, which have corresponding achievements) may be implemented. Daily drive is unlikely due to obvious restrictions.
- Additional EX options. You could start with the HUD disabled and need to find each android's HUD item. You could start with a virtual player count of 2, 3, or 4 and need to find items to reduce it. I think these might be more trouble than they are worth, but they could be optional for added challenge.
- Achievements as locations. Androids Assemble, Chain Gang, Nothing But Net, Perfection, and Scrambled Eggs all add something new to do.

Not implemented and likely will not be:
- Secondary weapons as items. I don't find it fun to play without dodges, nor do I find it fun to play with dodges but not secondary weapons, as I have autofire enabled. For now, the EX weapons are just a fun addition to a game that doesn't have enough items.
- Keys per-level instead of per-zone. Yes, this would add more items to the game, but at the cost of a significant amount of fiddling with the tracker to see which levels you have available.
