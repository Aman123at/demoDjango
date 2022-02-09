from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from demoapp.models import Todo
from demoapp.serializer import TodoSerializer
from pymongo import MongoClient
from bson.json_util import dumps, loads
import json

# Create your views here.
@csrf_exempt

def get_db_handle(db_name, url):
    client = MongoClient(url)
    db_handle = client[db_name]
    return db_handle, client
def get_collection_handle(db_handle,collection_name):
    return db_handle[collection_name]

def TodoApi(request,id=0):
    if request.method == "GET":
        url = "mongodb+srv://aman:12345@cluster0.iqbtk.mongodb.net/bigstack?retryWrites=true&w=majority"
        db_handle, mongo_client = get_db_handle("bigstack", url)
        collection_handle = get_collection_handle(db_handle, "myquestions")
        data = collection_handle.find({})
        list_cur = list(data)
        json_data = dumps(list_cur) 
        
        return JsonResponse(json.loads(json_data),safe=False)
    
        