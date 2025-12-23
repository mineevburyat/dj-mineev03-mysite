from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

class AjaxContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ваше имя'
        }),
        error_messages={
            'required': 'Пожалуйста, введите ваше имя',
            'max_length': 'Имя не должно превышать 100 символов'
        }
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ваш email'
        }),
        error_messages={
            'required': 'Пожалуйста, введите ваш email',
            'invalid': 'Пожалуйста, введите корректный email'
        }
    )
    
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Ваше сообщение',
            'rows': 5
        }),
        error_messages={
            'required': 'Пожалуйста, введите сообщение'
        }
    )
    
    phone = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ваш телефон (необязательно)'
        })
    )