from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "Cliente"),
    path('details/<int:id>',views.detailsCliente,name="detailsCliente"),
    path('add/',views.createCliente,name="addCliente"),
    path('edit/<id>',views.editCliente,name="editCliente"),
    path('status/<id>', views.changeStatus, name="changeStatusCliente")

]