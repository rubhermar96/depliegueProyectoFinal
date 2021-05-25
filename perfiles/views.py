from django.db.models.functions import Lower
from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import  login, authenticate
from django.utils import timezone

from django.views.generic import CreateView, TemplateView
from .models import Perfil, Oferta, Candidatura
from .forms import SignUpForm, FormCandidatura
from django.contrib.auth.views import LoginView, LogoutView
from .forms import FormOferta
# -*- coding: future_fstrings -*-

#REGISTRO USUARIO
class SignUpView(CreateView):
    model = Perfil
    form_class = SignUpForm
    template_name = 'perfiles/perfil_form.html'

    def form_valid(self, form):
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario,password=password)
        login(self.request,usuario)
        return redirect('/')

class BienvenidaView(TemplateView):
    template_name='perfiles/bienvenida.html'

#INICIO SESION
class SignInView(LoginView):
    template_name = 'perfiles/iniciar_sesion.html'

#CERRAR SESION
class SignOutView(LogoutView):
    pass

#LISTADO DE OFERTAS
def listado_ofertas(request):
    ofertas = Oferta.objects.order_by(Lower('published_date').desc())
    candidaturas = Candidatura.objects.order_by(Lower('published_date').desc())
    return render(request, 'ofertas/listado_ofertas.html',{'ofertas':ofertas,'candidaturas':candidaturas})

#VER DETALLES DE OFERTA
def detalle_oferta(request, pk):
    oferta = get_object_or_404(Oferta,pk=pk)
    return render(request,'ofertas/detalle_oferta.html',{'oferta':oferta})

#CREAR OFERTA
def crear_oferta(request):
    if request.method == "POST":
        form = FormOferta(request.POST)
        if form.is_valid():
            oferta = form.save(commit=False)
            oferta.author = request.user
            oferta.published_date = timezone.now()
            oferta.save()
            return redirect('detalle_oferta', pk=oferta.pk)
    else:
        form = FormOferta()
    return render(request, 'ofertas/editar_oferta.html',{'form':form})

#EDITAR OFERTA
def editar_oferta(request,pk):
    oferta = get_object_or_404(Oferta, pk=pk)
    if request.method=="POST":
        form = FormOferta(request.POST, instance=oferta)
        if form.is_valid():
            oferta = form.save(commit=False)
            oferta.author = request.user
            oferta.published_date=timezone.now()
            oferta.save()
            return redirect('detalle_oferta', pk=oferta.pk)
    else:
        form = FormOferta(instance=oferta)
    return render(request,'ofertas/editar_oferta.html',{'form':form})

#CANDIDATURAS
#LISTA CANDIDATURAS
def mis_candidaturas(request):
    candidaturas = Candidatura.objects.order_by(Lower('published_date').desc())
    return render(request, 'candidaturas/mis_candidaturas.html',{'candidaturas':candidaturas})

#MOSTAR DETALLE CANDIDATURA
def detalle_candidatura(request,pk):
    candidatura = get_object_or_404(Candidatura,pk=pk)
    return render(request,'candidaturas/detalle_candidatura.html',{'candidatura':candidatura})

#ELIMINAR CANDIDATURA
def eliminar_candidatura(request,pk):
    Candidatura.objects.filter(pk=pk).delete()
    return redirect('mis_candidaturas')

#CREAR CANDIDATURA
def crear_candidatura(request,pk):
    oferta = get_object_or_404(Oferta,pk=pk)
    if request.method=="POST":
        form = FormCandidatura(request.POST)
        if form.is_valid():
            candidatura = form.save(commit=False)
            candidatura.candidato=request.user
            candidatura.published_date=timezone.now()
            candidatura.oferta=oferta
            candidatura.save()
            return redirect('detalle_candidatura',pk=candidatura.pk)
    else:
        form = FormCandidatura()
    return render(request,'candidaturas/crear_candidatura.html',{'form':form})

#LISTA CANDIDATOS
def listado_candidatos(request,pk):
    oferta = get_object_or_404(Oferta,pk=pk)
    candidaturas = Candidatura.objects.order_by(Lower('published_date').desc())
    return render(request,'candidaturas/listado_candidatos.html',{'oferta':oferta,'candidaturas':candidaturas})

