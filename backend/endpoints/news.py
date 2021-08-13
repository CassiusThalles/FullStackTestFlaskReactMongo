from werkzeug.wrappers import response
from models.news import News as modelNews
from flask import request, jsonify
import json, datetime

def list_all_news():
    news = modelNews.objects().to_json()
    news = json.loads(news)
    response = jsonify(news)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response, 200

def create_news(data):
    req = json.loads(data)
    req['publish'] = datetime.datetime.now().strftime('%H:%M:%S %d/%m/%Y')
    try:
        news = modelNews(**req).save()
    except Exception as exc:
        return jsonify({'exception': str(exc)}), 400
    id = news.id
    return jsonify({'id': str(id)}), 201

def list_news(id):
    news = modelNews.objects().get(id=id).to_json()
    news = json.loads(news)
    return jsonify(news), 200

def update_news(id, data):
    req = json.loads(data)
    req['publish'] = datetime.datetime.now().strftime('%H:%M:%S %d/%m/%Y')
    model_news = modelNews.objects(id=id)
    try:
        model_news.update(**req)
    except Exception as exc:
        return jsonify({'exception': str(exc)}), 400
    return jsonify({'status': 'Notícia atualizada com sucesso'}), 200

def destroy_news(id):
    try:
        modelNews.objects(id=id).delete()
    except Exception as exc:
        return jsonify({'exception': str(exc)}), 400
    return jsonify({'status': 'Notícia deletada com sucesso'}), 204