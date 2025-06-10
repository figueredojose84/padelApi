from django.db import models
from equipos.models import Equipo



class Punto(models.Model):
    numeroPunto = models.IntegerField()
    

    def __str__(self):
        return f"{self.Equipo.nombreEquipo} {self.numeroPunto}"

    