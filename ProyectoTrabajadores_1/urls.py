"""
URL configuration for ProyectoTrabajadores_1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ProyectoTrabajadores import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),  
    path('ingresar/', views.iniciar_sesion, name='ingresar'), 
    path('listar-empleados/', views.listar_empleados, name='listar_empleados'),
    path('agregar-empleado/', views.agregar_empleado, name='agregar_empleado'),
    path('remover-empleado/<str:rut_trabajador>/', views.remover_empleado, name='remover_empleado'),
    path('editar-empleado/<str:rut_trabajador>/', views.editar_empleado, name='editar_empleado'),
    path('listar-contactos/', views.listar_contactos, name='listar_contactos'),
    path('agregar-contacto/', views.agregar_contacto, name='agregar_contacto'),
    path('editar-contacto/<str:rut_contacto>/', views.editar_contacto, name='editar_contacto'),
    path('remover-contacto/<str:rut_contacto>/', views.remover_contacto, name='remover_contacto'),
    path('listar-cargas/', views.listar_cargas, name='listar_cargas'),
    path('agregar-carga/', views.agregar_carga, name='agregar_carga'),
    path('editar-carga/<str:rut_carga>/', views.editar_carga, name='editar_carga'),
    path('remover-carga/<str:rut_carga>/', views.remover_carga, name='remover_carga'),
    path('agregar-lista-carga/', views.crear_lista_carga, name='agregar_lista_carga'),
    path('editar-lista-carga/<str:id_lista_cargas>/', views.editar_lista_carga, name='editar_lista_carga'),
    path('remover-lista-carga/<str:id_lista_cargas>/', views.remover_lista_carga, name='remover_lista_carga'),
    path('agregar-lista-contacto/', views.crear_lista_contacto, name='agregar_lista_contacto'),
    path('editar-lista-contacto/<str:id_lista_contactos>/', views.editar_lista_contacto, name='editar_lista_contacto'),
    path('remover-lista-contacto/<str:id_lista_contactos>/', views.remover_lista_contacto, name='remover_lista_contacto'),
    path('gestionar-rh/', views.listar_recursos_humanos, name='gestionar_rh'),
    path('buscar/', views.buscar_empleado, name='buscar_empleado'),

]

   


