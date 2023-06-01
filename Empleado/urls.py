from django.urls import path
from . import views

urlpatterns = [
    path('empleado/', views.index, name = "Empleado"),
    path('empleado/add', views.add, name = "AddEmpleado"),
    path('empleado/edit/<id>', views.details, name = "EditEmpleado"),
    path('empleado/details/<id>', views.details, name="DetailsEmpleado"),
    path('empleado/status/<id>', views.changeStatus, name="ChangeStatusEmpleado")
]