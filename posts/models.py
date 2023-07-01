from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from user.models import *
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField



class Kategori(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

class Posts(models.Model):
    author = models.ForeignKey(Profil, on_delete = models.CASCADE, verbose_name = 'Yazar')
    category = models.ForeignKey(Kategori, on_delete=models.SET_NULL, null=True, verbose_name='Kategori', related_name='posts')
    title = models.CharField(max_length = 100, verbose_name = 'Başlık')
    content = RichTextUploadingField(null=True, blank=True, verbose_name = 'Paragraf')
    image = models.ImageField(upload_to = 'postImages/')
    date = models.DateField(auto_now_add = True, null = True) 
    slug = models.SlugField(null=True, editable=False)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ['-date']

