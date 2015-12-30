from django import forms
from django.contrib.auth.models import User
from models import Actuaciones

class DefensoriasForm(forms.Form):
	nombre = forms.CharField()
	direccion = forms.CharField()
	telefono = forms.CharField()

class EstadoForm(forms.Form):
	nombre = forms.CharField()

class TipologiaForm(forms.Form):
	nombre = forms.CharField()

class TipoForm(forms.Form):
	nombre = forms.CharField()

class ActuacionForm(forms.Form):
	fecha_accion = forms.DateField()
	accion = forms.CharField(max_length= 100)
	fecha_resultado = forms.DateField()
	resultado = forms.CharField()

class ActuacionFormModel(forms.ModelForm):
	class Meta:
		model = Actuaciones
		fields = ('f_accion','accion','f_resultado','resultado' )

