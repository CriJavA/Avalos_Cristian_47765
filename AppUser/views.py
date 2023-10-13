from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from AppUser.models import *
from AppUser.forms import *
#----------------------------------------------------------------------------
def inicio (request):
    return render(request, "AppUser/inicio.html")
#----------------------------------------------------------------------------
def contacto (request):
    return render(request, "AppUser/contacto.html")
#----------------------------------------------------------------------------
def About (request):
    return render(request, "AppUser/About.html")
#----------------------------------------------------------------------------
def logIn (request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            xUser = form.cleaned_data.get("username")
            xPass = form.cleaned_data.get("password")
            authUser = authenticate(username=xUser, password=xPass)
            if authUser is not None:
                login(request, authUser)
                xArt = Articulo.objects.all()
                context = {"listaArticulos": xArt}
                return render(request, "AppUser/browser.html", context)
        else:
            return render(request, "AppUser/Inicio.html", {"MENSAJE1":"Lo sentimos", "MENSAJE2":"Datos incorrectos..."})
    else:
        form = AuthenticationForm()
    return render(request, "AppUser/logIn.html", {"FormLogin":form})
#----------------------------------------------------------------------------
def registro (request):
    if request.method == "POST":
        form = regUserforms(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
        return render(request, "AppUser/Inicio.html", {"MENSAJE1":"Felicitaciones!", "MENSAJE2":f"el usuario {username} fué creado con exito"})
    else:
        form= regUserforms()
    context = {"FormReg":form}
    return render(request, "AppUser/registro.html", context)
#----------------------------------------------------------------------------
def userEdit(request, userNick):
    xUser = User.objects.get(username=userNick)
    if request.method == "POST":
        xForm = editForm(request.POST)
        if xForm.is_valid():
            info = xForm.cleaned_data
            xUser.first_name = info["first_name"]
            xUser.last_name = info["last_name"]
            xUser.email = info["email"]
            xUser.set_password(info["password1"])
            xUser.UserDate = info["UserDate"]
            xUser.UserAddress = info["UserAddress"]
            xUser.UserTnum = info["UserTnum"]
            xUser.save()
            return render(request, "AppUser/Inicio.html", {"MENSAJE1":"Felicitaciones!", "MENSAJE2":f"el usuario {xUser} fué actualizado con exito"})
    else:
        xForm = editForm(initial={"first_name":xUser.first_name,
                                    "last_name":xUser.last_name,
                                    "email":xUser.email,
                                    "UserDate":xUser.UserDate,
                                    "UserAddress":xUser.UserAddress,
                                    "UserTnum":xUser.UserTnum,
                                    })        
    context = {"FormEdit":xForm,"UserEdit":userNick}
    return render(request, "AppUser/editarPerfil.html", context)
#----------------------------------------------------------------------------
def unAvatar(request):
    if request.method == "POST":
        xForm = avatarForm(request.POST, request.FILES)
        if xForm.is_valid():
            xUser = User.objects.get(username=request.user)
            xAvatar = Avatar(usuario=xUser, imagen=xForm.cleaned_data["imagen"])
            xAvatar.save()
            return render(request, "AppUser/Inicio.html")
    else:
        xForm = avatarForm()
    context = {"FormAvatar":xForm}
    return render(request, "AppUser/Avatar.html", context)
#----------------------------------------------------------------------------

#SERVICIOS
#----------------------------------------------------------------------------
def servicios (request):
    if request.method == "POST":
        form_z = serviceform(request.POST)
        if form_z.is_valid():
            infoC = form_z.cleaned_data
            serv = Service(Tipo=infoC["Tipo"],                           
                           Subtipo=infoC["Subtipo"],           
                           Precio=infoC["Precio"],
                           Descrip=infoC["Descrip"],
                           )
            serv.save()
            return render(request, "AppUser/Inicio.html")
    else:
        form_z = serviceform()
    return render(request, "AppUser/servicios.html", {"formKeyC":form_z})
#----------------------------------------------------------------------------
def BroServ(request):
    xSrv = Service.objects.all()
    context = {"listaServicios": xSrv}
    
    return render(request, "AppUser/browserServ.html", context)
#----------------------------------------------------------------------------
def SrvRead(request):
    xSrv = Service.objects.all()
    context = {"listaServicios": xSrv}
    
    return render(request, "AppUser/listaServicios.html", context)
#----------------------------------------------------------------------------
def srvDelete(request, srvSubtipo):
    xSrv = Service.objects.get(Subtipo=srvSubtipo)
    xSrv.delete()
    
    ySrv = Service.objects.all()
    context = {"listaServicios": ySrv}
    return render(request, "AppUser/listaServicios.html", context)
#----------------------------------------------------------------------------
def srvEdit(request, srvSubtipo1):
    xSrv = Service.objects.get(Modelo=srvSubtipo1)
    if request.method == "POST":
        xForm = serviceform(request.POST, request.FILES) #*
        if xForm.is_valid():
            info = xForm.cleaned_data
            xSrv.Marca = info["Marca"]
            xSrv.Modelo = info["Modelo"]
            xSrv.Year = info["Year"]
            xSrv.Color = info["Color"]
            xSrv.Precio = info["Precio"]
            xSrv.Usado = info["Usado"]
            xSrv.Descrip = info["Descrip"]
            xSrv.Imagen = xForm.cleaned_data["Imagen"]
            xSrv.save()
            
            xSrv = Service.objects.all()
            context = {"listaArticulos": xSrv}
            return render(request, "AppUser/listaServicios.html", context)
    else:
        xForm = serviceform(initial={"Marca":xSrv.Marca,
                                  "Modelo":xSrv.Modelo,
                                  "Year":xSrv.Year,
                                  "Color":xSrv.Color,
                                  "Precio":xSrv.Precio,
                                  "Usado":xSrv.Usado,
                                  "Descrip":xSrv.Descrip,
                                  "Imagen":xSrv.Imagen,
                                })        
    context = {"FormEdit":xForm,"ServiceEdit":srvSubtipo1}
    return render(request, "AppUser/editarServicio.html", context)
#----------------------------------------------------------------------------

#ARTÍCULOS
#----------------------------------------------------------------------------
def eShop (request):
    if request.method == "POST":
        form_y = articuloform(request.POST, request.FILES)
        if form_y.is_valid():
            xUser = User.objects.get(username=request.user)
            infoB = form_y.cleaned_data
            articulo = Articulo(Usuario=xUser,
                                Marca=infoB["Marca"],
                                Modelo=infoB["Modelo"],
                                Year=infoB["Year"],
                                Color=infoB["Color"],
                                Precio=infoB["Precio"],
                                Usado=infoB["Usado"],
                                Descrip=infoB["Descrip"],
                                Imagen=form_y.cleaned_data["Imagen"]
                                )
            articulo.save()
            xArt = Articulo.objects.all()
            context = {"listaArticulos": xArt}
            return render(request, "AppUser/browser.html", context)
    else:
        form_y = articuloform()
    context = {"formKeyB":form_y}
    return render(request, "AppUser/shop.html", context)
#----------------------------------------------------------------------------
def soloItem (request, artModelo2):
    xArt = Articulo.objects.get(Modelo=artModelo2)
    if request.method == "POST":
        xForm = articuloform(request.POST, request.FILES)
        if xForm.is_valid():
            xArt.Marca = xForm["Marca"]
            xArt.Modelo = xForm["Modelo"]
            xArt.Year = xForm["Year"]
            xArt.Color = xForm["Color"]
            xArt.Precio = xForm["Precio"]
            xArt.Usado = xForm["Usado"]
            xArt.Descrip = xForm["Descrip"]
            xArt.Imagen = xForm.cleaned_data["Imagen"]
    else:
        xForm = articuloform({"Marca":xArt.Marca,
                            "Modelo":xArt.Modelo,
                            "Year":xArt.Year,
                            "Color":xArt.Color,
                            "Precio":xArt.Precio,
                            "Usado":xArt.Usado,
                            "Descrip":xArt.Descrip,
                            "Imagen":xArt.Imagen,
                            })        

    context = {"FormSolo":xForm,"UserEdit":artModelo2}
    return render(request, "AppUser/items.html", context)
#----------------------------------------------------------------------------
def shopSearch(request):
    return render(request, "AppUser/shopSearch.html")
#----------------------------------------------------------------------------
def resSerch (request):
    
    if request.GET["Marca"]:
        marcaArt = request.GET["Marca"]
        artMarcas = Articulo.objects.filter(Marca__icontains=marcaArt)
        return render(request, "AppUser/resultado.html", {"artMarcas":artMarcas, "marcaArt":marcaArt})
    else:
        respuesta = "No ingresaste datos."
    
    return HttpResponse(respuesta)
#----------------------------------------------------------------------------
def Bro(request):
    xArt = Articulo.objects.all()
    context = {"listaArticulos": xArt}
    
    return render(request, "AppUser/browser.html", context)
#----------------------------------------------------------------------------
def ArtRead(request):
    xArt = Articulo.objects.all()
    context = {"listaArticulos": xArt}
    
    return render(request, "AppUser/listaArticulos.html", context)
#----------------------------------------------------------------------------
def artDelete(request, artModelo):
    xArt = Articulo.objects.get(Modelo=artModelo)
    xArt.delete()
    
    yArt = Articulo.objects.all()
    context = {"listaArticulos": yArt}
    
    return render(request, "AppUser/ListaArticulos.html", context)
#----------------------------------------------------------------------------
def artEdit(request, artModelo1):
    xArt = Articulo.objects.get(Modelo=artModelo1)
    if request.method == "POST":
        xForm = articuloform(request.POST, request.FILES) #*
        if xForm.is_valid():
            info = xForm.cleaned_data
            xArt.Marca = info["Marca"]
            xArt.Modelo = info["Modelo"]
            xArt.Year = info["Year"]
            xArt.Color = info["Color"]
            xArt.Precio = info["Precio"]
            xArt.Usado = info["Usado"]
            xArt.Descrip = info["Descrip"]
            xArt.Imagen = xForm.cleaned_data["Imagen"]
            xArt.save()
            
            xArt = Articulo.objects.all()
            context = {"listaArticulos": xArt}
            return render(request, "AppUser/listaArticulos.html", context)
    else:
        xForm = articuloform(initial={"Marca":xArt.Marca,
                                  "Modelo":xArt.Modelo,
                                  "Year":xArt.Year,
                                  "Color":xArt.Color,
                                  "Precio":xArt.Precio,
                                  "Usado":xArt.Usado,
                                  "Descrip":xArt.Descrip,
                                  "Imagen":xArt.Imagen,
                                })        
    context = {"FormEdit":xForm,"UserEdit":artModelo1}
    return render(request, "AppUser/editarArticulo.html", context)