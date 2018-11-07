from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import AutorForm, LibroForm, ClasificacionForm
from libros.models import Libro, Clasificacion, Autor
from django.contrib.auth.decorators import login_required

@login_required
def clasificacion_nueva(request):
    if request.method == "POST":
        formulario = AutorForm(request.POST)
        if formulario.is_valid():
            autor = Autor.objects.create(
            nombre = formulario.cleaned_data['nombre'],
            apellido = formulario.cleaned_data['apellido'],
            genero = formulario.cleaned_data['genero']
            )
            for libro_id in request.POST.getlist('libros'):
                clasificacion = Clasificacion(libro_id=libro_id, autor_id = autor.id)
                clasificacion.save()
            messages.add_message(request, messages.SUCCESS, 'Clasificacion creada satisfactoriamente.')
            return redirect('clasificacion_lista')
    else:
        formulario = AutorForm()
    return render(request, 'clasificaciones/clasificaciones_nueva.html', {'formulario': formulario})

@login_required
def clasificacion_lista(request):
    autores = Autor.objects.all()
    return render(request, 'clasificaciones/clasificaciones_lista.html', {'autores': autores})

@login_required
def clasificacion_detalle(request, pk):
     autor = get_object_or_404(Autor,pk=pk)
     clasificaciones = Clasificacion.objects.filter(autor__id=pk)
     return render(request,"clasificaciones/clasificaciones_detalle.html",{'autor':autor, 'clasificaciones':clasificaciones})

@login_required
def clasificacion_editar(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        formulario = ClasificacionForm(request.POST, request.FILES, instance=cliente)
        if formulario.is_valid():
            cliente = formulario.save()
            cliente.save()
            return redirect('clasificacion_lista')
    else:
        formulario = AutorForm(instance=autor)
    return render(request, 'clasificaciones/clasificacion_editar.html', {'formulario': formulario})

@login_required
def clasificacion_remove(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    autor.delete()
    return redirect('clasificacion_lista')

@login_required
def libro_lista(request):
    libros = Libro.objects.all()
    return render(request, 'libros/libro_lista.html', {'libros': libros})

@login_required
def libro_nuevo(request):
    if request.method == "POST":
        formulario = LibroForm(request.POST)
        if formulario.is_valid():
            libro = Libro.objects.create(
            nombre = formulario.cleaned_data['nombre'],
            editorial = formulario.cleaned_data['editorial'],
            precio = formulario.cleaned_data['precio'],
            unidades = formulario.cleaned_data['unidades'])
            messages.add_message(request, messages.SUCCESS, 'Clasificacion realizada con Exito.')
            return redirect('libro_lista')
    else:
        formulario = LibroForm()
    return render(request, 'libros/libro_crear.html', {'formulario': formulario})

@login_required
def libro_editar(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        formulario = LibroForm(request.POST, request.FILES, instance=libro)
        if formulario.is_valid():
            libro = formulario.save()
            libro.save()
            return redirect('libro_lista')
    else:
        formulario = LibroForm(instance=libro)
    return render(request, 'libros/libro_editar.html', {'formulario': formulario})

@login_required
def libro_remove(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    libro.delete()
    return redirect('libro_lista')
