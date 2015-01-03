from factory.django import DjangoModelFactory

from django.contrib.auth import get_user_model

from .models import Tag, Post


class TagFactory(DjangoModelFactory):
    class Meta:
        model = Tag


class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post

    title = "Test Post"
    body  = "<p>This is a Test Post</p>"