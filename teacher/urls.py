from django.urls import path

from teacher.views import (
    CreateTeacherView,
    DeleteTeacherView,
    EditTeacherView,
    GenerateTeacherViews,
    TeachersListView,
)


urlpatterns = [
    path('generate_teacher/<int:teacher_number>', GenerateTeacherViews.as_view(), name='generate-teacher'),
    path('list_teacher/', TeachersListView.as_view(), name='list-teacher'),
    path('create_teacher', CreateTeacherView.as_view(), name='create-teacher'),
    path('edit_teacher/<int:pk>/', EditTeacherView.as_view(), name='edit-teacher'),
    path('delete_teacher/<int:pk>/', DeleteTeacherView.as_view(), name='delete-teacher'),
]
