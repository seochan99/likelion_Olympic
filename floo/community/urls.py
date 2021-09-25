from django.contrib import admin
# from accounts import views
from community import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

app_name ="community"

urlpatterns = [
    path('home/', views.home, name='home'),
    path('bill_main/', views.bill_main, name="bill_main"),
    path('bill/<str:bill_id>', views.bill_detail, name="bill_detail"),
    path('bill_write/', views.bill_write, name="bill_write"),
    path('bill_create/', views.bill_create, name="bill_create"),
    path('bill_delete/<str:bill_id>', views.bill_delete, name="bill_delete"),
    path('debate/<str:debate_id>', views.debate_detail, name="debate_detail"),
    path('debate_main/', views.debate_main, name="debate_main"),
    path('mypage/',views.mypage,name="mypage"),
    path('bill/<str:bill_id>/comment/', views.comment_to_bill, name="comment_to_bill"),
    path('debate/<str:debate_id>/comment/', views.comment_to_debate, name="comment_to_debate"),
    path('forbidden/',views.forbidden,name="forbidden"),






] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
