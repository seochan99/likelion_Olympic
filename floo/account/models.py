from django.db import models
from django.contrib.auth.models import AbstractUser

RESULT_CHOICES={
    ('yolo','YOLO족'),
    ('fire','FIRE족'),
    ('null','미선택')
}

# Create your models here.
class CustomUser(AbstractUser):
    sex = models.CharField(max_length=3)
    age = models.CharField(max_length=10) 
    nickname = models.CharField(max_length=15)
    profile= models.ImageField(blank=True, null=True)
    result=models.CharField(max_length=5, choices=RESULT_CHOICES,default='null')
    