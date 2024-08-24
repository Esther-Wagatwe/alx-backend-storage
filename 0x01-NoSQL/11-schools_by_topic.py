#!/usr/bin/env python3
"""
This module provides a function to find and return a list of schools
that include a specific topic in their 'topics' field
within a MongoDB collection
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of school having a specific topic.

    Parameters:
    - mongo_collection: The pymongo collection object.
    - topic (str): The topic to search for in the 'topics' field.
    """
    return mongo_collection.find({"topics": topic})
