from django.db import models

class Package(models.Model):
    """Describes a package."""

    def __str__(self):
        return self.company.name

    class Meta:
        abstract = True

    PRICE = models.IntegerField()
    DESCRIPTION = models.CharField(max_length = 75)
    TIMESTAMP = models.DateTimeField(auto_now_add = True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
