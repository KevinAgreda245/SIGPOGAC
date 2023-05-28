from django.shortcuts import redirect, render
from .models import Usuario
from .forms import *

def index(request):
    return render(request, 'Administrador/index.html')    

def main(request):
    return render(request, 'Administrador/main.html')

def management(request):
    admins = Usuario.objects.filter(is_staff = 1)
    context = {
        "admins": admins
    }
    return render(request, 'Administrador/management.html',context)    

def add(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Administrador')
    else:
        form = CreateUserForm()
    context = {
        "form": form
    }
    return render(request, 'Administrador/add.html',context)

def details(request,id):
    admin = Usuario.objects.get(id = id)
    context = {
        "admin": admin
    }
    return render(request, 'Administrador/details.html',context)    