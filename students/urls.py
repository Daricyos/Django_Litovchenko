from django.urls import path

from students.views import (
    CreateStudentView,
    DeleteStudentView,
    EditStudentView,
    GenerateStudentView,
    HelloView,
    StudentsListView,
)

urlpatterns = [
    path('', HelloView.as_view(), name='hello'),
    path('list_students/', StudentsListView.as_view(), name='list-students'),
    path('generate_students/<int:student_number>', GenerateStudentView.as_view(), name='generate-students'),
    path('create_student', CreateStudentView.as_view(), name='create-student'),
    path('edit_student/<int:pk>/', EditStudentView.as_view(), name='edit-student'),
    path('delete_student/<int:pk>/', DeleteStudentView.as_view(), name='delete-student'),
]
