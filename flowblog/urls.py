from django.conf.urls import patterns, url

from flowblog import views

urlpatterns = patterns('',
    url(r'post/(?P<slug>\S+)/$', views.PostDetailView.as_view(), name="blog-post"),
    url(r'tag/(?P<slug>\S+)/$', views.TagListView.as_view(), name="blog-tag"),
    url(r'$', views.HomeListView.as_view(), name="blog-home"),
)