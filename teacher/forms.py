from django import forms

from .models import Teacher


class TeacherForm(forms.ModelForm):
    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='Last name', max_length=100)
    age = forms.CharField(label='age')

    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'age']
