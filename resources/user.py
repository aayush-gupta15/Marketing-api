from flask_restful import Resource, reqparse
from flask import jsonify, request
from flask_jwt_extended import create_access_token, jwt_required
from flask_jwt_extended import current_user

from model.user import UserModel
from application.utils.encoder import AlchemyEncoder
import json
from application.utils.logger import create_logger


class User(Resource):
    def __init__(self):
        self.__logger = create_logger()

    def post(self):
        data = request.get_json()
        username = data['username']
        password = data['password']

        user = UserModel.query.filter_by(username=username).one_or_none()
        if not user or not user.verify_password(password):
            self.__logger.info(f'Wrong username or password')
            return {'message': 'Wrong username or password.'}, 401
        access_token = create_access_token(
            identity=json.dumps(user, cls=AlchemyEncoder))
        return jsonify(access_token=access_token)

    @jwt_required()  # Requires data token
    def get(self):
        return jsonify(
            id=current_user.id,
            full_name=current_user.full_name,
            username=current_user.username,
        )


class UserRegister(Resource):
    def __init__(self):
        self.__logger = create_logger()

    def post(self):
        data = request.get_json()
        username = data['username']
        password = data['password']

        if UserModel.find_by_username(username):
            self.__logger.info(f'User already exist')
            return {'message': 'UserModel has already been created, aborting.'}, 400

        user = UserModel(username = username)
        user.hash_password(password)
        user.save_to_db()
        self.__logger.info(f'User created successfully')
        return {'message': 'user has been created successfully.'}, 201