from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("anmol", views.anmol, name="anmol"),
    path("anu", views.anu, name="anu"),
]
