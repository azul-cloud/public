from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from flowblog.models import Post, Tag


def home(request):
    #return all blog posts
    posts = Post.objects.filter(active=True)
    paginator = Paginator(posts, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request, 'flowblog/content/general.html', {'posts':posts})


def post(request, **kwargs):
    #display single blog post
    post = get_object_or_404(Post, id=kwargs['pk'])

    return render(request, 'flowblog/content/post.html', {'p':post})


def posts_tag(request, **kwargs):
    tag = get_object_or_404(Tag, id=kwargs['pk'])
    posts = Post.objects.filter(tags=tag, active=True)

    return render(request, 'flowblog/content/general.html',
        {'tag':tag, 'posts': posts})
