from django.urls import path
from .import views

# when pass it as class need add .as_view
urlpatterns = [
    path('function',views.productFun),
    path('class',views.ProductView.as_view()),
    # path('create',views.create),
    path('create/', views.upsert, name='product_create'),
    path('update/<int:id>/', views.upsert, name='product_update'),
    path('',views.get,name="get"),
    path('<int:id>',views.details,name="details")
]