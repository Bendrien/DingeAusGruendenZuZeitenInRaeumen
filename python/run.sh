echo "Running Rohdaten Parser."
python3 RohdatenParser.py
echo "Done!"

echo "Running Spotify ID Parser."
python3 SpotifyIDParser.py
echo "Done!"

echo "Running Validator."
python3 Validator.py
echo "Done!"

echo "Collecting Spotify Metadata."
python3 SpotifyMetadata.py
echo "All Done! Results are in FinalData.json"
