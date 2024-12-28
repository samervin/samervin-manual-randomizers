# assault-android-cactus-manual-randomizer

- Manual version: manual_stable_20241119
- Item count: 91 unique items, 118 total
- Location count: 226

- You start with a random android unlocked. You may freely use your primary and secondary weapons, but you may not pick up power-ups.
- Items unlock the ability to use each power-up. This is per-android, so e.g. Cactus may be able to use Shutdown only while Lemon can only use Firepower. There are two copies of each power-up in the pool; the second one does nothing.
- Items unlock the ability to use EX weapons. This is per-android, so e.g. Holly may have access to her Mega Seeker while Peanut must use her drill.
- The entirety of Zone 1 is always open to unlocked androids.
- Accessing levels in other Zones requires that android's Zone Key.
- Accessing 5-4 and 5-5 boss levels both require that android's Boss Key as well as all three powerups.
- You win when you defeat Collider and Medulla with any android by default, or all androids if selected in your player YAML.

Not implemented (yet):
- Additional modes: boss rush, daily drive, infinity drive. Boss rush is the most likely by far: another set of 9 locations, perhaps requiring each boss to first be defeated once with any android. Achieving certain layers on infinity drive (e.g. 15 and 25, which have corresponding achievements) may be implemented. Daily drive is unlikely due to obvious restrictions.
- Campaign+ zones. This would effectively double the amount of content in the game, as every campaign level has a corresponding + version. This might be too much of a time sink, but these levels are interesting challenges.
- Additional EX options. You could start with the HUD disabled and need to find each android's HUD item. You could start with a virtual player count of 2, 3, or 4 and need to find items to reduce it. I think these might be more trouble than they are worth, but they could be optional for added challenge.
- Achievements as locations. Androids Assemble, Chain Gang, Nothing But Net, Perfection, and Scrambled Eggs all add something new to do.
- Different goals
    - Longer game: Defeat Medulla+ (and Collider+) with any/all androids

Not implemented and likely will not be:
- Secondary weapons as items. I don't find it fun to play without dodges, nor do I find it fun to play with dodges but not secondary weapons, as I have autofire enabled. For now, the EX weapons are just a fun addition to a game that doesn't have enough items.
- Keys per-level instead of per-zone. Yes, this would add more items to the game, but at the cost of a significant amount of fiddling with the tracker to see which levels you have available.
