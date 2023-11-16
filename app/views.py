from django.shortcuts import render
from django.db.models import Count
from urllib import request
from django.http import HttpResponse
from django.views import View
from . models import Product

def home(request):
    return render(request,"app/home.html")

class CategoryView(View):
    def get(self,request,val):
        product=Product.objects.filter(category=val)
        title=Product.objects.filter(category=val).values('title')
        return render(request,"app/category.html",locals())

