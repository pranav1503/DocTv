from django.shortcuts import render,reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import re

from .forms import RegisterForm,DoctorForm,RegNumForm
################################################ PATIENT'S PORTAl #####################################


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = RegisterForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            new_user = authenticate(username=user_form.cleaned_data['username'],password=user_form.cleaned_data['password'])
            login(request, new_user)
            return HttpResponseRedirect(reverse('dashboard:dash'))
        else:
            print("Entered else")
            # if re.match('\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b', user_form.cleaned_data['email']) != None:
            #     message = "The user already exists."
            # else:
            #     message = "Enter appropriate email id"
            message = "Enter correct email or the user already exists."
            return render(request,'mainApp/register.html',{'user':user_form,'message':message})
    else:
        user_form = RegisterForm()

    return render(request,'mainApp/register.html',{'user':user_form})


class Home(TemplateView):
    template_name = 'mainApp/home.html'


def loginView(request):
    if request.method == 'POST':
        user = authenticate(username = request.POST.get('usernameL'),password = request.POST.get('passwordL'))
        login(request, user)
        return HttpResponseRedirect(reverse('dashboard:dash'))
    return render(request,'mainApp/login.html')

@login_required
def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('mainApp:home'))



#####################################  DOCTOR'S PORTAL ###################################################

def registerD(request):
    registered = True
    if request.method == 'POST':
        user_form = DoctorForm(data=request.POST)
        reg_form = RegNumForm(data=request.POST)

        if user_form.is_valid() and reg_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            reg = reg_form.save(commit=False)
            reg.user = user
            reg.save()
            registered = True
            return HttpResponseRedirect(reverse('mainApp:home'))
        else:
            registered = False
    else:
        user_form = DoctorForm()
        reg_form = RegNumForm()
    return render(request,'mainApp/docReg.html',{'user':user_form,'reg':reg_form,'registered':registered})
