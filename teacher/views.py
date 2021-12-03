from random import randrange

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.base import View
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic.list import ListView

from faker import Faker

from .forms import TeacherForm
from .models import Teacher


class TeachersListView(ListView):
    template_name = 'teachers_list.html'
    model = Teacher


class GenerateTeacherViews(View):
    def get(self, request, teacher_number=100, *args, **kwarks):
        fake = Faker()
        result = []

        for _ in range(teacher_number):
            result.append(Teacher(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                age=randrange(27, 80)
            ))
        Teacher.objects.bulk_create(result)
        return HttpResponseRedirect(reverse('list-teacher'))


class CreateTeacherView(View):
    from_class = TeacherForm
    template_name = 'create_teacher_form.html'

    def get(self, request, *args, **kwargs):
        form = self.from_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.from_class(request.POST)
        if form.is_valid():
            Teacher.objects.create(**form.cleaned_data)
            return HttpResponseRedirect(reverse('list-teacher'))

        return render(request, self.template_name, {'form': form})


class EditTeacherView(UpdateView):
    model = Teacher
    template_name = 'teacher_edit_form.html'
    form_class = TeacherForm
    success_url = reverse_lazy('list-teacher')


class DeleteTeacherView(DeleteView):
    model = Teacher
    success_url = reverse_lazy('list-teacher')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)
