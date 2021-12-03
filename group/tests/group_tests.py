from django.test import Client

import pytest

from ..models import Groups


@pytest.mark.django_db
def test_get_groups():
    Client().get('/list-group')
    assert Groups.objects.count() == 0


@pytest.mark.django_db
def test_create_group():
    Client().post("/create_groups", data={'group_name': 'Physics', 'group_student': 12})
    assert Groups.objects.count() == 1
    assert Groups.objects.get(pk=1).group_name == 'Physics'
    assert Groups.objects.get(pk=1).group_student == 12


@pytest.mark.django_db
def test_generate_group():
    Client().get('/group_db/10')
    assert Groups.objects.count() == 10
