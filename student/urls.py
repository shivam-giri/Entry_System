from django.conf.urls import url
from django.contrib import admin
from student import views
urlpatterns = [
    url(r'^$', views.EnterReg),
    url(r'^fetchDetails/$', views.fetchDetails),
    url(r'^saveDetails/$', views.saveDetails),
]
