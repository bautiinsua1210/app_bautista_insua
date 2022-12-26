from django.shortcuts import render
from .models import Client, Car, Service



from app_car.forms import ClientForm, CarForm, ServiceForm



def clients(request):
    return render (request, "AppCoder/profesores.html")

def cars(request):
    return render (request, "AppCoder/Cars.html")

def services(request):
    return render (request, "AppCoder/services.html")

def home(request):
    return render (request, "AppCoder/inicio.html")


##CLIENTS##
def clientForm(request):
    if request.method=="POST":
        form= ClientForm(request.POST)
        
        if form.is_valid():
            informacion=form.cleaned_data
            name= informacion["name"]
            surname= informacion["surname"]
            email= informacion["email"]
            job= informacion["job"]
            client= Client(name=name, surname=surname, email=email, job=job)
            client.save()
            clients=Client.objects.all()
            return render(request, "AppCoder/Profesores.html" ,{"clients":clients, "message": "Client saved correctly"})
        else:
            return render(request, "AppCoder/ProfeFormulario.html" ,{"form": form, "message": "Invalid data"})
        
    else:
        form= ClientForm()
        return render (request, "AppCoder/ProfeFormulario.html", {"form": form})


    

def readClient(request):

    clients=Client.objects.all()
    return render(request, "AppCoder/Profesores.html", {"clients": clients})


def deleteClient(request, id):
    client=Client.objects.get(id=id)
    print(client)
    client.delete()
    clients=Client.objects.all()
    return render(request, "AppCoder/Profesores.html", {"clients": clients, "message": "Client was deleted correctly"})


def editClient(request, id):
    client=Client.objects.get(id=id)
    if request.method=="POST":
        form= ClientForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            client.name=info["name"]
            client.surname=info["surname"]
            client.email=info["email"]
            client.job=info["job"]
            client.save()
            clients=Client.objects.all()
            return render(request, "AppCoder/Profesores.html" ,{"clients":clients, "message": "Client was edited correctly"})
        pass
    else:
        form= ClientForm(initial={"name":client.name, "surname":client.surname, "email":client.email, "job":client.job})
        return render(request, "AppCoder/editarProfesor.html", {"form": form, "client": client})


##CARS##
def carForm(request):
    if request.method=="POST":
        form= CarForm(request.POST)
        
        if form.is_valid():
            informacion=form.cleaned_data
            brand= informacion["brand"]
            model= informacion["model"]
            year= informacion["year"]
            miles= informacion["miles"]
            car= Car(brand=brand, model=model, year=year, miles=miles)
            car.save()
            cars=Car.objects.all()
            return render(request, "AppCoder/Cars.html" ,{"cars":cars, "message": "Car saved correctly"})
        else:
            return render(request, "AppCoder/carForm.html" ,{"form": form, "message": "Invalid data"})
        
    else:
        form= CarForm()
        return render (request, "AppCoder/carForm.html", {"form": form})


    

def readCar(request):

    cars=Car.objects.all()
    return render(request, "AppCoder/Cars.html", {"cars": cars})


def deleteCar(request, id):
    car=Car.objects.get(id=id)
    print(car)
    car.delete()
    cars=Car.objects.all()
    return render(request, "AppCoder/Cars.html", {"cars": cars, "message": "Car was deleted correctly"})


def editCar(request, id):
    car=Car.objects.get(id=id)
    if request.method=="POST":
        form= CarForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            car.brand=info["brand"]
            car.model=info["model"]
            car.year=info["year"]
            car.miles=info["miles"]
            car.save()
            cars=Car.objects.all()
            return render(request, "AppCoder/Cars.html" ,{"cars":cars, "message": "Car was edited correctly"})
        pass
    else:
        form= CarForm(initial={"brand":car.brand, "model":car.model, "year":car.year, "miles":car.miles})
        return render(request, "AppCoder/editCar.html", {"form": form, "car": car})

##SERVICE##
def serviceForm(request):
    if request.method=="POST":
        form= ServiceForm(request.POST)
        
        if form.is_valid():
            informacion=form.cleaned_data
            type= informacion["type"]
            time= informacion["time"]
            price= informacion["price"]
            service= Service(type=type, time=time, price=price)
            service.save()
            services=Service.objects.all()
            return render(request, "AppCoder/services.html" ,{"services":services, "message": "Service saved correctly"})
        else:
            return render(request, "AppCoder/serviceForm.html" ,{"form": form, "message": "Invalid data"})
        
    else:
        form= ServiceForm()
        return render (request, "AppCoder/serviceForm.html", {"form": form})


    

def readService(request):

    services=Service.objects.all()
    return render(request, "AppCoder/services.html", {"services": services})


def deleteService(request, id):
    service=Service.objects.get(id=id)
    print(service)
    service.delete()
    services=Service.objects.all()
    return render(request, "AppCoder/services.html", {"services": services, "message": "Service was deleted correctly"})


def editService(request, id):
    service=Service.objects.get(id=id)
    if request.method=="POST":
        form= ServiceForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            service.type=info["type"]
            service.time=info["time"]
            service.price=info["price"]
            service.save()
            services=Service.objects.all()
            return render(request, "AppCoder/services.html" ,{"services":services, "message": "Service was edited correctly"})
        pass
    else:
        form= ServiceForm(initial={"type":service.type, "time":service.time, "price":service.price})
        return render(request, "AppCoder/editService.html", {"form": form, "service": service})

