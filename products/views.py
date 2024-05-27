from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello Wolrd")


def new(request):
    return HttpResponse("New Products")

