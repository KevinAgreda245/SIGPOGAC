from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        contraseña = request.POST['password']
        usuarioAutenticado = authenticate(request, username = usuario, password = contraseña)
        if usuarioAutenticado is not None:
            login(request, usuarioAutenticado)
            #Pendiente validación para redigirir de acuerdo al rol del usuario
            return redirect('Main')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
            return render(request, 'Seguridad/index.html')   
    return render(request, 'Seguridad/index.html')    


@login_required(login_url='login')
def cerrarSesion(request):
    logout(request)
    return redirect('login')