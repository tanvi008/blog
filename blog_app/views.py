from django.shortcuts import render
from .models import Blog
from django.views.generic import ListView, DeleteView, CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model


def home(request):
    context = {
        'blogs' : Blog.objects.all()
    }
    return render(request, "blog_app/home.html", context)


def data(request):
    if request.method == "Post":
        title = request.POST.get('title')
        created_by = request.POST.get('created_by')
        content = request.POST.get('content')
        model_var = Blog(title=title, created_by=created_by, content=content)
        model_var.save()

    return render(request, "data.html")


class BlogListView(ListView):
    model = Blog
    template_name = 'blog_app/home.html'
    context_object_name = 'blogs'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_app/blog_detail.html'


class CreateBlog(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = "blog_app/create.html"
    fields = ['title', 'content', 'blog_image']
    success_url = reverse_lazy('home')
    success_message = 'New blog added successfully'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class UserBlogListView(ListView):
    model = Blog
    template_name = 'blog_app/user_blog.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        # breakpoint()
        context = super(UserBlogListView, self).get_context_data(**kwargs)
        user = get_object_or_404(get_user_model(), email=self.kwargs.get('email'))
        blogs = Blog.objects.filter(created_by=user)
        context['blogs'] = blogs
        context['user'] = user
        # breakpoint()
        return context


class UpdateBlog(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    template_name = "blog_app/create.html"
    fields = ['title', 'content', 'blog_image']
    success_url = '/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        blog =self.get_object()
        if self.request.user == blog.created_by:
            return True
        return False


class DeleteBlog(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    success_url = '/'
    template_name = "blog_app/confirm_delete.html"
    queryset = Blog.objects.all()

    def test_func(self):
        blog =self.get_object()
        if self.request.user == blog.created_by:
            return True
        return False