from django.urls import path
from . import views

urlpatterns = [
    path('tag/<str:name>', views.tag_posts, name='tag_posts'),
    path('post/<int:id>', views.post, name='post'),
    path('', views.blog_index, name='blog_index'),
] 