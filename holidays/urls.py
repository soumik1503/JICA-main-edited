# holidays/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("upload-holidays/", views.upload_holidays, name="upload_holidays"),
    path("holidays/", views.holiday_list, name="holiday_list"),  # JSON for calendar
]
