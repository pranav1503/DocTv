from django.conf.urls import url
from . import views
app_name = "timeslots"

urlpatterns = [
    url(r'^list', views.ListTimeSlot.as_view(), name="list")
]
