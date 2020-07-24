from django import forms

class FormularioContacto(forms.Form):
    nombre = forms.CharField(max_length=100)
    telefono = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=60)
    mensaje = forms.CharField(max_length=500)