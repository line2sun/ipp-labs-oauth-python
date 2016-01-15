from flask import jsonify, request

from oAuth import app
from models import User
import services.user as UserService
import routes


@app.route(routes.USERS, methods=['GET'])
def index():
    result = [user for user in User.objects()]
    return jsonify({'result': result})


@app.route(routes.USERS_REGISTER, methods=['GET'])
def users_register():
    client = request.args.get('app_id', '')
    name = request.args.get('name', '')
    email = request.args.get('email', '')
    password = request.args.get('password', '')

    if not client or not email or not password:
        return jsonify({'code': 2})

    token, code = UserService.register(client=client,
                                name=name,
                                email=email,
                                password=password)

    if token is None:
        return jsonify({'code': code})

    return jsonify({'token': token, 'code': code})


@app.route(routes.USERS_LOGIN, methods=['GET'])
def user_login():
    client = request.args.get('app_id', '')
    email = request.args.get('email', '')
    password = request.args.get('password', '')

    if not email or not client or not password:
        return jsonify({'code': 2})

    token, code = UserService.login(client=client,
                                    email=email,
                                    password=password)

    if token is None:
        return jsonify({'code': code})

    return jsonify({'token': token, 'code': code})


@app.route(routes.USERS_LAST_LOGIN, methods=['GET'])
def user_last_login():
    client = request.args.get('app_id', '')
    email = request.args.get('email', '')
    token = request.args.get('token', '')

    if not email or not client or not token:
        return jsonify({'code': 2})

    last_login, code = UserService.get_last_login(client=client,
                                                  email=email,
                                                  token=token)

    if last_login is None:
        return jsonify({'code': 2})

    return jsonify({'last_login': last_login, 'code': code})