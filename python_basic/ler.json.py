import json

with open('my_json', 'r') as file:
    d1_json = file.read()
    # Convertendo para dict
    d1_json = json.loads(d1_json)

for k, v in d1_json.items():
    print(k)
    for k1, v2 in v.items():
        print(k1, v2)