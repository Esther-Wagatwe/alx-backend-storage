#!/usr/bin/env python3
"""module to insert school document in a collection"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.

    :param mongo_collection: pymongo collection object
    :param kwargs: key-value pairs to insert as document fields
    :return: the new _id of the inserted document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
