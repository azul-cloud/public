from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify

# file path
# def get_blog_image_path(instance, filename):
#     return os.path.join('traits', filename)


class Tag(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(get_user_model())
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    title = models.CharField(max_length=60)
    body = models.TextField()
    heading = models.CharField(max_length=150, null=True, blank=True)
    create_date = models.DateField(auto_now_add=True)
    views = models.IntegerField(default=0)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']

    def get_absolute_url(self):
        return reverse('blog-post', kwargs={'pk':self.id, 'slug':slugify(self.title)})

    def __str__(self):
        return self.title