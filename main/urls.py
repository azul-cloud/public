from django.conf.urls import patterns, url
from main import views

urlpatterns = patterns('',
    #main
    url(r'^$', views.home, name="home"),
)