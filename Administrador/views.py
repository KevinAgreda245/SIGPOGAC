from django.shortcuts import render
from .models import Usuario

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

def details(request,id):
    admin = Usuario.objects.get(id = id)
    context = {
        "admin": admin
    }
    return render(request, 'Administrador/details.html',context)    