from django.db import models

from signup.models.company import Company

class Fair(models.Model):
    """Describes an instance of D-Dagen."""

    location = models.CharField(max_length=200)
    time = models.DateTimeField()
    max_number_of_companies = models.PositiveIntegerField()
    companies = models.ManyToManyField(Company)
