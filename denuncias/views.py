from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date, timedelta, datetime

from .forms import DefensoriasForm, EstadoForm, TipologiaForm, TipoForm, ActuacionFormModel
from models import Denuncia, Defensoria, Estado, Tipologia, Persona, Tipo, PerfilPersona, Domicilio, LogEstado, Actuaciones


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
def list_tipologias_view(request):
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

	formato_fecha = '%Y-%m-%d'
	
	tipo_victima = Tipo.objects.get(tipo = "Victima")
	tipo_familiar = Tipo.objects.get(tipo = "Familiar")
	tipo_denunciante = Tipo.objects.get(tipo = "Denunciante")
	tipo_denunciado = Tipo.objects.get(tipo = "Denunciado")

	fecha_denuncia = request.POST['date_form']
	codigo_dna= request.POST['codigo_dna']
	nro_atencion= request.POST['nro_atencion']
	tipologia= Tipologia.objects.get(id = request.POST['tipologia'])

	#Esto tiene que entrar en un bucle
	#Datos de victima
	nombres_vic= request.POST['nombres']
	apellidos_vic= request.POST['apellidos']
	
	gestante = c_nac = estudia = False
	if request.POST.get and 'gestante' in request.POST and request.POST['gestante']=="on":
		gestante = True	
		if request.POST.get and 'cernac' in request.POST and request.POST['cernac'] == "on":
			c_nac = True
			sexo_vic= request.POST['sexo']	
			if request.POST.get and 'estudia' in request.POST and request.POST['estudia']== "on":
				estudia = True

				ultimo_curso= request.POST['ucurso']
				f_nac= datetime.strptime(request.POST['fnac'], formato_fecha).date()

				victima = Persona(
					nombres = nombres_vic,
					apellidos = apellidos_vic,
					gestante = gestante,
					sexo = sexo_vic,
					c_nac = c_nac,
					estudia = estudia,
					ult_curso = ultimo_curso,
					f_nac = f_nac,
					)
				victima.save()
				victima.tipo.add(tipo_victima)
				victima.save()
	#Domicilio victima
	direccion= request.POST['domicilio']
	telefono= request.POST['telefono']
	comunidad= request.POST['domiciliocomunidaddir']
	dir_victima = Domicilio(
		domicilio = direccion,
		telefono = telefono,
		persona = victima
		)
	dir_victima.save()
	#fin Bucle

	#Bucle
	#Datos del grupo familiar
	nombres_fam= request.POST['nombresgf']
	apellidos_fam= request.POST['apellidosgf']
	parentesco= request.POST['parentescogf']
	f_nac_fam= datetime.strptime(request.POST['edadgf'], formato_fecha)
	sexo_fam= request.POST['sexogf']
	g_inst= request.POST['gradogf']
	ocupacion= request.POST['ocupaciongf']

	familiar = Persona(
		nombres = nombres_fam,
		apellidos = apellidos_fam,
		parentesco = parentesco,
		sexo = sexo_fam,
		f_nac = f_nac_fam,
		g_instruccion = g_inst,
		ocupacion = ocupacion,
		)
	familiar.save()
	familiar.tipo.add(tipo_familiar)
	familiar.save()

	#fin 

	#Datos denunciante
	

	if not request.POST.get and 'anonimo' in request.POST and request.POST['anonimo'] == "on":
		print 'entra al if de denunciante'
		nombres_denu= request.POST['dennombre']
		apellidos_denu = request.POST['denapellidos']
		parentesco_den= request.POST['denparentesco']
		cedula= request.POST['dencedula']
		dir_denun= request.POST['dendomicilio']
		tel_denun= request.POST['dentelefono']
		lug_trab_denun= request.POST['dentrabajo']
		ocup_denun= request.POST['denocupacion']
		anonimo = False

		denunciante = Persona(
			anonimo = anonimo,
			nombres = nombres_denu,
			apellidos = apellidos_denu,
			parentesco = parentesco_den,
			cedula = cedula,
			lugar_trabajo = lug_trab_denun,
			ocupacion = ocup_denun,
			)
		denunciante.save()
		denunciante.tipo.add(tipo_denunciante)
		denunciante.save()
		dir_denunciante = Domicilio(
			domicilio = dir_denun,
			telefono = tel_denun,
			persona = denunciante,
			)
		dir_denunciante.save()
	else:
		denunciante = Persona(
			anonimo = True,
			)
		denunciante.save()
		denunciante.tipo.add(tipo_denunciante)
		denunciante.save()
	#Bucle
	#Datos del denunciado

	nombres_dciado= request.POST['nombredciado']
	apellidos_dciado= request.POST['apellidodciado']
	sexo_dciado= request.POST['sexodciado']
	edad_dciado= datetime.strptime(request.POST['edaddciado'], formato_fecha)
	parentezco_dciado= request.POST['parentescodciado']
	dir_dciado= request.POST['domiciliodciado']
	tel_dciado= request.POST['telefonodciado']
	lug_trab_dciado= request.POST['trabajodciado']
	ocupacion_dciado= request.POST['ocupaciondciado']
	#denuncias_ant= request.POST['denunciadciado']
	#donde_den= request.POST['lugardciado']
	
	if not request.POST.get and 'identdcioado' in request.POST and request.POST['identdcioado'] == "on":
		print 'entra al if de denunciado'
		denunciado = Persona(
			anonimo = False,
			nombres = nombres_dciado,
			apellidos = apellidos_dciado,
			sexo = sexo_dciado,
			f_nac = edad_dciado,
			parentesco = parentezco_dciado,
			lugar_trabajo = lug_trab_dciado,
			ocupacion = ocupacion_dciado,
				# = denuncias_ant
				# = donde_den
				)
		denunciado.save()
		denunciado.tipo.add(tipo_denunciado)
		denunciado.save()
		dir_denunciado = Domicilio(
			domicilio = dir_dciado,
			telefono = tel_dciado,
			persona = denunciado,
			)
		dir_denunciado.save()

	else:
		denunciado = Persona(anonimo = True)
		denunciado.save()
		denunciado.tipo.add(tipo_denunciado)
		denunciado.save()

	#fin

	#Datos de la denuncia
	descripcion= request.POST['descdenuncia']
	historia_inf= request.POST['histodenun']
	if request.POST.get and 'opinion' in request.POST and request.POST['opinion'] == "on":
		denuncia = Denuncia(
			f_denuncia = fecha_denuncia, 
			codigo_dna = codigo_dna, 
			nro_atencion = nro_atencion, 
			inhabilitado = False,
			tipologia = tipologia,
			defensoria = request.user.defensoria,
			descripcion = descripcion,
			opinion = True,
			historia = historia,
			)
		denuncia.save()
		denuncia.usuarios.add(request.user)
		denuncia.save()
	else:
		denuncia = Denuncia(
			f_denuncia = fecha_denuncia, 
			codigo_dna = codigo_dna, 
			nro_atencion = nro_atencion, 
			inhabilitado = False,
			tipologia = tipologia,
			defensoria = request.user.defensoria,
			descripcion = descripcion,
			opinion = False,
			)
		denuncia.save()
		denuncia.usuarios.add(request.user)
		denuncia.save()




		estado = Estado.objects.get(nombre = 'Recepcion de la Denuncia')
		logEstado = LogEstado(
			denuncia = denuncia,
			estado = estado,
			)
		logEstado.save()


	#Acciones inmediatas a seguir
	acciones = request.POST['acciones']
	fecha = date.today() + timedelta(days = 1)
	actuacion = Actuaciones(
		f_accion = fecha,
		accion = acciones,
		denuncia = denuncia,
		usuario = request.user,
		)
	actuacion.save()

	perfilVictima = PerfilPersona(
		activo = True,
		tipo = tipo_victima,
		persona = victima,
		denuncia = denuncia,
		)
	
	perfilFamiliar = PerfilPersona(
		activo = True,
		tipo = tipo_familiar,
		persona = familiar,
		denuncia = denuncia,
		)
	
	perfilDenunciante = PerfilPersona(
		activo = True,
		tipo = tipo_denunciante,
		persona = denunciante,
		denuncia = denuncia,
		)
	
	perfilDenunciado = PerfilPersona(
		activo = True,
		tipo = tipo_denunciado,
		persona = denunciado,
		denuncia = denuncia,
		)

	perfilVictima.save()
	perfilFamiliar.save()
	perfilDenunciante.save()
	perfilDenunciado.save()
	

	print 'Denuncia guradada correctamente'
	return HttpResponseRedirect('/denuncias/listar_denuncias/')

@login_required(login_url = '/usuarios/')
def listar_denuncias(request):
	denuncias = Denuncia.objects.filter(usuarios = request.user)
	template = 'denuncias/listar_denuncias.html'
	return render(request, template, {'denuncias':denuncias})

#Vistas de tipo de personas
@login_required(login_url = '/usuarios/')
def list_tipos_view(request):
	tipos = Tipo.objects.all()
	template = 'denuncias/listar_tipos.html'
	return render(request, template, {'tipos':tipos})

@login_required(login_url = '/usuarios/')	
def agregar_tipo_view(request):
	if request.method == 'POST':
		nombre = request.POST['nombre']
		tipo = Tipo(tipo = nombre)
		tipo.save()
		return HttpResponseRedirect('/denuncias/listar_tipos/')

	else:
		form = TipoForm()
		template = 'denuncias/agregar_tipo.html'
	return render(request, template ,{'form':form})


@login_required(login_url = '/usuarios/')	
def edit_tipo_view(request):
	pass

def get_involucrados(denuncias):
	tipo_victima = Tipo.objects.get(tipo = "Victima")
	tipo_familiar = Tipo.objects.get(tipo = "Familiar")
	tipo_denunciante = Tipo.objects.get(tipo = "Denunciante")
	tipo_denunciado = Tipo.objects.get(tipo = "Denunciado")	
	
	for denuncia in denuncias:
		if denuncia.tipo == tipo_victima:
			if not denuncia.persona.nombres:
				victima = 'Anomimo'
			else:
				victima = denuncia.persona
		elif denuncia.tipo == tipo_denunciante:
			if not denuncia.persona.nombres:
				denunciante = 'Anonimo'
			else:
				denunciante = denuncia.persona
		elif denuncia.tipo == tipo_denunciado:
			if not denuncia.persona.nombres:
				denunciado = 'Se desconoce'
			else:
				denunciado = denuncia.persona
	
	involucrados = (victima, denunciante, denunciado,)
	return involucrados

@login_required(login_url = '/usuarios/')
def agregar_actuacion(request, denuncia_id):
	denuncia = Denuncia.objects.get(id = denuncia_id)
	if request.method == 'POST':
		fecha_accion = request.POST['fecha_accion']
		accion = request.POST['accion']
		fecha_resultado = request.POST['fecha_resultado']
		resultado = request.POST['resultado']
		actuacion = Actuaciones(
			f_accion = fecha_accion,
			accion = accion,
			f_resultado = fecha_resultado,
			resultado = resultado,
			denuncia = denuncia,
			usuario = request.user
			)
		actuacion.save()
	actuaciones = Actuaciones.objects.filter(denuncia = denuncia)
	denuncias = PerfilPersona.objects.filter(denuncia = denuncia)
	involucrados = get_involucrados(denuncias)
	victima = involucrados[0]
	denunciante = involucrados[1]
	denunciado = involucrados[2]
	template = 'denuncias/registrar_actuaciones.html'
	return render(request, template, {'victima':victima, 'denunciante':denunciante, 'denunciado': denunciado, 'tipologia':denuncia.tipologia, 'denuncia_id': denuncia_id, 'actuaciones':actuaciones})

@login_required(login_url = '/usuarios/')
def eliminiar_actuacion(request, actuacion_id):
	actuacion = Actuaciones.objects.get(id = actuacion_id)
	denuncia = actuacion.denuncia.id
	actuacion.delete()
	return HttpResponseRedirect('/denuncias/agregar_actuacion/%s' %denuncia)

@login_required(login_url = '/usuarios/')
def editar_actuacion(request, actuacion_id):
	actuacion = Actuaciones.objects.get(id = actuacion_id)
	if request.method == 'POST':
		form_actuacion = ActuacionFormModel(request.POST, instance = actuacion)
		if form_actuacion.is_valid():
			form_actuacion.save()
			return HttpResponseRedirect('/denuncias/agregar_actuacion/%s' %actuacion.denuncia.id)
	else:
		#formulario inicial
		form_actuacion = ActuacionFormModel(instance = actuacion)

	template = 'denuncias/editar_actuaciones.html'
	return render(request, template, {'form':form_actuacion})



