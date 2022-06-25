#!/usr/bin/env python3
""" Modul that inserts a new document in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """
    function to insert new do to collection
    """
    return mongo_collection.insert_one(kwargs).inserted_id
