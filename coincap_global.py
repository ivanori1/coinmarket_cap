import json
import requests
from datetime import datetime
currency = 'EUR'

global_url = 'https://api.coinmarketcap.com/v2/global/?convert='+ currency

request = requests.get(global_url)
results = request.json()
#print(json.dumps(results, sort_keys=True, intend=4))

active_currencies = results['data']['active_cryptocurrencies']
active_markets = results['data']['active_markets']
bitcoin_percentage = results['data']['bitcoin_percentage_of_market_cap']
last_updated = results['data']['last_updated']

total_market_cap = results['data']['quotes'][currency]['total_market_cap']
total_volume_24h = results['data']['quotes'][currency]['total_volume_24h']

active_currencies_string = '{:,}'.format(active_currencies)
active_markets_string = '{:,}'.format(active_markets)
global_cap_string = '{:,}'.format(total_market_cap)
global_volume_string = '{:,}'.format(total_volume_24h)
last_updated_string = datetime.fromtimestamp(last_updated).strftime('%B %d, %Y at %I:%M%p')


print()
print('There is currently ' + active_currencies_string + ' active cryptocurrencies and'
+ ' active markets '+ active_markets_string)
print('The global cap of all cryptos is '+ global_cap_string + ' '+ currency +
' and volume is ' + global_volume_string + ' ' + currency)
print('Bitcoin percentage in total is '+ str(bitcoin_percentage))
print('This information is last updated on ' + last_updated_string)
