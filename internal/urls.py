from django.conf.urls import patterns, url

from internal import views

urlpatterns = patterns('',
    #hours
    url(r'hours/$', views.HoursListView.as_view(), name="hours"),
    url(r'hours/(?P<user>\D+)/$', views.PersonHoursListView.as_view(), name="person-hours"),
    url(r'hours/project/(?P<pk>\d+)/$', views.project_hours, name="project-hours"),

    #invoices
    url(r'invoice/$', views.invoices, name="invoices"),
    url(r'invoice/(?P<pk>\d+)/$', views.project_invoice, name="project-invoice"),
    url(r'invoice/(?P<pk>\d+)/details/$', views.project_invoice_details,
            name="project-invoice-details"),

    url(r'^$', views.HomeTemplateView.as_view(), name="internal-home"),
)