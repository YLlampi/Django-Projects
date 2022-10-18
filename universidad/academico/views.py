from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Curso


# Create your views here.
def home(request):
    cursos = Curso.objects.all()
    messages.success(request, '¡Cursos listados..!')
    context = {
        'cursos': cursos
    }
    return render(request, 'academico/gestionCursos.html', context)


def registrarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']
    curso = Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)
    messages.success(request, '¡Curso registrado..!')

    return redirect('/')


def eliminarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    messages.success(request, '¡Curso Eliminado..!')
    return redirect('/')


def edicionCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    context = {
        'curso': curso,
    }
    return render(request, 'academico/edicionCurso.html', context)


def editarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos

    curso.save()
    messages.success(request, '¡Curso actualizado..!')
    return redirect('/')
    