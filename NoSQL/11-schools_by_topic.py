#!/usr/bin/env python3
"""
Module that returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Retrieve a list of schools from a MongoDB collection
    that have a specific topic.

    Args:
        mongo_collection: A pymongo collection object.
        topic: The topic to filter schools by.

    Returns:
        A list of school documents that contain the specified topic.
    """
    return [data for data in mongo_collection.find({"topics": topic})]
