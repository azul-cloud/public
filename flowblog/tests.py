from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse

from .models import Tag, Post

User = get_user_model()


class BlogSetup(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            'blog_user',
            'blog_user@gmail.com',
            'testpassword'
        )
        self.tag = Tag.objects.create(title="Test Tag")
        self.post = Post.objects.create(
            title="Test Blog",
            body="<p>This is a Test Post</p>",
            user=self.user
        )


class BlogModelTest(BlogSetup):
    def test_tag(self):
        Tag.objects.get(id=1)
        self.assertNotEqual(self.tag.slug, None)

    def test_post(self):
        Post.objects.get(id=1)
        self.assertNotEqual(self.post.slug, None)


class BlogViewTest(BlogSetup):
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