#!/usr/bin/env python3
"""schools_by_topic function module"""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of school having a specific topic"""
    return mongo_collection.find({'topics': topic})


if __name__ == "__main__":
    schools_by_topic(mongo_collection, topic)
