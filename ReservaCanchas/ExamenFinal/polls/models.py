from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(blank=True, null=True, max_length= 50)
    apellido = models.CharField(blank=True, null=True, max_length= 50)
   
    correo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    fecha_inicio = models.DateField()
    ci = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    direccion = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.id_ciudad.nombre} - {self.correo}"
    

