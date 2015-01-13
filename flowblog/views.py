from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView, UpdateView

from braces.views import StaffuserRequiredMixin

from .models import Post, Tag
from .forms import PostCreateForm, PostUpdateForm


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

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['recent_posts'] = self.model.active_objects.recent()
        return context


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

    def get_context_data(self, **kwargs):
        '''
        add the post list filtered by tag into the context
        '''
        context = super(TagListView, self).get_context_data(**kwargs)
        context['post_list'] = self.get_queryset()
        context['recent_posts'] = Post.active_objects.recent()
        return context


class BlogCreateView(StaffuserRequiredMixin, CreateView):
    model = Post
    template_name = "flowblog/content/create.html"
    form_class = PostCreateForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BlogCreateView, self).form_valid(form)


class BlogUpdateView(StaffuserRequiredMixin, UpdateView):
    model = Post
    template_name = "flowblog/content/update.html"
    form_class = PostUpdateForm


