from django import forms
from .models import Checkout


class BillingForm(forms.ModelForm):
    class Meta:
        model = Checkout
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First name: '
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last name: '
            }),
            'company_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Company name: '
            }),
            'phone_number': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone number: '
            }),
            'email_address': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email address'
            }),
            'country': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Country: '
            }),
            'address_line1': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Address line 1: '
            }),
            'address_line2': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Address line 2: '
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'City: '
            }),
            'district': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'District: '
            }),
            'zip': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Zip code: '
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Notes: '
            })
        }
        fields = ['first_name', 'last_name', 'company_name', 'phone_number', 'email_address', 'country', 'address_line1',
                  'address_line2', 'city', 'district', 'zip', 'notes']
