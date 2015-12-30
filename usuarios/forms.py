from django import forms
from django.contrib.auth.models import User
from denuncias.models import Defensoria

class RegistroUserForm(forms.Form):

    defensorias = Defensoria.objects.all()

    TYPE_USER = (('1','Trabajadora Social'),('2','Psicologo'),('3','Abogado'),('4','Jefatura'),('5','Secretaria'))

    nombres = forms.CharField()
    apellidos = forms.CharField()
    usuario = forms.CharField(min_length=5)
    password = forms.CharField(min_length=6, widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    tipo = forms.ChoiceField(choices = TYPE_USER)
    defensoria = forms.ModelChoiceField(defensorias)
    
    def clean_username(self):
        """Comprueba que no exista un username igual en la db"""
        usuario = self.cleaned_data['username']
        if User.objects.filter(username=usuario):
            raise forms.ValidationError('Nombre de usuario ya registrado.')
        return usuario

    def clean_password2(self):
        """Comprueba que password y password2 sean iguales."""
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('Las claves no coinciden.')
        return password2

