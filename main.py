import os
import certifi
import json
from fastapi import FastAPI
from pymongo import MongoClient
from typing import Annotated


app = FastAPI()

password = os.environ.get('MONGO_PASSWORD')
username = os.environ.get('MONGO_USERNAME')
atlas_ip = os.environ.get('ATLAS_IP')

mongo_uri = f'mongodb+srv://{username}:{password}@{atlas_ip}/?retryWrites=true&w=majority&appName=Cluster1'

client = MongoClient(mongo_uri, tlsCAFile=certifi.where())
db = client.sample_mflix
collection = db.comments

@app.get("/")
async def index():
    return "running"
    
@app.get("/get-doc")
async def index():
    r = collection.find_one({"name":"Mercedes Tyler"})
    data = {'name': r['name'], 'text':r['text']}

    return json.dumps(data)
