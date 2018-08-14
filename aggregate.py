from flask import Flask


def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():
    # complete the aggregation pipeline
    pipeline = [{"$match": {"region": "Köln"}},
                {"$unwind": "$skills"},
                {"$group": {"_id": "$skills", 
                            "count": {"$sum": 1}
                }},
                {"$sort": {"count": -1 }},
                {"$limit": 5}
                ]
    return pipeline

def aggregate(db, pipeline):
    return [doc for doc in db.itproject2.aggregate(pipeline)]

if __name__ == '__main__':
    db = get_db('projectfinder')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    print("Printing the first result:")
    import pprint
    pprint.pprint(result)
    

