level_names = [
    "1-1 Descent",
    "1-2 Turbine",
    "1-3 Filament",
    "1-4 Capacitor",
    "1-5 Embryo",
    "2-1 Hive",
    "2-2 Influx",
    "2-3 Oxygen",
    "2-4 Process",
    "2-5 Vespula",
    "3-1 Checkpoint",
    "3-2 Transit",
    "3-3 Heat",
    "3-4 Revolution",
    "3-5 Justice",
    "4-1 Assembly",
    "4-2 Relay",
    "4-3 Focus",
    "4-4 Repeater",
    "4-5 Venom",
    "5-1 Centrifuge",
    "5-2 Control",
    "5-3 Convection",
    "5-4 Collider",
    "5-5 Medulla",
]

android_names = [
    "Cactus",
    "Holly",
    "Lemon",
    "Coral",
    "Starch",
    "Aubergine",
    "Shiitake",
    "Peanut",
    "Liquorice",
]

import json

levels = []
for level_name in level_names:
    for android_name in android_names:
        level = {
            "name": f"{level_name} - {android_name}",
            "category": [
                level_name,
            ],
        }
        if level_name[0:3] in ["1-1", "1-2", "1-3", "1-4"]:
            level["requires"] = f"|Assault Android {android_name}|"
        if level_name[0:3] == "1-5":
            level["requires"] = f"|Assault Android {android_name}| and |Zone 1 Boss Key - {android_name}|"
        if level_name[0:3] in ["2-5", "3-5", "4-5", "5-5"]:
            level["requires"] = f"|Assault Android {android_name}| and |Zone {level_name[0]} Key - {android_name}| and |Zone {level_name[0]} Boss Key - {android_name}|"
        elif level_name[0] in "2345":
            level["requires"] = f"|Assault Android {android_name}| and |Zone {level_name[0]} Key - {android_name}|"
        levels.append(level)

victory_requirements = ""
for android_name in android_names:
    victory_requirements += f"(|Assault Android {android_name}| and |Zone 5 Key - {android_name}| and |Zone 5 Boss Key - {android_name}|) and "
levels.append({
    "name": "Defeat Medulla with all androids",
    "requires": victory_requirements[:-5], # chop off the last "and"
    "victory": True
})

with open('data/locations.json', 'w') as f:
    f.write(json.dumps(levels, indent=4))

items = []
for android_name in android_names:
    item = {
        "name": f"Assault Android {android_name}",
        "category": [android_name],
        "progression": True
    }
    items.append(item)
for android_name in android_names:
    item = {
        "name": f"{android_name} Accelerate",
        "category": [android_name],
        "useful": True
    }
    items.append(item)
for android_name in android_names:
    item = {
        "name": f"{android_name} Shutdown",
        "category": [android_name],
        "useful": True
    }
    items.append(item)
for android_name in android_names:
    item = {
        "name": f"{android_name} Firepower",
        "category": [android_name],
        "useful": True
    }
    items.append(item)
for android_name in android_names:
    item = {
        "name": f"{android_name} EX Weapon",
        "category": [android_name],
        "useful": True
    }
    items.append(item)
for zone in "2345":
    for android_name in android_names:
        item = {
            "name": f"Zone {zone} Key - {android_name}",
            "category": [android_name],
            "progression": True
        }
        items.append(item)
for zone in "12345":
    for android_name in android_names:
        item = {
            "name": f"Zone {zone} Boss Key - {android_name}",
            "category": [android_name],
            "progression": True
        }
        items.append(item)

with open('data/items.json', 'w') as f:
    f.write(json.dumps(items, indent=4))
