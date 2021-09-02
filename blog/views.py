from django.shortcuts import render
from .models import BlogPost, Tag
from django.shortcuts import get_object_or_404


def blog_index(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/index.html', {'posts':posts})


def post(request, id):
    post = get_object_or_404(BlogPost, pk=id)
    return render(request, 'blog/post.html', {'object': post})


def tag_posts(request, name):
    name = name.lower()
    title = 'Posts about {}'.format(name)
    tag = get_object_or_404(Tag, name=name)
    posts = BlogPost.objects.filter(tags=tag)
    return render(request, 'blog/filtered_post_list.html',
                  {'posts':posts, 'title':title})