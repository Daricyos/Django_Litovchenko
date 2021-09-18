from django.db import models


class Student(models.Model):
    first_name = models.CharField("First Name", max_length=200, db_column="First name")
    last_name = models.CharField("Last_name", max_length=200, db_column="Last name")
    age = models.IntegerField("Age", default=18, db_column="Age")
    phone = models.BigIntegerField(null=True, db_column="Phone")
    in_group = models.ForeignKey("group.Groups", null=True, on_delete=models.CASCADE, db_column="Group ID", verbose_name="Group ID")

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age}, {self.phone}"


class Logger(models.Model):
    method = models.CharField(max_length=10)
    path = models.CharField(max_length=200)
    execution_time = models.FloatField(null=False)
    created = models.DateTimeField(auto_now_add=True)
