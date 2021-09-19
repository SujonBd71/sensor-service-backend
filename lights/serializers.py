from django.contrib.auth.models import User
from rest_framework import serializers
from lights.models import Light

class LightSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex')
    class Meta:
        model = Light
        fields = ('id',
                  'name',
                    'ip', 
                    'broker', 
                    'stat_topic', 
                    'command_topic',
                    'payload', 
                    'mac',
                    'status'
        )

