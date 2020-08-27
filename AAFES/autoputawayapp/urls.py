from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='autoputaway-home'),
    path('summary/', views.productList, name='autoputaway-products'),
]