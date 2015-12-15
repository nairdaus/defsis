from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def create_user_view(request):
	return render()

def list_user_view(request):
	usuarios = User.objects.all()
	template = 'usuarios/listar_usuarios.html'
	return render(request, template, {'usuarios': usuarios})

def edit_user_view(request):
	return render()

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

# Esta vista es de prueba, y debe ser trasladada al modulo "denuncias"
@login_required(login_url = '/')
def registrar_denuncia(request):
	template = 'registrarDenuncia.html'
	return render(request, template)

@login_required(login_url = '/')
def mis_casos(request):
	template = 'misCasos.html'
	return render(request, template)

@login_required(login_url = '/')
def mis_casos(request):
	template = 'verCasos.html'
	return render(request, template)