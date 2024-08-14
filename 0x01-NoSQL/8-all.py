#!/usr/bin/env python3
"""Function that list all documents in a collection
using PyMongo operations."""

def list_all(mongo_collection):
    """
    Function lists all documents in collection.

    Args:
    mongo_collection: object of pymongo collection

    Returns:
    list: Returns an empty list if no documents are found.
    """
    doc_collections = list(mongo_collection.find())
    return doc_collections
