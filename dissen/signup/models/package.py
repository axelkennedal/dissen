from django import models

class Package(models.Model):
    """Describes a package."""

    PRICE = models.DecimalField(max_digits = 9, decimal_places = 2)
    DESCRIPTION = models.CharField(max_length = 75)
    TIMESTAMP = models.DateTimeField(auto_now_add = True)
    # todo: add reference to a company
