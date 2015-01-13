from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse

from django_webtest import WebTest

from .models import Tag, Post
from .factories import TagFactory, PostFactory
from main.factories import StaffFactory, UserFactory, AdminFactory

User = get_user_model()


'''
NOTE: There are currently 3 tests failinga and I'm not sure why.
test_post, test_update_form and test_update_post are all returning
404 errors. It has something to do with the post URL not working right
in the testing suite. It could possibly have something to do with SQLite
'''

class BlogSetup(TestCase):
    def setUp(self):
        # set up users
        self.user = UserFactory.create()
        self.staff_user = StaffFactory.create()
        self.admin_user = AdminFactory.create()

        # set up models
        self.tag = TagFactory.create(title="Test Tag")
        self.post = PostFactory.create(user=self.staff_user)
        self.post.tags.add(self.tag)


class BlogModelTest(BlogSetup):
    def test_tag(self):
        Tag.objects.get(id=1)
        self.assertNotEqual(self.tag.slug, None)

    def test_post(self):
        Post.objects.get(id=1)
        self.assertNotEqual(self.post.slug, None)

    def test_recent_posts(self):
        active_posts = Post.active_objects.recent()


class BlogViewTest(BlogSetup, WebTest):
    def test_home(self):
        url = reverse('blog-home')
        response = self.app.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        url = self.post.get_absolute_url()
        response = self.app.get(url)
        self.assertEqual(response.status_code, 200)

    def test_tag(self):
        url = self.tag.get_absolute_url()
        response = self.app.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_post(self):
        url = reverse('blog-create')
        
        anon_response = self.app.get(url)
        self.assertEqual(anon_response.status_code, 302)

        staff_response = self.app.get(url, user=self.staff_user)
        self.assertContains(staff_response, "Create")

    def test_update_post(self):
        url = reverse('blog-update', kwargs={'slug':self.post.slug})
        
        anon_response = self.app.get(url)
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

        response = self.app.post(url, post, user=self.staff_user)

        # make sure the response has the newly created post
        self.assertEqual(response.status_code, 302)

    def test_update_form(self):
        url = reverse('blog-update', kwargs={'slug':'posted-title'})

        post = {
            "title":"Changed Title",
            "heading":"My heading",
            "body":"<h1>Incoming from test</h1>",
        }

        response = self.app.post(url, post, user=self.staff_user)

        # make sure the title was changed successfully
        self.assertEqual(response.status_code, 302)


