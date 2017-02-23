import json
import csv

with open("FinalData.json") as file:
    data = json.load(file)

with open("FinalData.csv", "w") as file:
    csv_file = csv.writer(file)
    csv_file.writerow(data[0].keys())
    for item in data:
        csv_file.writerow(item.values())
