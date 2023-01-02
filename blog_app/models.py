from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    title = models.CharField(max_length=255, unique=True, default="")
    created_by = models.CharField(max_length=100 ,default="")
    content = models.CharField(max_length=255, default="")
    blog_image = models.ImageField(upload_to='documents/', default="")
