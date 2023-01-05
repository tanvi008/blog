from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog
from django.template import loader
from django.views.generic.list import ListView


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
    print("-----------------")
    if request.method == "POST":
        print("here=-----------------")
        print("-----------------------", request.POST)
        title = request.POST.get('title')
        created_by = request.POST.get('created_by')
        content = request.POST.get('content')
        image = request.FILES['myImage']
        Blog.objects.create(title=title, created_by=created_by, content=content, blog_image=image)

    context = {}
    return render(request, "blog_app/create.html", context=context)


# def my_blog(request):
#     mydata = Blog.objects.all().values()
#     print("^^^^^^^^^^^^^^^", mydata)
#     template = loader.get_template('blog_app/my_blog.html')
#     context = {
#         'my_members': mydata,
#     }
#     # return HttpResponse(template.render(context, request))
#     return render(request, "blog_app/my_blog.html", context=context)


class MyBlog(ListView):
    print("----------blog")
    template_name = 'blog_app/my_blog.html'
    model = Blog
    print("&&&&&&", model)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['page_title'] = 'Authors'
        return data

