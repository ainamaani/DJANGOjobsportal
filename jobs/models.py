from django.db import models

# Create your models here.

class Jobs(models.Model):
    title = models.CharField(max_length=30,null=True)
    description = models.TextField(null=True)
    company = models.CharField(max_length=30,null=True)
    email = models.CharField(max_length=25,null=True)
    location = models.CharField(max_length=20,null=True)
    salary = models.CharField(max_length=30,null=True)
    jobtype = models.CharField(max_length=30,null=True)
    category = models.CharField(max_length=20,null=True)
    contact = models.CharField(max_length=14,null=True)
    qualifications = models.TextField(null=True)
    skills = models.TextField(null=True)
    experience = models.TextField(null=True)
    aboutus = models.TextField(null=True)
    applicationmethod = models.TextField(null=True)

    def __str__(self) -> str:
        return self.title




