import requests
from datetime import datetime, timedelta

base_link = 'https://fapi.binance.com'
endpoint = '/fapi/v1/exchangeInfo'


def find_symbol(json_f, date):
    try:
        for json_s in json_f['symbols']:
            if json_s['baseAsset'] == 'BTC' and json_s['deliveryDate'] >= date:
                yield json_s['pair']
    except KeyError as e:
        print(f"Key error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def get_json(base_link=base_link, endpoint=endpoint):
    try:
        response = requests.get(f'{base_link}{endpoint}')
        response.raise_for_status()  # Raise an HTTPError for bad responses
        timestamp = datetime.now().timestamp()
        lookup_date = timestamp + 7 * 24 * 60 * 60

        yield from find_symbol(json_f=response.json(), date=lookup_date)
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    except ValueError as e:
        print(f"Value error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == '__main__':
    try:
        result = get_json()
        one_week_later = datetime.now() + timedelta(weeks=1)
        for pair in result:
            print(f"For baseAsset=BTC, and deliveryDate after {one_week_later}: {pair}")
    except Exception as e:
        print(f"An error occurred in the main block: {e}")
