import pymongo

username = "felipe"
password = "123"
mongo_client = pymongo.MongoClient('mongodb://127.0.0.1:27017/', username=username, password=password)

db = mongo_client["accounts"]

print(mongo_client.list_database_names())

col = db["customers"]

# x = col.insert_one({
#     "id": 1,
#     "name": "John",
#     "number": 123,
# })

# print(x.inserted_id)

# print(col.find()[0])
for doc in col.find():
    print(doc)

# db.company.insert_many([
#     {"id": 1},
#     {"id": 2},
#     {"id": 3},
#     {"id": 4},
#     {"id": 5}
# ])

# dblist = mongo_client.list_database_names()
# if "company" in dblist:
#     print("The database exists.")

mongo_client.close()