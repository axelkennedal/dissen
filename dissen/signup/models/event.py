from django.db import models

from company import Company

class Event(models.Model):
    EVENT_TYPE_CHOICES = ["Lunch lecture", "Pub", "Other"]
    event_type = models.ChoiceField(choices=event_type_choices)
    location = models.CharField(max_length=100)
    time = models.DateTimeField()
    price = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
