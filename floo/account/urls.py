from django.urls import path
from django.urls.resolvers import URLPattern
from .views import *

urlpatterns=[
    path('register/',register_view,name="register"),
    path('login/',login_view,name="login"),
]