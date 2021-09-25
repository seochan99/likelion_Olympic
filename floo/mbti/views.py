from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.db import models
from .models import Mbti_count

# Create your views here.

count_num = 0
participation = 0



def test_main(request): #test mainpage
    return render(request, "test_main.html")
def mbti1(request):  # 1 로 이동

    return render(request, 'mbti1.html',  {'count_num' : count_num})


def mbti2(request):  # 2로 이동
    
    global count_num
    if(request.method == 'POST'):
        count_n = request.POST['answer']
        count_num += int(count_n)
    return render(request, 'mbti2.html',  {'count_num' : count_num})


def mbti3(request):  # 3로 이동
    global count_num
    if(request.method == 'POST'):
        count_n = request.POST['answer']
        count_num += int(count_n)
    return render(request, 'mbti3.html',  {'count_num' : count_num})


def mbti4(request):
    global count_num
    if(request.method == 'POST'):
        count_n = request.POST['answer']
        count_num += int(count_n)
    return render(request, 'mbti4.html')


def mbti5(request):
    global count_num
    if(request.method == 'POST'):
        count_n = request.POST['answer']
        count_num += int(count_n)
    return render(request, 'mbti5.html')


def mbti6(request):
    global count_num
    if(request.method == 'POST'):
        count_n = request.POST['answer']
        count_num += int(count_n)
    return render(request, 'mbti6.html')


def mbti7(request):
    global count_num
    if(request.method == 'POST'):
        count_n = request.POST['answer']
        count_num += int(count_n)
    return render(request, 'mbti7.html')


def mbti8(request):
    global count_num
    if(request.method == 'POST'):
        count_n = request.POST['answer']
        count_num += int(count_n)

    return render(request, 'mbti8.html')


def mbti9(request):
    global count_num
    if(request.method == 'POST'):
        count_n = request.POST['answer']
        count_num += int(count_n)
    return render(request, 'mbti9.html')


def mbti10(request):
    global count_num
    if(request.method == 'POST'):
        count_n = request.POST['answer']
        count_num += int(count_n)

    return render(request, 'mbti10.html')


def result(request):
    global count_num
    if(request.method == 'POST'):
        count_n = request.POST['answer']
        count_num += int(count_n)
        user = Mbti_count()
        user.count_num = count_num

    return render(request, 'result.html', {'count_num' : count_num})
