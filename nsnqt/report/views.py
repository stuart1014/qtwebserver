#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
import report.mongo as mongo
import datetime as dt
 
def index(request):
    return render(request, 'index.html')

def daily(request):
    return render(request, 'daily.html')

def monitor(request):
    return render(request, 'monitor.html')

def recommend(request):
    return render(request, 'recommend.html')

def price(request):
    db = mongo.dbdata()
    out_format = ["policy", "current_balance", "enable_balance", "asset_balance", "stocknumber", "stocklist", "market_value", "limitnumber"]
    server = db.dbserver
    fund = db._getdata(db='trade',collection='policydetail', isfilt=False, out=out_format)
    return render(request, 'price.html',{'server':server, 'fund':fund})
