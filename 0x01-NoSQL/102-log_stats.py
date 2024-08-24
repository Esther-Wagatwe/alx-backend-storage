#!/usr/bin/env python3
"""
This script connects to a MongoDB database and provides statistics about Nginx
logs stored in the 'nginx' collection of the 'logs' database. It prints the
total number of logs, the number of logs for each HTTP method, the number
of logs for a specific method and path, and the top 10 most present IPs.
"""

from pymongo import MongoClient


def get_nginx_stats():
    """
    Connects to the MongoDB server and retrieves statistics
    from the 'nginx' collection.
    """
    print(f'{nginx_collection.count_documents({})} logs')

    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        req_count = nginx_collection.count_documents({'method': method})
        print(f'\tmethod {method}: {req_count}')

    status_checks_count = nginx_collection.count_documents({'method': 'GET',
                                                            'path': '/status'})
    print(f'{status_checks_count} status check')

    print('IPs:')
    top_ips = nginx_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    for ip in top_ips:
        print(f'\t{ip["_id"]}: {ip["count"]}')


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    get_nginx_stats()
