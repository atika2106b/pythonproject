from django.contrib.auth import authenticate,login,logout
from Ecom.form import UserForm
from django.shortcuts import render,redirect
from django.contrib import messages

def register(request):
    form = UserForm()
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Successfully Save")
            return redirect('/login')
    context={'form':form}
    return render(request,'Ecom/register.html',context)   

def login(request):
    
    if request.method=="POST":

        username = request.POST.get('username') 
        passwd = request.POST.get('password') 
        user = authenticate(request,username = username , password= passwd)
        if user is not None:
            # return render(request,'Ecom/register.html')   
            login(request,user)
            messages.success(request, "login successfully")
            return redirect("/")
        else:
            messages.error(request, "invalid Credientials")
            return redirect("login")    
    return render(request,'Ecom/login.html')   

