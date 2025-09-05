import json,csv
import os

print(os.path.dirname(__file__))

try:
    with open("json.input","r") as json_file:
        data = json.load(json_file)

    field_names = data[0].keys()    
    with open('output.csv', 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(data)

except FileNotFoundError:
    print('file not found')        

