from django.urls import path
from .import views

# when pass it as class need add .as_view
urlpatterns = [
    path('function',views.productFun),
    path('class',views.Product.as_view())
]