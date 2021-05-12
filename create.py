# 肥彥彥
# 開發時間: 2021/5/12 下午 08:38
from connect import Connect
from pymongo import MongoClient

# Call the class you just created
connection = Connect.get_connection()

# To access the test database:
client = MongoClient(
    "mongodb+srv://wilson6610:w6455i555@cluster0.zxojh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test

# Retrieve all documents in the inventory collection:
cursor = db.inventory.find({})

from pprint import pprint

for inventory in cursor:
    pprint(inventory)
