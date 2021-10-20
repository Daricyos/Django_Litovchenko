from django.core.management import call_command

from group.models import Groups

import pytest

from students.models import Student

from teacher.models import Teacher


@pytest.mark.django_db
def test_console_command():
    args = ['1']
    options = {}
    call_command('generate_teacher', *args, **options)
    assert Teacher.objects.count() == 1
    assert 1 <= Student.objects.count() <= 15
    assert Groups.objects.count() == 1