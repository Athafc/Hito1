from django.shortcuts import render

# Create your views here.

def Indice(request):
    return render(request, 'index.html')

def Acerca(request):
    return render(request, 'about.html')

def Bienvenido(request):
    return render(request, 'welcome.html')