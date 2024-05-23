import datetime
from pymongo import MongoClient
import threading
import random

def GetData():     #Gen Data
    NewData={
        "裝置": random.choice("ABCDE"),    # A, D, E, C, A, ....
        "溫度": random.randrange(0, 100),
        "時間": datetime.datetime.now()
    }
    Client = MongoClient("mongodb://localhost:27017/")
    #-------
    db=Client.IoTDatabase
    col=db.IoTDatabase
    Id=col.insert_one(NewData).inserted_id
    print(f"記錄Id:{Id}")
    #-------
    Client.close()
    threading.Timer(10, GetData).start()

if __name__== "__main__":
    GetData()