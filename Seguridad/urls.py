from django.urls import path
from django.contrib.auth import views as auth

from Seguridad.forms import UserPasswordChangeForm, UserPasswordResetForm
from . import views

urlpatterns = [
    path('login/', views.index, name = "login"),
    path('logout/', views.cerrarSesion, name = "logout"),
    path('profile/details/<id>', views.details, name="DetailsProfile"),
    path('profile/edit/<id>', views.edit, name="EditProfile"),

    path('restorePassword/', auth.PasswordResetView.as_view(template_name = 'Seguridad/passwordReset1.html', form_class=UserPasswordResetForm),  name="password_reset"),
    path('restorePasswordDone/', auth.PasswordResetDoneView.as_view(template_name = 'Seguridad/passwordReset2.html'), name="password_reset_done"),
    path('restorePasswordConfirm/<uidb64>/<token>/', auth.PasswordResetConfirmView.as_view(template_name = 'Seguridad/passwordReset3.html', form_class=UserPasswordChangeForm),  name="password_reset_confirm"),
    path('restorePasswordComplete/', auth.PasswordResetCompleteView.as_view(template_name = 'Seguridad/passwordReset4.html'), name="password_reset_complete")
]