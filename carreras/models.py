from django.db import models

# Create your models here.

class Carrera(models.Model):
    cod = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
