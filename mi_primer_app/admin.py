from django.contrib import admin

# Register your models here.
from .models import Familiar,Curso,Paciente

register_models=[Familiar,Curso,Paciente]
admin.site.register(register_models)
