#!/usr/bin/env python3
"""
Script that provides some stats about Nginx logs stored in MongoDB
"""
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
my_db = myclient['logs']
col = my_db['nginx']

get = 0
post = 0
put = 0
patch = 0
delete = 0
number_docs = 0

for doc in col.find():
    if doc['method'] == 'GET':
        get += 1
    elif doc['method'] == 'POST':
        post += 1
    elif doc['method'] == 'PUT':
        put += 1
    elif doc['method'] == 'PATCH':
        patch += 1
    elif doc['method'] == 'DELETE':
        delete += 1
    number_docs += 1

print(f"{number_docs} logs")
print("Methods:")
print(f'\tmethod GET: {get}')
print(f'\tmethod POST: {post}')
print(f'\tmethod PUT: {put}')
print(f'\tmethod PATCH: {patch}')
print(f'\tmethod DELETE: {delete}')
