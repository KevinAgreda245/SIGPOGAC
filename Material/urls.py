from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "Material"),
    path('add', views.add, name="MaterialAdd"),
    path('edit/<id>', views.edit, name="EditMaterial"),
    path('delete/<id>', views.delete, name="DeleteMaterial")
]