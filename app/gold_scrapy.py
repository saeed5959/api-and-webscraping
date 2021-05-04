import requests
from bs4 import BeautifulSoup

def price():
    url = "https://www.tgju.org/"

    content = requests.get(url)
    soup = BeautifulSoup(content.text, from_encoding="utf-8")

    gold = soup.find(id="l-irec_future")
    gold_price = gold.find(class_="info-price").text
    gold_change = gold.find(class_="info-change").text

    dollar = soup.find(id="l-price_dollar_rl")
    dollar_price = dollar.find(class_="info-price").text
    dollar_change = dollar.find(class_="info-change").text

    stock = soup.find(id="l-bourse")
    stock_price = stock.find(class_="info-price").text
    stock_change = stock.find(class_="info-change").text

    return gold_price,gold_change,dollar_price,dollar_change,stock_price,stock_change

