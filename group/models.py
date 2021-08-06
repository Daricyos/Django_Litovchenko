from django.db import models

class Groups(models.Model):
	group_name = models.CharField(max_length=200)
	group_student = models.IntegerField(default=18)

	def __str__(self):
		return '%s, %s, %s' % (self.id, self.group_name, self.group_student)