from django import http
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def su(Request):
    return HttpResponse('sashwath is good person')
