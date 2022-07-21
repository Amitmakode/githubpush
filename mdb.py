import pymongo
client = pymongo.MongoClient("mongodb+srv://amitkumar:Betul3146@amit.6qzfjzj.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d= {
    "name": "amit",
    "surname": "Kumar",
    "Email": "amit@theresource"
}

l = {"java": "c++", "javascript": "pyhton", "scala":"nodj"}

md= client["mdb"]
coll = md["test"]
coll.insert_one(d)
coll.insert_one(l)

d= {
    "name": "amit",
    "surname": "Kumar",
    "Email": "amit@theresource"