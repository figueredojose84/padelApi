from django.db import models

# Create your models here.
class Equipo(models.Model):
    nombreEquipo = models.CharField(max_length=100)

    
    
    def __str__(self):
        return f"{self.nombreEquipo}"

