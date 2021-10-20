from django.forms.models import model_to_dict
from django.test import Client

import pytest

from ..models import Teacher


@pytest.mark.django_db
def test_get_teacher():
    Client().get("/list_teacher")
    assert Teacher.objects.count() == 0


@pytest.mark.django_db
def test_create_teacher():
    Client().post("/create_teacher", data={'first_name': 'Maksim',
                                            'last_name': 'Ivanov',
                                            'age': 75
                                            })
    assert Teacher.objects.count() == 1
    assert 'Maksim' in Teacher.objects.last().__str__()


@pytest.mark.django_db
def test_generate_and_edit_teacher():
    Client().get('/generate_teacher/1')
    assert Teacher.objects.count() == 1

    Client().post("/edit_teacher/1/", data={'first_name': 'Lena',
                                            'last_name': 'Popkova',
                                            'age': 23,
                                            })
    assert model_to_dict(Teacher.objects.get(id=1)) == {'id': 1,'subject': '', 'first_name': 'Lena', 'last_name': 'Popkova', 'age': 23}
    assert 'Lena' in Teacher.objects.last().__str__()


@pytest.mark.django_db
def test_delete_teacher():
    Client().get('/generate_teacher/1')
    assert Teacher.objects.count() == 1
    Client().post("/delete_teacher/1/")
    assert Teacher.objects.count() == 0
