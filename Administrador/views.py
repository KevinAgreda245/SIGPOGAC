from django.shortcuts import render

def index(request):
    return render(request, 'Administrador/index.html')    

def main(request):
    return render(request, 'Administrador/main.html')

def management(request):
    return render(request, 'Administrador/management.html')    
