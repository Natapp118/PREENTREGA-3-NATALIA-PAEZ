from django.db import models

# Create your models here.
class Carrera(models.Model):
    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()
    
    def __str__(self):
        return f"Nombre de la carrera: {self.nombre} - Numero de comision: {self.comision}"


class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
def __str__(self):
        return f"Nombre del estudiante: {self.nombre}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)
def __str__(self):
        return f"Nombre profesor: {self.nombre}"

class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_de_Entrega = models.DateField()
    
def __str__(self):
     return f"Tipo de entrega: {self.nombre}"
