from django.forms import ModelForm, inlineformset_factory
from .models.company import Company
from .models.contact import Contact

class SignupForm(ModelForm):
    class Meta:
        # all of the fields declared in the Company model,
        # that the company should fill in
        model = Company
        fields = (
            'name',
            'description',
            #'logotype',
            'area_of_business',
            'employees',
            'first_time_at_fair',
            'billing_address')

# additional fields, for instances to be added to the company instance
# using relations (e.g. foreignkey or manytomany)
ContactFields = (
    'first_name',
    'last_name',
    'email_address',
    'cell_phone_number',
    'other_phone_number',
    'address')
ContactFormSet = inlineformset_factory(Company, Contact, fields=ContactFields, extra=2)
