from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list_view),
    path('products/<int:id>/', views.product_detail_view),
    path('login/', views.authorization),
    path('register/', views.registration),
    path('create_order/', views.create_order),
]
