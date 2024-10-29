import requests
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
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
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, "Logged in successfully!")

            return redirect(home)
        else:
            messages.error(request,"Invalid Credentials")
            return redirect(login)
    return render(request,'royalrumble/login.html')
def u_logout(request):
    logout(request)
    return redirect('login')

def signup(request):
    if request.method=='POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        c_pw = request.POST.get('c_pw')
        print(f'p1 ={password} p2={c_pw}')
        if password==c_pw:
            user = User.objects.create(
                username=username,
                email=email,
                password=password
            )
            messages.success(request,"Successfully Created Account ")
            return redirect(signup)
        else:
            messages.error(request,"Password Doesn't Match")
            return redirect(signup)


    return render(request,'royalrumble/signup.html')
def upload(request):
    if request.method=='POST':
        name = request.POST.get('name')
        weight = request.POST.get('weight')
        height = request.POST.get('height')
        signature = request.POST.get('signature')
        image = request.FILES.get('image')

        wrestler = Wrestlers(name=name, weight=weight, height=height, signature=signature, image=image,author = request.user)
        wrestler.save()
        messages.success(request, "Wrestler information uploaded successfully, You wanna upload another? :)!")
        return redirect(upload)
    return render(request, 'royalrumble/upload.html')
def edit(request, pk ):
    wrestler = Wrestlers.objects.get(id=pk)
    if request.method=='POST':
        name = request.POST.get('name')
        weight = request.POST.get('weight')
        height = request.POST.get('height')
        signature = request.POST.get('signature')
        image = request.FILES.get('image')

        wrestler.name = name
        wrestler.weight = weight
        wrestler.height = height
        wrestler.signature = signature
        wrestler.image = image

        wrestler.save()

        return redirect(edit)
    return render(request,"royalrumble/edit.html",{'wrestler':wrestler})