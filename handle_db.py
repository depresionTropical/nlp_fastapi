from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import dotenv_values
config = dotenv_values(".env")


class Database():
    client = MongoClient(config["ATLAS_URI"])
    db = client[config["DB_NAME"]]

    def get_all(self):
        return self.db.users.find()
        
    
    def get_one(self, id:str):
        return self.db.users.find_one({"_id": ObjectId(id)})
    def insert_one(self, data):
        return self.db.users.insert_one(data)
    
    
