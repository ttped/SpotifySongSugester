import pandas as pd

def get_song_by_name(song_list):
    df = pd.read_csv('Spotify/data.csv')
    df = df.drop(columns=['key', 'id', 'mode', 'year', 'release_date',
    'speechiness', 'tempo'])

    df['duration_ms'] = df['duration_ms'] / 60000
    df['popularity'] = df['popularity'] / 100

    model_output = df[df['name'].isin(song_list)]

    return model_output

## Todo get user input
def get_user_input_song(song):
    df = pd.read_csv('Spotify/data.csv')
    df = df.drop(columns=['key', 'id', 'mode', 'year', 'release_date',
    'speechiness', 'tempo'])

    df['duration_ms'] = df['duration_ms'] / 60000
    df['popularity'] = df['popularity'] / 10

    #dummy_song_list = ['Rough Ryder']

    model_output = df[df['name'].isin(song)]

    return model_output
