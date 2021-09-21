from django.shortcuts import render
import requests
from . models import *
from . serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer 
from django.http import HttpResponse
from django.core import serializers
# for deserialisation
import io
from rest_framework.parsers import JSONParser
from . serializers import StudentSerializersAdd
from . serializers import StudentUpdate
from . serializers import StudentDelete
from django.views.decorators.csrf import csrf_exempt

from api import serializers
# Create your views here.

def studentdetails(request):
    # sid = Student.objects.get(id = 1)
    sid = Student.objects.get(email = "pinalpatel@gmail.com")
    if sid:
        sid.password = "123456"
        serializer = StudentSerializers(sid)
        print("--------> serializer", serializer)
        # convert serialized data into json
        json_data = JSONRenderer().render(serializer.data)
        print("--------> json_data", json_data)
        return HttpResponse(json_data,content_type = "application/json")

def getall(request):
    sid = Student.objects.all()
    serializer = StudentSerializers(sid,many = True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type = "application/json")

def student_get(request,pk):
    sid = Student.objects.get(id = pk)
    if sid:
        serializer = StudentSerializers(sid)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type = "application/json")

def student_city(request,city):
    sid = Student.objects.filter(city = city)
    if sid:
        serializer = StudentSerializers(sid,many = True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type = "application/json")

# Deserialize
@csrf_exempt                    
def studentadd(request):
    if request.method == "POST":  # POST = to add/insert data
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializersAdd(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {"msg":"successfully saved data"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type = "application/json")

@csrf_exempt
def studentUpdate(request):
    if request.method == "PUT":   #  PUT = to update data
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id = id)
        serializer = StudentUpdate(stu,data = pythondata,partial = True)

        if serializer.is_valid():
            serializer.save()
            res = {"msg":"Successfully data updated"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type = "application/json")
        else:
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data,content_type = "application/json")

@csrf_exempt
def studentDelete(request):
    if request.method == "DELETE":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id = id)
        stu.delete()
        res = {"msg":"Successfully deleted data"}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data,content_type = "application/json")
            
   
