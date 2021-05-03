from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

def home(request):
    t = loader.get_template('home.html')
    return HttpResponse(t.render({}, request))