from random import randrange

from django.core.management.base import BaseCommand, CommandError # noqa

from faker import Faker

from teacher.models import Teacher


class Command(BaseCommand):
    help = 'Genereates random teacher base on input amount' # noqa

    def add_arguments(self, parser):
        parser.add_argument('number_of_teacher', nargs='?', type=int, default=100)

    def handle(self, *args, **options):
        fake = Faker()
        result = []

        if options['number_of_teacher'] > 100:
            self.stdout.write(self.style.SUCCESS('Error'))
        else:
            for i in range(options['number_of_teacher']):
                result.append(Teacher(
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    age=randrange(27, 80)
                ))
            Teacher.objects.bulk_create(result)

            self.stdout.write(self.style.SUCCESS('Successfully created teacher'))
