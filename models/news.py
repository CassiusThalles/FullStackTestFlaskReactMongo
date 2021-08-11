"""
This is responsible to create the News data Model
"""
from config.db import db, app

class News(db.Document):
    """
    Creation of the model
    - title: StringField is the title of the news
    - content: StringField is the content of the news
    - publish: DateTimeField is the publishing date of the news
    """
    title = db.StringField(max_length=200, required=True)
    content = db.StringField()
    publish = db.DateTimeField(required=True)
    