#!/usr/bin/env python3
"""Provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


client = MongoClient()
db = client.logs
collection = db.nginx

total = collection.count_documents({})
get = collection.count_documents({'method': 'GET'})
post = collection.count_documents({'method': 'POST'})
put = collection.count_documents({'method': 'PUT'})
patch = collection.count_documents({'method': 'PATCH'})
delete = collection.count_documents({'method': 'DELETE'})
status = collection.count_documents({'method': 'GET', 'path': '/status'})
nl = '\n'

print(f"{total} logs{nl}\
Methods:{nl}\
    method GET: {get}{nl}\
    method POST: {post}{nl}\
    method PUT: {put}{nl}\
    method PATCH: {patch}{nl}\
    method DELETE: {delete}{nl}\
{status} status check")
