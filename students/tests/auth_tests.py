from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.test import Client

import pytest


from pytz import timezone

from ..models import Logger, Student
from ..tasks import delete_logs


@pytest.mark.django_db
def test_user_create():
    User.objects.create_user('Maksym', 'maksym@pochta.com', 'maksympassword')
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_get_student_list():
    Client().get("/list_students")
    assert Student.objects.count() == 0


# @pytest.mark.urls('student_records.urls')
# def test_main(client):
#     response = client.get('')
#     assert response.status_code == 200
#     assert 'Navigation' in response.GET.content.decode("utf-8")


@pytest.mark.django_db
def test_create_adn_delete_student():
    Client().post("/create_student", data={'first_name': 'Maksym',
                                           'last_name': 'Petrenko',
                                           'age': 18,
                                           'phone': 380633911778,
                                           })
    assert Student.objects.count() == 1
    student = Student.objects.last()
    student.delete()
    assert Student.objects.count() == 0


@pytest.mark.django_db
def test_edit_student():
    Client().get('/generate_students/1')
    assert Student.objects.count() == 1

    Client().post('/edit_student/1/', data={'first_name': 'Vova',
                                            'last_name': 'Ivanov',
                                            'age': 28,
                                            'phone': 380999999999,
                                            })
    assert model_to_dict(Student.objects.get(id=1)) == {'id': 1,
                                                        'first_name': 'Vova',
                                                        'last_name': 'Ivanov',
                                                        'age': 28,
                                                        'phone': 380999999999,
                                                        'in_group': None,
                                                        }
    assert 'Vova' in Student.objects.last().__str__()
    p = Student.objects.last()
    p.phone = +380633911844
    p.save()
    assert Student.objects.last().phone == 380633911844


# def test_error_404():
#     response = Client().get("/students404error/")
#     assert response.status_code == 404


@pytest.mark.django_db
def test_loger():
    Client().get("/admin/")
    delete_logs()
    instance = Logger.objects.filter(created__lte=datetime.now(timezone('Europe/Kiev')) - timedelta(days=7))
    assert instance.count() == 0
    assert '' in instance.last().__str__()
