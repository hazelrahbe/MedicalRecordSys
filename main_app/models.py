from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Docs(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    specialization = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete = models.CASCADE, default=1)

    def __str__(self) -> str:
        return self.lastname
