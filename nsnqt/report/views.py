#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
 
def index(request):
    return render(request, 'index.html')

def daily(request):
    return render(request, 'daily.html')

def monitor(request):
    return render(request, 'monitor.html')

def recommend(request):
    return render(request, 'recommend.html')

def price(request):
    return render(request, 'price.html')
