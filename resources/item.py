from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource): 
    parser = reqparse.RequestParser()
    parser.add_argument('price',
            type = float,
            required = True,
            help = 'this field cannot be left blank')

    parser.add_argument('store_id',
            type = int,
            required = True,
            help = 'this field cannot be left blank')


    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name) # return an ItemModel object
        if item:
            return item.json() # return a dict
        return {"message": "item not found"}, 404    
    
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {"message": "An item with name '{}' already exists.".format(name)}, 400  # bad request 400

        data = Item.parser.parse_args()
        item = ItemModel(name, **data) # create an ItemModel object

        try:
            item.save_to_db()
        except:
            return {"message: " "An error occured inserting the item"}, 500 # Internal error

        return item.json(), 201 # created successfully: 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {'message': 'Item deleted'}

    def put(self, name):
        data = Item.parser.parse_args()        
        
        item = ItemModel.find_by_name(name) # return an ItemModel object

        if item is None:
            item = ItemModel(name, **data)  # create an ItemModel object if object not exists
        else:
            item.price = data['price']
            item.store_id = data['store_id']

        item.save_to_db()
        return item.json() # return a dict


class ItemList(Resource):
    def get(self): 
        return {'items': [item.json() for item in ItemModel.query.all()]}
        #return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}
        