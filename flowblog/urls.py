from django.conf.urls import patterns, url

from flowblog import views

urlpatterns = patterns('',
    url(r'post/(?P<pk>\d+)/(?P<slug>\S+)/$', views.post, name="blog-post"),
    url(r'tag/(?P<pk>\d+)/(?P<slug>\S+)/$', views.posts_tag, name="blog-tag"),
    url(r'$', views.home, name="blog-home"),
)