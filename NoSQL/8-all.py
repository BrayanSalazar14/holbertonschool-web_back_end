#!/usr/bin/env python3
"""
Module that lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    Retrieve all documents from a MongoDB collection.

    Args:
        mongo_collection: A pymongo collection object.

    Returns:
        A list containing all documents in the collection.
    """
    return [col for col in mongo_collection.find({})]
