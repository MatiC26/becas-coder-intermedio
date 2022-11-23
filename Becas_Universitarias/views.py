from django.shortcuts import render
from Becas_Universitarias.forms import PostulantesForms
from Becas_Universitarias.models import PostulantesModels, UniversidadesModel

def inicio (request):
    return render(request, "Becas_Universitarias/base.html")

def Universidades(request):
    universidad = UniversidadesModel.objects.all()
    return render(request, "Becas_Universitarias/universidades.html", {'universidad': universidad})

def Becas(request):
    return render(request, "Becas_Universitarias/becas.html")

def creacion_postulantesViews(request):
    if request.method == "POST":
        form = PostulantesForms(request.POST)
        postulante = PostulantesModels(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            contacto=request.POST["contacto"],
            email=request.POST["email"]
        )
        postulante.save()
    formulario = PostulantesForms()
    return render(request, "Becas_Universitarias/postulantes_formulario.html", {"formulario": formulario})

def buscar_postulantes(request):
    
    return render(request, "Becas_Universitarias/buscar_postulantes.html")
    
    
def resultados_busqueda_postulantes(request):
   nombre_postulante = request.GET["nombre_postulante"]
  
   postulante = PostulantesModels.objects.filter(nombre__icontains=nombre_postulante)
  
   return render(request, "Becas_Universitarias/resultados_busqueda_postulantes.html", {"postulante": postulante})