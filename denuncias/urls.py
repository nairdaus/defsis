from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.list_defensoria_view, name = 'listar_defensoria'),
	url(r'^agregar_defensoria/$', views.agregar_defensoria, name = 'agregar_defensoria'),
	url(r'^editar_defensoria/(\d+)$', views.edit_defensoria_view, name = 'edit_defensoria_view'),
	#CRUD Estados
	url(r'^listar_estados/$', views.list_estados_view, name = 'list_estados_view'),
	url(r'^agregar_estados/$', views.agregar_estados_view, name = 'agregar_estados_view'),
	url(r'^editar_estado/(\d+)$', views.edit_estado_view, name = 'edit_estado_view'),
	#CRUD Tipologias
	url(r'^listar_tipologias/$', views.list_tipolgias_view, name = 'list_tipologias_view'),
	url(r'^agregar_tipologia/$', views.agregar_tipologias_view, name = 'agregar_tipologias_view'),
	url(r'^editar_tipologia/(\d+)$', views.edit_tipologias_view, name = 'edit_tipologias_view'),
	#CRUD Denuncias
	url(r'^registrar_denuncia/$', views.registrar_denuncia, name = "registrar_denuncia"),
]
