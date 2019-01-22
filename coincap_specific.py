import requests
import json

convert = 'USD'

base_url = 'https://api.coinmarketcap.com/v2/'
listing_url = base_url + 'listings'
url_end = '?structure=array&convert=' + convert

request = requests.get(listing_url)
results = request.json()

data = results['data']

ticker_url_pairs = {}

for currency in data:
    symbol = currency['symbol']
    url = currency['id']
    ticker_url_pairs[symbol] = url

# print(ticker_url_pairs)

while True:
    print()
    choice = input('Enter the ticker of cryptocurrency: ')
    choice = choice.upper()
    ticker_url = (base_url + 'ticker/' + str(ticker_url_pairs[choice]) + '/'
        + url_end)

    request = requests.get(ticker_url)
    results = request.json()

    # print(json.dumps(results, sort_keys=True, indent=4))

    currency = results['data'][0]
    rank = currency['rank']
    name = currency['name']
    symbol = currency['symbol']
    circulating_supply = int(currency['circulating_supply'])
    total_supply = int(currency['total_supply'])

    quotes = currency['quotes'][convert]
    market_cap = quotes['market_cap']
    hour_change = quotes['percent_change_1h']
    day_change = quotes['percent_change_24h']
    week_change = quotes['percent_change_7d']

    price = quotes['price']
    volume = quotes['volume_24h']

    volume_string = '{:,}'.format(volume)
    market_cap_string = '{:,}'.format(market_cap)
    circulating_supply_string = '{:,}'.format(circulating_supply)
    total_supply_string = '{:,}'.format(total_supply)

    print(str(rank) + ': ' + name + ' (' + symbol + ')')
    print('Market cap is:\t$'+ market_cap_string)
    print('Price is \t\t$' + str(price))
    print('24h volume: \t\t$'+ volume_string)
    print('Hour Change is\t\t' + str(hour_change) + ' %')
    print('Day Change: \t\t' + str(day_change) + '%')
    print('Week Change: \t\t' + str(week_change) + '%')
    print('Total sypply : \t\t'+total_supply_string)
    print('Corculating supply \t'+ circulating_supply_string)
    print()

    choice = input('Again? (y/n)')
    if choice == 'n':
        break
