from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context )

def post_details(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {
        'post': post
    }
    return render(request, 'blog/post_details.html', context) 
