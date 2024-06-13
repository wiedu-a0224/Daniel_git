from pymongo import MongoClient
import bson.binary 

Client=MongoClient("mongodb://localhost:27017/")
#=========
db=Client.BSONDatabase
col=db.BSONCollection

with open("Images/IMG.jpg", "rb") as imageFile:
    imageBinary=bson.binary.Binary(imageFile.read())
    id=col.insert_one({
        "fileName":"IMG.jpg",
        "data":imageBinary
    }).inserted_id
    print(f"紀錄ID:{id}")

imageDocument=col.find_one({"fileName": "IMG.jpg"})
with open("IMG.jpg", "wb") as imageFile:
    imageFile.write(imageDocument["data"])

Client.close()