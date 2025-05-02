#!/usr/bin/env python3
"""Module that inserts a new document into a MongoDB collection"""
def insert_school(mongo_collection, **kwargs):
    """Inserts a new document into the given MongoDB collection.

    Args:
        mongo_collection: pymongo collection object.
        **kwargs: key-value pairs to insert as the document.

    Returns:
        The _id of the newly inserted document.
    """
    return mongo_collection.insert_one(kwargs).inserted_id
