#!/usr/bin/env python3
"""
This module provides a function to update the topics of a school document
in a MongoDB collection based on the school's name.
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates all documents in the collection where the 'name' field matches the
    provided name, setting the 'topics' field to the specified list of topics.

    Parameters:
    - mongo_collection: The pymongo collection object.
    - name (str): The name of the school whose topics need to be updated.
    - topics (list of str): The list of topics to set for the school.
    """
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
