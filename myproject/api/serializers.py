from rest_framework import serializers
from . models import *

class StudentSerializers(serializers.Serializer):
    firstname = serializers.CharField(max_length=20)
    lastname = serializers.CharField(max_length=20)
    email = serializers.CharField(max_length=30)
    contact = serializers.CharField(max_length=30)
    city = serializers.CharField(max_length=30,default="Ahmedabad")

class StudentSerializersAdd(serializers.Serializer):
    firstname = serializers.CharField(max_length=20)
    lastname = serializers.CharField(max_length=20)
    email = serializers.CharField(max_length=30)
    contact = serializers.CharField(max_length=30)
    city = serializers.CharField(max_length=30,default="Ahmedabad")

    def create(self,validatedata):
        return Student.objects.create(**validatedata)

class StudentUpdate(serializers.Serializer):
    firstname = serializers.CharField(max_length=20)
    lastname = serializers.CharField(max_length=20)
    email = serializers.CharField(max_length=30)
    contact = serializers.CharField(max_length=30)
    city = serializers.CharField(max_length=30,default="Ahmedabad")

    def update(self,obj,validate_data):
        obj.firstname = validate_data.get('firstname',obj.firstname)
        obj.lastname = validate_data.get('lastname',obj.lastname)
        obj.email = validate_data.get('email',obj.email)
        obj.contact = validate_data.get('contact',obj.contact)
        obj.city = validate_data.get('city',obj.city)

        obj.save()
        return obj

class StudentDelete(serializers.Serializer):
    firstname = serializers.CharField(max_length=20)
    lastname = serializers.CharField(max_length=20)
    email = serializers.CharField(max_length=30)
    contact = serializers.CharField(max_length=30)
    city = serializers.CharField(max_length=30,default="Ahmedabad")

    def delete(self,obj,validate_data):
        obj.firstname = validate_data.get('firstname',obj.firstname)
        obj.lastname = validate_data.get('lastname',obj.lastname)
        obj.email = validate_data.get('email',obj.email)
        obj.contact = validate_data.get('contact',obj.contact)
        obj.city = validate_data.get('city',obj.city)

        obj.delete()