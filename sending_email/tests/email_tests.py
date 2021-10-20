import pytest

from ..forms import ContactUsForm
from django.core.mail import send_mail


@pytest.mark.django_db
def test_email_form():
    forms = ContactUsForm(data = {
        'contact_name': 'Maksym',
        'title': 'Test',
        'message': 'Hello World',
        'email_from': 'maksym@lemail.com',
    })
    assert forms.is_valid()


@pytest.mark.django_db
def test_email_task():
    assert send_mail("test title",
                     "test message",
                     "maksym@lemail.com",
                     ["maksym1488@lemail.com"],
                     )