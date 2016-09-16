from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.http import HttpResponse

from .models.company import Company
from .forms import SignupForm

def index(request):
    return HttpResponse("Hello, world. You're at the signup index.")

class Signup(CreateView):
    form_class = SignupForm
    template_name = 'signup/formfield.html'
    model = Company
