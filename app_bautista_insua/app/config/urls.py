from django.contrib import admin
from django.urls import path
from app.views.family_member import members
urlpatterns = [
    path('family/', members),
]