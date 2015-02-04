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

from .models import Project, Hours, Invoice
from .forms import ProjectForm

from braces.views import StaffuserRequiredMixin


class HomeTemplateView(TemplateView):
    template_name = "internal/content/home.html"


##### INVOICING #####
class HoursListView(ListView):
    template_name = 'internal/content/hours/all_active.html'
    queryset = Hours.objects.filter(invoice=None)


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
        invoice.rate = project.pay_amount
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

        # add invoice start and end dates and save
        invoice.start_date = start_date
        invoice.end_date = end_date
        invoice.save()

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


class InvoiceListView(ListView):
    # Display all invoices and allow to edit
    template_name = 'internal/content/invoice/home.html'
    model = Invoice


class ProjectListView(ListView):
    # Display a list of all projects
    model = Project
    template_name = "internal/content/project/project_list.html"


class ProjectUpdateView(UpdateView):
    # Update an existing project
    model = Project
    template_name = "internal/content/project/update_project.html"
    form_class = ProjectForm


