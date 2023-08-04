from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(blank=True, null=True, max_length= 50)
    apellido = models.CharField(blank=True, null=True, max_length= 50)
    correo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    fecha_registro = models.DateField()
    fecha_nac = models.DateField()
    ci = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    direccion = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.correo}- {self.telefono}- {self.ci}- {self.fecha_registro}- {self.fecha_nac}- {self.tipo}- {self.direccion}- {self.conntrasena}"
    
class Sede(models.Model):
    nombre = models.CharField(blank=True, null=True, max_length= 50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} - {self.direccio} - {self.telefono}- {self.estado}"

class Cancha(models.Model):
    nombre = models.CharField(blank=True, null=True, max_length= 50)
    tipo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=50)
    id_sede = models.ForeignKey('Sede', on_delete=models.PROTECT, db_column='id_sede', blank=True, null=True)
    estado = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.nombre} - {self.tipo} - {self.descripcion}- {self.estado}"


class Reserva(models.Model):

    id_usuario = models.ForeignKey('Usuario', on_delete=models.PROTECT, db_column='id_usuario', blank=True, null=True)
    id_cancha = models.ForeignKey('Cancha', on_delete=models.PROTECT, db_column='id_cancha', blank=True, null=True)
    fecha = models.DateField()
    hora= models.TimeField()
    estado = models.CharField(max_length=20)
    observacion = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.fecha} - {self.id_usuario} - {self.id_cancha}- {self.estado}- {self.hora}- {self.observacion}"






