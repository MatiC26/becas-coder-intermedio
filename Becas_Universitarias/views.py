from django.shortcuts import render
from Becas_Universitarias.models import PostulantesModels, UniversidadesModel


def inicio (request):
    return render(request, "Becas_Universitarias/base.html")

def Universidades(request):
    universidad = UniversidadesModel.objects.all()
    return render(request, "Becas_Universitarias/universidades.html", {'universidad': universidad})

def Becas(request):
    return render(request, "Becas_Universitarias/becas.html")

def PostulantesModels(request):
    return render(request, "Becas_Universitarias/postulantes.html")

def creacion_postulantes(request):
    if request.method == "POST":
        nombre_postulantes = request.POST("nombre")
        apellido_postulantes = request.POST("apellido")
        contacto_postulantes = request.POST("contacto")
        email_postulantes = request.POST("email")
        postulantes = PostulantesModels(nombre=nombre_postulantes, apellido=apellido_postulantes, contacto=contacto_postulantes, email=email_postulantes)
        postulantes.save()
    
    return render(request, "Becas_Universitarias/postulantes_formulario.html")
    