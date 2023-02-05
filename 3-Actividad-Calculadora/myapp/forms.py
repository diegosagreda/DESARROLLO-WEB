from django import forms
OPERACIONES= [
    ('suma', 'Suma'),
    ('resta', 'Resta'),
    ('multiplicacion', 'Multiplicacion'),
    ('division', 'Division'),
    ]
class Calculadora(forms.Form):
    numero1 = forms.CharField(label="Numero 1", max_length=200)
    numero2 = forms.CharField(label="Numero 2", max_length=200)
    operacion = forms.CharField(widget=forms.RadioSelect(choices=OPERACIONES))
    