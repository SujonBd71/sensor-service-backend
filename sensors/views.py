from django.shortcuts import render
from MQTT import MQTTRepo
# Create your views here.
from sensors_services.settings import SECRET_KEY
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from sensors.serializers import SensorSerializer
from sensors.models import Sensor

from rest_framework import viewsets, status
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import logging
import boto3
from botocore.exceptions import ClientError
import uuid

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello, Flight Scheduler!</h1>")

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     # serializer_class = UserSerializer


@csrf_exempt
def getSensor(request, sensor_id):
    print(request)
    # light = Light(name="living room")
    if request.method == 'GET':
        light= Sensor.objects.get(id= uuid.UUID(sensor_id))
        repo= MQTTRepo.getRepo()
        print(light.stat_topic)
        light.status = repo.getStat(light.stat_topic)
        print(light.stat_topic)
        tutorials_serializer = SensorSerializer(light)
    
        print(tutorials_serializer)
        return JsonResponse(tutorials_serializer.data, safe=False)
    
    if request.method == 'PUT':
        light= Sensor.objects.get(id= uuid.UUID(sensor_id))
        tutorial_data = JSONParser().parse(request)
        tutorial_data['id'] = uuid.uuid4()
        tutorial_serializer = SensorSerializer(data=tutorial_data)
        print(tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_200_OK) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@csrf_exempt
def getSensorsOrCreate(request):
    print(request)
    
    if request.method == 'GET':
        tutorials = Sensor.objects.all()

        repo= MQTTRepo.getRepo()
        for t in tutorials:
            t.status =  repo.getStat(t.stat_topic)

        tutorials_serializer = SensorSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)

    if request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        # tutorial_serializer = tutorial_data
        tutorial_data['id'] = uuid.uuid4()
        tutorial_serializer = SensorSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

