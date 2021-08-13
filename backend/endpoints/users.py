from dotenv.main import load_dotenv
from models.user import User
from flask import request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from dotenv import load_dotenv
from config import app
from datetime import date, datetime, timedelta
import jwt, uuid, json

load_dotenv()

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message': 'Token is required'}), 401
        
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms="HS256")
            user = User.objects().get(public_id=data['public_id'])
        except:
            return jsonify({'message': 'Invalid Token'}), 401
        return f(user, *args, **kwargs)
    return decorated

def list_all_users():
    users = User.objects().to_json()
    users = json.loads(users)
    response = jsonify(users)
    return response, 200

def login_method():
    auth = request.form

    if not auth or not auth.get('email') or not auth.get('password'):
        return make_response(
            'The email or password is incorrect!',
            401,
            {'WWW-Authenticate' : 'Basic realm ="Login required !!"'}
        )
    user = User.objects().get(email = auth.get('email'))
    if not user:
        return make_response(
            'The email or password is incorrect!',
            401,
            {'WWW-Authenticate' : 'Basic realm ="Login required !!"'}
        )
    if check_password_hash(user.password, auth.get('password')):
        token = jwt.encode({
            'public_id': user.public_id,
            'exp': datetime.utcnow() + timedelta(days=2)
        }, app.config['SECRET_KEY'], algorithm="HS256")
        return make_response( jsonify({'token': token}), 201)
    return make_response(
        'The email or password is incorrect!',
        401,
        {'WWW-Authenticate' : 'Basic realm ="Login required !!"'}
    )

def sign_up_method():
    data = request.form

    name, email = data.get('name'), data.get('email')
    password = data.get('password')

    try:
        user = User.objects().get(email=email)
    except:
        user = None

    if not user:
        try:
            insert_data = {
                'public_id': str(uuid.uuid4()),
                'name': name,
                'email': email,
                'password': generate_password_hash(password)
            }
            user = User(**insert_data).save()
            id = user.id
        except Exception as exc:
            return jsonify({'exception': str(exc)}), 400
        return jsonify({'id': str(id), 'message': 'User successfully created'}), 201
    else:
        return make_response(
            'User already exists. Please log in',
            202
        )

def update_method(id):
    data = request.data
    data = json.loads(data)
    data['password'] = generate_password_hash(data['password'])
    user = User.objects().get(id=id)
    try:
        user.update(**data)
    except Exception as exce:
        return jsonify({'exception': str(exc)}), 400
    return jsonify({'status': 'Usuário atualizado com sucesso'}), 200

def destroy_user(id):
    try:
        User.objects(id=id).delete()
    except Exception as exc:
        return jsonify({'exception': str(exc)}), 400
    return jsonify({'status': 'Usuário deletado com sucesso'}), 204