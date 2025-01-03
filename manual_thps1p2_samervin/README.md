# Tony Hawk's Pro Skater 1 + 2

Implementation notes:
- For career levels, speedrun mode is recommended
- For competition levels, the listed score thresholds are provided for 2-minute single session runs (they approximate the scores required to medal). If you prefer, you can replay the competitions directly instead.
- You need a level's ticket in order to access that level
- Each regular career level has 10 goal locations
- Each competition career level has 3 medal locations
- Chopper Drop's only location is the 90 Ft gap
- Skate Heaven's only location is a single session score
- You start with zero special trick slots available and must find both special trick slots and special tricks to go in them
- You start with 1 stat in all categories and can find the other 9 stat points for each category
- Every goal can be completed with only 1 stat, but some are difficult, and I could not reproduce two of them myself. See below for help on some tough jumps.
    - Downtown's secret popcorn bucket can be reached by grinding the inside of the pool and the planter before jumping to the popcorn. This is also one of the rooftop gaps.
    - Downtown's other rooftop gap can be completed by grinding the outside of the pool before jumping between roofs.
    - Downhill Jam's Hydrophobic Gap can be completed by grinding the nearby rail and jumping the gap backwards.
    - Downhill Jam's secret tape can be reached by wallriding between the upper platforms, then grinding the final ramp.
    - Streets' life preserver between the vert ramps can be reaching by leveling out after jumping diagonally.
    - Streets' secret tape has been done, but I could not reproduce it without 1 additional speed stat, so that is currently required.
    - Streets' Hubba Gap can be cheesed by getting on top of the clear room nearby, then jumping across the area you would normally ollie over.
    - Hangar's Skycrane Hangtime gap has been done, but I could not reproduce it without 3 additional speed stats, so those are currently required.
    - Venice's VB Huge Transfer can be completed by grinding the high ramp, leveling out, then leaning forward to touch the far ramp.
    - Venice's secret tape can be reached by grinding the far rail underneath it, dropping off, then immediately jumping off the table.
- TODO Lock additional trick types behind items (manuals, reverts, transfers, grinds, flips, grabs, wallplants, etc.)
    - Grabs, flips, and lips can all be fully unbound in the skater tricks menu. Speedrun mode does not care if you don't have a required trick bound (e.g. Heelflip the Kicker Gap), you just won't be able to complete the goal.
- TODO Additional locations for single session scores for all maps
- TODO Additional locations for iconic gaps in each level