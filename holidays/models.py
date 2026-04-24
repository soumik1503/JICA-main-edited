# holidays/models.py
from django.db import models

class Holiday(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField(unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return f"{self.name} ({self.date})"
