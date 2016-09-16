from django.forms import ModelForm
from .models.company import Company

class SignupForm(ModelForm):
    # additional fields, for instances to be added to the company instance
    # using relations (e.g. foreignkey or manytomany)

    class Meta:
        # all of the fields declared in the Company model,
        # that the company should fill in
        model = Company
        fields = (
            'name',
            'description',
            'logotype',
            'area_of_business',
            'employees',
            'first_time_at_fair',
            'billing_address')
