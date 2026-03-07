import requests
from bs4 import BeautifulSoup

url = "https://www.cbr.ru/scripts/FinInfo.asp"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

rate = soup.find("td", text="USD").find_next_sibling("td").text
rate = float(rate.replace(",", "."))

class CurrencyConverter:
    def __init__(self, rate):
        self.rate = rate

    def convert_to_usd(self, amount):
        return amount / self.rate

converter = CurrencyConverter(rate)

local_amount = float(input("Введите сумму в вашей местной валюте:"))

usd_amount = converter.convert_to_usd(local_amount)

print(f"Сумма в долларах США составляет: {usd_amount:.2f}")
