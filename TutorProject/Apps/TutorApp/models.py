from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Class(models.Model):
    id = models.IntegerField(primary_key=True)
    coursenum = models.CharField(max_length=3)
    title = models.CharField(max_length=100)
    major = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_tutor = models.BooleanField(default=False)

class Admin(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, default=CustomUser.objects.get(username='admin_default'))

class Tutor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, default=CustomUser.objects.get(username='admin_default'))
    
    
    

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, default=CustomUser.objects.get(username='admin_default'))