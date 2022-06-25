#!/usr/bin/env python3
""" modul change document of collection"""


def update_topics(mongo_collection, name, topics):
    """
    change doc of collection
    """
    key_name = {'name': name}
    value = {"$set": {"topics": topics}}

    mongo_collection.update_one(key_name, value)
