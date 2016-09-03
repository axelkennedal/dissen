from django.db import models
from django.core.validators import MinValueValidator

class Company(models.Model):
    """Describes a company/organization participating or interested in D-Dagen"""

    def __str__(self):
        return self.name + ": " + area_of_business

    # filled in by company
    AREA_OF_BUSINESS_CHOICES = (
        ("finance", "Finance"),
        ("appdev", "App Development"),
        ("consulting", "Consulting"),
        ("games", "Games"),
        ("comm", "Communication")
    )
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1100)
    logotype = models.FileField()
    area_of_business = models.CharField(choices=AREA_OF_BUSINESS_CHOICES, default="Pick one", max_length=100)
    employees = models.IntegerField(validators=[MinValueValidator(1)])
    first_time_at_fair = models.BooleanField(default=True)
    billing_address = models.CharField(max_length=200)

    # for internal use only
    PRIORITY_CHOICES = (
        ("low", "LOW"),
        ("mid", "MID"),
        ("high","HIGH")
    )
    comment = models.CharField(max_length=500)
    priority = models.CharField(choices=PRIORITY_CHOICES, default=PRIORITY_CHOICES[0], max_length=100)
