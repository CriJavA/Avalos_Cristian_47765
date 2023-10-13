from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppUser.models import *

#class userforms(forms.Form):
 #   NickName = forms.CharField()
  #  UserName = forms.CharField()
   # UserDate = forms.DateField()
    #UserAddress = forms.CharField()
    #UserPass = forms.CharField()
    #UserEmail = forms.EmailField()
    #UserTnum = forms.CharField()
    
class articuloform(forms.Form):
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    Marca = forms.CharField()
    Modelo = forms.CharField()
    Year = forms.CharField(label="Año de fabricación")
    Color = forms.CharField()
    Precio = forms.FloatField()
    Usado = forms.BooleanField()
    Descrip = forms.CharField(label="Descripción")
    Imagen = forms.ImageField()
    
class serviceform(forms.Form):
    Tipo = forms.CharField()
    Subtipo = forms.CharField()
    Precio = forms.FloatField()
    Descrip = forms.CharField()
    
class loginform(forms.Form):
    NickName = forms.CharField()
    UserAddress = forms.CharField()
    
class regUserforms(UserCreationForm):
    UserDate = forms.DateField(label="Fecha de nacimiento")
    UserAddress = forms.CharField(label="dirección de residencia")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    email = forms.EmailField(label="E-mail")
    UserTnum = forms.CharField(label="Teléfono")
    
    class Meta:
        model = User
        exclude = ['password', 'last_login', 'is_superuser', 'groups','user_permissions', 'is_staff','is_active', 'date_joined']
        
class editForm(UserCreationForm):
    UserDate = forms.DateField(label="Fecha de nacimiento")
    UserAddress = forms.CharField(label="dirección de residencia")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    email = forms.EmailField(label="E-mail")
    UserTnum = forms.CharField(label="Teléfono")
    
    class Meta:
        model = User
        exclude = ['username', 'password', 'last_login', 'is_superuser', 'groups','user_permissions', 'is_staff','is_active', 'date_joined']
        
class avatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ["imagen"]
        exclude = ["usuario"]