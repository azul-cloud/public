from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

from django.contrib.sitemaps import GenericSitemap
from flowblog.models import Post


blog_info_dict = {
    'queryset': Post.objects.filter(active=True),
    'date_field': 'create_date'
}

sitemaps = {
    "blog": GenericSitemap(blog_info_dict, priority=0.6)
}

urlpatterns = patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT}),
    
    url(r'^', include('main.urls')),
    url(r'^internal/', include('internal.urls')),
    url(r'^blog/', include('flowblog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps})
)
