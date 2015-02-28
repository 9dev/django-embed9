from django.conf.urls import patterns, url

from main import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^images$', views.ImageListView.as_view(), name='image_list'),
    url(r'^texts$', views.TextListView.as_view(), name='text_list'),
    url(r'^image/(?P<pk>\d+)$', views.ImageDetailView.as_view(), name='image_detail'),
    url(r'^text/(?P<pk>\d+)$', views.TextDetailView.as_view(), name='text_detail'),
)

