# MongoDB codex packages; should be available in most python distributions
from bson import objectid
from bson.objectid import InvalidId

...
class ObjectIdField():
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
        return smart_text(value)
...
class YourModelSerializer(ModelSerializer):
    _id = ObjectIdField(read_only=True)

    class Meta:
        model = YourModel
        fields = '__all__'
