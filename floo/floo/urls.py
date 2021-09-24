from django.contrib import admin
# from accounts import views
from main import views as mv 
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mv.main, name='main'),
    path('home/',mv.showhome, name='home'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
