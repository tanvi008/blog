from .models import Blog
from django.forms import ModelForm


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
