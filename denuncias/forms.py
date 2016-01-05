# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from django import forms
from django.forms import Textarea
from django.contrib.auth.models import User
from models import Actuaciones, Defensoria, Estado, Tipologia, Tipo, Persona, Denuncia

class DateInput(forms.DateInput):
    input_type = 'date'

class DenunciaForm(forms.ModelForm):
	class Meta:
		model = Denuncia
		fields = {'f_denuncia','codigo_dna','nro_atencion','tipologia','descripcion','opinion', 'historia'}
		labels = {
			'f_denuncia': _('Fecha denuncia'),
			'nro_atencion': _('Numero de atencion')
		}
		widgets = {
            'f_denuncia': DateInput(),
            'descripcion': Textarea(),
            'historia': Textarea(),
        }

class VictimaForm(forms.ModelForm):
	class Meta:
		model = Persona
		fields = {'nombres','apellidos','gestante','f_nac','sexo','c_nac','estudia','ult_curso','tipo_trabajo'}
		labels = {
			'f_nac': _('Fecha de Nacimiento'),
			'c_nac': _('Certificado de Nacimiento'),
			'ult_curso': _('Ultimo Curso')
		}
		widgets = {
			'f_nac': DateInput(),
		}
class FamiliarForm(forms.ModelForm):
	class Meta:
		model = Persona
		fields={'nombres','apellidos', 'parentesco', 'f_nac', 'sexo', 'g_instruccion','ocupacion'}
		widgets = {
			'f_nac': DateInput(),
		}
#class DenuncianteForm(forms.ModelForm):
#	pass
#class DenunciadoForm(forms.ModelForm):
#	pass


class DefensoriasForm(forms.ModelForm):
	class Meta:
		model = Defensoria
		fields = {'nombre','direccion','telefono'}
	def clean_telefono(self):
		derensoria_limpia = self.cleaned_data

		telefono = derensoria_limpia.get('telefono')
		if len(telefono)>8:
			raise forms.ValidationError("El telefono debe tener menos de 8 caracteres")
		if telefono.isdigit() == False:
			raise forms.ValidationError("El telefono solo debe contener numeros")

		return telefono

class EstadoForm(forms.ModelForm):
	class Meta:
		model = Estado
		fields = {'nombre'}

class TipologiaForm(forms.ModelForm):
	class Meta:
		model = Tipologia
		fields = {'nombre'}

class TipoForm(forms.ModelForm):
	class Meta:
		model = Tipo
		fields = {'tipo'}

class ActuacionFormModel(forms.ModelForm):
	class Meta:
		model = Actuaciones
		fields = ('f_accion','accion','f_resultado','resultado' )
		labels = {
			'f_accion': _('Fecha Accion'),
			'f_resultado': _('Fecha Resultado')
		}

