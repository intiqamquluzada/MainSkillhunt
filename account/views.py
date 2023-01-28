from django.shortcuts import render, redirect

from account.forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('core:home')
    return render(request, 'account.html', {'form': form})


def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        user_login = authenticate(username=user.username, password=password)
        login(request, user_login)
        return redirect('account:login')
    return render(request,'register.html',{'form': form})


def logout_view(request):
    logout(request)
    return redirect('core:home')
