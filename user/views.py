from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def userRegister(request):
    if request.method == 'POST':
        kullanici = request.POST['kullanici']
        email = request.POST['email']
        meslek = request.POST['meslek']
        sifre = request.POST['sifre']
        sifre2 = request.POST['sifre2']

        if sifre == sifre2:
            if User.objects.filter(email = email).exists():
                messages.error(request, 'Bu email ile daha önce kayıt olunmuş!')
            elif len(sifre) < 6:
                messages.error(request, 'En az 6 karakter olmalıdır!')
            elif kullanici.lower() in sifre.lower():
                messages.error(request, 'Şifre kullanıcı adını içermemelidir!')
            else:
                #Kullanıcı kayıt işlemi
                user = User.objects.create_user(
                    username= kullanici,
                    email=email,
                    password=sifre
                )
                Profil.objects.create(
                    user = user,
                    job = meslek
                )
                user.save()
                messages.success(request, 'Kayıt tamamlandı. Giriş yapabilirsiniz.')
                return redirect('index')
        else:
            messages.error(request, 'Şifreler aynı değil!')
    return render(request, 'register.html')


def userLogin(request):
    if request.method == 'POST':
        kullanici = request.POST['kullanici']
        sifre = request.POST['sifre']

        user = authenticate(request, username = kullanici, password = sifre)

        if user is not None:
            login(request, user)
            messages.success(request, 'Giriş yapıldı.')
            return redirect('index')
        else:
            messages.error(request, 'Kullanıcı adı veya şifre hatalı!')
    return render(request, 'login.html')


def userLogout(request):
    logout(request)
    messages.success(request, 'Çıkış yapıldı.')
    return redirect('index')


@login_required(login_url='login')
def update(request):
    if request.method == 'POST':
        kullanici = request.POST['kullanici']
        email = request.POST['email']
        meslek = request.POST['meslek']
        twitter = request.POST['twitter']
        facebook = request.POST['facebook']
        instagram = request.POST['instagram']
        linkedin = request.POST['linkedin']
        
        profil = request.user.profil

        # Kullanıcı adı, email ve meslek alanlarını güncelle
        profil.user.username = kullanici
        profil.user.email = email
        profil.job = meslek

        # Sosyal medya bağlantılarını güncelle
        profil.twitter = twitter
        profil.facebook = facebook
        profil.instagram = instagram
        profil.linkedin = linkedin

        # Profil resmini güncelle (varsa)
        if 'resim' in request.FILES:
            pimage = request.FILES['resim']
            profil.ppic = pimage

        # Değişiklikleri kaydet
        profil.user.save()
        profil.save()

        messages.success(request, 'Bilgiler güncellendi')
        return redirect('profile-edit')
    return render(request, 'profile-edit.html')
