from django.db import models

from company import Company
class Contact(models.Model):
    """Describes a contact from a company."""

    def __str__(self):
        return self.first_name + ' ' + self.last_name + " @ " + self.company.name

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 75)
    last_name = models.CharField(max_length = 75)
    email_address = models.CharField(max_length = 100)
    cell_phone_number = models.CharField(max_length = 50)
    other_phone_number = models.CharField(max_length = 50)
    address = models.CharField(max_length = 100)
