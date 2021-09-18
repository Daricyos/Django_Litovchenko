from django.db import models


class Teacher(models.Model):
    subject = models.CharField('Subject', max_length=200, db_column='Subject')
    first_name = models.CharField("First name", max_length=200, db_column="First name")
    last_name = models.CharField("Last name", max_length=200, db_column="Last name")
    age = models.IntegerField("Age", default=18, db_column="Age")

    def __str__(self):
        return f"{self.subject}, {self.first_name} {self.last_name}, {self.age}"
