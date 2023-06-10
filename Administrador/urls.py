from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main, name = "Main"),
    path('administrador/', views.management, name = "Administrador"),
    path('administrador/add', views.add, name = "AddAdmin"),
    path('administrador/edit/<id>', views.edit, name = "EditAdmin"),
    path('administrador/details/<id>', views.details, name = "DetailsAdmin"),
    path('administrador/status/<id>', views.changeStatus, name="ChangeStatusAdmin"),
    path('administrador/delete/<id>', views.delete, name="deleteAdmin")
]