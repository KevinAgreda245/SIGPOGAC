from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "Proyecto"),
    path('add/1', views.add, name = "AddProyecto"),
    path('add/2', views.add, name = "AddProyecto2"),
]