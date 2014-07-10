import os
from django.db import models


# file paths
def get_trait_image_path(instance, filename):
    return os.path.join('traits', filename)

def get_example_image_path(instance, filename):
    return os.path.join('examples', filename)


# models
class Trait(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to=get_trait_image_path)
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class Example(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to=get_example_image_path)
    text = models.CharField(max_length=300)
    link = models.CharField(max_length=100)
    order = models.IntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=60)
    company = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    skype = models.CharField(max_length=40, null=True, blank=True)
    message = models.CharField(max_length=2000)

    def __str__(self):
        return '%s' % self.company