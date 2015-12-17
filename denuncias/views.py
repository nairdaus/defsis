from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

from .forms import DefensoriasForm, EstadoForm, TipologiaForm
from models import Denuncia, Defensoria, Estado, Tipologia


# CRUD defensorias
@login_required(login_url = '/usuarios/')
def list_defensoria_view(request):
	defensorias = Defensoria.objects.all()
	template = 'denuncias/listar_defensorias.html'
	return render(request, template, {'defensorias': defensorias})

@login_required(login_url = '/usuarios/')
def agregar_defensoria(request):
	if request.method =='POST':
		form = DefensoriasForm
		nombre = request.POST['nombre']
		direccion = request.POST['direccion']
		telefono = request.POST['telefono']

		defensoria = Defensoria(
				nombre = nombre,
				direccion = direccion,
				telefono = telefono,
			)
		defensoria.save();

		return HttpResponseRedirect('/denuncias/')
	else:
		form = DefensoriasForm()
	context = {'form':form}
	return render(request, 'denuncias/agregar_defensoria.html', context)

@login_required(login_url = '/usuarios/')
def edit_defensoria_view(request, id_defensoria):
	pass


#CRUD Estados
@login_required(login_url = '/usuarios/')
def list_estados_view(request):
	estados = Estado.objects.all()
	template = 'denuncias/listar_estados.html'
	return render(request, template, {'estados':estados})

@login_required(login_url = '/usuarios/')
def edit_estado_view(request, id_estado):
	pass

@login_required(login_url = '/usuarios/')
def agregar_estados_view(request):
	if request.method == 'POST':
		form = EstadoForm
		nombre = request.POST['nombre']

		estado = Estado(
				nombre = nombre,
			)
		estado.save()

		return HttpResponseRedirect('/denuncias/listar_estados/')
	else:
		form = EstadoForm()
		contexto = {'form':form}
	return render(request, 'denuncias/agregar_estados.html', contexto)

#CRUD Tipologias
@login_required(login_url = '/usuarios/')
def list_tipolgias_view(request):
	tipologias = Tipologia.objects.all()
	template = 'denuncias/listar_tipologias.html'
	return render(request, template, {'tipologias':tipologias})

@login_required(login_url = '/usuarios/')
def agregar_tipologias_view(request):
	if request.method == 'POST':
		form = TipologiaForm
		nombre = request.POST['nombre']

		tipologia = Tipologia(
				nombre = nombre,
			)
		tipologia.save()

		return HttpResponseRedirect('/denuncias/listar_tipologias/')
	else:
		titulo = 'Tipologias'
		form = TipologiaForm()
		contexto = {'form':form, 'titulo':titulo}
	return render(request, 'denuncias/agregar_generico.html', contexto)

@login_required(login_url = '/usuarios/')
def edit_tipologias_view(request, id_tipologia):
	pass

#CRUD Denuncias
@login_required(login_url = '/')
def registrar_denuncia(request):
	template = 'denuncias/registrar_denuncia.html'
	return render(request, template)	