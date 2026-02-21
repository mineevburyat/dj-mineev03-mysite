from django import forms
from django.core.mail import send_mail, EmailMessage
from captcha.fields import CaptchaField

class ContactForm(forms.Form):
    name = forms.CharField(
        label='Имя',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    subject = forms.CharField(
        label='Тема',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    message = forms.CharField(
        label='Сообщение',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5})
    )
    captcha = CaptchaField(
        label='Код с картинки',
        error_messages={
            'invalid': 'Неверный код с картинки. Попробуйте еще раз.',
            'required': 'Пожалуйста, введите код с картинки.'
        }
    )

