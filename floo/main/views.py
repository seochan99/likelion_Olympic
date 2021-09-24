from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.db import models


# Create your views here.
def main(request):
    
    return render(request, 'main.html')

