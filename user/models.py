from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

def get_default_profile_image():
    return 'static/image/profil_resimleri/avatar.png'

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Kullanıcı')
    ppic = models.ImageField(upload_to='profile/', null=True, blank=True, default=get_default_profile_image, verbose_name='Profil Resmi' )
    job = models.CharField(max_length=100, null=True, blank=True, verbose_name = 'Meslek')
    twitter = models.CharField(max_length=100, null=True, blank=True, verbose_name='Twitter')
    facebook = models.CharField(max_length=100, null=True, blank=True, verbose_name='Facebook')
    instagram = models.CharField(max_length=100, null=True, blank=True, verbose_name='Instagram')
    linkedin = models.CharField(max_length=100, null=True, blank=True, verbose_name='Linkedin')

    def __str__(self):
        return self.user.username
    
    
    
