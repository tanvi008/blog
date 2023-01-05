from django.urls import path
from .views import home, data, create, MyBlog

urlpatterns = [
    path('', home, name='home'),
    path('data', data, name='data'),
    path('create', create, name='create'),
    path('my_blog', MyBlog.as_view(), name='my_blog')

]
