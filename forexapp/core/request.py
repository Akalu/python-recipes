import requests
from http import HTTPStatus
import json


def fetch_exchange_rates_by_currency(currency, access_key):
    response = requests.get(f'http://data.fixer.io/api/latest?base={currency}&access_key={access_key}')

    if response.status_code == HTTPStatus.OK:
        return json.loads(response.text)
    elif response.status_code == HTTPStatus.NOT_FOUND:
        raise ValueError(f'Could not find the exchange rates for: {currency}.')
    elif response.status_code == HTTPStatus.BAD_REQUEST:
        raise ValueError(f'Invalid base currency value: {currency}')
    else:
        raise Exception((f'Something went wrong and we were unable to fetch'
                         f' the exchange rates for: {currency}'))
