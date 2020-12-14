from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *

def home_view(request):
    user = request.user
    hello = 'Hello world'

    context = {
        'user': user,
        'hello' : hello,
    }
    return render(request, 'home.html', context)
    
def register(request):                                             
    form=UserForm()
    if request.method == 'POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'You Have Successely Registered : ' +  user)
            return redirect("/")
       
    content={'form':form}
    return render(request,'register.html',content)

def login_id(request):

    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request,"User Is Not Created ")

    content={}
    return render(request,'login.html',content)




def logout_id(request):
    logout(request)
    return redirect("/")