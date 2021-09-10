from django.db import models

# Create your models here.
class Light(models.Model):
    name =            models.CharField(max_length=50)
    ip =              models.CharField(max_length=50)
    broker =          models.CharField(max_length=50)
    sub_topic           = models.CharField(max_length=50)
    pub_topic           = models.CharField(max_length=50)
    payload   = models.CharField(max_length=100)
    status     = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name + ',' + self.broker
        