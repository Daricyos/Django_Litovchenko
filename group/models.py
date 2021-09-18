from django.db import models


class Groups(models.Model):
    group_name = models.CharField("Group Name", max_length=200, db_column="Group name")
    group_student = models.IntegerField("Students in group", null=True, db_column='Students in group')
    group_curator = models.OneToOneField("teacher.Teacher", null=True, on_delete=models.CASCADE, db_column="Curator")
    group_headman = models.OneToOneField("students.Student", null=True, on_delete=models.CASCADE, db_column="Headman")

    def __str__(self):
        return f"{self.group_name}, {self.group_student}, {self.group_curator}, {self.group_headman}"
