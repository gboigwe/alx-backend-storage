#!/usr/bin/env python3
"""Operating mongoDB using pymongo"""


def top_students(mongo_collection):
    """Gets all students sorted out
    by average score"""
    top_student = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return top_student
