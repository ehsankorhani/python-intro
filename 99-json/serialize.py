import json

data = {
    "make": "BMW",
    "model": "X1",
    "navigation": True,
    "odometer": 12050,
    "features": ["Sunroof", "Service History"],
    "engine": {
        "type": "Petrol",
        "capacity": 2500
    },
    "owners": [
        {
            "name": "John Doe",
            "gender": "male"
        }
    ]
}

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)

# myX1 = json.dumps(data, indent=4)
# print (myX1)

# myX1 = json.dumps(data, indent=None, separators=(',', ':'))
# print (myX1)