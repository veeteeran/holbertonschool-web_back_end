#!/usr/bin/env python3
"""update_topics function module"""


def update_topics(mongo_collection, name, topics):
    """Changes all topics of a school document based on the name"""
    mongo_collection.update({'name': name}, {'$set': {'topics': topics}})


if __name__ == "__main__":
    insert_school(mongo_collection, name, topics)
