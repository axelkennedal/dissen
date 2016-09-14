from django.db import models
from django.core.validators import MinValueValidator

class Company(models.Model):
    """Describes a company/organization participating or interested in D-Dagen"""

    def __str__(self):
        return self.name + ": " + self.area_of_business

    # filled in by company
    AREA_OF_BUSINESS_CHOICES = (
        ("finance", "Finance"),
        ("appdev", "App Development"),
        ("consulting", "Consulting"),
        ("entertainment", "Entertainment"),
        ("comm", "Communication"),
        ("it", "IT Services"),
        ("prodev", "Product Development"),
        ("info", "Information"),
        ("edu", "Education"),
        ("data", "Data & Search"),
        ("fash", "Fashion"),
        ("sec", "Security"),
        ("man", "Management"),
    )
    name = models.CharField(max_length=50)
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
    priority = models.CharField(choices=PRIORITY_CHOICES, default=PRIORITY_CHOICES[0], max_length=10)

    def calculateTotalPrice(self):
        """Sum up the prices of the packages the company has selected for this instance of D-Dagen. Assumes there is only one instance of each package."""

        totalPrice = 0
        # todo
        return totalPrice

class CompanyStatus(models.Model):
    """A company can be in a specific status depending on how far they've come in the application process. A new instance of this class should be created each time the company changes status, so we can track change over time (using the TIMESTAMPs). Statuses are managed by the project team or automatically by the system."""

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    TIMESTAMP = models.DateTimeField(auto_now_add = True)
    STATUS_CHOICES = (
        ("notcontacted", "Not Contacted"),
        ("contacted", "Contacted - Waiting to sign up"),
        ("signedup", "Signed Up - Waiting for contract to be signed"),
        ("contractsigned", "Contract Signed"),
        ("dec", "Declined")
    )
    STATUS = models.CharField(choices=STATUS_CHOICES,default=STATUS_CHOICES[0], max_length=100)
