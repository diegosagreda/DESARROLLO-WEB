from django.shortcuts import render
from django.http import HttpResponse
from .forms import Calculadora

# Create your views here.
def calculadora (request):

    calculadora = Calculadora()
    respuesta = ''
    
    if request.method == "POST":
        numero1 = request.POST['numero1']
        numero2 = request.POST['numero2']
        try:
            operacion = request.POST['operacion']
        except:
            respuesta = "Selecciona operacion" 

        if operacion == "suma":
            respuesta = int(numero1) + int(numero2)
        elif operacion == "resta":
            respuesta = int(numero1) - int(numero2)
        elif operacion == "multiplicacion":
            respuesta = int(numero1) * int(numero2)
        elif operacion == "division":
            if int (numero2) != 0:
                respuesta = int(numero1) / int(numero2)
            else:
                respuesta = "Division por cero"
        else:
            respuesta = "Selecciona operacion"

        
    return render(request,'myapp/index.html',{
        'form':calculadora,
        'rta':respuesta,
        'test':test
    })
def test ():
    print('holaaaa')