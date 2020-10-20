import pandas as pd

def return_model_output():
    df = pd.read_csv('Spotify/data.csv')
    df = df.drop(columns=['key', 'id', 'mode', 'year', 'release_date',
    'speechiness', 'tempo'])

    df['duration_ms'] = df['duration_ms'] / 60000

    dummy_song_list = ['Bury Me Alive', 'you were good to me - shallou remix',
    'Glizzy', 'High Power', 'Wolves (with NAV)', 'All Around Me',
    'P2','My Truck (feat. Sam Hunt) - Remix',
    'Mr. Officer (feat. Queen Naija and members of the Detroit Youth Choir)','Multiple Flows (with Lil Uzi Vert)',
    'Second Chances. (ft. 6LACK)','Marsh','Stay Tonight','Say You Will',
    'Young & Sad','Vibes Only','Wet Em Up Pt. 2','Tycoon','Fine By Time','Rough Ryder']

    model_output = df[df['name'].isin(dummy_song_list)]

    return model_output

## Todo get user input
def get_user_input_song():
    df = pd.read_csv('Spotify/data.csv')
    df = df.drop(columns=['key', 'id', 'mode', 'year', 'release_date',
    'speechiness', 'tempo'])

    df['duration_ms'] = df['duration_ms'] / 60000

    dummy_song_list = ['Rough Ryder']

    model_output = df[df['name'].isin(dummy_song_list)]

    return model_output
