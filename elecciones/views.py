from inspect import ArgInfo
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Region2, Candidato2

def index(request):
    list_regi = Region2.objects.order_by('-pub_date')[:5]
    context={'list_regi':list_regi}
    return render(request, 'elecciones/index.html', context)

def resultados(request, region_id):
    list_cand = Candidato2.objects.filter(region=region_id)
    context={'list_cand':list_cand}
    return render(request, 'elecciones/resultados.html', context)