from django import forms
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from .models import Contact


class ContactForm(forms.ModelForm):
    # Validators
    name_validator = RegexValidator(
        regex=r'^[a-zA-Z\s\.-]+$',
        message="Name can only contain letters, spaces, dots, and hyphens."
    )

    # HTML Tag Validator (Sanitization)
    no_html_validator = RegexValidator(
        regex=r'^[^<>]*$',
        message="HTML tags (mapped by < or >) are not allowed."
    )

    name = forms.CharField(
        min_length=2,
        max_length=100,
        validators=[name_validator],
        widget=forms.TextInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
    )

    age = forms.IntegerField(
        validators=[MinValueValidator(10), MaxValueValidator(999)],
        widget=forms.NumberInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
            'max': '999',
            'min': '10'
        })
    )

    query = forms.CharField(
        min_length=10,
        max_length=2000,
        validators=[no_html_validator],
        widget=forms.Textarea(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500', 
            'rows': 4
        })
    )

    gender = forms.ChoiceField(
        choices=[
            ('', 'Select Gender'),
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Other', 'Other')
        ],
        required=True,
        widget=forms.Select(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
    )
    class Meta:
        model = Contact
        fields = ['name', 'age', 'gender', 'mobile', 'email', 'aadhar', 'query']
        widgets = {
            'mobile': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'email': forms.EmailInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'aadhar': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
        }


    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile', '')
        if not mobile.isdigit() or len(mobile) != 10:
            raise forms.ValidationError("Mobile number must be exactly 10 digits.")
        return mobile

    def clean_aadhar(self):
        aadhar = self.cleaned_data.get('aadhar', '')
        if not aadhar.isdigit() or len(aadhar) != 12:
            raise forms.ValidationError("Aadhar number must be exactly 12 digits.")
        return aadhar
