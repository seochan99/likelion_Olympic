from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):

    RESULT_CHOICES = (
        ('yolo', 'YOLO족'),
        ('fire', 'FIRE족'),
        ('null', '미선택'))

    SEX_CHOICES = (('M', '남'), ('W', '여'))

    AGE_CHOICES = (('5', '10대 이하'), ('10', '10대'), ('20', '20대'),
                   ('30', '30대'), ('40', '40대'), ('50', '50대 이상'))

    sex = models.CharField(
        max_length=3, choices=SEX_CHOICES, help_text='성별을 선택하세요')
    age = models.CharField(
        max_length=10, choices=AGE_CHOICES, help_text="나이대를 선택하세요")
    nickname = models.CharField(max_length=15, help_text='닉네임 입력하세요')
    profile = models.ImageField(blank=True, null=True, help_text='이미지 입력하세요')
    result = models.CharField(
        max_length=5, choices=RESULT_CHOICES, default='yolo')
