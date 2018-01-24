from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index), 
    url(r'^register$', views.register), 
    url(r'^login$', views.login), 
    url(r'^logout$', views.logout), 
    url(r'^home$', views.home), 
    url(r'^show/(?P<id>\d+)$', views.show), 
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^addFriend/(?P<id>\d+)$', views.addFriend)
]