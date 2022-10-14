from django.contrib import admin
from .models import Docs, Patient, Records
# Register your models here.
admin.site.register(Docs)
admin.site.register(Patient)
admin.site.register(Records)