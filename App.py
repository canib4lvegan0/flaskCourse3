import os

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api

from db import db

from resources.aline import Aline
from resources.home import Home
from resources.item import ItemRegister, Items, ItemId
from resources.store import StoreRegister, StoreId, Stores
from resources.user import UserRegister, UserLogin, Users, UserId, UserProfile

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'robsu'
app.config['JWT_AUTH_URL_RULE'] = '/login'
app.config['PROPAGATE_EXCEPTIONS'] = True

api = Api(app)
jwt = JWTManager(app)  # /not creating auth endpoint

@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return UserLogin.get_user_by_id(_id=identity)

@jwt.additional_claims_loader
def add_claims_to_jwt(user):
    if user.id == int(os.environ.get('ADMIN', '1')):
        return {'is_admin': True}
    return {'is_admin': False}


api.add_resource(ItemRegister, '/item_register', methods=['POST'])
api.add_resource(ItemId, '/item/<int:_id>', methods=['GET', 'PUT', 'DELETE'])
api.add_resource(Items, '/items', methods=['GET'])
api.add_resource(UserRegister, '/user_register', methods=['POST'])
api.add_resource(UserLogin, '/login', methods=['POST'])
api.add_resource(UserId, '/user/<param>', methods=['GET', 'PUT', 'DELETE'])
api.add_resource(Users, '/users', methods=['GET'])
api.add_resource(UserProfile, '/my_profile', methods=['GET'])
api.add_resource(StoreRegister, '/store_register', methods=['POST'])
api.add_resource(StoreId, '/store/<int:_id>', methods=['GET', 'PUT', 'DELETE'])
api.add_resource(Stores, '/stores', methods=['GET'])

api.add_resource(Aline, '/aline', methods=['GET'])
api.add_resource(Home, '/', methods=['GET'])


if os.environ.get('ENVIRONMENT') == 'dev':
    import run
    run.init(app, db)
else:
    db.init_app(app)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
