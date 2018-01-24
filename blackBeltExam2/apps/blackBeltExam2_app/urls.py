from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index), 
    url(r'^register$', views.register), 
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^home$', views.home), 
    url(r'^addQuote$', views.addQuote), 
    url(r'^addToFavorites$', views.addToFavorites),
    url(r'^addToFavorites/(?P<id>\d+)$', views.addToFavorites), 
    url(r'^delete/(?P<id>\d+)$', views.delete), 
    url(r'^user/(?P<id>\d+)$', views.user)
]