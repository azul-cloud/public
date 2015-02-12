from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Max, Min
from django.core.urlresolvers import reverse

######Choice lists used in CharFields######
JS_LIB_CHOICES = (
    ('J10', 'Jquery 10'),
    ('J21', 'Jquery 2.1'),
)

CSS_LIB_CHOICES = (
    ('BS2', 'Bootstrap 2'),
    ('BS3', 'Bootstrap 3'),
)

DJANGO_VER_CHOICES = (
    ('1.3', '1.3'),
    ('1.5', '1.5'),
    ('1.6', '1.6'),
    ('1.7', '1.7'),
)

WEBSITE_STATUS_CHOICES = (
    ('N', 'New'),
    ('I', 'In Progress'),
    ('P', 'Pending'),
    ('D', 'Closed'),
)

PAY_TYPE_CHOICES = (
    ('P', 'PayPal'),
    ('I', 'In Person')
)

PAY_CYCLE_CHOICES = (
    ('O', 'Irregular'),
    ('W', 'Weekly'),
    ('B', 'Bi-weekly'),
    ('M', 'Monthly')
)

INVOICE_STATUS_CHOICES = (
    ('P', 'Pending'),
    ('S', 'Sent'),
    ('C', 'Paid'),
    ('W', 'Waived'),
    ('O', 'Overdue')
)

class Contact(models.Model):
    '''
    separating out the contact allows us to have multiple contacts per client or
    project
    '''
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Client(models.Model):
    name = models.CharField(max_length=30)
    contacts = models.ManyToManyField(Contact, null=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    '''
    projects are tied to a specific client and can have items tied to the project
    such as a website, mobile app, consulting, or other things that pop up. Right
    now we just have website
    '''
    client = models.ForeignKey(Client)
    contacts = models.ManyToManyField(Contact, null=True)
    payroll_contacts = models.ManyToManyField(Contact, related_name="payroll_contacts", null=True, blank=True)
    title = models.CharField(max_length=30)
    description = models.TextField()
    active = models.BooleanField(default=True)
    pay_amount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    pay_type = models.CharField(max_length=1, choices=PAY_TYPE_CHOICES, default="P", null=True, blank=True)
    pay_cycle = models.CharField(max_length=1, choices=PAY_CYCLE_CHOICES, default="O", null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project-update', kwargs={'pk':self.id})

    def get_update_url(self):
        return self.get_absolute_url()


class Website(models.Model):
    '''
    information specific to a website on a project
    '''
    project = models.ForeignKey(Project)
    description = models.TextField()
    status = models.CharField(max_length=1, choices=WEBSITE_STATUS_CHOICES, default="N")
    css_library = models.CharField(max_length=3, choices=CSS_LIB_CHOICES)
    js_library = models.CharField(max_length=3, choices=JS_LIB_CHOICES)
    django_version = models.CharField(max_length=3, choices=DJANGO_VER_CHOICES)

    def __str__(self):
        return 'Website for ' + self.project.title


class Invoice(models.Model):
    project = models.ForeignKey(Project)
    status = models.CharField(max_length=1, choices=INVOICE_STATUS_CHOICES, default="P")
    rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    invoice_date = models.DateField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    expense = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.project.title + ' - ' + str(self.invoice_date)

    def total_amount(self):
        '''
        define the total amount for the individual invoice
        to the client
        '''
        total_hours = self.total_hours()

        return self.rate * total_hours + self.expense

    def total_hours(self):
        total_hours = 0
        for h in self.hours_set.filter(invoice=self):
            total_hours += h.hours

        return total_hours


class Hours(models.Model):
    '''
    Primary method to track hours and will be directly used to charge the client
    '''
    project = models.ForeignKey(Project)
    date = models.DateField()
    hours = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    invoice = models.ForeignKey(Invoice, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Hours"
        ordering = ['project__title', 'date']

    def __str__(self):
        return self.project.title + ' - ' + str(self.date)
