from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^userpage/(?P<user_id>\d+)$', views.user_info, name='userinfo'),
    url(r'^addfriend/(?P<friend_id>\d+)$', views.add_friend, name='addfriend'),
    url(r'^remove/(?P<friendship_id>\d+)$', views.remove_friend, name='removefriend'),
]
