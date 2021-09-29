from sensors_services.settings import SECRET_KEY
from django.shortcuts import render
import uuid

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from lights.models import Light
from lights.serializers import  LightSerializer
from rest_framework import viewsets, status
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import logging
import boto3
from botocore.exceptions import ClientError
from MQTT import MQTTRepo

from . import lightView

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello, Flight Scheduler!</h1>")

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     # serializer_class = UserSerializer


@csrf_exempt
def getLight(request, light_id):
    # light = Light(name="living room")
    print(light_id)
    light= Light.objects.get(id=uuid.UUID(light_id))
    repo= MQTTRepo.getRepo()
    print(light.stat_topic)
    light.status = repo.getStat(light.stat_topic)
    print(light.stat_topic)
    tutorials_serializer = LightSerializer(light)
 
    print(tutorials_serializer)
    return JsonResponse(tutorials_serializer.data, safe=False)

@csrf_exempt
def getLigtsListOrCreate(request):
    print("Request recvd")
    print(request)
    
    if request.method == 'GET':
        tutorials = Light.objects.all()
        print(tutorials)
        repo= MQTTRepo.getRepo()
        for t in tutorials:
            t.status =  repo.getStat(t.stat_topic)
        
        tutorials_serializer = LightSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)

    if request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        print("json parsed data")
        print(tutorial_data)
        tutorial_data['id'] = uuid.uuid4()
        tutorial_serializer = LightSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            print("saving new object")
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   
