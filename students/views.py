from random import randrange

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView, View
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic.list import ListView

from faker import Faker

from .forms import StudentForm
from .models import Student


class HelloView(TemplateView):
    template_name = "index.html"


class StudentsListView(ListView):
    model = Student


class GenerateStudentView(View):
    def get(self, request, student_number=100, *args, **kwargs):
        fake = Faker()
        result = []

        for _ in range(student_number):
            result.append(Student(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                age=randrange(16, 35)
            ))
        Student.objects.bulk_create(result)
        return HttpResponseRedirect(reverse('list-students'))


class CreateStudentView(View):
    from_class = StudentForm
    template_name = 'create_student_form.html'

    def get(self, request, *args, **kwargs):
        form = self.from_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.from_class(request.POST)
        if form.is_valid():
            Student.objects.create(**form.cleaned_data)
            return HttpResponseRedirect(reverse('list-students'))

        return render(request, self.template_name, {'form': form})


class EditStudentView(UpdateView):
    model = Student
    template_name = 'students_edit_form.html'
    form_class = StudentForm
    success_url = reverse_lazy('list-students')


class DeleteStudentView(DeleteView):
    model = Student
    success_url = reverse_lazy('list-students')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


def error404(request, exception):
    return render(request, '404page.html', status=404)


def error500(request):
    return render(request, '500page.html', status=500)
