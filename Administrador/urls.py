from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.index, name = "Login"),
    path('main/', views.main, name = "Main"),
    path('administrador/', views.management, name = "Administrador"),
    path('administrador/add', views.add, name = "AddAdmin"),
    path('administrador/<id>', views.details, name = "EditAdmin")
]