from django.shortcuts import render, redirect
from .models import Familiar,Curso,Paciente
from .forms import CursoForm,PacienteForm,FamiliaresForm

# Create your views here.
def crear_familiar(request):
    if request.method == 'POST':
        form = FamiliaresForm(request.POST)
        if form.is_valid():
            nuevo_familiar = Familiar(
                nombre = form.cleaned_data['nombre'],
                apellido= form.cleaned_data['apellido'],
                edad= form.cleaned_data['edad'],
                fecha_nacimiento= form.cleaned_data['fecha_nacimiento'],
                parentesco= form.cleaned_data['parentesco'],
            )
            nuevo_familiar.save()
            return redirect('inicio')
    else:
        form = FamiliaresForm()
        return render(request,"mi_primer_app/crear_familiar.html",{"form":form})


def saludo_con_template(request):
    return render(request, 'mi_primer_app/saludo.html')

def inicio(request):
    return render(request, 'mi_primer_app/inicio.html')

def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            nuevo_curso = Curso(
                nombre = form.cleaned_data['nombre'],
                descripcion= form.cleaned_data['descripcion'],
                duracion_semanas= form.cleaned_data['duracion_semanas'],
                fecha_inicio= form.cleaned_data['fecha_inicio'],
                activo= form.cleaned_data['activo'],
            )
            nuevo_curso.save()
            return redirect('inicio')
    else:
        form = CursoForm()
        return render(request,"mi_primer_app/crear_curso.html",{"form":form})
    
def crear_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            nuevo_paciente = Paciente(
                nombre = form.cleaned_data['nombre'],
                apellido= form.cleaned_data['apellido'],
                edad= form.cleaned_data['edad'],
                fecha_nacimiento= form.cleaned_data['fecha_nacimiento'],
                enfermedad= form.cleaned_data['enfermedad'],
            )
            nuevo_paciente.save()
            return redirect('pacientes')
    else:
        form = PacienteForm()
        return render(request,"mi_primer_app/crear_paciente.html",{"form":form})

def pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'mi_primer_app/pacientes.html', {'pacientes': pacientes})


def buscar_pacientes(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre', '')
        pacientes = Paciente.objects.filter(nombre__icontains=nombre)
        return render(request, 'mi_primer_app/pacientes.html', {'pacientes': pacientes, 'nombre': nombre})
    else:
        return redirect('inicio')  # Redirigir a inicio si no es una solicitud GET 