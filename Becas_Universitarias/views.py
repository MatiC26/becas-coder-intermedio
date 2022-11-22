from django.shortcuts import render
from django.http import HttpResponse
from Becas_Universitarias.forms import PostulantesForms
from Becas_Universitarias.models import PostulantesModels

def inicio (request):
    return render(request, "Becas_Universitarias/index.html")


def Universidades(request):
    return HttpResponse("Estas en la sección de universidades")


def Becas(request):
    return HttpResponse("Estas en la sección de becas")


def Postulantes(request):
    return HttpResponse("Estas en la sección de postulantes")


def nuevo_postulante(request):
    if request.method == "Post":
        form = PostulantesForms(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            postulante = PostulantesModels(
                nombre=data["nombre"],
                apellido=data["apellido"],
                contacto=data["contacto"],
                email=data["email"]
            )
            postulante.save()
    formulario = PostulantesForms()
    return render(request, "formulario_postulante.html", {"data": formulario})