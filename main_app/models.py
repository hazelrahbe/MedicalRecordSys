from email.policy import default
from enum import auto
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Docs(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    specialization = models.CharField(max_length=150)
    email = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.lastname

class Patient(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    ethnicity = models.CharField(max_length=150)
    dob = models.DateField()

    def __str__(self):
        return self.lastname

class Records(models.Model):
    history = models.CharField(max_length=200, null=True)
    allegries = models.CharField(max_length=150, null=True)
    condition = models.CharField(max_length=200, null=True)
    labresults = models.CharField(max_length=200, null=True)
    notes = models.CharField(max_length=300, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    docs = models.ForeignKey(Docs, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient.lastname