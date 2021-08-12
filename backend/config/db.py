"""
This is the database configure file 
"""
from . import app
from flask import Flask
from flask_mongoengine import MongoEngine
from dotenv import load_dotenv
import os

load_dotenv()

db = MongoEngine()

app.config['MONGODB_SETTINGS'] = {
    'db': os.environ.get('MONGODB_DATABASE'),
    'host': os.environ.get('MONGODB_URI'),
    # 'host': os.environ.get('MONGODB_HOST'),
    # 'port': int(os.environ.get('MONGODB_PORT'))
}

db.init_app(app)