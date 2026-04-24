# events/admin.py
from django.contrib import admin
from .models import Event, EventImage

class EventImageInline(admin.TabularInline):  # or StackedInline
    model = EventImage
    extra = 1


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "date")
    search_fields = ("title",)
    inlines = [EventImageInline]
