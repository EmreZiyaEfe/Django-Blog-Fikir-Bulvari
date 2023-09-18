from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
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
    author_info = get_object_or_404(Profil, id=author_id)
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = get_object_or_404(author_posts, id = post_id)
        if 'sil' in request.POST:
            post.delete()
            messages.success(request, 'Post Silindi')
            return redirect('author-posts',author_id=author_id)
        
        if 'duzenle' in request.POST:
            return redirect('edit-post', author_id=author_id, post_id=post_id)


    context = {
        'author_posts' : author_posts,
        'author_info' : author_info,
        'user':request.user
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


#Sayfada arama yapmak için gerekli fonksiyon

def search_posts(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        postlar = Posts.objects.filter(
            Q(title__icontains = searched) |
            Q(category__category__icontains = searched) |
            Q(author__user__username__icontains = searched)
        )
        context = {
            'searched': searched,
            'postlar': postlar
        }
        return render(request, 'post-search.html', context)
    else:

        return render(request, 'post-search.html')


#Sayfada arama yapmak için gerekli fonksiyon sonu

#Post düzenlemesi yapmak için gerekli fonksiyon

def editPost(request, author_id, post_id):

    #Yazar ve post idsine göre seçilen postu alıyoruz
    
    post = get_object_or_404(Posts, author_id=author_id, id=post_id)

    if request.method == 'POST':
        title = request.POST['baslik']
        content = request.POST['paragraf']

        post.title = title
        post.content = content

        #Post metodunda resim eklenip eklenmediğini sorguladığımız bölüm

        if 'resim' in request.FILES:
            image = request.FILES['resim']
            post.image = image

        post.save()
        messages.success(request, 'Post başarıyla düzenlendi')
        return redirect('author-posts', author_id=author_id)
    
    context = {
        'post': post
    }
    return render(request, 'edit-post.html', context)

#Post düzenlemesi yapmak için gerekli fonksiyon sonu
