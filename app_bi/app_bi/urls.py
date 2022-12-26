from django.contrib import admin
from django.urls import path, include
from app_car.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("app_car/", include("app_car.urls")),
    
]
