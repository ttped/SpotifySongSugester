""" Main app/routing file for Spotify"""

from flask import Flask, render_template, request, Markup
from Spotify.models import Song, DB
from os import getenv
from Spotify import spotify_service
import pandas as pd


## initalizing the app
def create_app():
    """creates and configures flask application"""

    labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
    ]


    values = [
        967.67, 1190.89, 1079.75, 1349.19,
        2328.91, 2504.28, 2873.83, 4764.87,
        4349.29, 6458.30, 9907, 16297
    ]

    colors = [
        "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
        "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
        "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

    app = Flask(__name__)
    app.config['SQLAlCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
    app.config['SQLAlCHEMY_TRACK_MODIFCATIONS'] = False
    DB.init_app(app)

    @app.route('/')
    def root():
        return render_template("base.html", title="Home")

    ## Send output for model
    @app.route('/song', methods=['POST'])
    def song_suggestor():
        df = pd.read_csv('Spotify/data.csv')
        df = df.drop(columns=['key', 'id', 'mode', 'year', 'release_date', 'artists',
        'speechiness', 'tempo'])
        df['duration_ms'] = df['duration_ms'] / 60000
        bar_labels=df.columns

        # The model output
        df = df[df['name'] == request.values['song_name']]

        # todo change request.values to model output values
        api_songs = spotify_service.test_query(request.values['song_name'])

        dummy_song_list = ['Chapter 3.4 - Zamek kaniowski', 'Rumours']
        model_output = df[df['name'].isin(dummy_song_list)]

        return render_template("song.html", songs=api_songs,
        title='Bitcoin Monthly Price in USD', max=20, labels=bar_labels, values=df.values, df=df,
        model_output=model_output)

    @app.route('/reset')
    def reset():
        # resets datatbase
        DB.drop_all()
        #creates database again
        DB.create_all()
        return render_template('base.html', title='Home')

    return app
