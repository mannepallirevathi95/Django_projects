obj = {
    "name":"cream bun",
    "description":"heavy loded vanilla cream bun",
    "price":59,
    "details":"",
    "Add to cart":"",
    "delete":""
}

import json

def readit(filename="db.json"):
    with open(filename, mode="r") as jsonFile:
        data = json.load(jsonFile)

        return data

def writeit(obj, filename="db.json"):
    with open(filename, mode="r") as jsonFile:
        data = json.load(jsonFile)
        temp = data["database"]["results"]
        temp.append(obj)

    with open(filename, mode="w") as jsonFile:
        json.dump(data, jsonFile)

writeit(obj = obj)
