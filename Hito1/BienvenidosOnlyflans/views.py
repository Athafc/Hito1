from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Bienvenidos(request):
    return HttpResponse("¡Bienvenidos a Onlyflans!")
