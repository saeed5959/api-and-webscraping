import requests
#https://www.coingecko.com/en/api#explore-api
def market(coin):
    m = requests.get("https://api.coingecko.com/api/v3/coins/markets", params={'ids': coin, 'vs_currency': 'usd'})
    return m

