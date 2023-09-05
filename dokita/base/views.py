from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'base/index.html')

def blogs(request):
    
    context={}
    return render(request, 'base/blogs.html', context)


def post(request):
    
    context={}
    return render(request, 'base/single_post.html', context)