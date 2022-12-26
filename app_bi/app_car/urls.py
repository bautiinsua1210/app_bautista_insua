from django.urls import path
from .views import *




urlpatterns = [
    path("clients/", clients, name="clients"),
    path("", home, name="home"),

    path("clientForm/", clientForm, name="clientForm"),

    path("readClient/", readClient, name="readClient"),
    path("deleteClient/<id>", deleteClient, name="deleteClient"),
    path("clientEdit/<id>", clientEdit, name="clientEdit"),

]