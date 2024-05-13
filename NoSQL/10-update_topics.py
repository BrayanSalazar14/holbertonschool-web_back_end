#!/usr/bin/env python3
"""
Module that changes all topics of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    Update the topics field of a document in a MongoDB collection.

    Args:
        mongo_collection: A pymongo collection object.
        name: The name of the document to be updated.
        topics: The new list of topics to be set for the document.

    Returns:
        None
    """
    new_values = {"$set": {"topics": topics}}
    mongo_collection.update_many({"name": name}, new_values)
