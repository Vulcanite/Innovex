from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.db import IntegrityError
from website1.decorators import unauthenticated_user


# Create your views here.
def home(request):
    return render(request, "index.html")


#@login_required(login_url='login')
def itdept(request):
    return render(request, "it.html")


#@login_required(login_url='login')
def compsdept(request):
    return render(request, "comps.html")


#@login_required(login_url='login')
def mechdept(request):
    return render(request, "mech.html")


#@login_required(login_url='login')
def extcdept(request):
    return render(request, "extc.html")


#@unauthenticated_user
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
    return render(request, 'index.html')


#@login_required(login_url='login')
def logout(request):
    logout(request)
    return redirect('login')


#@login_required(login_url='login')
def signup(request):
    if request.method == 'POST':
        user_reg = User.objects.create_user(first_name=request.POST.get('first_name'),
                                            password=request.POST.get('password1'),
                                            username=request.POST.get('username'))
        try:
            user_reg.save()
            groups = Group.objects.get(name=request.POST.get('access_level'))
            groups.user_set.add(user_reg)
            return render(request, "index.html")
        except IntegrityError:
            messages.info(request, "Username already present!!")
    return render(request, 'index.html')
