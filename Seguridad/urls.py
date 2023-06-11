from django.urls import path
from django.contrib.auth import views as auth
from Seguridad.forms import UserPasswordChangeForm, UserPasswordResetForm
from . import views
from . import decorators

urlpatterns = [
    path('login/', views.index, name = "login"),
    path('logout/', views.cerrarSesion, name = "logout"),
    path('profile/details/', views.details, name="DetailsProfile"),
    path('profile/edit/', views.edit, name="EditProfile"),

    #Rutas para restaurar contraseña
    #Se utilizan las rutas de django por defecto y se ha agregado un decorator
    #para evitar el ingreso de usuario autenticados a estas rutas
    path('restorePassword/', decorators.authenticated_user(auth.PasswordResetView.as_view(template_name = 'Seguridad/passwordReset1.html', form_class=UserPasswordResetForm)),  name="password_reset"),
    path('restorePasswordDone/', decorators.authenticated_user(auth.PasswordResetDoneView.as_view(template_name = 'Seguridad/passwordReset2.html')), name="password_reset_done"),
    path('restorePasswordConfirm/<uidb64>/<token>/', decorators.authenticated_user(auth.PasswordResetConfirmView.as_view(template_name = 'Seguridad/passwordReset3.html', form_class=UserPasswordChangeForm)),  name="password_reset_confirm"),
    path('restorePasswordComplete/', decorators.authenticated_user(auth.PasswordResetCompleteView.as_view(template_name = 'Seguridad/passwordReset4.html')), name="password_reset_complete")
]