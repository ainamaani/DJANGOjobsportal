from django.db import models

# Create your models here.

class Jobs(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    company = models.CharField(max_length=30)
    email = models.CharField(max_length=25)

class Employee(models.Model):
    name = models.CharField(max_length=23)

