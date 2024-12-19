import json

number_keys = 100
number_rooms = 10
keys_per_room = 10

items = [{
    "name": "Storage Key",
    "category": ["Storage Key"],
    "progression": True,
    "count": number_keys
}]

with open('data/items.json', 'w') as f:
    f.write(json.dumps(items, indent=4))

locations = [{
    "name": "All Junk Coverted",
    "category": ["Victory"],
    "requires": "|Storage Key:ALL|",
    "victory": True
}]

for i in range(number_rooms):
    room = {
        "name": f"Storage Room {i+1:03d}", # Three digits with leading zeroes
        "category": ["Storage Room"],
        "requires": f"|Storage Key:{keys_per_room * (i+1)}|"
    }
    locations.append(room)

with open('data/locations.json', 'w') as f:
    f.write(json.dumps(locations, indent=4))
