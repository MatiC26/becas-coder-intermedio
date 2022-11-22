from django import forms
from django.forms import CharField, IntegerField, EmailField


class PostulantesForms(forms.Form):
     nombre = CharField(min_length=3, max_length=100)
     apellido = CharField(min_length=3, max_length=100)
     descripcion = CharField(min_length=100, max_length=2000)
     contacto = IntegerField()
     email = EmailField()