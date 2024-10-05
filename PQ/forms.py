from django import forms
from .models import Cliente, Carro, Parqueadero, Reserva, Factura, Empleado, RegistroAcceso

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'telefono', 'carro']

class CarroForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = ['marca', 'modelo', 'placa']

class ParqueaderoForm(forms.ModelForm):
    class Meta:
        model = Parqueadero
        fields = ['nombre', 'ubicacion', 'capacidad']

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['cliente', 'carro', 'fecha_inicio', 'fecha_final', 'estado']

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['reserva', 'fecha', 'monto']

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'ubicacion', 'telefono', 'correo']

class RegistroAccesoForm(forms.ModelForm):
    class Meta:
        model = RegistroAcceso
        fields = ['parqueadero', 'carro', 'reserva', 'empleado', 'cliente', 'fecha_entrada', 'fecha_salida']