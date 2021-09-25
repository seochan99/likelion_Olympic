from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from main import *
from .forms import RegisterForm

# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('register')
    else:
        form = RegisterForm()
    return render(request,'register.html',{'form':form})

def login_view(request):
    '''
    if request.user.is_authenticated:
        return redirect('main')
    '''
        
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect('main')
        else:
            messages.add_message(request, messages.ERROR, ' 가입하지 않은 계정이거나, 잘못된 비밀번호입니다')
            return redirect('login')
    else:
        form = AuthenticationForm()
    return render(request,"login.html", {"form":form})