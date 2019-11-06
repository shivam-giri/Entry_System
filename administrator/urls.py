from django.conf.urls import url
from django.contrib import admin
from administrator import views
urlpatterns = [
    url(r'^$', views.admin_login),
    url(r'^verify_admin/$', views.verify_admin),
    url(r'^home/$', views.home),
    url(r'^regStudent/$', views.regStudent),
    url(r'^editStudent/$', views.editStudent),
    url(r'^fetchStudent/$', views.fetchStudent),
    url(r'^searchStudent/$', views.searchStudent),
    url(r'^contactParent/$', views.contactParent),
    url(r'^sendMail/$', views.sendMail),
    url(r'^logout/$', views.admin_logout),
]
