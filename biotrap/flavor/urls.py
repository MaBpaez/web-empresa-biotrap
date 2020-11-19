from django.urls import path
from flavor import views

urlpatterns = [
    path("", views.flavors, name="flavors"),
]
