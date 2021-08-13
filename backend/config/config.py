"""
This is the database configure file 
"""
from . import app
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

db = MongoEngine()

CORS(app)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

app.config['MONGODB_SETTINGS'] = {
    'db': os.environ.get('MONGODB_DATABASE'),
    'host': os.environ.get('MONGODB_URI'),
    # 'host': os.environ.get('MONGODB_HOST'),
    # 'port': int(os.environ.get('MONGODB_PORT'))
}

db.init_app(app)