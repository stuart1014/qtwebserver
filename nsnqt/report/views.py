#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
 
def index(request):
    return render(request, 'index.html')

def report(request):
	return render(request, 'report.html')

def monitor(request):
	return render(request, 'monitor.html')
