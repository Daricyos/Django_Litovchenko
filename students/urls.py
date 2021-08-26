from django.urls import path

from students.views import (
    create_student,
    delete_student,
    edit_student,
    generate_students,
    list_students,
    one_students,
)

urlpatterns = [
    path('list_students/', list_students, name='list-students'),
    path('one_students/', one_students, name='one-students'),
    path('generate_students/<int:student_number>', generate_students, name='generate-students'),
    path('create_student', create_student, name='create-student'),
    path('edit_student/<int:student_id>', edit_student, name='edit-student'),
    path('delete_student/<int:student_id>', delete_student, name='delete-student'),
]
