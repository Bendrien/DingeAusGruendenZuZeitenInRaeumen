# This script logs into the Spotify Web API and downloads the
# Audio Features that correspond with a Spotify ID.
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


from __future__ import print_function    # (at top of module)
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy
from Tokens import *


def main():
    client_credentials_manager = SpotifyClientCredentials(client_id = client_id, client_secret = client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


    with open('FinalData.json', 'w') as dataOutFile:
        with open('validatedData.json') as dataInFile:
            cleanedRawData = json.load(dataInFile)
            result = []

            for entry in cleanedRawData:
                features = sp.audio_features([entry["SpotifyID"]]) # element is null on error

                if (features[0] is None):
                    print("Error: Could not get track: " + str(entry["Query"]) + " with ID: "
                          + str(entry["SpotifyID"]))
                else:
                    entry["SP_energy"]           = features[0]["energy"]
                    entry["SP_danceability"]     = features[0]["danceability"]
                    entry["SP_acousticness"]     = features[0]["acousticness"]
                    entry["SP_liveness"]         = features[0]["liveness"]
                    entry["SP_time_signature"]   = features[0]["time_signature"]
                    entry["SP_valence"]          = features[0]["valence"]
                    entry["SP_loudness"]         = features[0]["loudness"]
                    entry["SP_speechiness"]      = features[0]["speechiness"]
                    entry["SP_mode"]             = features[0]["mode"]
                    entry["SP_tempo"]            = features[0]["tempo"]
                    entry["SP_key"]              = features[0]["key"]
                    entry["SP_instrumentalness"] = features[0]["instrumentalness"]
                    entry["SP_duration_ms"]      = features[0]["duration_ms"]

                    result.append(entry)


        json.dump(result, dataOutFile, indent=4, sort_keys=True)



if(__name__ == '__main__'):
    main()
