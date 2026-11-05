from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
# Class or Function Based View
def productFun(request):
    return HttpResponse("Products Function")

class Product(View):
    def get(self,request):
        return HttpResponse("Products Class")