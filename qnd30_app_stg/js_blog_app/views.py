# views.py

from django.shortcuts import render
from .models import BlogIndexPage, BlogPage

def blog_index(request):
    blog_index_page = BlogIndexPage.objects.live().first()
    context = {
        'blog_index_page': blog_index_page,
    }
    return render(request, 'blog/blog_index.html', context)

def blog_detail(request, blog_slug):
    blog_page = BlogPage.objects.live().get(slug=blog_slug)
    context = {
        'blog_page': blog_page,
    }
    return render(request, 'blog/blog_detail.html', context)
