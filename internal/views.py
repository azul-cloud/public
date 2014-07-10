from datetime import date, timedelta

from django.shortcuts import render, get_object_or_404
from django.core.mail import EmailMessage
from django.conf import settings
from django.template import Context
from django.template.loader import get_template
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect

from internal.models import Task, Project, Hours, Invoice
from internal.forms import TaskForm

from braces.views import StaffuserRequiredMixin

class HomeTemplateView(TemplateView):

    template_name = "internal/content/home.html"


###### TASK VIEWS #####
active_list = ["I", "L", "T", "E"]
inactive_list = ["C", "D"]

class TaskListHomeView(StaffuserRequiredMixin, ListView):
    '''
    View to supply a conglomeration of data sets to be displayed on the
    task home page
    '''

    model = Task
    template_name = "internal/content/task_home.html"
    active_list = ["I", "L"]
    inactive_list = ["C", "D"]

    def get_context_data(self, **kwargs):
        '''
        On the task home we want to get a few lists of data and have the
        user be able to go deeper into those subsets of data. Let's show
        the newest tasks, my tasks, and my active tasks
        '''
        context = super(TaskListHomeView, self).get_context_data(**kwargs)
        context['my_new_tasks'] = Task.objects.filter(assigned_to=self.request.user,
                                                        status="N")
        context['my_active_tasks'] = Task.objects.filter(assigned_to=self.request.user,
                                                        status__in=active_list)
        context['my_closed_tasks'] = Task.objects.filter(assigned_to=self.request.user,
                                                        status__in=inactive_list)
        return context


class TaskListView(StaffuserRequiredMixin, ListView):
    '''
    used for all the functional task views for ALL tasks, aka not filtered
    to the current user
    '''
    template_name = "internal/content/tasks.html"

    def get_queryset(self): #, **kwargs
        '''
        for now we have a user kwarg and a filter kwarg. The user kwarg will
        get a value of my, all, or a username. The filter right will have things
        such as active, inactive, new, completed, etc
        '''
        filter = self.kwargs['filter']
        user = self.kwargs['user']

        #start with all and then filter down
        qs = Task.objects.all()

        if user == "my":
            qs = qs.filter(assigned_to=self.request.user)

        if filter == "active":
            qs = qs.filter(status__in=active_list)
        elif filter == "inactive":
            qs = qs.filter(status__in=inactive_list)
        elif filter == "new":
            qs = qs.filter(status="N")

        return qs


class TaskCreateView(StaffuserRequiredMixin, CreateView):

    model = Task
    template_name = "internal/content/task_create.html"
    form_class = TaskForm
    success_url = reverse_lazy('task-create')

    def get_context_data(self, **kwargs):
        context = super(TaskCreateView, self).get_context_data(**kwargs)
        context['form_title_text'] = "Create New Task"
        return context


class TaskUpdateView(StaffuserRequiredMixin, UpdateView):

    model = Task
    template_name = "internal/content/task_update.html"
    form_class = TaskForm
    success_url = reverse_lazy('tasks',
                                kwargs={'user':'my', 'filter':'active'})


class TaskDeleteView(StaffuserRequiredMixin, DeleteView):

    model = Task


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
        '''
        get list of tasks that need to be sent for each project. If there are no
        tasks that fit the requirements, don't send any email
        '''
        tasks = Task.objects.filter(project=p,
                                    complete_date__isnull=False,
                                    status='C',
                                    sent_date=None,
                                    notify_client=True)

        if tasks:
            #add the contacts to send the email
            project_contacts = []
            for c in p.contacts.filter(project=p):
                project_contacts.append(c.email)

            #build the email and send it
            msg = EmailMessage(p.title + ' - Completed Tasks',
                                get_template('internal/email/status.html').render(
                                    Context({
                                        'tasks':tasks,
                                        'yesterday':yesterday
                                    })
                                ),
                                settings.EMAIL_HOST_USER,
                                project_contacts
                              )
            msg.content_subtype = "html"  # Main content is now text/html
            msg.send()

            #set the sent date which also acts as a sent flag
            for t in tasks:
                t.sent_date = date.today()
                t.save()

    return HttpResponse("Emails sent successfully")


##### HOUR TRACKING #####
class HoursListView(ListView):
    template_name = 'internal/content/hours/all_active.html'
    queryset = Hours.objects.filter(invoice=None)


class PersonHoursListView(ListView):
    template_name = 'internal/content/hours.html'
    model = Hours


def project_hours(request, **kwargs):
    '''
    Active hours against a project. Active hours are defined as not currently
    on an invoice.
    '''
    object_list = Hours.objects.filter(invoice=None, project=kwargs['pk'])
    project = get_object_or_404(Project, id=kwargs['pk'])

    if request.method == "POST":
        #on post create the invoice and then redirect to the invoice page
        invoice = Invoice()
        invoice.project = project
        invoice.invoice_date = date.today()
        invoice.save()

        if 'full' in request.POST:
            # add all active hours to the new invoice
            for h in object_list:
                h.invoice = invoice
                h.save()
        elif 'dates' in request.POST:
            start_date = request.POST['start']
            end_date = request.POST['end']
            # add dates within date range to the new invoice
            object_list = object_list.filter(date__range=(start_date, end_date))

            for h in object_list:
                h.invoice = invoice
                h.save()

        return HttpResponseRedirect(reverse('project-invoice', kwargs={'pk':invoice.id}))

    return render(request, 'internal/content/hours/project_hours.html',
        {'object_list':object_list, 'project':project})


def project_invoice(request, **kwargs):
    '''
    The invoice summary. This shows the general information about what we are
    charging a client
    '''
    invoice = get_object_or_404(Invoice, id=kwargs['pk'])
    invoice_hours = Hours.objects.filter(invoice=invoice)
    project = invoice.project

    if request.method == "POST":
        if 'delete' in request.POST:
            for h in invoice_hours:
                h.invoice = None
                h.save()

            invoice.delete()
            return HttpResponseRedirect(reverse('project-hours', kwargs={'pk':project.id}))
        elif 'email' in request.POST:
            pass

    return render(request, 'internal/content/invoice/summary.html',
         {'project':project, 'invoice':invoice})


def project_invoice_details(request, **kwargs):
    '''
    Shows a list of the hours included on an invoice and details about those hours
    '''
    invoice = get_object_or_404(Invoice, id=kwargs['pk'])
    invoice_hours = Hours.objects.filter(invoice=invoice)
    project = invoice.project

    return render(request, 'internal/content/invoice/detail.html',
        {'project':project, 'invoice_hours':invoice_hours, 'invoice':invoice})


def invoices(request):
    #displays a list of all invoices
    invoices = Invoice.objects.all()

    return render(request, 'internal/content/invoice/home.html',
        {'invoices':invoices})