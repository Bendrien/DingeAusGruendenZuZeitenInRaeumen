import spotipy
import json

def main():
    spotify = spotipy.Spotify()

    with open('cleanedRawdataWithSpotifyID.json', 'w') as dataOutFile:
        with open('cleanedRohdatenShort.json') as dataInFile:
            cleanedRawData = json.load(dataInFile)
            result = []

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
                    print(json.dumps(response, indent=4, sort_keys=True))


                # Print entry
                #print(json.dumps(entry, indent=4, sort_keys=True))

        json.dump(result, dataOutFile, indent=4, sort_keys=True)

if(__name__ == '__main__'):
    main()
