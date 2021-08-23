from django import forms


class GroupsForm(forms.Form):
    group_name = forms.CharField(label='Group name', max_length=100)
    group_student = forms.CharField(label='Students in a group')
