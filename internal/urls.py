from django.conf.urls import patterns, url

from internal import views
from internal.views import HomeTemplateView, TaskListView,  \
    TaskCreateView, TaskUpdateView, TaskDeleteView, TaskListHomeView, \
    HoursListView, PersonHoursListView

urlpatterns = patterns('',
    #tasks
    url(r'tasks/$', TaskListHomeView.as_view(), name="task-home"),
    url(r'tasks/update/(?P<pk>\d+)/$', TaskUpdateView.as_view(), name="task-update"),
    url(r'tasks/delete/(?P<pk>\d+)/$', TaskDeleteView.as_view(), name="task-delete"),
    url(r'tasks/create/$', TaskCreateView.as_view(), name="task-create"),
    url(r'tasks/(?P<user>\D+)/(?P<filter>\D+)/$', TaskListView.as_view(), name="tasks"),

    #hours
    url(r'hours/$', HoursListView.as_view(), name="hours"),
    url(r'hours/(?P<user>\D+)/$', PersonHoursListView.as_view(), name="person-hours"),
    url(r'hours/project/(?P<pk>\d+)/$', views.project_hours, name="project-hours"),

    #invoices
    url(r'invoice/$', views.invoices, name="invoices"),
    url(r'invoice/(?P<pk>\d+)/$', views.project_invoice, name="project-invoice"),
    url(r'invoice/(?P<pk>\d+)/details/$', views.project_invoice_details,
            name="project-invoice-details"),
    # url(r'invoice/(?P<pk>\d+)/delete/$', views.project_invoice_delete,
    #         name="invoice-delete"),

    url(r'emailtest/$', views.client_status_emails),
    url(r'^$', HomeTemplateView.as_view(), name="internal-home"),
)