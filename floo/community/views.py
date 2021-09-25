from django.shortcuts import get_object_or_404, render, redirect
from account.models import CustomUser
from .models import Bill, Debate, BillComment,DebateComment
from account.forms import RegisterForm
from django.db import models
from django.conf import settings

def home(request):
    return render(request,'home.html')

def bill_main(request):
    bills = Bill.objects.all()
    return render(request,'bill_main.html',{'bills':bills})

def bill_detail(request,bill_id):
    bill = get_object_or_404(Bill, pk=bill_id)
    bill_comments=BillComment.objects.filter(bill=bill)
    return render(request,'bill_detail.html',{'bill':bill,'bill_comments':bill_comments})

def bill_write(request):
    return render(request,"bill_create.html")

def bill_create(request):
    if request.user.is_authenticated:
        new_bill=Bill()
        if 'image' in request.FILES:
            new_bill.image=request.FILES['image']
        new_bill.author=request.user
        new_bill.text=request.POST.get('text',False)
        new_bill.title=request.POST.get('title',False)
        new_bill.yolo=0
        new_bill.fire=0
        new_bill.save()
        return redirect('bill_detail', new_bill.id)
    else:
        return redirect('404page')

def bill_delete(request,bill_id):
    delete_bill = Bill.objects.get(id=bill_id)
    if delete_bill.author == request.user:
        delete_bill.delete()
        return redirect('bill_main')
    else:
        return redirect('404page')

def debate_detail(request,debate_id):
    debate = get_object_or_404(Debate, pk=debate_id)
    return render(request,"debate_detail.html")

def debate_main(request):
    debates=Debate.objects.all()
    return render(request, 'debate_main.html',{'debates':debates})

def mypage(request):
    myquest = request.POST.get('myquest')

    bills = Bill.objects.filter(author=request.user)

    return render(request,"mypage.hmtl",{'bills':bills})


def comment_to_bill(request, bill_id):
    comment=BillComment()
    comment.author=request.user
    if comment.text:
        comment.bill=get_object_or_404(Bill, pk=bill_id)
        comment.save()
    return redirect('bill_detail',bill_id)


def comment_to_debate(request, debate_id):
    comment=DebateComment()
    comment.author=request.user
    if comment.text:
        comment.debate=get_object_or_404(Debate, pk=debate_id)
        comment.save()
    return redirect('debate_detail',debate_id)

def community_choose(request,user_type):

    if user_type==yolo:
        return render(request, "community_yolo.html")
    else:
        return render(request, "community_fire.html")

