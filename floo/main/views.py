from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.db import models
from account.models import CustomUser

# Create your views here.
def home(request):
    
    return render(request, 'home.html')

