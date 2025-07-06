from django.urls import path
from .views import crear_familiar

urlpatterns = [
    path('crear-familiar/<str:nombre>/', crear_familiar),
]