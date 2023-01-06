from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog
from django.template import loader
from django.views.generic import ListView, DeleteView, CreateView
from django.http import Http404


def home(request):
    return render(request, "blog_app/home.html")


def data(request):
    if request.method == "Post":
        title = request.POST.get('title')
        created_by = request.POST.get('created_by')
        content = request.POST.get('content')
        model_var = Blog(title=title, created_by=created_by, content=content)
        model_var.save()

    return render(request, "data.html")


def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        created_by = request.POST.get('created_by')
        content = request.POST.get('content')
        image = request.FILES['myImage']
        Blog.objects.create(title=title, created_by=created_by, content=content, blog_image=image)

    context = {}
    return render(request, "blog_app/create.html", context=context)


class CreateBlog(CreateView):
    pass


class MyBlog(ListView):
    template_name = 'blog_app/my_blog.html'
    model = Blog

    def get_context_data(self, **kwargs):
        context = super(MyBlog, self).get_context_data(**kwargs)
        return context


class DeleteBlog(DeleteView):
    success_url = '/'
    template_name = "blog_app/confirm_delete.html"
    queryset = Blog.objects.all()
