from django.db import models

class Company(models.Model):
    """Describes a company/organization participating or interested in D-Dagen"""

    # filled in by company
    company_name = models.CharField(max_length=100)
    description = models.CharField(max_length=1100)
    logotype = models.FileField()
    AREA_OF_BUSINESS_CHOICES = ["Finance", "App Development", "Consulting", "Games", "Communication"]
    area_of_business = models.ChoiceField(choices=AREA_OF_BUSINESS_CHOICES, initial="Pick one")
    employees = models.IntegerField(min_value=1)
    first_time_at_fair = models.BooleanField(default=True)
    billing_address = models.CharField(max_length=200)

    # for internal use only
    comment = models.CharField(max_length=500)
    PRIORITY_CHOICES = ["LOW", "MID", "HIGH"]
    priority = models.ChoiceField(choices=priority_choices, initial=priority_choices[0])
