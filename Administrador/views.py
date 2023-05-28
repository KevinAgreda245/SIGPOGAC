from django.shortcuts import render

def main(request):
    return render(request, 'Administrador/main.html')

def management(request):
    return render(request, 'Administrador/management.html')    
