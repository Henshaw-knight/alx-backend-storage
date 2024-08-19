#!/usr/bin/env python3
"""Python script that provides some stats about Nginx logs stored in
MongoDB in the required way"""
from pymongo import MongoClient


"""Connect to the MongoDB server"""
client = MongoClient(host="localhost", port=27017)
db = client.logs
collection = db.nginx


def count_and_print_stats():
    """Counts and prints the necessary stats"""
    total_log_count = collection.count_documents({})
    get_method_count = collection.count_documents({"method": "GET"})
    post_method_count = collection.count_documents({"method": "POST"})
    put_method_count = collection.count_documents({"method": "PUT"})
    patch_method_count = collection.count_documents({"method": "PATCH"})
    delete_method_count = collection.count_documents({"method": "DELETE"})
    status_path_count = collection.count_documents({"path": "/status"})

    print(f"{total_log_count} logs")
    print("Methods:")
    print(f"\tmethod GET: {get_method_count}")
    print(f"\tmethod POST: {post_method_count}")
    print(f"\tmethod PUT: {put_method_count}")
    print(f"\tmethod PATCH: {patch_method_count}")
    print(f"\tmethod DELETE: {delete_method_count}")
    print(f"{status_path_count} status check")


count_and_print_stats()
