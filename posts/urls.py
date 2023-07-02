from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('single-post/<postId>/<slug>/', singlePost, name='single'),
    path('type-post/', typePost, name='type-post'),
    path('author-posts/<int:author_id>/', authorPosts, name='author-posts'),
    path('posts-filter/<str:category_name>/', postsFilter, name='posts-filter'),
    path('search-posts/', search_posts, name='search-posts')
]