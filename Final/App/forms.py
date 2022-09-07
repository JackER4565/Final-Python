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