from django.contrib import admin
# from accounts import views
from mbti import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

app_name = 'mbti'

urlpatterns = [
    path('main/', views.test_main, name='test_main'),
    path('mbti1/', views.mbti1, name="mbti1"),
    path('mbti2/', views.mbti2, name="mbti2"),
    path('mbti3/', views.mbti3, name="mbti3"),
    path('mbti4/', views.mbti4, name="mbti4"),
    path('mbti5', views.mbti5, name="mbti5"),
    path('mbti6/', views.mbti6, name="mbti6"),
    path('mbti7/', views.mbti7, name="mbti7"),
    path('mbti8/', views.mbti8, name="mbti8"),
    path('mbti9/', views.mbti9, name="mbti9"),
    
    path('mbti10/', views.mbti10, name="mbti10"),
    path('result/', views.result, name="result"),







] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
