from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.list_user_view, name = "listar_user_view"),
	url(r'^crear_usuario/$', views.create_user_view, name = "create_user_view"),
	url(r'^editar_usuario/$', views.edit_user_view, name = "edit_user_view"),
	url(r'^cerrar_sesion/$', views.cerrar_sesion, name = "cerrar_sesion"),
	url(r'^registrar_denuncia/$', views.registrar_denuncia, name = "registrar_denuncia"),
	url(r'^mis_casos/$', views.mis_casos, name = "mis_casos"),
	url(r'^registrar_actuaciones/$', views.registrar_actuaciones, name = "registrar_actuaciones"),
	url(r'^listado_casos/$', views.listado_casos, name = "listado_casos"),
	url(r'^detalles_del_caso/$', views.detalles_del_caso, name = "detalles_del_caso"),
	url(r'^calendario/$', views.calendario, name = "calendario"),
]