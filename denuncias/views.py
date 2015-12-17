from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

from .forms import DefensoriasForm, EstadoForm
from models import Denuncia, Defensoria, Estado


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

