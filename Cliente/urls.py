from django.urls import path
from . import views

urlpatterns = [
    path('', views.portal, name = "Portal"),
    path('cliente/', views.index, name = "Cliente"),
    path('cliente/details/<int:id>',views.detailsCliente,name="detailsCliente"),
    path('cliente/add/',views.createCliente,name="addCliente"),
    path('cliente/edit/<id>',views.editCliente,name="editCliente"),
    path('cliente/status/<id>', views.changeStatus, name="changeStatusCliente")


]