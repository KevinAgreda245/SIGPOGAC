from django.shortcuts import render

def index(request):
    return render(request, 'Proyecto/index.html')

def add(request):
    return render(request, 'Proyecto/add.html')