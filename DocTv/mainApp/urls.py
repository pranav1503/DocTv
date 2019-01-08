from django.conf.urls import url,include
from mainApp import views

app_name = "mainApp"
urlpatterns = [
    url(r'^$', views.Home.as_view(),name="home"),
    url(r'^register', views.register,name="register"),
    url(r'^login', views.loginView,name="login"),
    url(r'^logout', views.logoutView,name="logout"),
    url(r'^doctor/register', views.registerD,name="registerD"),
    
]
