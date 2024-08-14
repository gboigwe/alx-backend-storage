#!/usr/bin/env python3
"""Operating mongoDB using pymongo"""


def schools_by_topic(mongo_collection, topic):
    """Function for having a specific topic
    in a list of school"""
    docs = mongo_collection.find({"topics": topic})
    return list(docs)
