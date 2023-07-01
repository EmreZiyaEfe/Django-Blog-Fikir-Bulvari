from .models import *
from user.models import *
from django.db.models import Q

def get_category(request):
    kategoriler = Kategori.objects.all()
    context = {
        'kategoriler':kategoriler
    }

    return context


# def get_search(request):
#     search = ''
#     if request.GET.get('search'):
#         search = request.GET.get('search')
#         postlar = Posts.objects.filter(
#             Q(title__icontains = search) |
#             Q(category__category__icontains = search) |
#             Q(author__user__username__icontains = search)
#         )
#     context = {
#         'search' :search
#     }

#     return context