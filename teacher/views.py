from random import randrange

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from faker import Faker

from .forms import TeacherForm
from .models import Teacher


def list_teacher(request):
    teacher_list = list(Teacher.objects.values().all())
    return HttpResponse(teacher_list)


def generate_teacher(request, teacher_number=100):
    fake = Faker()
    result = []

    if teacher_number > int(100):
        zero = "Не возможно вывести больше 100"
        return HttpResponse(zero)

    elif type(teacher_number) == int:
        for i in range(teacher_number):
            result.append(Teacher(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                age=randrange(27, 80)
            ))
        Teacher.objects.bulk_create(result)

        teacher_get = Teacher.objects.filter().order_by('-id')[:teacher_number]
        output = [f"{teacher.id} {teacher.first_name} {teacher.last_name}, {teacher.age}; \n" for teacher in teacher_get]
        return HttpResponse(output, content_type="text/plain")


def get_teacher(request):
    if request.method == 'GET':
        query = {key: value for key, value in request.GET.items()}
        teachers = Teacher.objects.filter(**query).all()

        output = [f"{teacher.first_name} {teacher.last_name}, {teacher.age}; " for teacher in teachers]
        return HttpResponse(output)


def create_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            Teacher.objects.create(**form.cleaned_data)
            return HttpResponseRedirect(reverse('list-teacher'))
    else:
        form = TeacherForm()

    return render(request, 'create_teacher_form.html', {'form': form})
