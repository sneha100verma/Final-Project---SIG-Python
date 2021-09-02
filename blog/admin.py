from blog.models import BlogPost
from django.contrib import admin
from .models import BlogPost, Tag

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Tag)