#!/usr/bin/env python3
"""Function that inserts a new document in a
collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    Function for insertion in a MongoDB collection
    based on kwargs.

    Args:
    mongo_collection: object collection for pymongo
    **kwargs: Representing keyword arguments.
    
    Returns
    str: new _id of an inserted document
    """
    return = mongo_collection.insert(kwargs)


if __name__ == "__main__":
    pass
