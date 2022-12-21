import requests


def get_currency():
    data = requests.get("https://www.cbr-xml-daily.ru/daily_json.js").json()
    return dict(USD=data["Valute"]["USD"], EUR=data["Valute"]["EUR"])
