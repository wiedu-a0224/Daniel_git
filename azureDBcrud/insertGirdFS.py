from pymongo import MongoClient
import gridfs

Client=MongoClient("mongodb://localhost:27017/")
db=Client.GridFSDatabase
fs=gridfs.GridFS(db)

def WriteGridFS(imageFilename):
    with open(imageFilename, "rb") as imageFile:
        imageBinary=imageFile.read()
        id=fs.put(imageBinary, filename=imageFilename)
        print(f"紀錄ID:{id}")
        return id

def ReadGridFS(id, outFilename):
    imageBinary=fs.get(id).read()
    with open(outFilename, "wb") as imageFile:
        imageFile.write(imageBinary)

id=WriteGridFS("Images/IMG.jpg")
ReadGridFS(id,"IMG.jpg")
Client.close()