from pymongo import MongoClient

# database
host = "localhost"
port = "27017"

mongo_client = MongoClient(host, int(port))
database = mongo_client.get_database('mydb')

def connect_DB(host,port):
    mongo_client = MongoClient(host, int(port))
    database = mongo_client.get_database('mydb')
    return database

def insert_document(document_list,collection):
    for document in document_list:
        collection.insert_one(document)
    return "insert success"

def find_DB(collection):
    result = collection.find()
    for i in result:
        print(i)

#input crawling data
def insert_data(document_list):
    database = connect_DB(host,port)
    aws_col = database.get_collection('aws') #있으면 안넣고, 없는 데이터만 넣기
    #collection.delete_many({})

    insert_document(document_list,aws_col)
    #find_DB(collection)

#input email data
def insert_email(email):
    database = connect_DB(host,port)
    email_col =database.get_collection('email')

    email_document={"email":email}
    email_col.insert_one(email_document)
    print("insert "+email_document['email']+" success!")

def find_email(collection):
    database = connect_DB(host,port)
    email_col =database.get_collection(collection)

    result = email_col.find()
    return result