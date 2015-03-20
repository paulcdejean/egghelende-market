from django.conf.urls import patterns, url

from market import views

urlpatterns = patterns('',
    url(r'^$', views.items, name='items'),
)
