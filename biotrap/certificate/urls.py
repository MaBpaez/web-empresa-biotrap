from django.urls import path
from certificate import views

urlpatterns = [
    path("", views.certificate, name="certificate"),
]
