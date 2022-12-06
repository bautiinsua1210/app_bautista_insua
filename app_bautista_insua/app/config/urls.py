from django.contrib import admin
from django.urls import path
from app.views.family_member import members
from app.views.index import index

urlpatterns = [
    path('', index),
    path('family/', members),
]