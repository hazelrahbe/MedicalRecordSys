from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
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
            return redirect("home")
        else:
            return redirect("signup")

class Docs(View):
    def get(self, request):
        return HttpResponse("docs")

class Docs(TemplateView):
    template_name = 'docs.html'