from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField(default=18)
    phone = models.BigIntegerField(max_length=15, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age}, {self.phone}"


class Logger(models.Model):
    method = models.CharField(max_length=10)
    path = models.CharField(max_length=200)
    execution_time = models.FloatField(null=False)
    created = models.DateTimeField(auto_now_add=True)
