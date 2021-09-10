from sensors_services.settings import SECRET_KEY
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from lights.models import Light
# from sensors.serializers import  ScheduleSerializer
from rest_framework import viewsets, status
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import logging
import boto3
from botocore.exceptions import ClientError


from . import lightView

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello, Flight Scheduler!</h1>")

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     # serializer_class = UserSerializer


@csrf_exempt
def getLight(request, light_id):
    return JsonResponse({'foo': str(light_id)})
    # # return HttpResponse("<h1>Hello, Flight Scheduler!</h1>")
    # return lightView.create(request)

@csrf_exempt
def getLigtsListOrCreate(request):

    
    if request.method == 'GET':
        try:
            s3_client = boto3.client('s3', region_name="us-east-1", 
                aws_access_key_id="AKIAWV4YFBTBIV2KGF5U",
                aws_secret_access_key="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")
            
            
            # s3 = boto3.client(
            #     "s3",
            #     aws_access_key_id="AKIAWV4YFBTBIV2KGF5U",
            #     aws_secret_access_key="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",
            # )


            bucket_name = "sujon-s3-va",
            key='wedding/file.jpg',
            sec_key = "DIQK8j/7M70/SabV9XbBOhb38k9yzz9lZQPPEPWR"
            fields={"Content-Type": "image/jpg"},
            # conditions=["starts-with", "$Content-Type", "image/"],
            response = s3_client.generate_presigned_post(Bucket = bucket_name,
                                                        Key = key,
                                                        Fields=fields,
                                                        
                                                        ExpiresIn=3600)
            print(response)
            return HttpResponse("<h1>Hello, Flight Scheduler!</h1>")
        except ClientError as e:
            logging.error(e)
            return None


        return HttpResponse(response)
        # schedules = Light.objects.all()
        # for i in Light.objects.all().iterator():
        #     print(i)
        # schedule_serializer = ScheduleSerializer(schedules, many=True)
    #    return JsonResponse({'list': [1,2,3]})

    if request.method == 'POST':
        schedule_data = JSONParser().parse(request)
        schedule_serializer = ScheduleSerializer(data = schedule_data)
        if schedule_serializer.is_valid():
            schedule_serializer.save()
            return JsonResponse(schedule_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(schedule_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'DELETE':
        pass
        # Schedule.objects.all().delete()
    #     return HttpResponse(status=status.HTTP_204_NO_CONTENT) 
