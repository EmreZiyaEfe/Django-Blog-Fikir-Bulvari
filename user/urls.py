from django.urls import path
from .views import *


urlpatterns = [
    path('register/', userRegister, name='register'),
    path('login/', userLogin, name='login'),
    path('logout/', userLogout, name='logout'),
    path('profile-edit/', update, name='profile-edit'),
    path('change-password/', changePassword, name='change-password')
]