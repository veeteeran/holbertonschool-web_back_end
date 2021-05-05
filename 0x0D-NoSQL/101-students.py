#!/usr/bin/env python3
"""top_students module"""


def top_students(mongo_collection):
    """Returns all students sorted by average score"""
    average_grades = mongo_collection.aggregate([
        {'$unwind': {'path': '$topics'}},
        {'$group': {'_id': '$_id',
                    'name': {'$first': '$name'},
                    'avgScore': {'$avg': '$topics.score'}}},
        {'$sort': {'avgScore': -1}}
    ])

    return average_grades
