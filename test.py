# 肥彥彥
# 開發時間: 2021/5/12 上午 12:23
import pymongo
import datetime

# Create a new document to insert into your collection.
# 指令將 document 除存在變數 personDocument，還沒儲存到 Collection
client = pymongo.MongoClient(
    "mongodb+srv://wilson6610:w6455i555@cluster0.zxojh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test
people = db.people # Create a collection

personDocument = {
    "name": {"first": "Alan", "last": "Turing"},
    "birth": datetime.datetime(1912, 6, 23),
    "death": datetime.datetime(1954, 6, 7),
    "contribs": ["Turing machine", "Turing test", "Turingery"],
    "views": 1250000
}

# Insert the document into your collection
# people.insert_one (personDocument)
# the people variable refers to our people collection we specified in
# a previous step of this section, and personDocument contains
# the document we want to insert.

# View Your Cluster Data
# reading that data with the PyMongo find_one () method.
# The following command returns one document from the people collection
# that has a name.last value of Turing:
# people.find_one ({"name.last": "Turing"})
