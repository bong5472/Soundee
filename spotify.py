from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pprint


client_id = "client_id"
client_secret = "client_secret"

lz_uri = 'spotify:artist:6VuMaDnrHyPL1p4EHjYLi7' # Charlie Puth

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

results = sp.artist_top_tracks(lz_uri)

# get top 10 tracks
for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()