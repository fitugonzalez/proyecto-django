from django.shortcuts import render
from .models import Familiar

# Create your views here.
def crear_familiar(request,nombre):
    if nombre is not None:
        nuevo_familiar=Familiar (
            nombre=nombre,
            apellido="Gonzalez",
            edad=30,
            fecha_nacimiento="1993-01-01",
            parentesco="Hermano"
        )
        nuevo_familiar.save()
    return render(request, 'mi_primer_app/crear_familiar.html', {'nombre': nombre})