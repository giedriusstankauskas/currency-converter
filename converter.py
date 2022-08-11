import requests

to_ = "EUR"
from_ = "GBP"
amount = 100

api_key = "OuFA7kcBjSgF8T0FqY5c2lz4sLbdGEbY"
url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_}&from={from_}&amount={amount}"

payload = {}
headers = {
  "apikey": api_key
}

response = requests.get(url, headers=headers, data=payload)

result = response.json()
print(result['result'])



