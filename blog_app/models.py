from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(max_length=255, unique=True, default="")
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.CharField(max_length=255, default="")
    blog_image = models.ImageField(upload_to='documents/', default="")
    is_deleted = models.BooleanField(default=False)
    # created_at = models.DateField(auto_now=True, blank=True, null=True)

    # def get_absolute_url(self):
    #     return reverse('home')
