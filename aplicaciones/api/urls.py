from django.urls import path
from . import views

urlpatterns = [
    path('get_municipios/', views.filtrar_direccion, name='api_get_municipios')
]
