
# Create your models here.
from django.db import models
import uuid

# Create your models here.
class Sensor(models.Model):
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name =            models.CharField(max_length=50)
    ip =              models.CharField(max_length=50)
    broker =          models.CharField(max_length=50)
    command_topic           = models.CharField(max_length=50)
    stat_topic           = models.CharField(max_length=50)
    payload   = models.CharField(max_length=100, blank=True)
    mac = models.CharField(max_length=50)
    status     = models.JSONField(max_length=500)
    
    def __str__(self):
        return self.name + ',' + self.broker
        