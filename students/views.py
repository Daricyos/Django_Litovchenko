from django.http import HttpResponse
from faker import Faker
from random import randrange
from .models import Student


def one_students(request):
    fake = Faker()
    resul = []

    resul.append(Student(
        first_name = fake.first_name(),
        last_name = fake.last_name(),
        age = randrange(16, 35)
    ))

    Student.objects.bulk_create(resul)

    students_one = Student.objects.filter().order_by('-id')[0]
    remove_comma = str(students_one).replace(',', ' ')

    return HttpResponse(remove_comma)

def list_students(request):
    students_list = list(Student.objects.values().all())
    return HttpResponse(students_list)

# def get_student(request):
#     if request.method == 'GET':
#         name_filter = request.GET.get('first_name', '')
#         students_list = Student.objects.filter(first_name=name_filter).all()
#         output = '\n '.join(
#             [f"{student.id} {student.first_name} {student.last_name}, {student.age}; " for student in students_list]
#         )
#         return HttpResponse(output)
#     return HttpResponse('Method not found')

def generate_students(request, student_number = 100):
    fake = Faker()
    result = []

    if student_number > int(100):
        zero = "Не возможно вывести больше 100"
        return HttpResponse(zero)

    elif type(student_number)  ==  int:
        for i in range(student_number):
            result.append(Student(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                age=randrange(16,35)
            ))
        Student.objects.bulk_create(result)

        students_get = Student.objects.filter().order_by('-id')[:student_number]
        output = [f"{student.id} {student.first_name} {student.last_name}, {student.age}; \n" for student in students_get]
        return HttpResponse(output, content_type="text/plain")