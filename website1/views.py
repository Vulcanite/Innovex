from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.db import IntegrityError
from website1.decorators import unauthenticated_user
from website1.models import Project
from website1.models import UserModel
from website1.models import Feedback

phn=0
org=""
role=""

def home(request):
    

    #add in if to add only unique email:  not UserModel.objects.filter(user_email=request.user.email).exists()
    if request.user.is_authenticated and not UserModel.objects.filter(user_email=request.user.email).exists():
        UserModel.objects.create(organisation=org, user_phone=phn ,user_designation=role, user_name=request.user.username, user_email=request.user.email)
    return render(request, "website1/index.html")

@login_required(login_url='/')
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

    if request.method=="POST":
        rating = int(request.POST.get("rating"))
        cmts = request.POST.get("comments")
        feedb_for_name = request.POST.get("for_proj") 
        # print(rating,cmts,feedb_for_name,request.user, "thisss issssssssssss ")
        Feedback.objects.create(rating=rating, user_feedback=cmts , project_dept=Project.objects.get(proj_title=feedb_for_name).dept , project_f=Project.objects.get(proj_title=feedb_for_name), user_f=UserModel.objects.get(user_email=request.user.email))


    return render(request, "website1/it.html",context)

@login_required(login_url='/')
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

    if request.method=="POST":
        rating = int(request.POST.get("rating"))
        cmts = request.POST.get("comments")
        feedb_for_name = request.POST.get("for_proj") 
        # print(rating,cmts,feedb_for_name,request.user, "thisss issssssssssss ")
        print(Project.objects.get(proj_title=feedb_for_name).dept,'thiss issssssssssss')
        Feedback.objects.create(rating=rating, user_feedback=cmts , project_dept=Project.objects.get(proj_title=feedb_for_name).dept , project_f=Project.objects.get(proj_title=feedb_for_name), user_f=UserModel.objects.get(user_email=request.user.email))

    return render(request, "website1/comps.html",context)

@login_required(login_url='/')
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

    if request.method=="POST":
        rating = int(request.POST.get("rating"))
        cmts = request.POST.get("comments")
        feedb_for_name = request.POST.get("for_proj") 
        # print(rating,cmts,feedb_for_name,request.user, "thisss issssssssssss ")
        print(Project.objects.get(proj_title=feedb_for_name).dept,'thiss issssssssssss')
        Feedback.objects.create(rating=rating, user_feedback=cmts , project_dept=Project.objects.get(proj_title=feedb_for_name).dept , project_f=Project.objects.get(proj_title=feedb_for_name), user_f=UserModel.objects.get(user_email=request.user.email))

    return render(request, "website1/mech.html",context)

@login_required(login_url='/')
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

    if request.method=="POST":
        rating = int(request.POST.get("rating"))
        cmts = request.POST.get("comments")
        feedb_for_name = request.POST.get("for_proj") 
        # print(rating,cmts,feedb_for_name,request.user, "thisss issssssssssss ")
        print(Project.objects.get(proj_title=feedb_for_name).dept,'thiss issssssssssss')
        Feedback.objects.create(rating=rating, user_feedback=cmts , project_dept=Project.objects.get(proj_title=feedb_for_name).dept , project_f=Project.objects.get(proj_title=feedb_for_name), user_f=UserModel.objects.get(user_email=request.user.email))
        
    return render(request, "website1/extc.html",context)

def dataentry(request):
    return render(request, "website1/dataentry.html")    

def edit_data(request):
    global phn
    global org
    global role

    if UserModel.objects.filter(user_email=request.user.email).exists():
        return redirect("/")
    elif request.method=="POST":
         
        phn   =request.POST.get("mobile")
        org   =request.POST.get("org")
        role  = request.POST.get("role")
        print(phn,org,role,"thisss issssssssssss ")

        return redirect("/")

    context={
        'email':request.user.email,
        'name' :request.user.first_name + " " + request.user.last_name
    }

    return render(request, "website1/form.html",context) 

@login_required(login_url='login')
def logout(request):
    logout(request)
    return redirect('login')


