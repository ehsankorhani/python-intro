import json

with open("data_file.json", "r") as read_file:
    data = json.load(read_file)

print (data)
print (type(data))


jsonData = json.dumps(data)
myX1 = json.loads(jsonData)

print (myX1)
print (type(myX1))