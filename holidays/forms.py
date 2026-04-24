# holidays/forms.py
from django import forms

class HolidayUploadForm(forms.Form):
    file = forms.FileField(
        help_text="Upload a CSV/Excel file with columns: name,date,description"
    )
