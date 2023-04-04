from django import forms

class Curso(forms.Form):

    nombre = forms.CharField(max_length=20)
    camada = forms.IntegerField()

class Entregable(forms.Form):
    nombre = forms.CharField(max_length=30)
    FechaDeEntrega = forms.DateField()

class Estudiante(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()

class Profesor(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30) 

