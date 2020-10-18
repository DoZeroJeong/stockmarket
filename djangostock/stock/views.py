from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
# Create your views here.


def home(request):

    try:
        ticker = request.GET['ticker']
        stock_api = requests.get(
            "https://cloud.iexapis.com/stable/stock/"+ticker+"/quote?token=pk_db6737ecb57f4d10a7eded7efcee08f8")
        stock = json.loads(stock_api.content)
    except Exception as e:
        stock = ""

    content = {'stock': stock}
    return render(request, 'stock/home.html', content)
