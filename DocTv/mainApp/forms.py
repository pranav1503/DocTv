from django import forms
from django.contrib.auth.models import User
from .models import DoctorInfoModel
class RegisterForm(forms.ModelForm):

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder' : 'Your Name'
        }
    ),label='')

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder' : 'Username'
        }
    ),label='')

    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'placeholder' : 'Email'
        }
    ),label='')

    password = forms.CharField(widget=forms.TextInput(
        attrs={
            'type' : 'password',
            'placeholder' : 'Password'
        }
    ),label='')

    class Meta:
        model = User
        fields = ['first_name','email','username','password']


class DoctorForm(forms.ModelForm):

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder' : 'First Name'
        }
    ),label='')

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder' : 'Last Name'
        }
    ),label='')

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder' : 'Username'
        }
    ),label='')

    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'placeholder' : 'Email'
        }
    ),label='')

    password = forms.CharField(widget=forms.TextInput(
        attrs={
            'type' : 'password',
            'placeholder' : 'Password'
        }
    ),label='')

    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password']

FIELD_OF_PRACTICE = (("General Physician","General Physician"),("Bones","Bones"),("Kidney","Kidney"),("ENT","ENT"),("Pediatrician","Pediatrician"))

class RegNumForm(forms.ModelForm):
    reg_num = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder' : 'reg_num'
        }
    ),label='')
    field_of_practice = forms.ChoiceField(choices = FIELD_OF_PRACTICE, label="Field Of Practice",initial="Field Of Practice", widget=forms.Select(), required=True)
    class Meta:
        model = DoctorInfoModel
        fields = ['reg_num','field_of_practice']
