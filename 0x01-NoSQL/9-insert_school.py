#!/usr/bin/env python3
""" Function that inserts a new document in a
collection based on kwargs """


def insert_school(mongo_collection, **kwargs):
    """ Function for insertion in a MongoDB collection
    based on kwargs"""

    return = mongo_collection.insert(kwargs)
