from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.index, name = "login"),
    path('logout/', views.cerrarSesion, name = "logout"),
    path('profile/details/<id>', views.details, name="DetailsProfile"),
    path('profile/edit/<id>', views.edit, name="EditProfile"),
]