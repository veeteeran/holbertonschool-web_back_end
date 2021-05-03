#!/usr/bin/env python3
"""list_all function module"""


def list_all(mongo_collection):
    """Lists all documents in a collection"""
    return mongo_collection.find() or []


if __name__ == "__main__":
    list_all(mongo_collection)
