from django.shortcuts import render , redirect
from .models import *
from django.http.response import JsonResponse


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
            context={'products':product}
        else:
            return redirect("/")
    else:
        return redirect("/")
    return render(request,"Ecom/productdetail.html",context)   


def addtocart(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('prod_id'))
        product_check = Product.objects.get(id=prod_id)
        if(product_check):
            if(Cart.objects.filter(user=request.user.id, product_id=prod_id)):
                return JsonResponse({'status':"Product already in car"})
            else:
                prod_qty = int(request.POST.get('prod_quantity'))

                if product_check.quantity >= prod_qty:
                    Cart.objects.create(user=request.user, product_id=prod_id ,product_qty=prod_qty)
                    return JsonResponse({'status':"Product added "})
                else:
                    return JsonResponse({'status':"Only"+ str(product_check.quantity)+"quantity avaiable"})
        else:
            return JsonResponse({'status':"no such product"})
    else:
        return JsonResponse({'status':"Login to continue"})
    
    return redirect("/")



# Create your views here.
