from django.contrib.auth.models import User
from rest_framework import serializers
from sensors.models import Sensor


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url','username','email')
        
class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = (  'id',
                    'name',
                    'ip', 
                    'broker', 
                    'stat_topic', 
                    'command_topic',
                    'payload', 
                    'mac',
                    'status'
        )

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Person
#         fields = (  'id',
#                     'name',
#                     'email', 
#                     'password'
#         )
