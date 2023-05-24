from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "Administrador"),
    path('main/', views.main, name = "Main")
]