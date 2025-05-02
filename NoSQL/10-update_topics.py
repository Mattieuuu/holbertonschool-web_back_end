#!/usr/bin/env python3
"""Module to update topics of a school document"""
def update_topics(mongo_collection, name, topics):
    """Updates all topics of a school document based on the school name.

    Args:
        mongo_collection: pymongo collection object.
        name (str): school name to match.
        topics (list of str): list of topics to set.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
