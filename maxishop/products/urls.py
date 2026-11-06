from django.urls import path
from .import views

# when pass it as class need add .as_view
urlpatterns = [
    path('function',views.productFun),
    path('class',views.ProductView.as_view()),
    path('create',views.create),
    path('',views.get)
]