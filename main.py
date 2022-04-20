import csv
import re
import json

with open('defensive_technique_info.json', 'r') as file:
    data = json.load(file)

toWrite = []

for title in data:
    definition = ''
    for key, val in title.items():
        for definitions in val.values():
            definition += definitions.replace('\n', ' ')
    if key == 'Certificate Pinning':
        print(definition)
    toWrite.append([key, definition])


with open('defensive_technique_info.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(toWrite)
