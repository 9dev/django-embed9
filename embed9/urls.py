from django.conf.urls import patterns, url

from embed9 import views

urlpatterns = patterns('',
    url(r'^widget/(?P<app>[0-9a-z_.]+)/(?P<model>[0-9a-z_]+)/(?P<pk>\d+)$', views.widget, name='widget'),
)
