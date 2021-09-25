
from django.contrib import messages
from main import *
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from .models import CustomUser
from community import views

# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if CustomUser.objects.filter(username=request.POST['username']).exists():
            error = "이미 등록된 Username입니다"
            return render(request, 'register.html', {'form': form, 'error': error})
        if request.POST['password1'] != request.POST['password2']:
            error = "비밀번호가 서로 다릅니다"
            return render(request, 'register.html', {'form': form, 'error': error})
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect("main")

    else:

        form = RegisterForm()
        return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect("main")



def login_view(request):
    

    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(
                request=request, username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect('main')
        else:
            messages.add_message(request, messages.ERROR,
                                 ' 가입하지 않은 계정이거나, 잘못된 비밀번호입니다')
            return redirect('login')
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})
