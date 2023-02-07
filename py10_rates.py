import json
import urllib.request
from http.client import HTTPResponse


def get_rate(currency: str) -> float:
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    with urllib.request.urlopen(url) as result:
        text = result.read().decode("utf-8")

    # Десериализация JSON
    rates = json.loads(text)
    # Выведите одной строкой кода курс доллара (12:12)
    return rates['Valute'][currency]['Value']


def display_rates_table(currencies: list[str]) -> None:
    print("Валюта\tКурс")
    for currency in currencies:
        rate = get_rate(currency)
        print(f"{currency}\t\t{rate}")


if __name__ == "__main__":
    # print(get_rate("USD"), get_rate("EUR"), get_rate("AZN"))

   display_rates_table(["USD", "EUR", "AZN"])
