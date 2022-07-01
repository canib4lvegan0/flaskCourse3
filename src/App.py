from flask import Flask
from flask_restful import Api
from flask_jwt import JWT, timedelta
from security import authenticate, identity

from src.resources.user import UserRegister, Users, UserId
from src.resources.item import ItemRegister, Items, ItemId
from src.resources.store import StoreRegister, StoreId, Stores
# from src.db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'robsu'
api = Api(app)
app.config['JWT_EXPIRATION_DELTA'] = timedelta(minutes=60)
app.config['JWT_AUTH_URL_RULE'] = '/login'

jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(ItemId, '/item/<int:_id>')
api.add_resource(Items, '/items')
api.add_resource(ItemRegister, '/item_register')
api.add_resource(UserRegister, '/user_register')
api.add_resource(Users, '/users')
api.add_resource(UserId, '/user/<param>', methods=['GET', 'PUT'])
api.add_resource(StoreRegister, '/store_register', methods=['POST'])
api.add_resource(StoreId, '/store/<int:_id>', methods=['GET', 'PUT', 'DELETE'])
api.add_resource(Stores, '/stores', methods=['GET'])


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
