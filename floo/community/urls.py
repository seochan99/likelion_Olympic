from django.contrib import admin
# from accounts import views
from community import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('<str:bill_id>', views.bill_detail, name="bill_detail"),
    path('bill_write/', views.bill_write, name="bill_write"),
    path('bill_create/', views.bill_create, name="bill_create"),
    path('bill_main/', views.bill_main, name="bill_main"),
    path('<str:debate_id>', views.debate_detail, name="debate_detail"),
    path('debate_write/', views.debate_write, name="debate_write"),
    path('debate_create/', views.debate_create, name="debate_create"),
    path('debate_main/', views.debate_main, name="debate_main"),
    path('mypage/',views.mypage,name="mypage"),
    path('bill/<int:bill_id>/comment/', views.comment_to_bill, name="comment_to_bill"),
    path('communitcation/', views.community_choose, name="community_choose"),
    






] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
