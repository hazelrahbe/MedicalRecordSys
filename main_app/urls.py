from xml.etree.ElementInclude import include
from django.urls import path
from . import views

urlpatterns = [
 path('', views.Home.as_view(), name="home"),
 path('signup/', views.Signup.as_view(), name="signup"),
 path('docs/', views.DocsList.as_view(), name="docs"),
 path('patient/', views.PatientList.as_view(), name="patient")
]