from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .form import ProductForm
from .models import Product

# Create your views here.
# Class or Function Based View

# Function-Based View (FBV)
def productFun(request):
    return HttpResponse("Products Function")

# Class-Based View (CBV)
class ProductView(View):
    def get(self,request):
        return HttpResponse("Products Class")

def create(request):
    form = ProductForm()

    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Success")
    return render(request,'create.html',{'form':form})

def get(request):
    products = Product.objects.all()
    return render(request,"index.html",{'products':products})