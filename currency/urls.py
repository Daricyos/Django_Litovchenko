from currency.views import (
    ExchangeListView,
)

from django.urls import path


urlpatterns = [
    path('exchange/', ExchangeListView.as_view(), name='exchange-list')
]
