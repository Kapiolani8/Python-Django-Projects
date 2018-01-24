from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^amadon/buy$', views.amadon_buy),
    url(r'^success$', views.success)

]