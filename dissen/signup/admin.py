from django.contrib import admin

from signup.models.company import Company
from signup.models.event import Event
# Register your models here.

admin.site.register(Company)
admin.site.register(Event)
