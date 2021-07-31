from django.contrib import admin
from django.urls import path
from students.views import one_students, list_students, generate_students
from group.views import group_db
from teacher.views import generate_teacher

urlpatterns = [
    path('one_students/', one_students),
    path('list_students/', list_students),
    path('generate_students/<int:student_number>', generate_students),
    path('generate_students/', generate_students),
    path('generate_teacher/', generate_teacher),
    path('group_db/', group_db),

    path('admin/', admin.site.urls),
]
