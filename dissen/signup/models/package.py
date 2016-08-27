from django.db import models

class Package(models.Model):
    """Describes a package."""

    PRICE = models.IntegerField()
    DESCRIPTION = models.CharField(max_length = 75)
    TIMESTAMP = models.DateTimeField(auto_now_add = True)
    # todo: add reference to a company
