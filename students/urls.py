from django.urls import path

from students.views import (
    create_student,
    generate_students,
    list_students,
    one_students,
)

urlpatterns = [
    path('students/', list_students, name='list-students'),
    path('one_students/', one_students, name='one-students'),
    path('generate_students/<int:student_number>', generate_students, name='generate-students'),
    path('create_student', create_student, name='create-student'),
]
