from django.shortcuts import render
from django.http import HttpResponse
import requests

def index(request):
    return render(request, 'request/index.html')


def detail(request):
    #if 'POST' in request.method.lower():

    res = requests.get("https://weather.tsukumijima.net/api/forecast/city/{'location'}")
    context = {
        'res':res,
    }

    return render(request, 'request/detail.html', context)