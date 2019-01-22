import json
import requests

ticker_url ='https://api.coinmarketcap.com/v2/ticker/?structure=array'
while True:

    limit = 1
    start = 1
    sort = 'volume_24'
    convert = 'USD'

    choice = input("Do you want to enter any custom parametheres? (y/n)")
    if choice == 'y':
        limit = input('What is the custom limit?: ')
        start = input('What is the custom start number?: ')
        sort = input('What do you want to sort by?: ')
        convert = input('What is your local currency?: ')

        ticker_url += ('&limit='+ str(limit) + '&sort=' + sort + '&start='+ str(start)
         + '&convert=' + convert)

    request = requests.get(ticker_url)
    results = request.json()

    #print(json.dumps(results, sort_keys = True, indent = 4))

    data = results['data']


    for currency in data:
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
