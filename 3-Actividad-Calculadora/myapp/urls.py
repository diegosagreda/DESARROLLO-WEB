
from . import views
from django.urls import path

urlpatterns = [
    path('',views.calculadora),
    path('/',views.calculadora),
    
]