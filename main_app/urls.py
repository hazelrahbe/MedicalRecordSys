from xml.etree.ElementInclude import include
from django.urls import path
from . import views

urlpatterns = [
 path('', views.Home.as_view(), name="home"),
 path('signup/', views.Signup.as_view(), name="signup"),
 path('docs/', views.DocsList.as_view(), name="docs"),
 path('patient/', views.PatientList.as_view(), name="patient"),
 path('patient/new/', views.PatientCreate.as_view(), name="patient_create"),
 path('patient/<int:pk>/', views.RecordDeets.as_view(), name="patient_details"),
 path('patient/<int:pk>/update/', views.RecordDeetsUpdate.as_view(), name="patient_details_update")
]