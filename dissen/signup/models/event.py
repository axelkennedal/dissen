from django.db import models

from company import Company

class Event(models.Model):
    EVENT_TYPE_CHOICES = (
        ("lunch", "Lunch lecture"),
        ("pub", "Pub"),
        ("other", "Other")
    )
    event_type = models.CharField(choices=EVENT_TYPE_CHOICES, max_length=100)
    location = models.CharField(max_length=100)
    time = models.DateTimeField()
    price = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
