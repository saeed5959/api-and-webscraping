from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import app.gold_scrapy as gold_scrapy
import app.coin_api as coin_api

# Create your views here.

def home(request):
    t = loader.get_template('home.html')
    gold_price ,gold_change ,dollar_price,dollar_change,stock_price,stock_change  =gold_scrapy.price()

    if request.method=='POST':
        coin = request.POST.get('search')
        coin_price = coin_api.price(coin)
        return HttpResponse(t.render({"gold_price": gold_price, "gold_change": gold_change,
                                      "dollar_price": dollar_price, "dollar_change": dollar_change,
                                      "stock_price": stock_price, "stock_change": stock_change,
                                      "coin": coin, "coin_price": coin_price,}, request))

    return HttpResponse(t.render({"gold_price":gold_price,"gold_change":gold_change,
                                  "dollar_price":dollar_price,"dollar_change":dollar_change,
                                  "stock_price":stock_price,"stock_change":stock_change,}, request))