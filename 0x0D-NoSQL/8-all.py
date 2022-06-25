#!/usr/bin/env python3
""" modul to list all doc in collection using pymongo"""


def list_all(mongo_collection):
    """
    list all documents in collection
    """
    if mongo_collection is None:
        return []
    return mongo_collection.find()
