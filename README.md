# REST_API_Flask
A simple RESTful API (Store, Item, User) created with Python Flask, Flask-RESTful, Flask-SQLalchemy

# Introduction
The api have three parts: Stores, items and Users.
A user can login in and post/delete/put/get items or Stores.

# Database initalize – Flask-sqlalchemy
db.py inialize the database SQLite3 : db = SQLAlchemy()

# Folder "models", inherite from db.Model: database Configuration and methods
class ItemModel: 
table'items': id(primary_key), name(String), price(Float), store_id(Integer, foreign_key('stores.id')
method: __init__, json, find_by_name, save_to_db, delete_from_db

class StoreModel:
table'stores': id(primary_key), name(String), items('ItemModel')
method: __init__, json, save_to_db, delete_from_db, find_by_name(classmethod)

class UserModel:
table'users': id(primary_key), username(String), password(String)
method: __init__, save_to_db, find_by_username(classmethod), find_by_id(classmethod)

# Folder "resources", inherite from Resource(flask_restful): deal with requests from users
class Item: get(name), post(name), delete(name), put(name)
class ItemList: get

class Store: get(name), post(name), delete(name)
class StoreList: get

class UserRegister: post

# security.py: authenticate(), identity
# app.py
Flask_api configuration of endpoint
1. User authenticate: /auth
2. User Register: /register
3. Store/StoreList/Item/ItemList endpoint
