from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
# Class or Function Based View

# Function-Based View (FBV)
def productFun(request):
    return HttpResponse("Products Function")

# Class-Based View (CBV)
class Product(View):
    def get(self,request):
        return HttpResponse("Products Class")