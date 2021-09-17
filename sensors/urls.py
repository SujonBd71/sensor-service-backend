from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
     # url(r'^$', views.index, name='index'),
    url(r'^$', views.getSensorsOrCreate,name='lights'),
    url(r'^(?P<sensor_id>[0-9]+)/$', views.getSensor,name='light'),

]
