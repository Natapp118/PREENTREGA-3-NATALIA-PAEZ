from django.urls import path, include
from MYAPP import views

urlpatterns=[
    path('inicio/', views.inicio, name="inicio"),
    path('Carrera/', views.Carrera, name="Carrera"),
    path('profesores/', views.profesores, name="profesores"),
    path('estudiantes/', views.estudiantes, name="estudiantes"),
    path('entregables/', views.entregables, name="entregables"),
    path('about/',views.about, name='about')


]