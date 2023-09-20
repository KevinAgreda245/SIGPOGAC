from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "Proyecto"),
    path('add', views.add, name = "AddProyecto"),
    path('details/<id>', views.details, name = "DetailsProyecto"),


    path('transporte', views.transporteForm, name = "transporteForm"),
    path('agregar_empleado', views.agregarEmpleado, name = "agregarEmpleado")
]