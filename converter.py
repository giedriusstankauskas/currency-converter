import requests
from dotenv import load_dotenv
import os

load_dotenv()

# to_ = "GBP"
# from_ = "EUR"
# amount = 100


def convert(to_, from_, amount):
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_}&from={from_}&amount={amount}"

    payload = {}
    headers = {
        "apikey": os.getenv('API_KEY')
    }

    response = requests.get(url, headers=headers, data=payload)

    result = response.json()
    return round(result['result'], 2)
