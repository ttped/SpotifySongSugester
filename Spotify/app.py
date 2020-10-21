""" Main app/routing file for Spotify"""

from flask import Flask, render_template, request, Markup
from Spotify.models import Song, DB
from Spotify import utility
from os import getenv
from Spotify import spotify_service
import pandas as pd
import numpy as np
from Spotify import seans_model


## initalizing the app
def create_app():
    """creates and configures flask application"""

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

    # Get Seans songs
    @app.route('/get_song_list', methods=['POST'])
    @app.route('/get_song_list')
    def get_song_list():
        song_list = seans_model.song_suggestion(request.values['song_name'])
        return render_template("pick_song.html", songs=song_list)


    ## Send output for model
    @app.route('/song', methods=['POST'])
    def song_suggestor():
        #df = pd.read_csv('Spotify/data.csv')
        #df = wrangle.wrangle(df)
        song_list = seans_model.get_prediced_songs(request.values['song_name'])

        df = utility.get_song_by_name(song_list)
        picked_song = utility.get_song_by_name([request.values['song_name']])

        # todo change request.values to model output values
        api_songs = spotify_service.test_query(request.values['song_name'])

        df2 = df.drop(columns=['artists'])
        df2['popularity'] = df2['popularity'] / 100
        ss1 = df2.iloc[0].values

        df2 = pd.concat([picked_song, df2]).reset_index(drop = True)

        max = df2.drop(columns=['name']).max().max()
        min = df2.drop(columns=['name']).min().min()

        max = int(max) + 1
        min = int(min) - 1

        max = np.max([max, abs(min)])

        return render_template("song.html", songs=api_songs,
            title='Song Characteristics',
            max=max, min=min,
            labels=df2.columns,
            model_output=df2.to_dict(orient='records'),
            picked_song=picked_song.to_dict(orient='records'))

    @app.route('/test')
    def test():
        return render_template('test.html')

    @app.route('/reset')
    def reset():
        # resets datatbase
        DB.drop_all()
        #creates database again
        DB.create_all()
        return render_template('base.html', title='Home')

    return app
