from django.conf.urls import url

from . import views 

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register), 
    url(r'^home$', views.home), 
    url(r'^logout$', views.logout), 
    url(r'^show/(?P<id>\d+)$', views.show),
    url(r'^edit$', views.edit), 
    url(r'^add_newUser$', views.add_newUser)
]