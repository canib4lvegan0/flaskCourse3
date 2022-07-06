from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from sqlalchemy.exc import SQLAlchemyError

from models.item import ItemModel


def _item_parser(to):
    parser = reqparse.RequestParser()
    if to == 'post':
        parser.add_argument('title', type=str, required=True, help="Title cannot be blank.")
        parser.add_argument('description', type=str, required=False, help="Description invalid.")
        parser.add_argument('price', type=float, required=True, help="Price cannot be blank.")
        parser.add_argument('store_id', type=int, required=True, help="Every item needs a store_id.")

    if to == 'put':
        parser.add_argument('title', type=str, required=False)
        parser.add_argument('description', type=str, required=False)
        parser.add_argument('price', type=float, required=False)
        parser.add_argument('store_id', type=int, required=False)

    return parser


# noinspection PyUnreachableCode
class ItemRegister(Resource):
    def post(self):
        data = _item_parser('post').parse_args()
        new_item = ItemModel(**data)

        try:
            new_item.save_to_db()
            return {'message': 'Item created successfully.'}, 201
        except SQLAlchemyError as ex:
            return {'message': ex.__str__()}, 500


# noinspection PyUnreachableCode
class ItemId(Resource):
    def get(self, _id):
        if result := ItemModel.find_by_id(_id):
            return {'item': result.to_json()}

    @jwt_required()
    def put(self, _id):
        data = _item_parser('put').parse_args()

        if result := ItemModel.find_by_id(_id):
            result.title = data['title']
            result.description = data['description']
            result.price = data['price']
            result.price = data['store_id']

            result.save_to_db()

            return {'id': result.id}, 201
        else:
            return {'message': 'Item not found'}, 404

    @jwt_required()
    def delete(self, _id):

        if result := ItemModel.find_by_id(_id):
            result.delete_from_db()
            return {'id': result.id}, 200

        return {'message': 'Item not found'}, 404


# noinspection PyUnreachableCode
class Items(Resource):
    def get(self):
        if result := ItemModel.get_items():
            items = [i.to_json() for i in result]
            return {'items': items}, 200
        else:
            return {}, 404
