from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def blog_post_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog_post_list.html', {'posts': posts})

def blog_post_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'blog_post_detail.html', {'post': post})
