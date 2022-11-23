from django.db import models
from django.db.models.fields import CharField, EmailField, IntegerField

class UniversidadesModel(models.Model):
    
    nombre = CharField(max_length= 100)
    localizacion = CharField(max_length= 100)
    direccion = CharField(max_length= 100)
    zip_code = IntegerField()
    descripcion = CharField(max_length= 2000)
    contacto = EmailField(max_length=100)
    
class Becas(models.Model):

    nombre = CharField(max_length= 100)
    descripcion = CharField(max_length= 2000)
    fecha_de_inscripcion = CharField(max_length= 100)
    promedio = IntegerField()
    id_universidad = IntegerField()
    
class PostulantesModels(models.Model):
    nombre = CharField(max_length= 100)
    apellido = CharField(max_length=100)
    contacto = IntegerField()
    email = EmailField(max_length= 100)