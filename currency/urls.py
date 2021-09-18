from django.urls import path

from currency.views import (
    ExchangeListView,
)

urlpatterns = [
    path('exchange/', ExchangeListView.as_view(), name='exchange-list')
]