from django.urls import path, include
from django.contrib.auth.views import LogoutView
from AppUser.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('Inicio/', inicio, name="Inicio"),
    path('Login/', logIn, name="Login"),
    path('Registro/', registro, name="Registro"),
    path('Contacto/', contacto, name="Contacto"),
    path('Logout', LogoutView.as_view(template_name="AppUser/Inicio.html"), name="Logout"),
    path('Editar/', userEdit, name="UserEdit"),
    path('Avatar/', unAvatar, name="Avatar"),
    path('About/', About, name="About"),
    # Urls de Articulos:
    path('Shop/', eShop, name="Shop"),
    path('Browser/', Bro, name="Browser"),
    path('ListaArticulos/', ArtRead, name="LstaArticulos"),
    path('EliminarArticulo/<artModelo>', artDelete, name="EliminarArticulo"),
    path('EditarArticulo/<artModelo1>', artEdit, name="EditarArticulo"),
    path('Items/<artModelo2>', soloItem, name="Items"),
    path('ShopSearch/', shopSearch, name="BusquedaArt"),
    path('Resultado/', resSerch, name="ResuntadosBusquedaArt"),
    # Urls de Servicios:
    path('Servicios/', servicios, name="Servicios"),
    path('BrowserServ/', BroServ, name="BrowserServ"),
    path('ListaServicios/', SrvRead, name="ListaServicios"),
    path('EliminarServicio/<srvSubtipo>/', srvDelete, name="EliminarServicio"),
    path('EditarServicio/<srvSubtipo1>', srvEdit, name="EditarServicio"),
    
    
    
   
    
]
