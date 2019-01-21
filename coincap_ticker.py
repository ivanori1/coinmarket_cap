import json
import requests

ticker_url ='https://api.coinmarketcap.com/v2/ticker/?structure=array'

limit = 1
start = 1
sort = 'volume_24'
convert = 'EUR'

choice = input("Do you want to enter any custom parametheres? (y/n)")
if choice == 'y':
    limit = input('What is the custom limit?: ')
    start = input('What is the custom start number?: ')
    sort = input('What do you want to sort by?: ')
    convert = input('What is your local currency?: ')

    ticker_url += '&limit='+ limit + '&sort=' + sort + '&start='+ start + '&convert=' + convert

request = requests.get(ticker_url)
results = request.json()

print(json.dumps(results, sort_keys = True, indent = 4))

data = results['data']


for currency in data:
    rank = currency['rank']
    name = currency['name']
    symbol = currency['symbol']
    supply = int(currency['circulating_supply'])
    quotes = currency[quotes][convert]
    markets = quotes['market_cap']
    price = quotes['price']
    volume = quotes['volume_24']
