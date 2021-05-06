# api_webscraping

**https://saeed-api-scrapy.herokuapp.com/**
~~~~
Back-end:Django(Python)
Front-end:HTML&CSS
~~~~

####This website contains :

~~~~
1)WEB SCRAPY
    prices of gold & dollar & stock market
    using "web scrapy" tool from https://www.tgju.org/

~~~~

~~~~
2)API
    prices of crypto market
    using "api" tool from  https://www.coingecko.com/

~~~~
####How to use?
~~~~
1)clone this repository
git clone https://github.com/saeed5959/mywebsite

2)go to repository's path
cd python-django

3)Create virtualenv named build
virtualenv -p python3 build
source build/bin/activate

2)install all needed packages and migrate and run
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver