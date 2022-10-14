from multiprocessing import context
from re import template
from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Docs, Patient, Records
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
# Create your views here.
class Home(View):
    def get(self, request):
        return HttpResponse("Medical Report System")

class Home(TemplateView):
    template_name = "home.html"

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {'form': form}
        return render(request, "registration/signup.html", context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("docs")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)

# class Docs(View):
#     def get(self, request):
#         return HttpResponse("This is the page for Docs")

@method_decorator(login_required, name='dispatch')
class DocsList(TemplateView):
    model = Docs
    template_name = "docs.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["docs"] = Docs.objects.filter(user=self.request.user)
        return context

# class Patient(View):
#     def get(self, request):
#         return HttpResponse("patient")

class PatientList(TemplateView):
    model = Patient
    template_name = "patient.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['patient'] = Patient.objects.all()
        searchName = self.request.GET.get("lastname")
        if searchName != None:
            context["patient"] = Patient.objects.filter(lastname__icontains=searchName)
        else:
            context["patient"] = Patient.objects.all()
        return context

class PatientCreate(CreateView):
    model = Patient
    fields = ['firstname', 'lastname', 'ethnicity', 'dob']
    template_name = "patient_create.html"
    def form_valid(self, form):
        return super(PatientCreate, self).form_valid(form)
    success_url = "/patient/"

class RecordDeets(TemplateView):
    model = Patient
    template_name = "patient_details.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["patient"] = Patient.objects.get(pk=context['pk'])
        tab = self.request.GET.get('tab')
        context['tab'] = tab
        print(context)
        return context