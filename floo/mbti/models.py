from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser






User = get_user_model()


class Mbti_count(models.Model):
    count_num = models.IntegerField(default=0, blank=True, null=True)
