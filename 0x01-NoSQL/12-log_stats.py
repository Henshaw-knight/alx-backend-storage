#!/usr/bin/env python3
"""Python script that provides some stats about Nginx logs stored in
MongoDB in the required way"""
from pymongo import MongoClient


"""Connect to the MongoDB server"""
client = MongoClient(host="localhost", port=27017)
db = client.logs
collection = db.nginx

"""Count all documents in the collection"""
total_log_count = collection.count_documents({})

"""Count all documents in the collection with a GET method"""
get_method_count = collection.count_documents({"method": "GET"})

"""Count all documents in the collection with a POST method"""
post_method_count = collection.count_documents({"method": "POST"})

"""Count all documents in the collection with PUT method"""
put_method_count = collection.count_documents({"method": "PUT"})

"""Count all documents in the collection with PATCH method"""
patch_method_count = collection.count_documents({"method": "PATCH"})

"""Count all documents in the collection with DELETE method"""
delete_method_count = collection.count_documents({"method": "DELETE"})

"""Count all documents in the collection with status path"""
status_path_count = collection.count_documents({"path": "/status"})

print(f"{total_log_count} logs")
print("Methods:")
print(f"\tmethod GET: {get_method_count}")
print(f"\tmethod POST: {post_method_count}")
print(f"\tmethod PUT: {put_method_count}")
print(f"\tmethod PATCH: {patch_method_count}")
print(f"\tmethod DELETE: {delete_method_count}")
print(f"{status_path_count} status check")
