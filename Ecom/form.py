from django.contrib.auth.forms import UserCreationForm

from .models import User 

from django import forms

class UserForm(UserCreationForm):
    username= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placholder':'Enter Your Name'}))
    email= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placholder':'Enter Your email'}))
    password1= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placholder':'Enter Your pasword'}))
    password2= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placholder':'Confrim password'}))

    class meta:
        model = User
        fields = ['username,email,password1,password2']
    