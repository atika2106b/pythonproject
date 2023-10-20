from django.shortcuts import render
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
def register(request):
    return render(request,'Ecom/register.html')        
# Create your views here.
