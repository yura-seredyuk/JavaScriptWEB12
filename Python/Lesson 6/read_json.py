import json


with open("files/file.json", 'r') as file:
    # data = json.load(file)
    data = file.read()
    data = json.loads(data)
    print(data)
