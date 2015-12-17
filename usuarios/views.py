from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegistroUserForm


def create_user_view(request):
	if request.method == 'POST':
		form = RegistroUserForm(request.POST)
		if form.is_valid():
			cleaned_data = form.cleaned_data
			nombres = cleaned_data.get('nombres')
			apellidos = cleaned_data.get('apellidos')
			username = cleaned_data.get('usuario')
			password = cleaned_data.get('password')
			tipo = cleaned_data.get('tipo')

			user_model = User.objects.create_user(username = username,  password = password)
			user_model.first_name = nombres
			user_model.last_name = apellidos
			user_model.acces = tipo

			user_model.save()
			
			
			return HttpResponseRedirect('/usuarios/')

	else:
		form = RegistroUserForm()
	context = {
		'form': form
	}
	return render(request, 'usuarios/nuevo_usuario.html', context)

def list_user_view(request):
	usuarios = User.objects.all()
	template = 'usuarios/listar_usuarios.html'
	return render(request, template, {'usuarios': usuarios})

@csrf_exempt
def login_view(request):
	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username = usuario, password = clave)
			if acceso is not None and acceso.is_active:
				login(request, acceso)
				return HttpResponseRedirect('inicio')
			else:
				return render_to_response('usuarios/login.html', {'autenticacion': False, 'formulario':formulario},  context_instance = RequestContext(request))
	else:
		formulario = AuthenticationForm()

	return render_to_response('usuarios/login.html', {'formulario':formulario},  context_instance = RequestContext(request))

@login_required(login_url = '/')
def dashboard_view(request):
	template = 'dashboard.html'
	usuario = request.user
	return render(request, template)

@login_required(login_url = '/')
def cerrar_sesion(request):
	logout(request)
	return HttpResponseRedirect('/')

@login_required(login_url = '/')
def edit_user_view(request, id_user):
	usuario = User.objects.get(id = id_user)
	template = 'usuarios/editar_usuario.html'
	return render(request, template, {'usuario': usuario} )

@csrf_exempt
@login_required(login_url = '/')
def save_modify(request):
	user_id = request.POST['id']
	nombre = request.POST['first_name']
	apellidos = request.POST['last_name']
	usuario = request.POST['user_name']
	clave = request.POST['password']
	seleccion = request.POST['seleccion']
	tipos = {'Psicologo(a)':1,'Trabajador(a) Social':2,'Abogado(a)':3,'Jefatura':4,'Secretaria':5}
	tipo_usuario = tipos[seleccion]

	current_user = User.objects.get(id=user_id)
	current_user.first_name = nombre
	current_user.last_name = apellidos
	current_user.username = usuario
	current_user.password = clave
	current_user.acces = tipo_usuario
	current_user.save()

	print 'Usuario Actualizado correctamente'

	return HttpResponseRedirect('/usuarios/')

# Esta vista es de prueba, y debe ser trasladada al modulo "denuncias"
@login_required(login_url = '/')
def registrar_denuncia(request):
	template = 'registrarDenuncia.html'
	return render(request, template)
