from django.contrib.auth.models import User
from rest_framework import fields
from sensors.models import Sensor
from rest_framework import serializers
from django.utils import encoding

# MongoDB codex packages; should be available in most python distributions
from bson import objectid
from bson.objectid import InvalidId

...
class ObjectIdField(serializers.Field):
    """ Serializer field for Djongo ObjectID fields """
    def to_internal_value(self, data):
        # Serialized value -> Database value
        try:
            return objectid(str(data))  # Get the ID, then build an ObjectID instance using it
        except InvalidId:
            print("invalid id error exceptions")


    def to_representation(self, value):
        # Database value -> Serialized value
        if not objectid.is_valid(value):  # User submitted ID's might not be properly structured
            raise InvalidId
        return str(value)
...
# class YourModelSerializer(ModelSerializer):
#     _id = ObjectIdField(read_only=True)

#     class Meta:
#         model = YourModel
#         fields = '__all__'

class SensorSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex')
    status = serializers.JSONField()
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
