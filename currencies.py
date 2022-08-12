import requests
from dotenv import load_dotenv
import os

load_dotenv()


def create_currency_list():
    currencies = []

    url = f"https://api.apilayer.com/exchangerates_data/symbols"
    payload = {}
    headers = {"apikey": os.getenv('API_KEY')}
    response = requests.get(url, headers=headers, data=payload)
    result = response.json()
    for key, value in result['symbols'].items():
        val = f'{value} {key}'
        currencies.append((key, val))
    return currencies
