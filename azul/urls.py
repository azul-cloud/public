from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

from django.contrib.sitemaps import GenericSitemap
from internal.models import Task
from flowblog.models import Post

task_info_dict = {
    'queryset': Task.objects.all(),
    'date_field': 'create_date'
}

blog_info_dict = {
    'queryset': Post.objects.filter(active=True),
    'date_field': 'create_date'
}

sitemaps = {
    "task": GenericSitemap(task_info_dict, priority=0.6),
    "blog": GenericSitemap(blog_info_dict, priority=0.6)
}

urlpatterns = patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}),
    url(r'^', include('main.urls')),
    url(r'^internal/', include('internal.urls')),
    url(r'^blog/', include('flowblog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps})
)
