from django.shortcuts import render, redirect
from .forms import PeliculaForm, DirectorForm, CriticaForm, BuscarPeliculaForm
from .models import Pelicula

def index(request):
    return render(request, 'peliculas/index.html')

def crear_pelicula(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PeliculaForm()
    return render(request, 'peliculas/crear_pelicula.html', {'form': form})

def crear_director(request):
    if request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DirectorForm()
    return render(request, 'peliculas/crear_director.html', {'form': form})

def crear_critica(request):
    if request.method == 'POST':
        form = CriticaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CriticaForm()
    return render(request, 'peliculas/crear_critica.html', {'form':form})

def buscar_pelicula(request):
    peliculas = []
    if request.method == 'POST':
        form = BuscarPeliculaForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            peliculas = Pelicula.objects.filter(titulo__icontains=titulo)
    else:
        form = BuscarPeliculaForm()
    return render(request, 'peliculas/buscar_pelicula.html', {'form': form, 'peliculas': peliculas})
