from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "Equipo"),
    path('add', views.add, name="AddEquipo"),
    path('edit/<id>', views.edit, name="EditEquipo"),
    path('details/<id>', views.details, name="DetailsEquipo"),
    path('delete/<id>', views.Delete, name="DeleteEquipo")
]