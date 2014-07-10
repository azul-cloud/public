from datetime import date, timedelta
# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "azul.settings")

from django.shortcuts import render
from django.core.mail import EmailMessage
# from django.conf import settings
from django.template import Context
from django.template.loader import get_template

from internal.models import Task, Project


# Create your views here.
def client_status_emails(request):
    '''
    this function will get the status emails that are to be sent to clients
    we will get the tasks from the previous day. Sometimes the task will be
    completed after midnight but the completed day we're still going to mark
    as the previous day.
    '''

    yesterday = date.today() - timedelta(1)
    projects = Project.objects.filter(active=True)

    for p in projects:
        #get list of tasks that need to be sent for each project
        #tasks = Task.objects.filter(project=p)
        tasks = Task.objects.filter(project=p, complete_date=yesterday,
                                    sent_date=None, notify_client=True)

        #add the contacts to send the email
        project_contacts = []
        for c in p.contacts.filter(project=p):
            project_contacts.append(c.email)

        #build the email and send it
        msg = EmailMessage('Azul Cloud Studio - Completed Tasks',
                            get_template('internal/email/status.html').render(
                                Context({
                                    'tasks':tasks,
                                    'yesterday':yesterday
                                })
                            ),
                            'awwester@gmail.com',#settings.EMAIL_HOST_USER,
                            project_contacts
                          )
        msg.content_subtype = "html"  # Main content is now text/html
        msg.send()

    return render(request, 'internal/content/status_email.html',
        {'tasks':tasks, 'yesterday':yesterday})
