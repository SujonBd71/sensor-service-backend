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
from rest_framework.parsers import DataAndFiles, JSONParser
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import logging
import boto3
from botocore.exceptions import ClientError, EndpointConnectionError
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
    if request.method == 'GET':
        print(light_id)
        light= Light.objects.get(id=uuid.UUID(light_id))
        repo= MQTTRepo.getRepo()
        print(light.stat_topic)
        light.status = repo.getStat(light.stat_topic)
        print(light.stat_topic)
        tutorials_serializer = LightSerializer(light)
    
        print(tutorials_serializer)
        return JsonResponse(tutorials_serializer.data, safe=False)
    elif request.method == 'PUT':
        body = JSONParser().parse(request)
        print(body)
        print(body['command_topic'])
        print(body['status'])
        
        MQTTRepo.getRepo().publish (body['command_topic'], body["status"])
 
        return JsonResponse({'foo':'bar'})


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
        tutorial_data['id'] = uuid.uuid4()
        tutorial_serializer = LightSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            print("saving")
            print(tutorial_serializer)
            MQTTRepo.getRepo().addSubscriber(tutorial_data["stat_topic"])
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   
