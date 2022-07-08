import os

from flask import Flask
from flask_restful import Api

from flask_jwt_extended import JWTManager

from resources.user import UserRegister, UserLogin, Users, UserId
from resources.item import ItemRegister, Items, ItemId
from resources.store import StoreRegister, StoreId, Stores
from resources.aline import Aline
from resources.home import Home

from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['JWT_SECRET_KEY'] = 'robsu'
api = Api(app)
# app.config['JWT_EXPIRATION_DELTA'] = timedelta(minutes=60)
app.config['JWT_AUTH_URL_RULE'] = '/login'
app.config['PROPAGATE_EXCEPTIONS'] = True

jwt = JWTManager(app)  # /not creating auth endpoint

api.add_resource(ItemRegister, '/item_register')
api.add_resource(ItemId, '/item/<int:_id>')
api.add_resource(Items, '/items')

api.add_resource(UserRegister, '/user_register', methods=['POST'])
api.add_resource(UserLogin, '/login', methods=['POST'])
api.add_resource(UserId, '/user/<param>')
api.add_resource(Users, '/users', methods=['GET'])

api.add_resource(StoreRegister, '/store_register', methods=['POST'])
api.add_resource(StoreId, '/store/<int:_id>', methods=['GET', 'PUT', 'DELETE'])
api.add_resource(Stores, '/stores', methods=['GET'])

api.add_resource(Aline, '/aline', methods=['GET'])
api.add_resource(Home, '/', methods=['GET'])


db.init_app(app)
if __name__ == '__main__':
    app.run(port=5000, debug=True)
