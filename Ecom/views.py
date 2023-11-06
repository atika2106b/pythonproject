from django.shortcuts import render , redirect
from .models import *

def home(request):
    categories=Category.objects.filter(status=0)
    context={'category':categories}
    return render(request,'Ecom/index.html',context)

def productviwes(request,myslug):
    if(Category.objects.filter(slug=myslug , status=0)):
        product=Product.objects.filter(category__slug=myslug)
        context={'myproducts':product}
        return render(request,'Ecom/products.html',context)


def productDetails(request,cat_slug,prod_slug):
    if(Category.objects.filter(slug=cat_slug , status=0)):
        if(Product.objects.filter(slug=prod_slug, status=0)):
            product=Product.objects.filter(slug=prod_slug,status=0).first
            context={'singleprod':product}
        else:
            return redirect("/")
    else:
        return redirect("/")
    return render(request,"Ecom/productdetail.html",context)        
     
# Create your views here.
