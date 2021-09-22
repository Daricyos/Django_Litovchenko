from django.urls import path

from sending_email.views import (
    show_email_form,
)

urlpatterns = [
    path('email-us/', show_email_form, name='email-us')
]
