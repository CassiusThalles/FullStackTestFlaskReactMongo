from config.config import db, app
from flask import request
from endpoints.users import destroy_user, list_all_users, login_method, sign_up_method, token_required, update_method
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

@app.route('/user', methods=['GET'])
@token_required
def get_all_users(user):
    return list_all_users()

@app.route('/user/<id>', methods=['PUT'])
@token_required
def update_user_info(user, id):
    return update_method(id)

@app.route('/user/<id>', methods=['DELETE'])
@token_required
def delete_user(user, id):
    return destroy_user(id)

@app.route('/login', methods=['POST'])
def login():
    return login_method()

@app.route('/signup', methods=['POST'])
def signup():
    return sign_up_method()