"""
Definition of views.
"""

from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django import forms
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.template import RequestContext
from django.db import models
from app.models import Person,Item,Vendor
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

@csrf_protect
def userlogin(request):
    context = {}

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request,user)
            return HttpResponseRedirect(reverse('menu'))
        else:
             context["error"] = "Provide valid credentials !!"
             return render(request,'app/userlogin.html',context)

    else:
        return render(request,'app/userlogin.html',context)


@login_required
def menu(request):


    context = {
            'title':'Main Menu'
        }

    user_id = request.user.id
    staff = Person.objects.get(user_id = user_id)

    if staff.person_role == 'FINANCE' :
        return render(request,'app/menufinance.html',context)
    else:
        return render(request,'app/menu.html',context)

