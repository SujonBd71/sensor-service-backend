from django.conf.urls import url
from . import views

app_name = 'lights'

# 'polls/<str:poll_id>'
# path('polls/<str:poll_id>', views.polls_detail)

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.getLigtsListOrCreate,name='lights'),
    # url(r'^(?P<light_id>[a-f0-9]+)/$', views.getLight,name='light'),
    url(r'^(?P<light_id>[\w\-]+)/$', views.getLight,name='light'),
    # url(r'^(?P<string>[\w\-]+)/$', views.getLight,name='light'),
    # url('slug:light_id/$', views.getLight,name='light'),
    # url(r'^(?P<album_id>[0-9]+)/delete_album/$', views.getLight, name='delete_album'),

    # url(r'^register/$', views.register, name='register'),
    # url(r'^login_user/$', views.login_user, name='login_user'),
    # url(r'^logout_user/$', views.logout_user, name='logout_user'),
    # url(r'^sensors/$', views.sensors, name='sensors'),

    # url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    # url(r'^(?P<song_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    # url(r'^songs/(?P<filter_by>[a-zA_Z]+)/$', views.songs, name='songs'),
    # url(r'^create_album/$', views.create_album, name='create_album'),
    # url(r'^(?P<album_id>[0-9]+)/create_song/$', views.create_song, name='create_song'),
    # url(r'^(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),
    # url(r'^(?P<album_id>[0-9]+)/favorite_album/$', views.favorite_album, name='favorite_album'),
    # url(r'^(?P<album_id>[0-9]+)/delete_album/$', views.delete_album, name='delete_album'),
]
