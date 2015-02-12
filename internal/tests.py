import datetime
from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse

from .models import Project, Invoice, Hours, Website, \
                    Client, Contact

User = get_user_model()


class InternalSetup(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            'internal_user',
            'internal_user@gmail.com',
            'testpassword'
        )
        self.contact = Contact.objects.create(
            first_name="Test",
            last_name="Contact",
            email="test.contact@gmail.com"
        )
        # can't overwrite self.client
        self._client = Client.objects.create(
            name="Test Client",
        )
        self.project = Project.objects.create(
            client = self._client,
            title = "Test Project",
            description = "This is a test project.",
            pay_amount = 50.00
        )
        self.website = Website.objects.create(
            project = self.project,
            description = "This is the test website object",
            css_library = "BS3",
            js_library = "J21",
            django_version = "1.7"
        )
        self.invoice = Invoice.objects.create(
            project = self.project,
            rate = 50.00
        )
        self.hours1 = Hours.objects.create(
            project = self.project,
            invoice = self.invoice,
            date = datetime.datetime.now().date(),
            hours = 5
        )
        self.hours1 = Hours.objects.create(
            project = self.project,
            invoice = self.invoice,
            date = datetime.datetime.now().date() + datetime.timedelta(days=1),
            hours = 7
        )
        self.hours2 = Hours.objects.create(
            project = self.project,
            date = datetime.datetime.now().date() + datetime.timedelta(days=2),
            hours = 6
        )

        self.project.contacts.add(self.contact)
        self._client.contacts.add(self.contact)


class InternalModelTest(InternalSetup):
    def test_contact(self):
        Contact.objects.get(id=1)

    def test_client(self):
        Client.objects.get(id=1)

    def test_project(self):
        Project.objects.get(id=1)

    def test_website(self):
        Website.objects.get(id=1)

    def test_invoice(self):
        invoice = Invoice.objects.get(id=1)
        total_hours = invoice.total_hours()
        total_amount = invoice.total_amount()

        self.assertEqual(total_hours, 12)
        self.assertEqual(total_amount, 600)

        invoice.expense = Decimal(20.50)
        invoice.save()
        total_amount = invoice.total_amount()

        self.assertEqual(total_amount, 620.50)

    def test_hours(self):
        Hours.objects.get(id=1)


class InternalViewTest(InternalSetup):
    def test_home(self):
        url = reverse('internal-home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_hours(self):
        url = reverse('hours')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_hours_project(self):
        url = reverse('project-hours', kwargs={
            'pk':self.project.id
        })
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_invoice(self):
        url = reverse('invoices')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_project_invoice(self):
        url = reverse('project-invoice', kwargs={
            'pk':self.project.id
        })
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_project_invoice_details(self):
        url = reverse('project-invoice-details', kwargs={
            'pk':self.project.id
        })
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_projects(self):
        url = reverse('projects')
        response = self.client.get(url)
        self.assertContains(response, self.project.title)

    def test_project_update(self):
        url = self.project.get_update_url()
        response = self.client.get(url)
        self.assertContains(response, self.project.title)


# class BlogViewTest(BlogSetup):
#     def test_home(self):
#         url = reverse('blog-home')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)

#     def test_post(self):
#         url = reverse('blog-post', kwargs={'slug':self.post.slug})
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)

#     def test_tag(self):
#         url = reverse('blog-tag', kwargs={'slug':self.tag.slug})
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)