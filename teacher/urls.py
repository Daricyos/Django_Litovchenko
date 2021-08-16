from django.urls import path

from teacher.views import (
    create_teacher,
    generate_teacher,
    get_teacher,
    list_teacher,
)


urlpatterns = [
    path('generate_teacher/', generate_teacher, name='generate-teacher'),
    path('get_teacher/', get_teacher, name='get-teacher'),
    path('list_teacher/', list_teacher, name='list-teacher'),
    path('create_teacher', create_teacher, name='create-teacher'),
]
