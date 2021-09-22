from django.views.generic.list import ListView

from .models import Exchange


class ExchangeListView(ListView):
    model = Exchange
