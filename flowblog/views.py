from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.detail import SingleObjectMixin

from flowblog.models import Post, Tag


class HomeListView(ListView):
    '''
    home page for the blog
    '''
    queryset = Post.objects.filter(active=True)
    template_name = 'flowblog/content/home.html'


class PostDetailView(DetailView):
    '''
    individual post page
    '''
    model = Post
    template_name = 'flowblog/content/post.html'


class TagListView(SingleObjectMixin, ListView):
    '''
    get list of articles that are filtered by the Tag
    '''
    template_name = 'flowblog/content/tag.html'

    def get(self, request, *args, **kwargs):
        # need to override to get the object
        tag_slug = self.kwargs['slug']
        self.object = get_object_or_404(Tag, slug=tag_slug)
        return super(TagListView, self).get(request, *args, **kwargs)

    def get_queryset(self, **kwargs):
        post_list = Post.objects.filter(tags=self.object, active=True)
        return post_list
