from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.http import HttpResponse

from signup.models.company import Company

def index(request):
    return HttpResponse("Hello, world. You're at the signup index.")

class SignupForm(CreateView):
    model = Company
    fields = ['name', 'description', 'logotype', 'area_of_business', 'employees',
    'first_time_at_fair', 'billing_address']
