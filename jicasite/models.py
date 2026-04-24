
from django.db import models

class VisitorStats(models.Model):
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Total Visitors: {self.count}"
