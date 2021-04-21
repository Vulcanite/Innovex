from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.db import IntegrityError
from website1.decorators import unauthenticated_user
from website1.models import Project
from website1.forms import RegistrationForm, AccountAuthentication

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


def signin(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("home")
    if request.POST:
        form = AccountAuthentication(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user= authenticate(email = email, password=password)

        if user:
            login(request, user)
            return redirect("itdept")
    else:
        form = AccountAuthentication()
    context['form'] = form

    return render(request, 'website1/login.html', context)



#@login_required(login_url='login')
def logout(request):
    logout(request)
    return redirect('login')


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account =  authenticate(email, password = raw_password)
            login(request, account)
            return redirect('itdept')
        else:
            context['registration_form'] = form

    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'index.html', context)