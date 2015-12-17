from django import forms
from django.contrib.auth.models import User

class DefensoriasForm(forms.Form):
	nombre = forms.CharField()
	direccion = forms.CharField()
	telefono = forms.CharField()

class EstadoForm(forms.Form):
	nombre = forms.CharField()

class TipologiaForm(forms.Form):
	nombre = forms.CharField()

