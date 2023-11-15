from django.shortcuts import render
from django.http import HttpResponse

def send(request):
    return HttpResponse("sendEmail, send funtion!")

# Create your views here.
