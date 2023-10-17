from django.db import models

# Create your models here.
class Class(models.Model):
    id = models.IntegerField(primary_key=True)
    coursenum = models.CharField(max_length=3)
    title = models.CharField(max_length=100)
    major = models.CharField(max_length=20)

    def __str__(self):
        return self.title
