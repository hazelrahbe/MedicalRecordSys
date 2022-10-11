from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your models here.

class Docs(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    specialization = models.CharField(max_length=150)
    email = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.lastname

class Patient(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    ethnicity = models.CharField(max_length=150)
    dob = models.DateField()

    def __str__(self):
        return self.lastname