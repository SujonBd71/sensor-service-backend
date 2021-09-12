from django.contrib.auth.models import User
from rest_framework import serializers
from lights.models import Light


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url','username','email')
        
class LightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Light
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
