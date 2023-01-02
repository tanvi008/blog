from django.shortcuts import render, redirect
from .models import *
# from .forms import BlogForm
from django.contrib import messages
from django.http import HttpResponse
from .forms import BlogForm


# Create your views here.

def home(request):
    return render(request, "home.html")

def data(request):
    if request.method == "Post":
        title=request.POST.get('title')
        created_by = request.POST.get('created_by')
        content = request.POST.get('content')
        model_var = Blog(title=title ,created_by=created_by,content=content)
        model_var.save()

    return render(request, "data.html")


def create(request):
    print("-----------------")
    if request.method == "POST":
        print("here=-----------------")
        # title=request.POST.get('title')
        # created_by = request.POST.get('created_by')
        # content = request.POST.get('content')
        # model_var = Blog(title=title ,created_by=created_by,content=content)
        # model_var.save()
        print("-----------------------",request.POST)
        title = request.POST.get('title')
        created_by = request.POST.get('created_by')
        content = request.POST.get('content')
        image = request.FILES['myImage']
        Blog.objects.create(title=title, created_by=created_by, content=content, blog_image=image)

    context={}
    return render(request, "create.html", context=context)

