"""
This is responsible to create the User data Model
"""
from config.config import db, app

class User(db.Document):
    """
    Creation of the model
    """
    public_id = db.StringField(max_length=50, unique=True)
    name = db.StringField(max_length=100)
    email = db.StringField(max_length=70, unique=True)
    password = db.StringField(max_length=200)
    