#!/usr/bin/env python3
"""schools_by_topic function module"""


def schools_by_topic(mongo_collection, topic):
    """Function that returns the list of school having a specific topic"""
    result = mongo_collection.find({"topics": {"$in": [topic]}})
    return result
