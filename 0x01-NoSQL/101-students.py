#!/usr/bin/env python3
"""
This module provides functionality to retrieve and sort students based on
their average score from a MongoDB collection.
"""


def top_students(mongo_collection):
    """Returns a list of students sorted by their average score."""
    students = mongo_collection.aggregate(
        [
            {
                '$project': {
                    '_id': 1,
                    'name': 1,
                    'averageScore': {
                        '$avg': {
                            '$avg': '$topics.score',
                        },
                    },
                    'topics': 1,
                },
            },
            {
                '$sort': {'averageScore': -1},
            },
        ]
    )
    return students
