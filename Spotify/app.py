""" Main app/routing file for Spotify"""

from flask import Flask, render_template, request
from .models import songname
from os import getenv
import spotify_service


## initalizing the app
def create_app():
    """creates and configures flask application"""
    
    app = Flask(__name__)
    app.config['SQLAlCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
    app.config['SQLAlCHEMY_TRACK_MODIFCATIONS'] = False
    DB.init_app(app)

    @app.route('/')
    def root():
    #return render_template("base.html", title="Home", users= User.query.all())
        return render_template("base.html", title="Home")
## getting output for model
    @app.route('/Input Song', methods=['POST'])
    def song_suggestor(message=''):

## return song from Spotify/query
 @app.route('/results', methods= ['GET'])
    def results(name = None, message=''):
        # either grab an user that already exist in our DB or grab the users input
        name = name or request.values['user_name']

        try:
            #if button is clicked then do this:
            if request.method == 'POST':
                add_or_update_user(name)
                message = 'User {} sucessfully added!'.format(name)
            tweets = User.query.filter(User.name == name).one().tweets
        except Exception as e:
            message = 'Error adding {}: {}'.format(name, e)
            #if we get an error then no tweets are displayed
            tweets=[]
        
        return render_template('user.html', title= name, tweets=tweets, message=message)



    @app.route('/reset')
    def reset():
    # resets datatbase
    DB.drop_all()
    #creates database again    
    DB.create_all()
    return render_template('base.html', titel='Home')
"""
@app.route('/compare', methods=['POST'])
    def compare(message=''):
        #grabs inputted values from dropdown
        user0, user1 = sorted ([request.values['user1'],
            request.values['user2']])
        
        if user0 == user1:
            #tells application user they can't compre the same users
            message = "Cannot compare users to themselves!"
    
        else:
           #running prediction and return the prediction to user as a message 
            prediction = predict_user(user0, user1, request.values['tweet_text'])
            message = "{} is morely to be said by {} than {}".format(
                request.values['tweet_text'], user1 if prediction else user0,
                user0 if prediction else user1 )

        return render_template( 'prediction.html', title ='Prediction', message = message)   
    
    
    
    @app.route('/user', methods=['POST'])
    @app.route('/user/<name>', methods= ['GET'])
    def user(name = None, message=''):
        # either grab a user that already exist in our DB or grab the users input
        name = name or request.values['user_name']

        try:
            #if button is clicked then do this:
            if request.method == 'POST':
                add_or_update_user(name)
                message = 'User {} sucessfully added!'.format(name)
            tweets = User.query.filter(User.name == name).one().tweets
        except Exception as e:
            message = 'Error adding {}: {}'.format(name, e)
            #if we get an error then no tweets are displayed
            tweets=[]
        
        return render_template('user.html', title= name, tweets=tweets, message=message)




    @app.route('/update')
    def update():
        #updates our users from the function in twitter.py
        update_all_users()
        return render_template('base.html',title = "Tweets have been updated", users=User.query.all())
    
    @app.route('/reset')
    def reset():
        # resets datatbase
        DB.drop_all()
        #creates database again    
        DB.create_all()
        return render_template('base.html', titel='Home')
        
    
    return app

"""


    return app