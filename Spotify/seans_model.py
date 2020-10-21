from sklearn.decomposition import PCA
from sklearn.neighbors import NearestNeighbors
import pandas as pd
import numpy as np
# !python -m spacy download en_core_web_sm
import spacy
nlp = spacy.load('en_core_web_sm')

#steps to do:
# train the model here
# create a class for user input
# run user input through model_1
# run user input through model_2


### model training ###
#STEP 1:

def get_word_vectors(song_name):
  #converts of words to their own vectors
  return [nlp(word).vector for word in w]

#STEP 2: train a NN model for just the song names
names= ds['name']
    # Vectorize the song names in the dataset
s1_PCA_song_names = PCA(n_components=2)
s1_PCA_song_names.fit(get_word_vectors(names))
s1_name_vect = s1_PCA_song_names.transform(get_word_vectors(names))

#THESE next steps are for training the second model that analyzes all the features of the dataset
#STEP 3: reduce artist and name columns to 1-D vector representations
s2_PCA_song_names = PCA(n_components=1)
s2_PCA_song_names.fit(get_word_vectors(names))
name_vect = s2_PCA_song_names.transform(get_word_vectors(names))
#
artists = ds['artists']
PCA_artist_names = PCA(n_components=1)
PCA_artist_names.fit(get_word_vectors(artists))
artist_vect = PCA_artist_names.transform(get_word_vectors(artists))

# step 4: remove the non-vectorized name and artist columns
fdf= ndf_slim.drop(['name', 'artists'], axis=1)
fdf['1d_vectorized_name'] = name_vect
fdf['1d_vectorized_artist'] = artist_vect
print(fdf.columns)
print(fdf.shape)
fdf.head()

#step5: PCA the entire dataset now to reduce each obseration to just 2D vectors
pca2 = PCA(n_components=2)
pca2.fit(fdf)
last_vector = pca2.transform(fdf)

#step6: dataset ready for training the NN model
nn2 = NearestNeighbors(n_neighbors=10, radius=0.5, algorithm='ball_tree', n_jobs=2)
nn2.fit(last_vector)



def model_step_1(song_name):

    user_song = s1_PCA_song_names.transform(get_word_vectors(song_name))
    return nn1.kneighbors(new)

def model_step_two(clicked):

    return nn2.kneighbors(clicked)



   