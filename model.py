"""Models for Spotify App."""
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
import os

db = SQLAlchemy()

@dataclass
class User(db.Model):
    user_id: int
    access_token: str
    refresh_token: str
    expiration: str
    spotify_id: str

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    access_token = db.Column(db.String, nullable=False)
    refresh_token = db.Column(db.String, nullable=False)
    expiration = db.Column(db.String, nullable=False)
    spotify_id = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<User id={self.user_id} access={self.access_token}'


@dataclass
class SavedPlaylist(db.Model):
    savedPlaylist_id: int
    user_id: int
    orig_playlist_id: str
    saved_playlist_id: str
    interval: str
    title: str

    __tablename__ = "savedPlaylists"

    savedPlaylist_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    orig_playlist_id = db.Column(db.String, nullable=False)
    saved_playlist_id = db.Column(db.String, nullable=False)
    interval = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<SavedPlaylist title={self.title} user_id={self.user_id}>'


def example_data():
    """Create sample data for testing."""

    # In case this query runs more than once, remove existing data
    SavedPlaylist.query.delete()
    User.query.delete()

    # Populate with sample user and playlists
    user1 = User(
        user_id = 1,
        access_token = os.environ['ACCESS_TOKEN'],
        refresh_token = os.environ['REFRESH_TOKEN'],
        expiration = os.environ['EXPIRATION'],
        spotify_id = os.environ['SPOTIFY_USER']
    )

    # savedPlaylist = SavedPlaylist(
    #     user_id = 1, 
    #     orig_playlist_id = '37i9dQZEVXcHh9eQliKRvV',
    #     saved_playlist_id = '2PBhJSpglqQCo5ND349wNs',
    #     interval = 'weekly', 
    #     title='VCR DB Test Playlist'
    # )

    db.session.add(user1)
    db.session.commit()



def connect_to_db(flask_app, db_uri='postgresql:///spotify_db', echo=False):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
