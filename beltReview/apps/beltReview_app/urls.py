from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register), 
    url(r'^login$', views.login),
    url(r'^home$', views.home), 
    url(r'^message/(?P<id>\d+)$', views.new_message),
    url(r'^add_message/(?P<id>\d+)$', views.add_message), 
    url(r'^view_messages$', views.view_messages)
]