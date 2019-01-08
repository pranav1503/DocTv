from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class DoctorInfoModel(models.Model):
    user = models.OneToOneField(User,related_name="doctor",on_delete=models.DO_NOTHING)
    reg_num = models.CharField(max_length=20,unique=True)
    verify_choice = (
        ('no','no'),
        ('yes','yes'),
    )
    verify = models.CharField(max_length=3,choices=verify_choice,default="no")
    field_of_practice = models.CharField(max_length=20)
    def __str__(self):
        return self.reg_num+" "+ self.user.username
