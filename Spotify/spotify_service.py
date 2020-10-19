from os import getenv  
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
  client_id=getenv("Client_id"),
  client_secret=getenv("Client_secret")))


def query(songnames):
  output_list=[]
  for songs in songnames:
    results = sp.search(q=songs, limit=30)
    new_list= []
    for idx, track in enumerate(results['tracks']['items']):
      new_list.append(track['name'])
    output_list.append(new_list)
  return(output_list)

