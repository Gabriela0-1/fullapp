from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'),
    path('registrar-cliente/', views.registrar_cliente, name='registrar_cliente'),  
    ]