from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    short_description = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name
