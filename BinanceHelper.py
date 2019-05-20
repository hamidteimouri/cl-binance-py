import requests


class BinanceHelper:
    api_key = ''
    secret_key = ''

    base_api_url = "https://api.binance.com"

    def ticker24(self):
        reqeustResult = requests.get(self.base_api_url + '/api/v1/ticker/24hr')
        content = reqeustResult.content
        return content
