from django.urls import path
from .views import (crear_familiar,saludo_con_template,inicio,crear_curso,
                    crear_paciente,buscar_pacientes,pacientes,
                    AutoListView, AutoCreateView, AutoDeleteView, AutoDetailView, AutoUpdateView)

urlpatterns = [
    path('', inicio, name='inicio'),
    path('crear-familiar/', crear_familiar, name='crear_familiar'),
    path('saludo/', saludo_con_template),
    path('crear-curso/', crear_curso, name='crear_curso'),
    path('crear-paciente/', crear_paciente, name='crear_paciente'),
    path('pacientes/', pacientes, name='pacientes'),
    path('pacientes/buscar', buscar_pacientes, name='buscar_pacientes'),

    # urls con vistas basadas en clase
    path('crear-auto/', AutoCreateView.as_view(), name='crear-auto'),
    path('listar-autos/', AutoListView.as_view(), name='listar-autos'),
    path('detalle-auto/<int:pk>', AutoDetailView.as_view(), name='detalle-auto'),
    path('eliminar-auto/<int:pk>', AutoDeleteView.as_view(), name='eliminar-auto'),
    path('editar-auto/<int:pk>', AutoUpdateView.as_view(), name='editar-auto'),

]
