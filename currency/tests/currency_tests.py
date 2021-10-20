import pytest

import requests

from ..models import Exchange
from ..tasks import get_currency_rates


@pytest.mark.django_db
def test_get_currency():
    exchange = Exchange(
        currency='USD',
        source='bank',
        buy_price=28.50,
        sell_price=28.40,
    )
    exchange.save()
    assert Exchange.objects.all().count() == 1
    assert Exchange.objects.get(pk=1).source == 'bank'
    assert 'bank' in Exchange.objects.last().__str__()


@pytest.mark.django_db
def test_get_currency_task():
    assert get_currency_rates() == "Exchange saved"