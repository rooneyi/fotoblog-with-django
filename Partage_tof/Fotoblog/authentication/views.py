from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.conf import settings
from . import forms


def Signup_page(request):
    form = forms.signupForm()
    if request.method == 'POST':
        form = forms.signupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/signup.html', context={'form': form})


def upload_profile_photo(request):
    form = forms.UploadProfilePhotoForm(instance=request.user)
    if request.method == 'POST':
        form = forms.UploadProfilePhotoForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'authentication/upload_profile_photo.html', context={'form': form})


def logout_user(request):
    logout(request)
    return redirect('login')
