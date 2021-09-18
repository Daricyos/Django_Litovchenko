from django.contrib import admin

from .models import Logger
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "age", "phone", "group_id", "group_name")
    list_filter = ("age", "last_name")
    search_fields = ("last_name__startswith", "first_name__startswith")


    def group_id(self, obj):
        return f"Group ID: {obj.in_group.id}"
    group_id.short_description = 'Group ID'


    def group_name(self, obj):
        return obj.in_group.group_name
    group_name.short_description = 'Group name'


@admin.register(Logger)
class LoggerAdmin(admin.ModelAdmin):
    list_display = ("method", "path", "execution_time", "created")
