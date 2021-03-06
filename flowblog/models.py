from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from django.utils.text import slugify

# file path
# def get_blog_image_path(instance, filename):
#     return os.path.join('traits', filename)


class SaveSlug(models.Model):
    '''
    Base class to create a slugfield
    '''
    title = models.CharField(max_length=50)
    slug = models.SlugField(db_index=True, unique=True, 
        editable=False, blank=True)
    objects = models.Manager()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        '''
        set the slug based on the title field
        '''
        self.slug = slugify(self.title)
        
        super(SaveSlug, self).save(*args, **kwargs)


class Tag(SaveSlug):

    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('blog-tag', kwargs={'slug':self.slug})

    def __str__(self):
        return self.title


class ActivePostManager(models.Manager):
    '''
    manager that will only return active posts
    '''
    def recent(self):
        '''
        return a post queryset of recent posts
        '''
        return Post.active_objects.all()[:4]

    def get_queryset(self):
        return super(ActivePostManager, self).get_queryset().filter(active=True)


# Create your models here.
class Post(SaveSlug):
    user = models.ForeignKey(get_user_model())
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    body = models.TextField()
    heading = models.CharField(max_length=150, null=True, blank=True)
    create_date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=False)
    active_objects = ActivePostManager()

    class Meta:
        ordering = ['-id']

    def get_absolute_url(self):
        return reverse('blog-post', kwargs={'slug':self.slug})

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


