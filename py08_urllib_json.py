import json
import urllib.request
from http.client import HTTPResponse

url = "https://www.cbr-xml-daily.ru/daily_json.js"
with urllib.request.urlopen(url) as result:
    text = result.read().decode("utf-8")
# print(text)

# Десериализация JSON
rates = json.loads(text)
# print(rates)
# Выведите одной строкой кода курс доллара (12:12)
print(rates['Valute']['USD']['Value'])