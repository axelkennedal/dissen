from django.db import models

class Package(models.Model):
    """A package is a set of services D-Dagen can provide to a company."""

    def __str__(self):
        return self.company.name

    class Meta:
        abstract = True

    PRICE = models.IntegerField()
    DESCRIPTION = models.CharField(max_length = 200)
    TIMESTAMP = models.DateTimeField(auto_now_add = True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
