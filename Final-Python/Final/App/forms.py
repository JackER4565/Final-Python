from django import forms
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField  
from django.forms.forms import Form  

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	username = forms.CharField(label="Usuario")
	password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
	password2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)

	class Meta:
		model = User
		fields =['username', 'email', 'password1', 'password2']
		help_texts = {k:"" for k in fields}



class AgregarBlog(forms.Form):
    titulo = forms.CharField(label='Título', max_length=20)
    subtitulo = forms.CharField(label='Subtítulo',max_length=20)
    texto_corto = forms.CharField(label="Texto Corto", max_length=40)
    texto_largo = forms.CharField(label="Texto largo", max_length=255)
    autor = forms.CharField(label="Autor", max_length=40)
    imagen = forms.ImageField(label="Imagen")