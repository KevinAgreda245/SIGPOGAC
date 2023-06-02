from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "Empleado"),
    path('add', views.add, name = "AddEmpleado"),
    path('edit/<id>', views.edit, name = "EditEmpleado"),
    path('details/<id>', views.details, name = "DetailsEmpleado"),
    path('status/<id>', views.changeStatus, name="ChangeStatusEmpleado")
]