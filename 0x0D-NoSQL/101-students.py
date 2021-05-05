#!/usr/bin/env python3
"""top_students module"""


def top_students(mongo_collection):
    """Returns all students sorted by average score"""
    average_score = mongo_collection.aggregate([
        {'$unwind': {'path': '$topics'}},
        {'$group': {'_id': '$_id',
                    'name': {'$first': '$name'},
                    'averageScore': {'$avg': '$topics.score'}}},
        {'$sort': {'averageScore': -1}}
    ])

    return average_score
