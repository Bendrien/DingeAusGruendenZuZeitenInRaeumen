import csv
import json

def main():
    with open('cleanedRohdaten.json', 'w') as jsonFile:
        with open('Rohdaten.csv') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            result = []
            idCounter = 0;
            for row in reader:
                for i in range(1, 11):
                    entry = {}
                    entry["ID"] = idCounter
                    idCounter += 1
                    entry["Query"]         = row["tr"            + str(i)]
                    entry["Anspruchsvoll"] = row["anspruchsvoll" + str(i) + "_1"]
                    entry["Intensiv"]      = row["intensiv"      + str(i) + "_2"]
                    entry["Sanft"]         = row["sanft"         + str(i) + "_3"]
                    entry["Komplex"]       = row["komplex"       + str(i) + "_4"]
                    entry["Emotional"]     = row["emotional"     + str(i) + "_5"]
                    entry["Erregend"]      = row["erregend"      + str(i) + "_6"]
                    entry["Entspannend"]   = row["entspannend"   + str(i) + "_7"]
                    entry["Intellektuell"] = row["intellektuell" + str(i) + "_8"]
                    entry["Tanzbar"]       = row["tanzbar"       + str(i) + "_9"]
                    entry["Fröhlich"]      = row["froehlich"     + str(i) + "_10"]
                    entry["Traurig"]       = row["traurig"       + str(i) + "_11"]
                    entry["Warm"]          = row["warm"          + str(i) + "_12"]
                    entry["Einfach"]       = row["einfach"       + str(i) + "_13"]

                    result.append(entry)

            json.dump(result, jsonFile, indent=4, sort_keys=True)


if(__name__ == '__main__'):
    main()
