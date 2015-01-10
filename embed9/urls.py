from django.conf.urls import patterns, url
from django.views.decorators.csrf import csrf_exempt

from embed9 import views

urlpatterns = patterns('',
    url(r'^widget/(?P<app>[0-9a-z_.]+)/(?P<model>[0-9a-z_]+)/(?P<pk>\d+)$', views.widget, name='widget'),
    url(r'^loader/(?P<app>[0-9a-z_.]+)/(?P<model>[0-9a-z_]+)/(?P<pk>\d+)$', views.loader, name='loader'),
    url(r'^preview/(?P<app>[0-9a-z_]+)/(?P<model>[0-9a-z_]+)/(?P<pk>\d+)$', csrf_exempt(views.preview), name='preview'),
)
