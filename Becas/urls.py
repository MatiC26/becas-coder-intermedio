from django.contrib import admin
from django.urls import path
from Becas_Universitarias.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', inicio, name="global-inicio"),
    path('universidades/', Universidades, name="global-universidades"),
    path('becas/', Becas, name="global-becas"),
    path('postulantes/', creacion_postulantesViews, name="global-postulantes"),
    path('postulantes/buscar/', buscar_postulantes, name="global-postulantes-buscar"),
    path('postulantes/buscar/resultados/', resultados_busqueda_postulantes, name="global-postulantes-resultados"),
]
