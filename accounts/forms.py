from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django.core.exceptions import ValidationError
import re

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')
        widgets = {
            'phone_number': forms.NumberInput(attrs={
                'placeholder': '07XXXXXXXX or 01XXXXXXXX',
                'oninput': "this.value=this.value.replace(/[^0-9]/g,'');"  # JavaScript to restrict input to numbers only
            }),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        
        # Check that phone_number is a string and contains only digits
        if not isinstance(phone_number, str) or not phone_number.isdigit():
            raise ValidationError("Phone number must contain only digits.")
        
        # Ensure the phone number is exactly 10 digits and starts with '07' or '01'
        if len(phone_number) != 10 or not phone_number.startswith(('07', '01')):
            raise ValidationError("Phone number must start with '07' or '01' and be exactly 10 digits.")
        
        return phone_number


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )
