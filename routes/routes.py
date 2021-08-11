from config.db import db, app
from models.news import News as modelNews
from flask import request, jsonify
import json

@app.route('/news', methods=['GET'])
def get_news():
    news = modelNews.objects().to_json()
    news = json.loads(news)
    return jsonify(news), 200
