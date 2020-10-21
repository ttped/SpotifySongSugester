import pandas as pd
import numpy as np
import spacy
from sklearn.decomposition import PCA
from sklearn.neighbors import NearestNeighbors

nlp = spacy.load('my_model')

df = pd.read_csv('Spotify/data.csv')
df = df[:5001]
df['artists'] = df['artists'].apply(lambda x: x[1:-1].replace("'", ''))

df_slim = df.drop(['id', 'release_date', 'year', 'mode', 'key'], axis=1)

def standardizer(data):
  d_maxes = data.max()
  d_mins = data.min()
  data/d_maxes
  return d_maxes, d_mins

df_slim['duration_ms'] = df_slim['duration_ms']/5403500
df_slim['popularity'] = df_slim['popularity']/100
df_slim['tempo'] = df_slim['tempo']/244.091
df_slim['loudness'] = abs(df_slim['loudness']/60)

ndf_slim = df_slim[:2000]

def get_word_vectors(w):
  #converts of words to their own vectors
  return [nlp(word).vector for word in w]

df_name=ndf_slim['name']

s1_PCA_song_names = PCA(n_components=2)

s1_PCA_song_names.fit(get_word_vectors(df_name))

s1_name_vect = s1_PCA_song_names.transform(get_word_vectors(df_name))

nn1 = NearestNeighbors(n_neighbors=10, radius=0.5, algorithm='ball_tree', n_jobs=2)

nn1.fit(s1_name_vect)

names = ndf_slim['name']

s2_PCA_song_names = PCA(n_components=1)

s2_PCA_song_names.fit(get_word_vectors(names))

name_vect = s2_PCA_song_names.transform(get_word_vectors(names))

artists = ndf_slim['artists']
PCA_artist_names = PCA(n_components=1)

PCA_artist_names.fit(get_word_vectors(artists))

artist_vect = PCA_artist_names.transform(get_word_vectors(artists))

fdf= ndf_slim.drop(['name', 'artists'], axis=1)
fdf['1d_vectorized_name'] = name_vect
fdf['1d_vectorized_artist'] = artist_vect

pca2 = PCA(n_components=2)

pca2.fit(fdf)

last_vector = pca2.transform(fdf)

names = ndf_slim['name']

nn2 = NearestNeighbors(n_neighbors=10, radius=0.5, algorithm='ball_tree', n_jobs=2)
X = last_vector
nn2.fit(X)

names = ndf_slim['name']

def song_suggestion(song):
    new_song = ([song])
    new = get_word_vectors(new_song)
    new = s1_PCA_song_names.transform(new)

    song_list = []

    for number in nn1.kneighbors(new)[1]:
      song_list.append(df_name[number])

    temp = pd.DataFrame(song_list).values[0]

    temp_list = []
    for val in temp:
      temp_list.append(val)

    return temp_list

def get_prediced_songs(user_song):
 index = df[df['name'] == user_song].index[0]
 song_list = []

 for number in nn2.kneighbors([X[index]])[1]:
     song_list.append(df_name[number])

 temp = pd.DataFrame(song_list).values[0]
 temp_list = []
 for val in temp:
   temp_list.append(val)

 return temp_list
