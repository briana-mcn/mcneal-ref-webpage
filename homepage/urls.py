from django.urls import include, re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^contact/$', views.contact, name='contact'),
    re_path(r'^team/$', views.team, name='team'),

]
