from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'),
    
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('clientes/registrar/', views.registrar_cliente, name='registrar_cliente'),
    path('clientes/<int:cliente_id>/actualizar/', views.actualizar_cliente, name='actualizar_cliente'),
    path('clientes/<int:cliente_id>/eliminar/', views.eliminar_cliente, name='eliminar_cliente'),

    # URLs para Carro
    path('carros/', views.listar_carros, name='listar_carros'),
    path('carros/registrar/', views.registrar_carro, name='registrar_carro'),
    path('carros/<int:carro_id>/actualizar/', views.actualizar_carro, name='actualizar_carro'),
    path('carros/<int:carro_id>/eliminar/', views.eliminar_carro, name='eliminar_carro'),

    # URLs para Parqueadero
    path('parqueaderos/', views.listar_parqueaderos, name='listar_parqueaderos'),
    path('parqueaderos/registrar/', views.registrar_parqueadero, name='registrar_parqueadero'),

    # URLs para Reserva
    path('reservas/', views.listar_reservas, name='listar_reservas'),
    path('reservas/registrar/', views.registrar_reserva, name='registrar_reserva'),

    # URLs para Factura
    path('facturas/', views.listar_facturas, name='listar_facturas'),
    path('facturas/registrar/', views.registrar_factura, name='registrar_factura'),

    # URLs para Empleado
    path('empleados/', views.listar_empleados, name='listar_empleados'),
    path('empleados/registrar/', views.registrar_empleado, name='registrar_empleado'),

    # URLs para Registro de Acceso
    path('Acceso/', views.listar_registros_acceso, name='listar_registros_acceso'),
    path('Acceso/registrar/', views.registrar_registro_acceso, name='registrar_registro_acceso'),
]