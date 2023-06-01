from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "Cliente"),
    path('details/<int:id>',views.detailsCliente,name="detailsCliente"),
]