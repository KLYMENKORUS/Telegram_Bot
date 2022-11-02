import json

cenzura = []

with open('cenz.txt', encoding='utf-8') as file:
    for f in file:
        j = f.lower().split('\n')[0]
        if j != '':
            cenzura.append(j)

with open('cenz.json', 'w', encoding='utf-8') as file_json:
    json.dump(cenzura, file_json)
