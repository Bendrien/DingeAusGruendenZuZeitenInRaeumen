# This script parses the raw data and converts it into a nice JSON file.
# Copyright (C) 2017  Maximilian Wagenbach

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


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
