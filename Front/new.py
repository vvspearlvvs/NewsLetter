from pymongo import MongoClient

import Emailing
import Crawling

def connect_DB(host,port):
    mongo = MongoClient(host, int(port))
    print("DB Connect Success")
    return mongo

def insert_DB(document_list,collection):
    for document in document_list:
        collection.insert_one(document)
    return "insert success"

def find_DB(collection):
    result = collection.find()
    for i in result:
        print(i)


def main():
    document_list = Crawling.get_crawling_aws()
    print(document_list)

    #Emailing.create_html(document_list,post())


if __name__ == '__main__':
    main()
