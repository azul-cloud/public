from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse

from django_webtest import WebTest

from .models import Tag, Post
from .factories import TagFactory, PostFactory
from main.factories import StaffFactory, UserFactory, AdminFactory

User = get_user_model()


class BlogSetup(TestCase):
    def setUp(self):
        self.user = UserFactory.create()
        self.staff_user = StaffFactory.create()
        self.admin_user = AdminFactory.create()

        self.tag = TagFactory.create(title="Test Tag")
        self.post = PostFactory.create(user=self.staff_user)


class BlogModelTest(BlogSetup):
    def test_tag(self):
        Tag.objects.get(id=1)
        self.assertNotEqual(self.tag.slug, None)

    def test_post(self):
        Post.objects.get(id=1)
        self.assertNotEqual(self.post.slug, None)


class BlogViewTest(BlogSetup, WebTest):
    def test_home(self):
        url = reverse('blog-home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        url = reverse('blog-post', kwargs={'slug':self.post.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_tag(self):
        url = reverse('blog-tag', kwargs={'slug':self.tag.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_post(self):
        url = reverse('blog-create')
        
        anon_response = self.client.get(url)
        self.assertEqual(anon_response.status_code, 302)

        staff_response = self.app.get(url, user=self.staff_user)
        self.assertContains(staff_response, "Create")

    def test_update_post(self):
        url = reverse('blog-update', kwargs={'slug':self.post.slug})
        
        anon_response = self.client.get(url)
        self.assertEqual(anon_response.status_code, 302)

        staff_response = self.app.get(url, user=self.staff_user)
        self.assertContains(staff_response, "Update")


class BlogFormTest(BlogSetup, WebTest):
    csrf_checks = False

    def test_create_form(self):
        url = reverse('blog-create')

        post = {
            "title":"Posted Title",
            "heading":"My heading",
            "body":"<h1>Incoming from test</h1>",
        }

        response = self.app.post(url, post, user=self.admin_user)

        # make sure the response has the newly created post
        self.assertEqual(response.status_code, 302)

    def test_update_form(self):
        url = reverse('blog-update', kwargs={'slug':self.post.slug})

        post = {
            "title":"Changed Title",
            "heading":"My heading",
            "body":"<h1>Incoming from test</h1>",
        }

        response = self.app.post(url, post, user=self.admin_user)

        # make sure the title was changed successfully
        self.assertEqual(response.status_code, 302)


