from django.shortcuts import get_object_or_404, render, redirect
from account.models import CustomUser
from .models import Bill, Debate, BillComment, DebateComment, TalkRoom_Y, TalkRoom_F
from account.forms import RegisterForm
from django.db import models
from django.conf import settings
from django.utils import timezone


def home(request):
    return render(request,'home.html')

def bill_main(request):
    bills = Bill.objects.all()
    return render(request,'bill_main.html',{'bills':bills})

def bill_detail(request,bill_id):
    selected_bill = get_object_or_404(Bill, pk=bill_id)
    bill_comments=BillComment.objects.filter(bill=selected_bill)
    return render(request,'bill_detail.html',{'bill':selected_bill,'bill_comments':bill_comments})

def bill_write(request):
    return render(request,"bill_write.html")

def bill_create(request):
    if request.user.is_authenticated:
        new_bill=Bill()
        if 'image' in request.FILES:
            new_bill.image=request.FILES['image']
        new_bill.author=request.user
        new_bill.text=request.POST.get('bill_text',False)
        new_bill.title=request.POST.get('bill_title',False)
        new_bill.yolo=0
        new_bill.fire=0
        new_bill.save()
        return redirect('community:bill_detail', new_bill.id)
    else:
        return redirect('community:forbidden')

def bill_delete(request,bill_id):
    delete_bill = Bill.objects.get(id=bill_id)
    if delete_bill.author == request.user:
        delete_bill.delete()
        return redirect('community:bill_main')
    else:
        return redirect('community:forbidden')

def debate_detail(request,debate_id):
    selected_debate = get_object_or_404(Debate, pk=debate_id)
    debate_comments=BillComment.objects.filter(debate=selected_debate)
    return render(request,"debate_detail.html",{'debate':selected_debate,'debate_comments':debate_comments})

def debate_main(request):
    debates=Debate.objects.all()
    return render(request, 'debate_main.html',{'debates':debates})

def mypage(request):
    myquest = request.POST.get('myquest')

    bills = Bill.objects.filter(author=request.user)

    return render(request,"mypage.html",{'bills':bills})


def comment_to_bill(request, bill_id):
    comment=BillComment()
    comment.author=request.user
    if comment.text:
        comment.text=request.POST.get('comment_text',False)
        comment.bill=get_object_or_404(Bill, pk=bill_id)
        comment.save()
    return redirect('community:bill_detail',bill_id)


def comment_to_debate(request, debate_id):
    comment=DebateComment()
    comment.author=request.user
    if comment.text:
        comment.debate=get_object_or_404(Debate, pk=debate_id)
        comment.text=request.POST.get('debate_text',False)
        comment.save()
    return redirect('community:debate_detail',debate_id)

def community_choose(request):
    #print(request.user.result)
    user = request.user
    if request.user.result == "yolo":
        talks = TalkRoom_Y.objects.all()
        return render(request, "community_yolo.html",{'talks':talks},{"user":user})
    elif request.user.result=="fire":
        talks = TalkRoom_F.objects.all()
        return render(request, "community_fire.html", {'talks': talks}, {"user": user})
    else:

        return redirect('mbti:test_main')


def forbidden(request):
    return render(request,"forbidden.html")


def community_to_talk_Y(request):
    
    form = Talking_y()
    response = {
        'form': form,
        
    }

    if request.method == "POST":
        form = Talking_f(request.POST)
        if form.is_valid():
            talk = form.save(commit=False)
            talk.time = timezone.now()
            talk.author = request.user
            talk.save()
            return redirect('community_choose')

    return render(request, 'community_comment.html')
    
