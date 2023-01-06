from django.urls import path
from .views import home, data, create, MyBlog, DeleteBlog

urlpatterns = [
    path('', home, name='home'),
    path('data', data, name='data'),
    path('create', create, name='create'),
    path('my_blog', MyBlog.as_view(), name='my_blog'),
    path('<int:pk>/delete', DeleteBlog.as_view(), name='delete_blog'),

]
