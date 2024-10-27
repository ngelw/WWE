import requests
from django.contrib import messages
from bs4 import BeautifulSoup
from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def home(request):
    wrestler = Wrestlers.objects.all()
    
    context = {
        'wrestler':wrestler,
    }
    return render(request, 'royalrumble/index.html',context)
def signup(request):
    return render(request,'royalrumble/signup.html')
def upload(request):
    if request.method=='POST':
        name = request.POST.get('name')
        weight = request.POST.get('weight')
        height = request.POST.get('height')
        signature = request.POST.get('signature')
        image = request.FILES.get('image')

        wrestler = Wrestlers(name=name, weight=weight, height=height, signature=signature, image=image)
        wrestler.save()
        messages.success(request, "Wrestler information uploaded successfully, You wanna upload another? :)!")
        return redirect(upload)


    

    return render(request, 'royalrumble/upload.html')
