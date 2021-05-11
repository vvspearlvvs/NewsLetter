from pymongo import MongoClient
import Crawling

# database
host = "localhost"
port = "27017"

def connect_DB(host,port):
    mongo = MongoClient(host, int(port))
    print("DB Connect Success")
    return mongo

def insert_document(document_list,collection):
    for document in document_list:
        collection.insert_one(document)
    return "insert success"

def find_DB(collection):
    result = collection.find()
    for i in result:
        print(i)

#input crawling data
def insert_data():
    mongo_client = connect_DB(host,port)
    database = mongo_client.get_database('mydb')
    collection =database.get_collection('aws') #있으면 안넣고, 없는 데이터만 넣기
    #collection.delete_many({})

    document_list = Crawling.get_crawling_aws()
    print(document_list)

    insert_document(document_list,collection)
    #find_DB(collection)

def insert_Email(email):
    mongo_client = connect_DB(host,port)
    database = mongo_client.get_database('mydb')
    collection =database.get_collection('email')
    email_document={"email":email}
    collection.insert_one(email_document)
    print("insert email success")
