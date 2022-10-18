from django.db import models


# Create your models here.
class Task(models.Model):
    PRIORITY = (
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High')
    )

    name = models.CharField(max_length=255, blank=False, null=False)
    date = models.DateTimeField(default=None, null=True, blank=True)
    completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=1, choices=PRIORITY, default='L')

    def __str__(self):
        return self.name
