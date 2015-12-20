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
@login_required(login_url = '/usuarios/')
def registrar_denuncia(request):
	tipologias = Tipologia.objects.all()
	template = 'denuncias/registrar_denuncia.html'
	return render(request, template, {'tipologias': tipologias})

@login_required(login_url = '/usuarios/')
def guardar_denuncia(request):

	fecha_denuncia = request.POST['']
	codigo_dna= request.POST['']
	nro_atencion= request.POST['']
	tipologia= request.POST['']
	#Esto tiene que entrar en un bucle
	#Datos de victima
	nombres_vic= request.POST['']
	apellidos_vic= request.POST['']
	gestante= request.POST['']
	sexo= request.POST['']
	c_nac= request.POST['']
	estudia= request.POST['']
	ultimo_curso= request.POST['']
	f_nac= request.POST['']
	#Domicilio victima
	direccion= request.POST['']
	telefono= request.POST['']
	comunidad= request.POST['']
	#fin Bucle

	#Bucle
	#Datos del grupo familiar
	nombres_fam= request.POST['']
	apellidos_fam= request.POST['']
	parentezco= request.POST['']
	edad= request.POST['']
	sexo_fam= request.POST['']
	g_inst= request.POST['']
	ocupacion= request.POST['']
	#fin 

	#Datos
	relacion= request.POST['']
	nombres_denu= request.POST['']
	parentezco_den= request.POST['']
	cedula= request.POST['']
	dir_denun= request.POST['']
	tel_denun= request.POST['']
	lug_trab_denun= request.POST['']
	ocup_denun= request.POST['']

	#Bucle
	#Datos del denunciado
	desconocido= request.POST['']
	nombres_dciado= request.POST['']
	apellidos_dciado= request.POST['']
	sexo_dciado= request.POST['']
	edad_dciado= request.POST['']
	parentezco_dciado= request.POST['']
	dir_dciado= request.POST['']
	tel_dciado= request.POST['']
	lug_trab_dciado= request.POST['']
	ocupacion_dciado= request.POST['']
	denuncias_ant= request.POST['']
	donde_den= request.POST['']
	#fin

	#Datos de la denuncia
	descripcion= request.POST['']
	opinion= request.POST['']
	historia_inf= request.POST['']

	#Acciones inmediatas a seguir
	acciones= request.POST['']


@login_required(login_url = '/usuarios/')
def editar_denuncia(request):	
	pass

@login_required(login_url = '/usuarios/')
def listar_denuncias(request):
	pass