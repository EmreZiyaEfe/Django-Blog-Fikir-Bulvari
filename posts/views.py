from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

# <-------------------------------*******************************------------------------------->

#index sayfasında postların görünmesini sağlayan fonksiyon

def index(request):
    postlar = Posts.objects.all()
    context = {
        'posts' : postlar
    }
    return render(request, 'index.html', context)

#index sayfasında postların görünmesini sağlayan fonksiyon sonu

# <-------------------------------*******************************------------------------------->

# Postun detayını göstermesi için gerekli fonksiyon


def singlePost(request, postId, slug):
    postum = Posts.objects.get(id = postId, slug = slug)
    context = {
        'post': postum
    }
    return render(request, 'singlePost.html', context)

# Postun detayını göstermesi için gerekli fonksiyon sonu

# <-------------------------------*******************************------------------------------->

# Yazara ait postların hepsini sayfada göstermek için getiren fonksiyon

def authorPosts(request, author_id):
    author_posts = Posts.objects.filter(author_id=author_id)
    author_info = Profil.objects.get(id=author_id)
    context = {
        'author_posts' : author_posts,
        'author_info' : author_info
    }
    return render(request, 'authorPosts.html', context)

# Yazara ait postların hepsini sayfada göstermek için getiren fonksiyon sonu

# <-------------------------------*******************************------------------------------->

# Bir kategoriye ait postları getirmeyi sağlayan fonksiyon

def postsFilter(request, category_name):
    category = Kategori.objects.get(category = category_name)
    posts_filter = category.posts.all()
    context = {
        'posts_filter' : posts_filter
    }
    return render(request, 'posts-filter.html', context)

# Bir kategoriye ait postları getirmeyi sağlayan fonksiyon sonu

# <-------------------------------*******************************------------------------------->


#Sayfada Post Yazmak için gerekli fonksiyon

@login_required(login_url='login')
def typePost(request):
    if  request.method == 'POST':
        category = request.POST['kategori']
        title = request.POST['baslik']
        paragraf = request.POST['paragraf']
        resim = request.FILES['resim']

        profile_name = request.user.profil

        post = Posts.objects.create(
            category_id = category,
            content = paragraf,
            title = title,
            image = resim,
            author_id = profile_name.id
        )
        post.save()
        messages.success(request, 'Post Yayınlandı')
        return redirect('index')
    return render(request, 'type.html')


#Sayfada Post Yazmak için gerekli fonksiyon sonu