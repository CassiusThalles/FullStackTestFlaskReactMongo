from config.config import db, app
from flask import request
from endpoints.news import list_all_news, create_news, update_news, destroy_news, list_news

@app.route('/news', methods=['GET'])
def get_news():
    return list_all_news()

@app.route('/news', methods=['POST'])
def post_news():
    data = request.data.decode('utf-8')
    return create_news(data)

@app.route('/news/<id>', methods=['GET'])
def single_news(id):
    return list_news(id)

@app.route('/news/<id>', methods=['PUT'])
def put_news(id):
    data = request.data.decode('utf-8')
    return update_news(id, data)

@app.route('/news/<id>', methods=['DELETE'])
def delete_news(id):
    return destroy_news(id)