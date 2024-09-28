from django.contrib import admin
from .models import Cliente
from .models import Carro
from .models import Parqueadero
from .models import Reserva
from .models import Factura
from .models import Empleado
from .models import RegistroAcceso
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Carro)
admin.site.register(Parqueadero)
admin.site.register(Reserva)
admin.site.register(Factura)
admin.site.register(Empleado)
admin.site.register(RegistroAcceso)





