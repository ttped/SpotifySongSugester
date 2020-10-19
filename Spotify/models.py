from flask_sqlalchemy import SQLAlchemy


DB = SQLAlchemy()

class Song(DB.Model):
    """Twitter Users corresponding to Tweets"""
    name = DB.Column(DB.String, nullable=False)
    accousticness= DB.Column(DB.Integer, nullable=False)
    artists= DB.Column(DB.String, nullable=False)
    danceability= DB.Column(DB.Integer, nullable=False)
    duration_ms= DB.Column(DB.Integer, nullable=False)
    energy= DB.Column(DB.Integer, nullable=False)
    explicit= DB.Column(DB.Integer, nullable=False)
    id= DB.Column(DB.String, nullable=False, primary_key=True)
    instrumental= DB.Column(DB.Integer, nullable=False)
    key= DB.Column(DB.Integer, nullable=False)
    liveness= DB.Column(DB.Integer, nullable=False)
    loudness= DB.Column(DB.Integer, nullable=False)
    mode = DB.Column(DB.Integer, nullable=False)
    name= DB.Column(DB.String, nullable=False)



    def __repr__(self):
        return "<Song: {}>".format(self.name)
