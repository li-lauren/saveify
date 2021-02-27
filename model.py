"""Models for Spotify App."""
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass

db = SQLAlchemy()

@dataclass
class User(db.Model):
    user_id: int
    access_token: str
    refresh_token: str
    expiration: str

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    access_token = db.Column(db.String, nullable=False)
    refresh_token = db.Column(db.String, nullable=False)
    expiration = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<User id={self.user_id} access={self.access_token}'


@dataclass
class SavedPlaylist(db.Model):
    savedPlaylist_id: int
    user_id: int
    spotify_id: str
    orig_playlist_id: str
    saved_playlist_id: str
    interval: str
    title: str

    __tablename__ = "savedPlaylists"

    savedPlaylist_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    spotify_id = db.Column(db.String, nullable=False)
    orig_playlist_id = db.Column(db.String, nullable=False)
    saved_playlist_id = db.Column(db.String, nullable=False)
    interval = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<SavedPlaylist title={self.title} user_id={self.user_id}>'


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
