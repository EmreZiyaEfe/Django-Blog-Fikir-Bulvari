from .models import *

def get_author(request, pk):
    author_info = Profil.objects.filter(id = pk)
    context = {
        'info':author_info
    }
    return context