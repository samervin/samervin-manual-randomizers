# Burnout Paradise

Notes
- Intended to be played using the Remastered version
- You can force the game to make a new save file by renaming or deleting `%LOCALAPPDATA%\Criterion Games\Burnout Paradise Remastered\Save\Profile.BurnoutParadiseSave`. I renamed mine to `Profile.BurnoutParadiseSave.Backup`.
- Playing on a completed file is possible, as you can retry events at will. The events will all be in their hardest mode though, and the road rules are difficult to track as the timer stops running if you go over your previous time.
- The game does track things like billboards and jumps, but I think that's too much hassle. The regular events are all clearly visible on the map and easy to find, and there are already a lot of locations.
- Unlocking a car gives you the ability to use it if it is in your garage. There is no way I know of to grant yourself a car without playing on a completed file or using mods, which I have not personally tried.
- Getting a new license resets all completed events. There is no good way of noting this in-game, so use the tracker to find events.
- Except for the burning routes, the vanilla game does not put any requirements on any events.
- To limit the size of sphere 1, the six major areas of the map will be locked behind maps. You can still drive through locked areas and complete events that finish there, but you cannot (logically) start events there.
- In future, I may logically lock certain location types behind additional items, e.g. road rules may require an item to complete. I don't think I will want regional event type locks though, i.e. "Races in Downtown Paradise only". I'm OK with relatively few locking items / large spheres as this game is very open-world and the events are not especially difficult.
- Best guide for listing all cars and events is here: https://steamcommunity.com/sharedfiles/filedetails/?id=2291470178
- Any events marked with a ??? have not been confirmed in-game

Locations:
- 40 races + 4-6 DLC (what do the Tours count as?)
- 16 road rage + 3 DLC
- 15 marked man + 2 DLC
- 14 stunt run + 3 DLC
- 64 time road rules + 12 DLC
- 64 showtime road rules + 12 DLC
- 19 bike burning rides
- 19 bike midnight rides
- 64 bike day road rules + 12 DLC
- 64 bike night road rules + 12 DLC
- 35 burning routes + 1 DLC
    - These are not included right now. They require the base car to complete, and unless you are playing on a completed file it takes a long time to get late-game cars.

Items:
- 6 maps, to complete events in different areas
    - 2 additional map items for Auto Repair and Gas Station drive-throughs
- 70 cars + 6 carbon cars
- 4 bikes + 1 toy
- 33 PCPD variant cars
- 23 other DLC cars (legendary, toys, specials, Big Surf Island)

Victory:
- There are 36 identical "Archipelago License" items. Once you collect 24, you finish your license and win immediately.

# TODO

- Fix locations marked with ???
- More categories. At a minimum, every region should have a category for all its road rules and events. Preferably in reading order.
- Better list of cars and when they can be unlocked (or a mod that unlocks them all)
- "Use what you find" mode for cars

# MODDING

Mods list:

- https://bpr.bo98.uk/
    - Download BPR Modder, use that to install Core Bugfixes, Traffic Toggle, and Brick Remastered
- https://matty-ross.github.io/bpr-mods/
    - Extract mod-manager.dll and imgui.dll to the game's root folder
    - Extract mods/free-camera.dll to the game's mods folder
- Burnout Hints Discord
    - Download webcam.dll and hud_remover.dll to the game's mods folder
- https://www.patreon.com/posts/red-0-0-1-3-64021669
    - Download RED and point it to the game's root folder
- https://github.com/burninrubber0/Bundle-Manager
    - Download Bundle Manager release, extract, and run as administrator
- Others
    - https://github.com/matty-ross/bpr-utility-mods/tree/main/binaries
    - https://docs.google.com/spreadsheets/d/19_5ZXKY3zBkhileGWTMg3pcm7l8ZsGtQ/edit?gid=1618638281#gid=1618638281

What do these do?

- Core Bugfixes fixes a few small bugs
- Traffic Toggle lets you turn traffic on and off with F5
- Brick Remastered has a lot of features: F9 for menu, F10 to toggle mod HUD
    - Portable junkyard for all vehicles
        - NPC vehicles included. They have extremely low stats unfortunately, and the camera is buggy, but you can fix the camera with the free-camera mod
        - Online-only cars, etc. seem to be included
    - Painting, speedometer, boost switching, etc.
- Free Camera lets you change camera angles: F7 for menu
- Webcam turns off the check for webcams, which saves time after every event
- HUD Remover toggles the in-game HUD with F10
    - Yes, this is the same hotkey as the Brick Remastered HUD. You can toggle the Brick HUD from within its F9 menu in order to get the two toggles in sync as needed
- RED is a save editor. There's a lot of things you can change, but the most interesting to me are:
    - Profile 1.0
        - Current Progression Rank aka License (can you set this to "Burnout" so events never reset?)
        - Cars (can you unlock all cars? How does this perform for NPC vehicles? some overlap with the Brick Remastered mod)
        - Events (you can toggle Discovered, Won, and other fields)
        - Player Road Rules (what are "Time Dirty" and "Showtime Dirty" fields? can you mark showtimes as done?)
        - Seen Training (turn off various tutorial reminders)
    - Profile 1.3
        - Cars (can you unlock the normally online-only cars?)
    - Profile 1.4
        - Bikes (can you unlock all bikes?)
        - Events (you can toggle Discovered, Won, and other fields)
    - Profile 1.9
        - Cars (can you unlock all Big Surf Island cars?)
        - Events (you can toggle Discovered, Won, and other fields)
- Bundle Manager lets you edit the bundles that come with the game. The most interesting file to me is PROGRESSION.DAT, which stores some game data, like:
    - LicenceDataEntries > LicenceData > NumEventWinsRequired, AKA the number of wins needed to upgrade the license.
    - EventJunctionEntries > various EventData fields. Some fields seem easy to edit, like AppearsWhen (an integer enum), TrafficDensityMultiplier (frequently 0.60), Target Time, NumberOfAIRivalsToUse (max 7 apparently)
    - RivalEntries, a list of cars that normally need to be taken down while roaming
    - I downloaded a HARDER_PROGRESSION.DAT file that claims to have more difficult AI drivers, but I cannot find what the difference is.
