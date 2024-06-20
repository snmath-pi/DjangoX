from django.db import models

# Create your models here.

class Student(models.Model):
    # id = models.AutoField() added automatically by Django
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    email = models.EmailField()
    address = models.TextField()
    files = models.FileField()
    
class Product(models.Model):
    pass

#what if some migration is deleted