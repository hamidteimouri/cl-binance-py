from BinanceHelper import BinanceHelper
import json

exchange = BinanceHelper()

ticker24 = exchange.ticker24()
ticker24 = json.loads(ticker24)

for ticker in ticker24:
    print(ticker)
