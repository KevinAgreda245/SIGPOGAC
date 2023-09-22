from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "Proyecto"),
    path('add', views.add, name = "AddProyecto"),
    path('details/<id>', views.details, name = "DetailsProyecto"),


    path('transporte', views.transporteForm, name = "transporteForm"),
    path('renta_equipo', views.rentaEquipoForm, name = "rentaEquipoForm"),
    path('concreto', views.concretoForm, name = "concretoForm"),
    path('renta_desimetro', views.rentaDesimetroForm, name = "rentaDesimetroForm"),
    path('levantamiento_topografico', views.levantamientoTopograficoForm, name = "levantamientoTopograficoForm"),
    path('estructura_metalica', views.estructuraMetalicaForm, name="estructuraMetalicaForm"),

    path('empleado', views.registerEmployees, name = "registerEmployees"),
    path('empleado/delete/<int:id>', views.deleteEmployee, name = "deleteEmployee"),

    path('equipo', views.registerEquipment, name = "registerEquipment"),
    path('equipo/delete/<int:id>', views.deleteEquipment, name = "deleteEquipment"),

    path('material', views.registerMaterial, name = "registerMaterial"),
    path('material/delete/<int:id>', views.deleteMaterial, name = "deleteMaterial"),

    path('save', views.save, name = "saveProyecto")

]