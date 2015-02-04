from django.conf.urls import patterns, url

from internal import views

urlpatterns = patterns('',
    #hours
    url(r'hours/$', views.HoursListView.as_view(), name="hours"),
    url(r'hours/project/(?P<pk>\d+)/$', views.project_hours, name="project-hours"),

    #invoices
    url(r'invoices/$', views.invoices, name="invoices"),
    url(r'invoice/(?P<pk>\d+)/$', views.project_invoice, name="project-invoice"),
    url(r'invoice/(?P<pk>\d+)/details/$', views.project_invoice_details,
            name="project-invoice-details"),

    #projects
    url(r'projects/$', views.ProjectListView.as_view(), name="projects"),
    url(r'project/(?P<pk>\d+)/$', views.ProjectUpdateView.as_view(), 
        name="project-update"),

    url(r'^$', views.HomeTemplateView.as_view(), name="internal-home"),
)