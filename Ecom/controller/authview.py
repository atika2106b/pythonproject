from django.contrib.auth import authenticate,login,logout
from Ecom.form import UserForm
from django.shortcuts import render

def register(request):
    form = UserForm()
    context={'form':form}
    return render(request,'Ecom/register.html')   