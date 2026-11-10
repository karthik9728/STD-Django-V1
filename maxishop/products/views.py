from django.shortcuts import redirect, render, get_object_or_404
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
    return render(request,'product_form.html',{'form':form})

def upsert(request,id=None):
    product = None
    if id:
        product = get_object_or_404(Product, id=id)
    if request.method == "POST":
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('product')
    else:
        form = ProductForm(instance=product)

    return render(request,'product_form.html',{'form':form})

def get(request):
    products = Product.objects.all()
    return render(request,"index.html",{'products':products})

def details(request,id):
    product = get_object_or_404(Product,id = id)
    return render(request, 'details.html', {'product': product})