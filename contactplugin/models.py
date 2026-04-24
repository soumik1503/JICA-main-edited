from cms.models.pluginmodel import CMSPlugin
from django.db import models

class ContactPluginModel(CMSPlugin):
    success_message = models.CharField(max_length=200, default="Thanks for contacting us")


class Contact(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    aadhar = models.CharField(max_length=12)
    query = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"
