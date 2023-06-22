from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('single-post/<postId>/<slug>/', singlePost, name='single'),
    path('type-post/', typePost, name='type-post')
]