from django.contrib import admin

from .models import Groups


@admin.register(Groups)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("group_name", "group_student")
    list_filter = ("group_student", "group_name")
    search_fields = ("group_name__startswith",)
