import spotipy
import json

def main():
    spotify = spotipy.Spotify()
    results = spotify.search(q='Berliner Philharmoniker eine kleine nachtmusik', type='track', limit=5)
    first_track = results["tracks"]["items"][0]
    print(json.dumps(first_track, indent=4, sort_keys=True))

if(__name__ == '__main__'):
    main()
