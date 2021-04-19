from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.db import IntegrityError
from website1.decorators import unauthenticated_user
from website1.models import Project

def itdept(request):
    datait=Project.objects.filter(dept='it')
    datait_rb=Project.objects.filter(dept='it').filter(proj_category='RESEARCH BASED')
    datait_pd=Project.objects.filter(dept='it').filter(proj_category='PRODUCT DEVELOPMENT')
    datait_env=Project.objects.filter(dept='it').filter(proj_category='ENVIRONMENT SUSTAINABILITY')
    # data=Project.objects.all()

    # print(datait.values())
    # print(datait_rb.values())
    # print(datait_pd.values())
    # print(datait_env.values())
    context={
    'datait':datait,
    'datait_rb':datait_rb,
    'datait_pd':datait_pd,
    'datait_env':datait_env
    }
    return render(request, "website1/it.html",context)


def compsdept(request):
    datacomps=Project.objects.filter(dept='comps')
    datacomps_rb=Project.objects.filter(dept='comps').filter(proj_category='RESEARCH BASED')
    datacomps_pd=Project.objects.filter(dept='comps').filter(proj_category='PRODUCT DEVELOPMENT')
    datacomps_env=Project.objects.filter(dept='comps').filter(proj_category='ENVIRONMENT SUSTAINABILITY')
    # data=Project.objects.all()

    # print(datacomps.values())
    # print(datacomps_rb.values())
    # print(datacomps_pd.values())
    # print(datacomps_env.values())
    context={
    'datacomps':datacomps,
    'datacomps_rb':datacomps_rb,
    'datacomps_pd':datacomps_pd,
    'datacomps_env':datacomps_env
    }
    return render(request, "website1/comps.html",context)


def mechdept(request):
    datamech=Project.objects.filter(dept='mech')
    datamech_rb=Project.objects.filter(dept='mech').filter(proj_category='RESEARCH BASED')
    datamech_pd=Project.objects.filter(dept='mech').filter(proj_category='PRODUCT DEVELOPMENT')
    datamech_env=Project.objects.filter(dept='mech').filter(proj_category='ENVIRONMENT SUSTAINABILITY')
    # data=Project.objects.all()

    # print(datamech.values())
    # print(datamech_rb.values())
    # print(datamech_pd.values())
    # print(datamech_env.values())
    context={
    'datamech':datamech,
    'datamech_rb':datamech_rb,
    'datamech_pd':datamech_pd,
    'datamech_env':datamech_env
    }
    return render(request, "website1/mech.html",context)


def extcdept(request):
    dataextc=Project.objects.filter(dept='extc')
    dataextc_rb=Project.objects.filter(dept='extc').filter(proj_category='RESEARCH BASED')
    dataextc_pd=Project.objects.filter(dept='extc').filter(proj_category='PRODUCT DEVELOPMENT')
    dataextc_env=Project.objects.filter(dept='extc').filter(proj_category='ENVIRONMENT SUSTAINABILITY')
    # data=Project.objects.all()

    # print(dataextc.values())
    # print(dataextc_rb.values())
    # print(dataextc_pd.values())
    # print(dataextc_env.values())
    context={
    'dataextc':dataextc,
    'dataextc_rb':dataextc_rb,
    'dataextc_pd':dataextc_pd,
    'dataextc_env':dataextc_env
    }
    return render(request, "website1/extc.html",context)

def dataentry(request):
    return render(request, "website1/dataentry.html")    


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
    return render(request, 'website1/index.html')


#@login_required(login_url='login')
def logout(request):
    logout(request)
    return redirect('login')


def signup(request):
    if request.method == 'POST':
        user_reg = User.objects.create_user(first_name=request.POST.get('first_name'),
                                            password=request.POST.get('password1'),
                                            username=request.POST.get('username'))
        try:
            user_reg.save()
            groups = Group.objects.get(name=request.POST.get('access_level'))
            groups.user_set.add(user_reg)
            return render(request, "website1/index.html")
        except IntegrityError:
            messages.info(request, "Username already present!!")
    return render(request, 'website1/index.html')
