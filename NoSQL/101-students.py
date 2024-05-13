#!/usr/bin/env python3
"""
Module that returns all students sorted by average score
"""


def top_students(mongo_collection):
    """
    Calculates the average score for each student in a MongoDB collection
    containing information about students and their scores in different topics.
    Updates the collection by adding an 'averageScore' field for each student
    with their calculated average score.

    Args:
        mongo_collection: A pymongo collection object representing the MongoDB
            collection containing student information.

    Returns:
        A pymongo cursor pointing to a query result containing
        documents of students
        sorted by their average score in descending order.
    """
    for document in mongo_collection.find():
        add_score = 0
        numbers_score = 0
        for topic in document['topics']:
            add_score += topic['score']
            numbers_score += 1
        average = add_score / numbers_score
        mongo_collection.update_one(
            {"name": document['name']}, {'$set': {'averageScore': average}})
    return mongo_collection.find().sort('averageScore', -1)
