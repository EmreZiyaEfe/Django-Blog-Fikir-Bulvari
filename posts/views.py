from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def index(request):
    postlar = Posts.objects.all()
    context = {
        'posts' : postlar
    }
    return render(request, 'index.html', context)


def singlePost(request, postId, slug):
    postum = Posts.objects.get(id = postId, slug = slug)
    context = {
        'post': postum
    }
    return render(request, 'singlePost.html', context)




@login_required(login_url='login')
def typePost(request):
    kategoriler = Kategori.objects.all()
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

    context = {
        'kategoriler' : kategoriler
    }
    return render(request, 'type.html', context)