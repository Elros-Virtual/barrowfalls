from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(response):
    return HttpResponse("This is a site")


def v1(response):
    return HttpResponse("v1")
