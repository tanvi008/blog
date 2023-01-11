from django.contrib import admin
from .models import *

class BlogAdmin(admin.ModelAdmin):
    fields = ('title', 'created_by', 'content', 'blog_image', )
    list_display = ('title', 'less_content', 'created_by', 'is_deleted', )
    list_display_links = ('title', 'less_content', 'created_by', )
    list_filter = ('is_deleted', )
    list_per_page = 5
    readonly_fields = ('blog_image',)

    def less_content(self, obj):
        """this will display only less number of lines"""
        return obj.content[:10]

admin.site.register(Blog, BlogAdmin)
