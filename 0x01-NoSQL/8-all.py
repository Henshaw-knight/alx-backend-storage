#!/usr/bin/env python3
"""Python script that has a function that lists all documents in a
MongoDB collection"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """Function that lists all documents in a collection"""
    documents_list = []
    for document in mongo_collection.find():
        documents_list.append(document)
    return documents_list
