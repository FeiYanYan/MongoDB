# 肥彥彥
# 開發時間: 2021/5/12 下午 08:37
from pymongo import MongoClient


# Put your connection code in a class so that it can be reused.
class Connect(object):
    @staticmethod
    def get_connection():
        return MongoClient(
            "mongodb+srv://wilson6610:w6455i555@cluster0.zxojh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
