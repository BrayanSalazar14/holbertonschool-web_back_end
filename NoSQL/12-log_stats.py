#!/usr/bin/env python3
"""
Script that provides some stats about Nginx logs stored in MongoDB
"""
if __name__ == "__main__":
    import pymongo
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    my_db = myclient['logs']
    col = my_db['nginx']
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print(f'{col.count_documents({})} logs')
    print('Methods:')
    for method in methods:
        print('\t' + f'method {method}: ',
              col.count_documents({'method': method}))
    status_check = col.count_documents({'path': '/status'})
    print(status_check, 'status check')
