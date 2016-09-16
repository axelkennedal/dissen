from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse

from .models.company import Company
from .forms import SignupForm, ContactFormSet

def index(request):
    return HttpResponse("Hello, world. You're at the signup index.")

def signup_form(request):
    # The form (has been filled in and) is being submitted
    if request.POST:
        form = SignupForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            contact_formset = ContactFormSet(request.POST, instance = company)
            if contact_formset.is_valid():
                company.save()
                contact_formset.save()
                return HttpResponseRedirect(reverse('signup_complete'))

    # The request type is GET, someone wants to fill it in!
    else:
        form = SignupForm()
        contact_formset = ContactFormSet(instance=Company())
    return render_to_response('signup/signupform.html', {
        "form" : form,
        "contact_formset" : contact_formset,
    }, context_instance=RequestContext(request))

def signup_complete(request):
    return HttpResponse("Thank you for signing up for D-Dagen!")
