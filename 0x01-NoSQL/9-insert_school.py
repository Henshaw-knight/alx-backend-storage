#!/usr/bin/env python3
"""insert_school function module"""


def insert_school(mongo_collection, **kwargs):
    """function that inserts a new document in a collection based on kwargs"""
    added_document = mongo_collection.insert_one(kwargs)
    return added_document.inserted_id
