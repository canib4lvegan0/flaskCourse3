from flask_jwt import jwt_required
from flask_restful import Resource, reqparse

from models.user import UserModel
from utils import convert_to_dec_or_alpha


def _user_parser(to):
    parser = reqparse.RequestParser()

    if to == 'post':
        parser.add_argument('username', type=str, required=True, help='Invalid cannot be blank!')
        parser.add_argument('password', type=str, required=True, help='Invalid cannot be blank!')

    if to == 'put':
        parser.add_argument('username', type=str, required=False)

    return parser


# noinspection PyUnreachableCode
class UserRegister(Resource):
    def post(self):
        data = _user_parser('post').parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': 'This username already exists'}, 409

        new_user = UserModel(**data)

        try:
            new_user.save_to_db()
            return {'message': 'User created successfully.'}, 201

        except new_user.SQLAlchemyError as ex:
            return {'message': ex}, 500


# noinspection PyUnreachableCode
class UserId(Resource):
    @jwt_required()
    def get(self, param):
        converted = convert_to_dec_or_alpha(param)

        result = None
        if type(converted) == str:
            result = UserModel.find_by_username(converted)
        elif type(converted) == int:
            result = UserModel.find_by_id(int(converted))
        else:
            return {'message': 'Invalid parameter.'}, 400

        if result:
            return result.to_json(), 200
        return {'message': 'User not found'}, 404

    @jwt_required()
    def put(self, param):
        converted = convert_to_dec_or_alpha(param)

        result = None
        if type(converted) == str:
            result = UserModel.find_by_username(converted)
        elif type(converted) == int:
            result = UserModel.find_by_id(int(converted))
        else:
            return {'message': 'Invalid parameter.'}, 400

        if result is None:
            return {'message': 'User not found'}, 404

        data = _user_parser('put').parse_args()

        try:
            result.username = data['username']
            result.save_to_db()
            return {'id': result.id}, 201
        except result.SQLAlchemyError as ex:
            return {'message': ex}, 500


# noinspection PyUnreachableCode
class Users(Resource):

    @jwt_required()
    def get(self):
        if result := UserModel.get_users():
            users = [u.to_json() for u in result]
            return {'users': users}, 200
        else:
            return {}, 404