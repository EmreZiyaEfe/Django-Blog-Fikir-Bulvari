from .models import *
from user.models import *

def get_category(request):
    kategoriler = Kategori.objects.all()
    context = {
        'kategoriler':kategoriler
    }

    return context

