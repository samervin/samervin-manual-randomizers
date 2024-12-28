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
                android_name
            ],
        }
        if level_name[0] == "1":
            level["requires"] = f"|Assault Android {android_name}|"
        elif level_name[0:3] in ["5-4", "5-5"]:
            level["requires"] = f"|Assault Android {android_name}| and |{android_name} Boss Key| and |{android_name} Accelerate| and |{android_name} Firepower| and |{android_name} Shutdown|"
        else:
            level["requires"] = f"|Assault Android {android_name}| and |{android_name} Zone {level_name[0]} Key|"
        levels.append(level)

one_android_victory = ""
for android_name in android_names:
    one_android_victory += f"(|Assault Android {android_name}| and |{android_name} Boss Key| and |{android_name} Accelerate| and |{android_name} Firepower| and |{android_name} Shutdown|) or "
levels.append({
    "name": "Defeat Collider and Medulla with any android",
    "requires": one_android_victory[:-4], # chop off the last "or"
    "category": ["Victory"],
    "victory": True
})
all_android_victory = ""
for android_name in android_names:
    all_android_victory += f"|Assault Android {android_name}| and |{android_name} Boss Key| and |{android_name} Accelerate| and |{android_name} Firepower| and |{android_name} Shutdown| and "
levels.append({
    "name": "Defeat Collider and Medulla with all androids",
    "requires": all_android_victory[:-5], # chop off the last "and"
    "category": ["Victory"],
    "victory": True
})

with open('locations.json', 'w') as f:
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
        "count": 2,
        "progression": True
    }
    items.append(item)
for android_name in android_names:
    item = {
        "name": f"{android_name} Shutdown",
        "category": [android_name],
        "count": 2,
        "progression": True
    }
    items.append(item)
for android_name in android_names:
    item = {
        "name": f"{android_name} Firepower",
        "category": [android_name],
        "count": 2,
        "progression": True
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
            "name": f"{android_name} Zone {zone} Key",
            "category": ["Keys"],
            "progression": True
        }
        items.append(item)
for android_name in android_names:
    item = {
        "name": f"{android_name} Boss Key",
        "category": ["Keys"],
        "progression": True
    }
    items.append(item)

with open('items.json', 'w') as f:
    f.write(json.dumps(items, indent=4))
