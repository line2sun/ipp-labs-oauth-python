from flask import jsonify, request
from bson.json_util import dumps
import mongoengine
import json

from oAuth import app, db
from models import User
import services.user as UserService
import routes


@app.route(routes.USERS, methods=['GET'])
def index():
    result = [user for user in User.objects()]
    return jsonify({'result': result})


@app.route(routes.USERS_REGISTER, methods=['GET'])
def users_register():
    name = request.args.get('name', '')
    email = request.args.get('email', '')
    password = request.args.get('password', '')

    user = UserService.register(name=name, email=email, password=password)

    if user is None:
        return jsonify({"status": "FAILED"})

    return jsonify(user.__repr__())





