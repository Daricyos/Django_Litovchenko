from django.urls import path

from sending_email.views import (
    ShowEmailFormView,
)

urlpatterns = [
    path('email-us/', ShowEmailFormView.as_view(), name='email-us')
]
