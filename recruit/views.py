from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomRegisterForm, LoginWithCaptchaForm
from .models import CustomUser


def register_view(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('recruit:user_list')
    else:
        form = CustomRegisterForm()
    return render(request, 'recruit/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginWithCaptchaForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('recruit:user_list')
    else:
        form = LoginWithCaptchaForm()
    return render(request, 'recruit/login.html', {'form': form})


@login_required
def user_list_view(request):
    users = CustomUser.objects.all()
    return render(request, 'recruit/user_list.html', {'user_list': users})


def logout_view(request):
    logout(request)
    return redirect('recruit:login')
