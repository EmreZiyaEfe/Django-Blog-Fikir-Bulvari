from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'date', 'category']
    list_display_links = ['author', 'title']
    list_filter = ['author', 'title']
    search_fields = ['author', 'title']
    readonly_fields = ['id', 'date', 'slug']

class KategoriAdmin(admin.ModelAdmin):
    list_display = ['id', 'category']
    readonly_fields = ['id', 'category']

admin.site.register(Posts, PostAdmin)
admin.site.register(Kategori, KategoriAdmin)
# admin.site.register(Kategori)