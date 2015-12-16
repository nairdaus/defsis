from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.list_user_view, name = "listar_user_view"),
	url(r'^crear_usuario/$', views.create_user_view, name = "create_user_view"),
	url(r'^editar_usuario/(\d+)$', views.edit_user_view, name = "edit_user_view"),
	url(r'^guardar_modificar/$', views.save_modify, name = "guardar_modificar"),
	url(r'^cerrar_sesion/$', views.cerrar_sesion, name = "cerrar_sesion"),
	url(r'^registrar_denuncia/$', views.registrar_denuncia, name = "registrar_denuncia")
]