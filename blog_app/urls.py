from django.urls import path
from .views import home, data, CreateBlog, BlogListView, DeleteBlog, UserBlogListView, BlogDetailView, UpdateBlog

urlpatterns = [
    path('', home, name='home'),
    path('data', data, name='data'),
    path('create', CreateBlog.as_view(), name='create'),
    path('my_blog', BlogListView.as_view(), name='my_blog'),
    path('my_blog/<int:pk>', BlogDetailView.as_view(), name='blog-detail'),
    path('my_blog/<int:pk>/update', UpdateBlog.as_view(), name='blog-update'),
    path('<str:email>/user', UserBlogListView.as_view(), name='user_blog_list'),
    path('my_blog/<int:pk>/delete', DeleteBlog.as_view(), name='delete_blog'),

]
