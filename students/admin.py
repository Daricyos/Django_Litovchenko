from django.contrib import admin

from .models import Logger
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "age", "phone")
    list_filter = ("age", "last_name")
    search_fields = ("last_name__startswith", "first_name__startswith")


@admin.register(Logger)
class LoggerAdmin(admin.ModelAdmin):
    list_display = ("method", "path", "execution_time", "created")
