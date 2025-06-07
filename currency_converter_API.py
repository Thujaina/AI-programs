import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}"
    response = requests.get(url)
    data = response.json()
    rate = data['rates'][to_currency.upper()]
    result = amount * rate
    print(f"{amount} {from_currency} = {result:.2f} {to_currency}")

convert_currency(100, 'USD', 'INR')
