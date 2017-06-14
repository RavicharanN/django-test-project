# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .forms import UserForm

# Create your views here.
# def login_user(request):
# 	if request.method == "POST":
# 		username = request.POST['username']
# 		password = request.POST['password']
# 		user = authenticate(username=username,password=password)
# 		if user is not None:
# 			if user.is_active:
#                 login(request, user)
#                 return render(request, 'index.html', {})
#             else:    
#                 return render(request, 'music/login.html', {'error_message': 'Your account has been disabled'})
# 		else:
# 			return render(request,'login_user.html',{'error_message':'INvalid Credentials! Plz re-enter'})
# 	return render(request,'login_user.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                #albums = Album.objects.filter(user=request.user)
                return render(request, 'index.html', {})
            else:
                return render(request, 'login_user.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login_user.html', {'error_message': 'Invalid login'})
    return render(request, 'login_user.html')

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'login_user.html', context)
		

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'index.html', {})
    context = {
        "form": form,
    }
    return render(request, 'register.html', context)

def index(request):
	if not request.user.is_authenticated():
		return render(request,'login_user.html')
	else :	
		return render(request,'index.html', {})



