from random import randrange

from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from faker import Faker

from .forms import StudentForm
from .models import Student


def one_students(request):
    fake = Faker()
    resul = []

    resul.append(Student(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        age=randrange(16, 35)
    ))

    Student.objects.bulk_create(resul)

    students_one = Student.objects.filter().order_by('-id')[0]
    remove_comma = str(students_one).replace(',', ' ')

    return HttpResponse(remove_comma)


def list_students(request):
    students_list = Student.objects.all()
    return render(request, 'students_list.html', {'students': students_list})


def generate_students(request, student_number=100):
    fake = Faker()
    result = []

    if student_number > int(100):
        zero = "Не возможно вывести больше 100"
        return HttpResponse(zero)

    elif type(student_number) == int:
        for i in range(student_number):
            result.append(Student(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                age=randrange(16, 35)
            ))
        Student.objects.bulk_create(result)

        students_get = Student.objects.filter().order_by('-id')[:student_number]
        output = [f"{student.id} {student.first_name} {student.last_name}, {student.age}; \n" for student in students_get]
        return HttpResponse(output, content_type="text/plain")


def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            Student.objects.create(**form.cleaned_data)
            return HttpResponseRedirect(reverse('list-students'))
    else:
        form = StudentForm()

    return render(request, 'create_student_form.html', {'form': form})


def edit_student(request, student_id):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            Student.objects.update_or_create(defaults=form.cleaned_data, id=student_id)
            return HttpResponseRedirect(reverse('list-students'))
    else:
        student = Student.objects.filter(id=student_id).first()
        form = StudentForm(model_to_dict(student))

    return render(request, 'students_edit_form.html', {'form': form, 'student_id': student_id})


def delete_student(request, student_id):
    student = Student.objects.filter(id=student_id)
    student.delete()
    return HttpResponseRedirect(reverse('list-students'))
