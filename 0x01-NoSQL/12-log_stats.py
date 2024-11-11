#!/usr/bin/env python3
''' A Python3 Module '''


from pymongo import MongoClient


def log_start():
    '''
    provides some stats about Nginx logs stored in MongoDB
    '''
    params = MongoClient()
    mongo_caller = params.logs
    collection_caller = mongo_caller.nginx

    log_count = collection_caller.count_documents({})
    print(f"{log_count} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods: ")

    for method in methods:
        counts_method = collection_caller.count_documents({"method": method})
        print(f"\tmethod {method}: {counts_method}")

    status_check = collection_caller.count_documents({
        "method": "GET", "path": "/status"
        })

    print(f"{status_check} status check")


if __name__ == "__main__":
    log_start()
