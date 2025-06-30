from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear_pelicula/', views.crear_pelicula, name='crear_pelicula'),
    path('crear_director/', views.crear_director, name='crear_director'),
    path('crear_critica/', views.crear_critica, name='crear_critica'),
    path('buscar_pelicula/', views.buscar_pelicula, name='buscar_pelicula'),
]
