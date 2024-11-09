from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date', 'slug')
    prepopulated_fields = {'slug': ('title',)}
