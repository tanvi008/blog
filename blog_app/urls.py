from django.urls import path
from .views import home, data, create

urlpatterns=[
    path('home', home, name='home'),
    path('data', data, name='data'),
    path('create', create, name='create'),


]