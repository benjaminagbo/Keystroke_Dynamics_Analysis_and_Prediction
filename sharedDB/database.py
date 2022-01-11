import pymongo
import os
from flask_pymongo import pymongo
from pymongo import MongoClient
from flask import Flask



class Database(object):
    #app = Flask(__name__)
    #app.config["MONGO_URI"] = "mongodb+srv://Benjamin:Benjamin123@cluster0.qhttk.mongodb.net/Bank"
    #mongo = pymongo(app)

    DATABASE = None
    #URI = os.environ.get("mongodb+srv://Benjamin:Benjamin123@cluster0.qhttk.mongodb.net/Bank")
    MONGO_URI = "mongodb+srv://Benjamin:Benjamin123@cluster0.qhttk.mongodb.net/Bank"
    @staticmethod
    def initialize():
        clients =MongoClient(Database.MONGO_URI)
        Database.DATABASE = clients['Bank']

    @staticmethod
    def insert(self, collection, data):
        #data=0
        for i in range(len(collection)):
            if collection[i]==data:
                data=data+1
        #return data
        Database.DATABASE[collection].insert(data)



    @staticmethod
    def find(self, collection, query):
        return Database.DATABASE[collection].find(self,query)

    @staticmethod
    def find_one(collection, query):
        # print(collection,query)
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def find_collection(collection):
        return Database.DATABASE[collection].find()

    @staticmethod
    def update(collection, query, values):
        Database.DATABASE[collection].update_one(query, values)
        return Database.DATABASE[collection]

    @staticmethod
    def delete_one_record(collection, query):
        # print(collection,query)
        return Database.DATABASE[collection].delete_one(query)

    @staticmethod
    def delete_many_record(collection, query):
        # print(collection,query)
        return Database.DATABASE[collection].delete_many(query)
