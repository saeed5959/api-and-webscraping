from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import app.gold_scrapy as gold_scrapy
import app.coin_api as coin_api
from app.models import contact_form

# Create your views here.

def home(request):
    t = loader.get_template('home.html')
    gold_price ,gold_change ,dollar_price,dollar_change,stock_price,stock_change  =gold_scrapy.price()

    if request.method=='POST':
        if 'crypto' in request.POST:
            coin = request.POST.get('search')
            coin_object = coin_api.market(coin)
            if coin_object.text!='[]':
                coin_market = coin_object.json()[0]
                return HttpResponse(t.render({"gold_price": gold_price, "gold_change": gold_change,
                                              "dollar_price": dollar_price, "dollar_change": dollar_change,
                                              "stock_price": stock_price, "stock_change": stock_change,
                                              "coin": coin_market['name'], "coin_price": coin_market['current_price'],
                                              "high_24h": coin_market["high_24h"], "low_24h": coin_market["low_24h"],
                                              "price_change_24h": coin_market["price_change_24h"],
                                              'price_change_percentage_24h': coin_market['price_change_percentage_24h'],
                                              "image":coin_market["image"],"error":""}, request))
            else:
                return HttpResponse(t.render({"gold_price": gold_price, "gold_change": gold_change,
                                              "dollar_price": dollar_price, "dollar_change": dollar_change,
                                              "stock_price": stock_price, "stock_change": stock_change,
                                              "error":"there is not such a coin"}, request))

        elif 'contact' in request.POST:
            p = contact_form(Name=request.POST["Name"], Email=request.POST['Email'],
                             Subject=request.POST['Subject'], Message=request.POST['Message'])
            p.save()
            return HttpResponse(t.render({"gold_price": gold_price, "gold_change": gold_change,
                                          "dollar_price": dollar_price, "dollar_change": dollar_change,
                                          "stock_price": stock_price, "stock_change": stock_change,
                                          "error": "","thank": "ممنون به خاطر نظری که قرار دادی!"}, request))

    return HttpResponse(t.render({"gold_price":gold_price,"gold_change":gold_change,
                                  "dollar_price":dollar_price,"dollar_change":dollar_change,
                                  "stock_price":stock_price,"stock_change":stock_change,
                                  "error": ""}, request))