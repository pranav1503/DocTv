from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,ListView,CreateView,UpdateView,DeleteView
from django.utils import timezone
from django.urls import reverse_lazy
from .models import TimeSlot

class ListTimeSlot(ListView):
    login_url = reverse_lazy('mainApp:login')
    model = TimeSlot
    template_name = 'timeslots/timelist.html'
    context_object_name = 'time_slot_list'
    def get_queryset(self):
        query = TimeSlot.objects.filter(doc = self.request.user)
        print(query)
        return TimeSlot.objects.filter(doc = self.request.user)
