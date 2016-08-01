from django.db import models

class Contact(models.Model):
    """Describes a contact from a company."""

    first_name = models.CharField(max_length = 75)
    last_name = models.CharField(max_length = 75)
    email_address = models.CharField(max_length = 100)
    cell_phone_number = models.CharField(max_length = 50)
    other_phone_number = models.CharField(max_length = 50)
    address = models.CharField(max_length = 100)
    # todo: add a reference to a company
