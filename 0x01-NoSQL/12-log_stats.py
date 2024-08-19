#!/usr/bin/env python3
"""Python script that provides some stats about Nginx logs stored in
MongoDB in the required way"""
from pymongo import MongoClient


def count_all_necessary_docs_by_query(collection):
    """Counts and prints out the necessary result after the query"""
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


def run():
    """Connects to the MongoDB server and runs the above function"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx
    count_all_necessary_docs_by_query(nginx_collection)


if __name__ == "__main__":
    run()
