from django.shortcuts import render
from .models import Proyectos

def proyecto_list(request):
    proyectos = Proyectos.objects.all()
    return render(request, 'proyectosapp/proyecto.html', {'proyectos': proyectos})

def proyecto_detail(request, pk):
    proyectos = Proyectos.objects.get(pk=pk)
    return render(request, 'proyectosapp/proyecto_detail.html', {'proyectos': proyectos})