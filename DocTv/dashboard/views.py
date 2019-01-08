from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from mainApp.models import DoctorInfoModel
@login_required
def dash(request):
    return render(request,"dashboard/dash.html")

def verify_doctor(request):
    query = DoctorInfoModel.objects.all().filter(verify="no")
    print(query)
    context = {
        'not_verified' : query,
    }
    return render(request,"dashboard/dash.html",context)

def verified(request,pk=None):
    if pk:
        query = DoctorInfoModel.objects.get(pk=pk)
        query.verify = "yes"
        query.save()
    return HttpResponseRedirect(reverse('dashboard:verify'))
