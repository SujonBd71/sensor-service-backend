from django.contrib.auth.models import User
from rest_framework import serializers
from sensors.models import Light
from users.models import Person

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url','username','email')
        
class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Light
        fields = (  'id',
                    'name',
                    'ip', 
                    'broker', 
                    'sub_topic', 
                    'pub_topic',
                    'payload', 
                    'status'
        )

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = (  'id',
                    'name',
                    'email', 
                    'password'
        )
