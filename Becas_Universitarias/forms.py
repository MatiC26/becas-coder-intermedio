from django import forms
from django.forms import CharField, IntegerField, EmailField


class PostulantesForms(forms.Form):
     nombre = forms.CharField(min_length=3, max_length=100)
     apellido = forms.CharField(min_length=3, max_length=100)
     descripcion = forms.CharField(min_length=100, max_length=2000)
     contacto = forms.IntegerField()
     email = forms.EmailField()