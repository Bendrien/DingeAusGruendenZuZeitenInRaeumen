# This script takes the cleaned raw data and searches for it on Spotify.
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


import spotipy
import json

def main():
    spotify = spotipy.Spotify()

    with open('cleanedRawdataWithSpotifyID.json', 'w') as dataOutFile:
        with open('cleanedRohdaten.json') as dataInFile:
            cleanedRawData = json.load(dataInFile)
            result = []
            fails = []

            for entry in cleanedRawData:
                #print("Entry: " + json.dumps(entry, sort_keys=True))

                response = spotify.search(q = entry["Query"], type='track', limit=5)

                if response["tracks"]["items"]:
                    first_track = response["tracks"]["items"][0]

                    entry["SongName"]  = first_track["name"]
                    entry["SpotifyID"] = first_track["id"]
                    entry["Artist"]    = first_track["artists"][0]["name"]
                    entry["URI"]       = first_track["uri"]

                    result.append(entry)
                else:
                    error = {}
                    error["ID"] = entry["ID"]
                    error["Query"] = entry["Query"]

                    fails.append(error)

                    print("Error #" + str(len(fails)) + ": Something went wrong while getting ID: "
                          + str(entry["ID"]) + " with query: " + str(entry["Query"]))
                    print(json.dumps(response, sort_keys=True))



                # Print entry
                #print(json.dumps(entry, indent=4, sort_keys=True))

        json.dump(result, dataOutFile, indent=4, sort_keys=True)

        with open('IdErrors.json', 'w') as errorFile:
            json.dump(fails, errorFile, indent=4, sort_keys=True)

        print("Errors: " + str(len(fails)) + " of " + str(len(cleanedRawData)) + " possible fuckups!")


if(__name__ == '__main__'):
    main()
