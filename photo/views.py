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
from sensors_services import auth
import boto3
from botocore.exceptions import ClientError
from botocore.config import Config

AWS_STORAGE_BUCKET_NAME = 'sujon-s3-va',
AWS_STORAGE_BUCKET_NAME = 'sujon-static'

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello, Flight Scheduler!</h1>")

@csrf_exempt
def getPhoto(request, photo_id):
    def generate_presigned_url(bucket_name, object_key, expiry=3600):
        response = None
        client = boto3.client("s3",region_name="us-east-1",
                            aws_access_key_id=auth.aws_auth.key_id,
                            aws_secret_access_key= auth.aws_auth.secret_key)
        try:
            response = client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,'Key': object_key},
                                                    ExpiresIn=expiry)
            print(response)
        except ClientError as e:
            print(e)
        return response
    
    res = generate_presigned_url(AWS_STORAGE_BUCKET_NAME, 'testfolder/file1.txt')
    print(res)

    return JsonResponse({'url': res})


def create_presigned_upload(expiration=3600):
    s3_client = boto3.client("s3", config=Config(signature_version='s3v4'),
                             region_name="us-east-1",
                             aws_access_key_id=auth.aws_auth.key_id,
                             aws_secret_access_key=auth.aws_auth.secret_key
                             )
    try:
        response = s3_client.generate_presigned_post(Bucket=AWS_STORAGE_BUCKET_NAME,
                                                     Key="testfolder/file1.txt",
                                                     ExpiresIn=3600)

        print(response)
    except ClientError as e:
        return None

    # The response contains the presigned URL and required fields
    return response


@csrf_exempt
def getPhotoList(request):
    if request.method == 'GET':
       resp  = create_presigned_upload()

       return JsonResponse(resp)