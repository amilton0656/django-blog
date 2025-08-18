from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all()  #.order_by('-id')     #order_by('-data_publicacao')[:5]

    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context )

def blog(request):
    posts = Post.objects.all().order_by('-id')
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog.html', context )

def post_details(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {
        'post': post
    }
    return render(request, 'blog/post_details.html', context) 
