from random import randrange

from django.core.management.base import BaseCommand, CommandError # noqa

from faker import Faker

from group.models import Groups

from students.models import Student

from teacher.models import Teacher


teacher_subjects = ['English', 'Math', 'Physics', 'Computer science', 'History', 'Geography', 'Geometry', 'Japanese']
    
class Command(BaseCommand):
    help = 'Genereates random teacher base on input amount' # noqa

    def add_arguments(self, parser):
        parser.add_argument('number_of_teacher', nargs='?', type=int, default=1)

    def handle(self, *args, **options):
        fake = Faker()
        for i in range(options['number_of_teacher']):
            teacher = Teacher(subject=teacher_subjects[fake.random_int(0, 7)],
                              first_name=fake.first_name(),
                              last_name=fake.last_name(),
                              age=fake.random_int(27, 60))
            teacher.save()

            group = Groups(group_name=teacher.subject)
            group.save()

            result = []
            for student in range(fake.random_int(5, 15)):
                student = Student(first_name=fake.first_name(),
                                  last_name=fake.last_name(),
                                  age=fake.random_int(18, 26),
                                  in_group=group)
                result.append(student)

            Student.objects.bulk_create(result)
            monitor = Student.objects.filter(in_group=group.id).last()

            group.group_student = len(result)
            group.group_curator = teacher
            group.group_headman = monitor
            group.save()

        self.stdout.write(self.style.SUCCESS(f"Successfully created {options['number_of_teacher']} teacher(s)"))
