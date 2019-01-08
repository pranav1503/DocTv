from django.conf.urls import url
from dashboard import views
app_name = 'dashboard'
urlpatterns = [
    url(r'^$',views.dash,name="dash"),
    url(r'^verify/$',views.verify_doctor,name="verify"),
    url(r'^verify/(?P<pk>\d+)$',views.verified,name="verified"),
]
