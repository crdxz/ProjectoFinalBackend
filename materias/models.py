from django.db import models
from carreras.models import Carrera

# Create your models here.

class Materia(models.Model):
    cod = models.CharField(primary_key=True, max_length=6)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, related_name='materias')
    nombre = models.CharField(max_length=50)
    creditos = models.IntegerField()
    horas_td = models.IntegerField()
    horas_tc = models.IntegerField()
    horas_ta = models.IntegerField()
