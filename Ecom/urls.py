from django.urls import path
from . import views
from Ecom.controller import  authview

urlpatterns= [

    path('',views.home , name="home"),
    path('productviwes/<str:myslug>',views.productviwes , name="productviwes"),
    path('register',authview.register , name="register")
    
]