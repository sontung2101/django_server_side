from django.db import models

# Create your models here.
class Student(models.Model):
    studentNo = models.CharField(max_length=20,unique=True)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name