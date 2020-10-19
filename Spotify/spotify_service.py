from os import getenv
import spotipy as spot
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

sp = spot.Spotify(auth_manager=SpotifyClientCredentials(
  client_id = getenv("Client_id"),
  client_secret = getenv("Client_secret")))

def test_query(song):
    results = sp.search(q=song, limit=30)
    new_list = []
    for idx, track in enumerate(results['tracks']['items']):
      new_list.append(track['name'])
    return tuple(new_list)


def query(songnames):
  output_list=[]
  for songs in songnames:
    results = sp.search(q=songs, limit=30)
    for idx, track in enumerate(results['tracks']['items']):
      output_list.append(track['name'])
  return tuple(output_list)

#test_query("Sunfish")
