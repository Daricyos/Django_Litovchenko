from random import randrange

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import View
from django.views.generic.list import ListView

from faker import Faker

from .forms import GroupsForm
from .models import Groups


class GenerateGroupsView(View):
    def get(self, request, group_number=10, *args, **kwargs):
        fake = Faker()
        resul = []

        for _ in range(group_number):
            resul.append(Groups(
                group_name=fake.job(),
                group_student=randrange(18, 25)
            ))
        Groups.objects.bulk_create(resul)
        return HttpResponseRedirect(reverse('list-group'))


class CreateGroupsView(View):
    from_class = GroupsForm
    template_name = 'create_group_form.html'

    def get(self, request, *args, **kwargs):
        form = self.from_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.from_class(request.POST)
        if form.is_valid():
            Groups.objects.create(**form.cleaned_data)
            return HttpResponseRedirect(reverse('list-group'))

        return render(request, self.template_name, {'form': form})


class GroupsListView(ListView):
    model = Groups
    template_name = 'groups_list.html'
