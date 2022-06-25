#!/usr/bin/env python3
""" Modul that inserts a new document in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """
    function to insert new do to collection
    """
    for arg in kwargs.values():
        return mongo_collection.insertOne(arg).inserted_id 