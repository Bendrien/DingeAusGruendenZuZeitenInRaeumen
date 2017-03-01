# This script does a fuzzy comparison that a found songs is the right one.
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


from difflib import SequenceMatcher
import json


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def main():
    with open('validatedData.json', 'w') as dataOutFile:
        with open('cleanedRawdataWithSpotifyID.json') as dataInFile:
            cleanedRawDataID = json.load(dataInFile)
            passed = []
            failed = []

            for entry in cleanedRawDataID:

                spotifyName = entry["Artist"] + " " + entry["SongName"]
                query = entry["Query"]
                ratio = similar(spotifyName, query)

                if (ratio > 0.6):
                    passed.append(entry)
                else:
                    error = {}
                    error["ID"] = entry["ID"]
                    error["Query"] = entry["Query"]
                    error["Artist"] = entry["Artist"]
                    error["SongName"] = entry["SongName"]

                    failed.append(error)


        json.dump(passed, dataOutFile, indent=4, sort_keys=True)

        with open('ValidationErrors.json', 'w') as errorFile:
            json.dump(failed, errorFile, indent=4, sort_keys=True)

        print("Errors: " + str(len(failed)) + " of " + str(len(cleanedRawDataID)) + " possible fuckups!")
        print("Leaving " + str(len(passed)) + " valid results!")


if(__name__ == '__main__'):
    main()
