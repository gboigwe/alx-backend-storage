#!/usr/bin/env python3
"""Function for updating topics of a school document in MongoDB"""

def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name.

    Args:
        mongo_collection: pymongo object collection
        name (str): document name to update
        topics (list of str): List of topics taken in school
    """
    result = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    return
