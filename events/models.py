# events/models.py
from django.db import models
from cms.models.pluginmodel import CMSPlugin

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="event_gallery/")
    caption = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.event.title} - {self.caption or 'Image'}"
