from django.urls import path
from .views import *



urlpatterns = [
    path("profesores/", clients, name="clients"),
    path("cars/", cars, name="cars"),
    path("services/", services, name="services"),
    path("", home, name="home"),

    path("profeFormulario/", clientForm, name="clientForm"),
    path("carForm/", carForm, name="carForm"),
    path("serviceForm/", serviceForm, name="serviceForm"),

    path("leerProfesores/", readClient, name="readClient"),
    path("eliminarProfesor/<id>", deleteClient, name="deleteClient"),
    path("editarProfesor/<id>", editClient, name="editClient"),
    path("readCar/", readCar, name="readCar"),
    path("deleteCar/<id>", deleteCar, name="deleteCar"),
    path("editCar/<id>", editCar, name="editCar"),
    path("readService/", readService, name="readService"),
    path("deleteService/<id>", deleteService, name="deleteService"),
    path("editService/<id>", editService, name="editService"),
]