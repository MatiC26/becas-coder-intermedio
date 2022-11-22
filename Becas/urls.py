from django.contrib import admin
from django.urls import path
from Becas_Universitarias.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("inicio/", inicio),
    path('universidades/', Universidades),
    path('becas', Becas),
    path('postulantes/', Postulantes),
]
