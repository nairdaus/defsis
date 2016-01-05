from django.conf.urls import url
from . import views

urlpatterns = [
	#CRUD Defensorias
	url(r'^$', views.listar_defensoria_view, name = 'listar_defensoria'),
	url(r'^agregar_defensoria/$', views.agregar_defensoria, name = 'agregar_defensoria'),
	url(r'^editar_defensoria/(\d+)$', views.editar_defensoria_view, name = 'edit_defensoria_view'),
	#CRUD Estados
	url(r'^listar_estados/$', views.listar_estados_view, name = 'list_estados_view'),
	url(r'^agregar_estados/$', views.agregar_estados_view, name = 'agregar_estados_view'),
	url(r'^editar_estado/(\d+)$', views.editar_estado_view, name = 'edit_estado_view'),
	#CRUD Tipologias
	url(r'^listar_tipologias/$', views.listar_tipologias_view, name = 'list_tipologias_view'),
	url(r'^agregar_tipologia/$', views.agregar_tipologias_view, name = 'agregar_tipologias_view'),
	url(r'^editar_tipologia/(\d+)$', views.editar_tipologias_view, name = 'edit_tipologias_view'),
	#CRUD Denuncias
	url(r'^listar_denuncias/$', views.listar_denuncias, name = "listar_denuncias"),
	url(r'^registrar_denuncia/$', views.agregar_denuncia, name = "registrar_denuncia"),
	url(r'^iniciar_denuncia/$', views.iniciar_denuncia, name = "iniciar_denuncia"),
	url(r'^agregar_victima/(\d+)$', views.agregar_victima, name = "agregar_victima"),
	url(r'^agregar_familiar/(\d+)$', views.agregar_familiar, name = "agregar_familiar"),
	#url(r'^editar_denuncias/$', views.edit_denuncia_view, name = "edit_denuncia_view"),
	#CRUD Tipos de denuncia
	url(r'^listar_tipos/$', views.listar_tipos_view, name = 'list_tipos_view'),
	url(r'^agregar_tipo/$', views.agregar_tipo_view, name = 'agregar_tipo_view'),
	url(r'^editar_tipo/(\d+)$', views.editar_tipo_view, name = 'editar_tipo_view'),
	#CRUD Registrar Actuaciones
	url(r'^agregar_actuacion/(\d+)$', views.agregar_actuacion, name = 'agregar_actuacion'),
	url(r'^editar_actuacion/(\d+)/$', views.editar_actuacion, name = 'editar_actuacion'),
	url(r'^eliminiar_actuacion/(\d+)/$', views.eliminiar_actuacion, name = 'eliminiar_actuacion'),
]
