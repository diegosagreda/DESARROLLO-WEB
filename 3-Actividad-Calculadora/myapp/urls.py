
from . import views
from django.urls import path

urlpatterns = [
    path('calculadora/',views.calculadora)
]