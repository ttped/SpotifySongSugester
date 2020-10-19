from os import getenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
  client_id="504089650162462d81b6b94b90e40747",
  client_secret="8d7af6e2e11748599046d25e85d82035 "))


def test_query(song):
    results = sp.search(q="weezer", limit=30)
    for idx, track in enumerate(results['tracks']['items']):
      print(idx, track['name'])

def query(songnames):
  output_list=[]
  for songs in songnames:
    results = sp.search(q=songs, limit=30)
    new_list= []
    for idx, track in enumerate(results['tracks']['items']):
      new_list.append(track['name'])
    output_list.append(new_list)
  return(output_list)
