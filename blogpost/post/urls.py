from django.urls import path
from .views import blog_post_list, blog_post_detail

urlpatterns = [
    path('blog/', blog_post_list, name='blog_post_list'),
    path('blog/<slug:slug>/', blog_post_detail, name='blog_post_detail'),
]
