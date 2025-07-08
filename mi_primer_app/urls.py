from django.urls import path
from .views import crear_familiar,saludo_con_template,inicio,crear_curso,crear_paciente,buscar_pacientes,pacientes

urlpatterns = [
    path('', inicio, name='inicio'),
    path('crear-familiar/', crear_familiar, name='crear_familiar'),
    path('saludo/', saludo_con_template),
    path('crear-curso/', crear_curso, name='crear_curso'),
    path('crear-paciente/', crear_paciente, name='crear_paciente'),
    path('pacientes/', pacientes, name='pacientes'),
    path('pacientes/buscar', buscar_pacientes, name='buscar_pacientes'),
]