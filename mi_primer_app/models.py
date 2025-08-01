from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    parentesco = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.edad} años)"
    
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    duracion_semanas = models.IntegerField(default=4)
    fecha_inicio = models.DateField()
    activo = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre
    
class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    enfermedad = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.nombre
    
class Auto(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"{self.marca} {self.modelo})"
    