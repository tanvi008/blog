from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# from django.urls import reverse
import uuid




# class BaseModel(models.Model):
#     uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
#     created_at =models.DateField(auto_now_add=True)
#     updated_at=models.DateField(auto_now_add=True) #check here while using auto_now=True
#
#     class Meta:
#         abstract=True
#
#
# class BlogCategory(BaseModel):
#     category_name=models.CharField(max_length=100)

class Blog(models.Model):
# class Blog(BaseModel):
#     category=models.ForeignKey(BlogCategory, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255, unique=True, default="")
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.CharField(max_length=255, default="")
    blog_image = models.ImageField(upload_to='documents/', default="")
    is_deleted = models.BooleanField(default=False)

    # created_at = models.DateField(auto_now=True, blank=True, null=True)

    # def get_absolute_url(self):
    #     return reverse('home')

    # def __str__(self):
    #     return self.title
