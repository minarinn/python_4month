from django.views import View
from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser
from .forms import CustomRegisterForm, LoginWithCaptchaForm

class RegisterView(View):
    def get(self, request):
        form = CustomRegisterForm()
        return render(request, 'recruit/register.html', {'form': form})

    def post(self, request):
        form = CustomRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recruit:login')
        return render(request, 'recruit/register.html', {'form': form})


class LoginView(View):
    def get(self, request):
        form = LoginWithCaptchaForm()
        return render(request, 'recruit/login.html', {'form': form})

    def post(self, request):
        form = LoginWithCaptchaForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('recruit:user_list')
        return render(request, 'recruit/login.html', {'form': form, 'error': 'Неверные данные'})

class UserListView(ListView):
    model = CustomUser
    template_name = 'recruit/user_list.html'
    context_object_name = 'users'
    ordering = ['-id']

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')