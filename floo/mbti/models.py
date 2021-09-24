from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    count_num = models.IntegerField(default=0, blank=True, null=True)
