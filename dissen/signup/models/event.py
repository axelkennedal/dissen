from django.db import models

from company import Company

class Event(models.Model):
    """Describes an Event a company organizes together with D-Dagen"""

    def __str__(self):
        return self.company.name + " " + self.event_type + " " + self.time

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    TIMESTAMP = models.DateTimeField(auto_now_add = True)
    EVENT_TYPE_CHOICES = (
        ("lunch", "Lunch lecture"),
        ("pub", "Pub"),
        ("other", "Other")
    )
    event_type = models.CharField(choices=EVENT_TYPE_CHOICES, max_length=100)
    location = models.CharField(max_length=100)
    time = models.DateTimeField()
    price = models.IntegerField()
