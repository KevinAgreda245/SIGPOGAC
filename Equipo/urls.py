from django.urls import path
from . import views

urlpatterns = [
    path('equipo/', views.index, name = "Equipo"),
]