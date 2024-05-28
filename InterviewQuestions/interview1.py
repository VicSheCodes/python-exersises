import requests
from datetime import datetime, timedelta

base_link = 'https://fapi.binance.com'
endpoint = '/fapi/v1/exchangeInfo'


def find_symbol(json_f, date):
    for json_s in json_f['symbols']:
        if json_s['baseAsset'] == 'BTC' and json_s['deliveryDate'] >= date:
            yield json_s['pair']


def get_json(base_link=base_link, endpoint=endpoint):
    response = requests.get(f'{base_link}{endpoint}')
    timestamp = datetime.now().timestamp()
    lookup_date = timestamp + 7 * 24 * 60 * 60

    if response.status_code == 200:
        yield from find_symbol(json_f=response.json(), date=lookup_date)


if __name__ == '__main__':
    result = get_json()
    one_week_later = datetime.now() + timedelta(weeks=1)
    for pair in result:
        print(f"For baseAsset=BTC, and deliveryDate after {one_week_later}: {pair}")
