from django.shortcuts import get_object_or_404, render, redirect
from account.models import CustomUser
from .models import Bill, Debate
from account.forms import RegisterForm
from django.db import models
from django.conf import settings


def home(request):

    return render(request,'home.html')

def bill_detail(request,bill_id):

    return render(request,bill_detail)


def bill_write(request):
    return render(request,"bill_write.html")


def bill_create(request):
    new_bill=Bill()
    return redirect('bill_detail', new_bill.id)


def bill_main(request):
    return render(request,'bill_main.html')

def debate_detail(request,debate_id):
    
    return render(request,bill_detail)


def debate_write(request):
    return render(request,"bill_write.html")



def debate_create(request):
    new_bill=Bill()
    return redirect('bill_detail', new_bill.id)


def debate_main(request):
    return render(request, 'debate_main.html')

def mypage(request):
    myquest = request.POST.get('myquest')

    bills = Bill.objects.filter(author=request.user)

    return render(request,"mypage.hmtl",{'bills':bills})


def comment_to_bill(request, bill_id):
    
    return render(request, 'comment_to_bill.html')


def community_choose(request,user_type):

    if user_type==yolo:
        return render(request, "community_yolo.html")
    else:
        return render(request, "community_fire.html")


