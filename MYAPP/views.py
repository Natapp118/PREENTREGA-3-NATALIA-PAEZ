from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Carrera, Profesor


def about(request):
    return HttpResponse('ABOUT')


def inicio(request):
    return render(request,'MYAPP/index.html')

def Carrera(request): 
       
    return render(request, 'MYAPP/Carrera.html', {"Carrera":Carrera})

def profesores(request): 
   
    return render(request, 'MYAPP/profersores.html', {"profes":profesores})
    

def estudiantes(request):
    return render(request, 'MYAPP/estudiantes.html')

def entregables(request):
    return render(request, "MYAPP/entregables.html")
