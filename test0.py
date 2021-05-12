# 肥彥彥
# 開發時間: 2021/5/11 下午 11:08
import pymongo

# Connect to MongoDB Atlas
client = pymongo.MongoClient(
    "mongodb+srv://wilson6610:w6455i555@cluster0.zxojh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test

# Create a new database on your cluster
# We have already established our client connection and
# stored it in a variable called client.
# Run the following command in your Python shell to create a database
# on your cluster:
# db = client.test

# Create a collection for your database.
# Run the following command in your
# Python shell to create a new collection for your database:
# people = db.people
# This command creates a new collection in your test database called people.
# The variable people points to your new collection.
