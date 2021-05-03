#!/usr/bin/env python3
"""insert_school function module"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection based on kwargs"""
    return mongo_collection.insert(kwargs)


if __name__ == "__main__":
    insert_school(mongo_collection, **kwargs)
