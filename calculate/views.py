from django.shortcuts import render
from django.http import HttpResponse

def calculate(request):
    return HttpResponse("calculate, calculate function!")

# Create your views here.
