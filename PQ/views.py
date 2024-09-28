from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Cliente
from django import forms

def home(request):
    return render(request, 'PQ/home.html')
    
# Crear un formulario para el modelo Cliente
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'telefono', 'carro']  # Incluye los campos necesarios

def registrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()  # Guardar el nuevo cliente
            return redirect('lista_clientes')  # Redirigir a una página después de guardar
    else:
        form = ClienteForm()
    return render(request, 'clientes/registrar_cliente.html', {'form': form})
