from django.db import models

# Create your models here.
class Hotel(models.Model):

    id=models.IntegerField
    nombre=models.CharField(max_length=200)
    direccion=models.CharField(max_length=500)
    ciudad=models.CharField(max_length=200)
    Telefono=models.CharField(max_length=15)
    Email=models.CharField(max_length=120)

    def __str__(self):
        return self.nombre
    

class Reserva(models.Model):

    idreserva=models.IntegerField
    fecha_de_entrada=models.DateField
    fecha_de_salida=models.DateField
    nro_de_huespedes=models.IntegerField
    tipo_habitacion=models.IntegerField
    precio_total=models.IntegerField
    estado=models.CharField(max_length=50)
    idhotel=models.ForeignKey(Hotel, on_delete=models.CASCADE)


    def __str__(self):
        return self.fecha_de_entrada


