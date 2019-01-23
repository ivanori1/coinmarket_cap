import os
import json
import time
import requests
from datetime import datetime
from prettytable import PrettyTable

convert = 'EUR'
base_url = 'https://api.coinmarketcap.com/v2/'
listings_url = 'listings/?convert='+ convert
url_end = '/?structure=array&convert=' + convert
request = requests.get(base_url + listings_url)
results = request.json()
data = results['data']

ticker_url_pairs = {}

for currency in data:
    symbol = currency['symbol']
    url = currency['id']
    ticker_url_pairs[symbol] = url


print()
print('ALERT TRACKING')
print()

already_hit_symbol = []

while True:
    with open('alert.txt') as inp:
        for line in inp:
            ticker, amount = line.split()
            ticker = ticker.upper()
            ticker_url = base_url + 'ticker/' + str(ticker_url_pairs[ticker]) + url_end
            request = requests.get(ticker_url)
            results = request.json()

            currency = results['data'][0]
            name = currency['name']
            last_updated = currency['last_updated']
            symbol = currency['symbol']
            quotes = currency['quotes'][convert]
            price = quotes['price']

            if float(price) >= float(amount) and symbol not in already_hit_symbol:
                last_updated_string = datetime.fromtimestamp(last_updated).strftime('%B %d %Y at %I:%M%p')
                print(name + ' hit ' + amount + ' on ' + last_updated_string)
                already_hit_symbol.append(symbol)

    print('...')
    time.sleep(300)