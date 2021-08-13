from django.contrib import admin
from django.urls import path

from group.views import group_db

from students.views import generate_students, list_students, one_students

from teacher.views import generate_teacher, get_teacher

urlpatterns = [
    path('one_students/', one_students),
    path('list_students/', list_students),
    path('generate_students/<int:student_number>', generate_students),
    path('generate_students/', generate_students),
    path('generate_teacher/', generate_teacher),
    path('get_teacher/', get_teacher),
    path('group_db/', group_db),

    path('admin/', admin.site.urls),
]
