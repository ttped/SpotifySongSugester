def wrangle(df):
    df = df.copy()
    df = df.drop(columns=['key', 'id', 'mode', 'year', 'release_date',
    'speechiness', 'tempo'])

    df['duration_ms'] = df['duration_ms'] / 60000
    df['popularity'] = df['popularity'] / 100

    return df
