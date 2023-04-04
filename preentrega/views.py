from django.shortcuts import render
from django.http import HttpResponse
from preentrega.forms import *
from preentrega.models import *

# Create your views here.

def cursos(request):
    return render(request, "preentrega/cursos.html")

def profesores(request):
    return render(request, "preentrega/profesores.html")

def estudiantes(request):
    return render(request, "preentrega/estudiantes.html")

def entregables(request):
    return render(request, "preentrega/entregables.html")

def index(request):
    return render(request, "preentrega/index.html")


def cursoFormulario(request):
      if request.method == 'POST':
      
        nombre = request.POST["curso"]
        camada = request.POST["camada"]
        curso = Curso(nombre=nombre, camada=camada)
        curso.save()
        return render(request, "preentrega/index.html")
      return render(request,"preentrega/cursoFormulario.html")

def entregableFormulario(request):
      if request.method == 'POST':
        nombre = request.POST["nombre"]
        FechaDeEntrega = request.POST["fechadeentrega"]
        entregables = Entregable(nombre=nombre, FechaDeEntrega=FechaDeEntrega)
        entregables.save()
        return render(request, "preentrega/index.html")
      return render(request,"preentrega/entregableFormulario.html")

def estudianteFormulario(request):
      if request.method == 'POST':
      
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        email = request.POST["email"]
        estudiante = Estudiante(nombre=nombre, apellido=apellido, email=email)
        estudiante.save()
        return render(request, "preentrega/index.html")
      return render(request,"preentrega/estudianteFormulario.html")

def profesorFormulario(request):
      if request.method == 'POST':
      
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        email = request.POST["email"]
        profesion = request.POST["profesion"]
        profesor = Profesor(nombre=nombre, apellido=apellido, email=email)
        profesor.save()
        return render(request, "preentrega/index.html")
      return render(request,"preentrega/profesorFormulario.html")



