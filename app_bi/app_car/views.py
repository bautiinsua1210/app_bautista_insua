from django.shortcuts import render
from .models import Client

from app_car.forms import ClientForm 




def clients(request):
    return render (request, "templates\client.html")

def home(request):
    return render (request, "templates\home.html")



##CLIENT'S##

def clientForm(request):
    if request.method=="POST":
        form= ClientForm(request.POST)
        
        if form.is_valid():
            informacion=form.cleaned_data
            name= informacion["name"]
            surname= informacion["surname"]
            email= informacion["email"]
            role= informacion["role"]
            client= Client(name=name, surname=surname, email=email, role=role)
            client.save()
            clients=Client.objects.all()
            return render(request, "templates\client.html" ,{"clients":clients, "message": "Client was saved correctly"})
        else:
            return render(request, "templates\clientForm.html" ,{"form": form, "message": "Invalid data"})
        
    else:
        form= ClientForm()
        return render (request, "templates\clientForm.html", {"form": form})


def readClient(request):

    clients=Client.objects.all()
    return render(request, "templates\client.html", {"clients": clients})


def deleteClient(request, id):
    client=Client.objects.get(id=id)
    print(client)
    client.delete()
    clients=Client.objects.all()
    return render(request, "templates\client.html", {"clients": clients, "message": "Client was deleted correctly"})


def clientEdit(request, id):
    client=Client.objects.get(id=id)
    if request.method=="POST":
        form= ClientForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            client.name=info["name"]
            client.surname=info["surname"]
            client.email=info["email"]
            client.role=info["role"]
            client.save()
            clients=Client.objects.all()
            return render(request, "templates\client.html" ,{"clients":clients, "message": "Client was edited correctly"})
        pass
    else:
        form= ClientForm(initial={"name":client.name, "surname":client.surname, "email":client.email, "role":client.role})
        return render(request, "templates\clientEdit.html", {"form": form, "profesor": client})













"""def busquedaComision(request):
    return render(request, "AppCoder/busquedaComision.html")

def buscar(request):
    
    comision= request.GET["comision"]
    if comision!="":
        cursos= Curso.objects.filter(comision__icontains=comision)#buscar otros filtros en la documentacion de django
        return render(request, "AppCoder/resultadosBusqueda.html", {"cursos": cursos})
    else:
        return render(request, "AppCoder/busquedaComision.html", {"mensaje": "Che Ingresa una comision para buscar!"})"""


    


