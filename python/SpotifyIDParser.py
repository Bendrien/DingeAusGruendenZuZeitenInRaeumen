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
                    print("Something went wrong while getting ID: " + str(entry["ID"])
                          + " with query: " + str(entry["Query"]))
                    print(json.dumps(response, sort_keys=True))
                    error = {}
                    error["ID"] = entry["ID"]
                    error["Query"] = entry["Query"]

                    fails.append(error)



                # Print entry
                #print(json.dumps(entry, indent=4, sort_keys=True))

        json.dump(result, dataOutFile, indent=4, sort_keys=True)

        with open('IdErrors.json', 'w') as errorFile:
            json.dump(fails, errorFile, indent=4, sort_keys=True)

        print("Errors: " + str(len(fails)) + " of " + str(len(cleanedRawData)) + " possible fuckups!")


if(__name__ == '__main__'):
    main()
