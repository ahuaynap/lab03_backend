from django.db import models

class Visitante(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombres = models.CharField(max_length=150)
    apellidos = models.CharField(max_length=150)
    fecha_nacimiento = models.DateField()
    estatura = models.FloatField()
    direccion = models.CharField(max_length=150)
    latitud = models.FloatField()
    longitud = models.FloatField()
    ts = models.DateTimeField(auto_now_add=True)
    
class Chequeo(models.Model):
    id = models.BigAutoField(primary_key=True)
    visitante_id = models.ForeignKey(Visitante, on_delete=models.CASCADE)
    peso = models.FloatField()
    temperatura = models.FloatField()
    presion = models.PositiveSmallIntegerField()
    saturacion = models.PositiveSmallIntegerField()
    ts = models.DateTimeField(auto_now_add=True)