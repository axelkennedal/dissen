from django.contrib import admin

from signup.models.company import Company
from signup.models.event import Event
from signup.models.contact import Contact
from signup.models.fair import Fair
# Register your models here.

admin.site.register(Company)
admin.site.register(Event)
admin.site.register(Contact)
admin.site.register(Fair)
