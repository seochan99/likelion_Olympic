from django.db import models
from django.contrib.auth.models import AbstractUser

RESULT_CHOICES={
    ('yolo','YOLO족'),
    ('fire','FIRE족')
}

# Create your models here.
class CustomUser(AbstractUser):
    sex = models.CharField(max_length=3)
    age = models.CharField(max_length=10) 
    nickname = models.CharField(max_length=15)
    profile= models.ImageField(blank=True, null=True)
    result=models.CharField(max_length=5, choices=RESULT_CHOICES)
    count_num = models.IntegerField(default=0, blank=True, null=True)
    