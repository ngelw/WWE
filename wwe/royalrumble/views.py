import requests
from bs4 import BeautifulSoup
from django.shortcuts import render

# Create your views here.
def home(requests):
    return render(requests, 'royalrumble/index.html')
def upload(requests):
    return render(requests, 'royalrumble/upload.html')