from django import forms
from .models import Auto

class CursoForm(forms.Form):
    nombre = forms.CharField()
    descripcion=forms.CharField(widget=forms.Textarea,required=False)
    duracion_semanas = forms.IntegerField(min_value=1,initial=4)
    fecha_inicio = forms.DateField(
        widget=forms.DateInput(attrs={'type':'date'}))
    activo = forms.BooleanField(required=False,initial=True)

class PacienteForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField(min_value=0)
    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(attrs={'type':'date'}))
    enfermedad = forms.CharField(required=False, max_length=100)

class FamiliaresForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField(min_value=0)
    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(attrs={'type':'date'}))
    parentesco = forms.CharField(max_length=50)

class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = ['marca', 'modelo', 'descripcion']
        