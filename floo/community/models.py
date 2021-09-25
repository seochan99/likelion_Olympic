from django.db import models
from django.conf import settings

# Create your models here.
class Bill(models.Model):
    image= models.ImageField(null=False)
    date=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE) 
    text=models.CharField(max_length=200)
    title=models.CharField(max_length=30)
    yolo=models.IntegerField(default=0)
    fire=models.IntegerField(default=0)

    def summary(self):
        return self.text[:50]

class BillComment(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    text=models.CharField(max_length=150)


    

class Debate(models.Model):
    text=models.CharField(max_length=200)
    title=models.CharField(max_length=100)

class DebateComment(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    text=models.CharField(max_length=150)
    like=models.IntegerField(default=0)
    debate = models.ForeignKey(Debate, on_delete=models.CASCADE)





