
# Create your models here.
from django.db import models

# Create your models here.
class Sensor(models.Model):
    name =            models.CharField(max_length=50)
    ip =              models.CharField(max_length=50)
    broker =          models.CharField(max_length=50)
    command_topic           = models.CharField(max_length=50)
    stat_topic           = models.CharField(max_length=50)
    payload   = models.CharField(max_length=100, blank=True)
    mac = models.CharField(max_length=50)
    status     = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name + ',' + self.broker
        