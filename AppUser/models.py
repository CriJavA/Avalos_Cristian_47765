from django.db import models
from django.contrib.auth.models import User

class MainUser(models.Model):
    NickName = models.CharField(max_length=60)
    UserName = models.CharField(max_length=60)
    UserDate = models.DateField()
    UserAddress = models.CharField(max_length=60)
    UserPass = models.CharField(max_length=20)
    UserEmail = models.EmailField()
    UserTnum = models.CharField(max_length=20)
    
    def __str__(self):
        return self.NickName
    
class Articulo(models.Model):
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Marca = models.CharField(max_length=60)
    Modelo = models.CharField(max_length=60)
    Year = models.CharField(max_length=4)
    Color = models.CharField(max_length=20)
    Precio = models.FloatField(max_length=10)
    Usado = models.BooleanField(default=False)
    Descrip = models.TextField(max_length=500)
    Imagen = models.ImageField(upload_to="ItemsPic", null=True, blank=True)
    
    def __str__(self):
        return self.Modelo
    
class Service(models.Model):
    Tipo = models.CharField(max_length=30)
    Subtipo = models.CharField(max_length=30)
    Precio = models.FloatField(max_length=10)
    Descrip = models.CharField(max_length=500)
    
    def __str__(self):
        return self.Subtipo
    
class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatar", null=True, blank=True)
    
