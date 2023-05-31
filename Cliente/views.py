from django.shortcuts import render
from Cliente.models import Cliente

def index(request):
    clientes=Cliente.objects.all()
    return render(request, 'Cliente/index.html',{'clientes':clientes})

def detailsCliente(request,id):
    cliente=Cliente.objects.get(SK_CLIENTE=id)
    return render(request,'Cliente/details.html',{"cliente":cliente})
