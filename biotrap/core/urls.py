from django.urls import path
from core import views

urlpatterns = [
    path("", views.home, name="home"),
    path("formulario-enviado/", views.successfully, name="successfully"),
]
