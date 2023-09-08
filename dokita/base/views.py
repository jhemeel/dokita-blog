from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

def home(request):
    return render(request, 'base/index.html')

def blogs(request):
    blogs = Post.objects.all()
    
    context={'blogs': blogs}
    return render(request, 'base/blogs.html', context)


def post(request, pk):
    page = 'single_page'
    blog = Post.objects.get(id=pk)
    
    context={'blog': blog, 'page':page}
    return render(request, 'base/single_post.html', context)