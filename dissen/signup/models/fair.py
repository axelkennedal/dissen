from django.db import models

class Fair(models.Model):
    """Describes an instance of D-Dagen."""

    location = models.CharField(max_length=200)
    time = models.DateTimeField()
    max_number_of_companies = models.PositiveIntegerField()
