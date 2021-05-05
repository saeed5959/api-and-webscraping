import requests
#https://www.coingecko.com/en/api#explore-api
def price(coin):
    m = requests.get("https://api.coingecko.com/api/v3/simple/price", params={'ids': coin, 'vs_currencies': 'usd'})
    first = m.text.find("usd") + 5
    last = m.text.find("}")
    price = m.text[first:last]
    return price

