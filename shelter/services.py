import json

import requests
from django.conf import settings


def exchange_currency(amount, to_):
    """Возвращает размер ЗП с учетом пересчета в рубли по текущему курсу"""
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_}&from=RUB&amount={amount}"
    headers = {"apikey": settings.CURRENCY_API_KEY}

    if amount > 0:
        response = requests.get(url, headers=headers)
        # print(response.json())
        status_code = response.status_code
        # data = json.loads(response.text) - поскольку текст, то выдаст без дробных
        # return int(data['result'])
        return response.json().get('result')


class MyBot:
    URL = 'https://api.telegram.org/bot'
    TOKEN = settings.TELEGRAM_TOKEN

    def send_tg_message(self, text):
        requests.post(
            url=f'{self.URL}{self.TOKEN}/sendMessage',
            data={
                'chat_id': '459156742',
                'text': text
            }
        )
