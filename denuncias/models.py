from __future__ import unicode_literals

from django.db import models

class Tipo(models.Model):
	tipo = models.CharField(max_length = 40)

	def __str__(self):
		return self.tipo.encode('utf-8')
		
class Persona(models.Model):
	
	BOOL_CHOICES = (('S','Si'),('N','No'))
	SEX_CHOICES = (('H','Hombre'),('M','Mujer'))

	nombres = models.CharField(max_length = 40)
	apellidos = models.CharField(max_length = 40)
	gestante = models.CharField(max_length = 1, choices = BOOL_CHOICES, blank = True, null = True)
	sexo = models.CharField(max_length = 1, choices = SEX_CHOICES)
	f_nac = models.DateField(blank = True, null = True)
	c_nac = models.CharField(max_length = 1, choices = BOOL_CHOICES, blank = True, null = True)
	estudia = models.CharField(max_length = 1, choices = BOOL_CHOICES,blank = True, null = True)
	ult_curso = models.CharField(max_length = 40, blank = True, null = True)
	tipo_trabajo = models.CharField(max_length = 40, blank = True, null = True)
	parentesco = models.CharField(max_length = 40, blank = True, null = True)
	g_instruccion = models.CharField(max_length = 40, blank = True, null = True)
	ocupacion = models.CharField(max_length = 40, blank = True, null = True)
	cedula = models.CharField(max_length = 40, blank = True, null = True)
	lugar_trabajo = models.CharField(max_length = 40, blank = True, null = True)
	# Relaciones 
	tipo = models.ManyToManyField(Tipo)

	def __str__(self):
		return '%s %s' %(nombres, apellidos)

class Domicilio(models.Model):
	domicilio = models.CharField(max_length = 100)
	telefono = models.CharField(max_length = 10)
	persona = models.ForeignKey(Persona);


class Defensoria(models.Model):
	nombre = models.CharField(max_length = 40)
	direccion = models.CharField(max_length = 100, blank = True, null = True)
	telefono = models.CharField(max_length = 40, blank = True, null = True)

class Tipologia(models.Model):
	nombre = models.CharField(max_length = 40)

	def __str__(self):
		return self.nombre.encode('utf-8')

class Denuncia(models.Model):
	f_denuncia = models.DateField()
	codigo_dna = models.CharField(max_length = 10)
	nro_atencion = models.CharField(max_length = 10)
	inhabilitado = models.BooleanField()
	tipologia = models.ForeignKey(Tipologia)
	defensoria = models.ForeignKey(Denuncia)

	def __str__(self):
		return self.codigo_dna.encode('utf-8')

class PerfilPersona(models.Model):
	activo = models.BooleanField()
	f_creacion = models.DateField(auto_now_add=True)
	f_modificacion = models.DateField(auto_now=True)
	tipo = models.ForeignKey(Tipo)
	persona = models.ForeignKey(Persona)	
	usuario = models.ManyToManyField(User)
	denuncia = models.ForeignKey(Denuncia)


class Estado(models.Model):
	nombre = models.CharField(max_length = 40)
	tipo = models.CharField(max_length = 10)
	ianus = models.CharField(max_length = 15)
	estado = models.ForeignKey(Denuncia)

class Sentencia(models.Model):
	sentencia = models.TextField()
	observaciones = models.TextField()
	f_sent = models.DateField(auto_now = True)
	denuncia = models.ForeignKey(Denuncia)

class Actuaciones(models.Model):
	f_accion = models.DateField()
	accion = models.CharField(max_length = 100)
	f_resultado = models.DateField(blank = True, null = True)
	resultado = models.CharField(max_length = 100, blank = True, null = True)
	pag_adjuntas = models.CharField(max_length = 40, blank = True)
	denuncia = models.ForeignKey(Denuncia)



class Cierre(models.Model):
	resuelto = models.BooleanField()
	derivado = models.BooleanField()
	observaciones = models.TextField()
	denuncia = models.ForeignKey(Denuncia)

