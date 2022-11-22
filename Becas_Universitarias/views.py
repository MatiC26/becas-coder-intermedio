from django.shortcuts import render
from Becas_Universitarias.forms import PostulantesForms
from Becas_Universitarias.models import PostulantesModels

def inicio (request):
    return render(request, "Becas_Universitarias/base.html")


def Universidades(request):
    return render(request, "Becas_Universitarias/universidades.html")

def Becas(request):
    return render(request, "Becas_Universitarias/becas.html")


def Postulantes(request):
    return render(request, "Becas_Universitarias/postulantes.html")


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