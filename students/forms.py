from django import forms
from django.core.validators import RegexValidator


class StudentForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='Last name', max_length=100)
    age = forms.CharField(label='Age')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{12,15}$', message="Номер телефона необходимо вводить в формате «+380999999999». Допускается до 12 цифр.")
    phone = forms.CharField(label='Phone', required=False, validators=[phone_regex], empty_value=None, widget=forms.TextInput(attrs={'placeholder': '380xxxxxxxxx'}), max_length=12)
